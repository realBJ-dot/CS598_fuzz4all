import subprocess
import time
from typing import List, Union

import torch

from Fuzz4All.target.target import FResult, Target
from Fuzz4All.util.Logger import LEVEL
from Fuzz4All.util.util import comment_remover


class SQLINNODBTarget(Target):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if kwargs["template"] == "fuzzing_with_config_file":
            config_dict = kwargs["config_dict"]
            self.prompt_used = self._create_prompt_from_config(config_dict)
            self.config_dict = config_dict
        else:
            raise NotImplementedError

    def wrap_prompt(self, prompt: str) -> str:
        return (
            f"-- {prompt}\n{self.prompt_used['separator']}\n{self.prompt_used['begin']}"
        )

    def wrap_in_comment(self, prompt: str) -> str:
        return f"-- {prompt}"

    def filter(self, code: str) -> bool:
        code = code.replace(self.prompt_used["begin"], "").strip()
        code = comment_remover(code)
        if self.prompt_used["target_api"] not in code:
            return False
        return True

    def clean(self, code: str) -> str:
        code = comment_remover(code)
        return code

    def clean_code(self, code: str) -> str:
        code = code.replace(self.prompt_used["begin"], "").strip()
        code = comment_remover(code)
        code = "\n".join([line for line in code.split("\n") if line.strip() != ""])
        return code

    def write_back_file(self, code):
        try:
            with open(
                "/tmp/temp{}.sql".format(self.CURRENT_TIME), "w", encoding="utf-8"
            ) as f:
                f.write(code)
        except:
            pass
        return "/tmp/temp{}.sql".format(self.CURRENT_TIME)

    def validate_individual(self, filename) -> (FResult, str):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                code = f.read()
        except:
            pass
        self.write_back_file(code)
        try:
            exit_code = subprocess.run(
                #need to change file position
                f"sudo mysql -u CS598 --password=test1234 < /tmp/temp{self.CURRENT_TIME}.sql",
                shell=True,
                capture_output=True,
                encoding="utf-8",
                timeout=5,
                text=True,
            )
        except subprocess.TimeoutExpired as te:
            pname = f"'temp{self.CURRENT_TIME}'"
            subprocess.run(
                ["ps -ef | grep " + pname + " | grep -v grep | awk '{print $2}'"],
                shell=True,
            )
            subprocess.run(
                [
                    "ps -ef | grep "
                    + pname
                    + " | grep -v grep | awk '{print $2}' | xargs -r kill -9"
                ],
                shell=True,
            )  # kill all tests thank you
            return FResult.TIMED_OUT, "sql"
        except UnicodeDecodeError as ue:
            return FResult.FAILURE, "decoding error"
        if exit_code.returncode == 1:
            # catch these operational errors
            # ER_TABLESPACE_AUTO_EXTEND_ERROR (Error 1112): Related to issues when the InnoDB tablespace cannot extend.
            # ER_DISK_FULL (Error 1021): Occurs when the disk is full, affecting database operations.
            # ER_LOCK_WAIT_TIMEOUT (Error 1205): Indicates that a lock wait timeout has exceeded, which can occur in high contention scenarios
            if '1112' in exit_code.stderr or '1021' in exit_code.stderr or '1205' in exit_code.stderr:
                return FResult.ERROR, exit_code.stderr
            return FResult.FAILURE, exit_code.stderr
        elif exit_code.returncode == 0:
            return FResult.SAFE, exit_code.stdout
        else:
            return FResult.ERROR, exit_code.stderr
