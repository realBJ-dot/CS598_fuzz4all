from typing import Any, Dict, List, Optional, Tuple, Union
from Fuzz4All.target.target import Target
from Fuzz4All.target.JSHERMES import JSHERMESTarget


def make_target_with_config(config_dict: Dict[str, Any]) -> Target:
    """Create a target from a configuration dictionary."""

    llm = config_dict["llm"]
    fuzzing = config_dict["fuzzing"]
    target = config_dict["target"]

    target_compat_dict = {
        # simple mapping
        "language": target["language"],
        "folder": fuzzing["output_folder"],
        "bs": llm.get("batch_size", 1),
        "temperature": llm.get("temperature", 1.0),
        "device": llm.get("device", "cuda"),
        "model_name": llm.get("model_name", "bigcode/starcoder"),
        "max_length": llm.get("max_length", 1024),
        "use_hw": fuzzing.get("use_hand_written_prompt", False),
        "no_input_prompt": fuzzing.get("no_input_prompt", False),
        "prompt_strategy": fuzzing.get("prompt_strategy", 0),
        "level": fuzzing.get("log_level", 0),
        # compatibility conversion
        # signalling the target to use the config file
        "template": "fuzzing_with_config_file",
        "config_dict": config_dict,
        "target_name": fuzzing.get("target_name", "target"),
    }

    # print the target config
    print("=== Target Config ===")
    for k, v in target_compat_dict.items():
        print(f"{k}: {v}")
    print("====================")


    if target["language"] == "js-hermes":
        return JSHERMESTarget(**target_compat_dict)
    else:
        raise ValueError(f"Invalid target {target['language']}")