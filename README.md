# <p style="text-align: center;">  🌌️Fuzz4All: Universal Fuzzing with LLMs </p>

<p align="center">
    <a href="https://arxiv.org/abs/2308.04748"><img src="https://img.shields.io/badge/arXiv-2308.04748-b31b1b.svg?style=for-the-badge">
    <a href="https://doi.org/10.5281/zenodo.10456883"><img src="https://img.shields.io/badge/DOI-10456883-blue?style=for-the-badge">
    <a href="https://hub.docker.com/r/stevenxia/fuzz4all/tags"><img src="https://img.shields.io/badge/docker-fuzz4all-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=blue">
    <a href="https://github.com/fuzz4all/fuzz4all/blob/master/LICENSE"><img src="https://forthebadge.com/images/badges/cc-by.svg" style="height: 28px"></a>
</p>

This repository contains the source code for our ICSE'24 paper <i> "Fuzz4All: Universal Fuzzing with Large Language Models" </i>

## 🌌️ About

`Fuzz4All` -- the first fuzzer that can universally target many input languages and features of these languages.
> The key idea behind `Fuzz4All` is to leverage large language models (LLMs) as an input generation and mutation engine, which enables the 
> approach to produce diverse and realistic inputs for any practically relevant language. 

To realize this potential, we present a novel **autoprompting technique**, which creates LLM prompts 
that are well-suited for fuzzing, and a novel **LLM-powered fuzzing loop**, which iteratively updates 
the prompt to create new fuzzing inputs.

![](./resources/overview.gif)

## ⚡ Quick Start

> [!Important]
> We highly recommend running `Fuzz4All` in a sandbox environment/machine such as docker. 
> Since LLMs may generate potential harmful code your machine, please proceed with caution.
> We have provided a complete docker image in our artifact here: https://doi.org/10.5281/zenodo.10456883

### Setup

First, create the corresponding environment and install the required packages

```bash
conda create -n fuzz4all python=3.10
conda activate fuzz4all

pip install -r requirements.txt
pip install -e .
```

Next, we need to quickly configure the environmental variables. Here are the default parameters:

```bash
export FUZZING_BATCH_SIZE=5
export FUZZING_MODEL="bigcode/starcoderbase-1b"
export FUZZING_DEVICE="gpu"
```

The exact parameters will depend on the machine you are running `Fuzz4All` on.

To use the autoprompting mechanism of `Fuzz4All` via GPT-4, please also export your openai key

```
export OPENAI_API_KEY={key_here}
```
### Fuzzing Javascript and MySQL engine
For our group project, we specially fuzz on Javascript and MySQL engine. 

The config files we used for JavaScript engines can be found under config/full_run: `javascript_hermes.yaml` and `javascript_v8.yaml`.

The config file we used for MySQL InnoDB engine can be found under config/full_run: `sql_innodb.yaml`.

To perform the test, engines for them need to be manually built in advance, here is the list of sources:

[`Meta Hermes Engine`](https://github.com/facebook/hermes) After building the engine, the scripts can be directly executed.

[`V8 Engine`](https://v8.dev/docs/build) After building the engine, the scripts can be directly executed.

[`MySQL Engine`](https://dev.mysql.com/doc/refman/8.0/en/linux-installation.html) After building the engine. You need to start mysql service, login as `root`, then create user `CS598` with password `test1234` and grant it with all priorities on database `sampleDB`. Then the scripts can be executed.

We included the scripts for them under `/scripts`:

| Engine    | Path |
| -------- | ------- |
| Hermes  | js-hermes.sh    |
| V8 | js-v8.sh     |
| MySQL    | sql.sh   |

To use these scripts, you might need to change `--target` to refer to the path of executable, and `--folder` to output paths.

We also included  scripts that execute each test that was logged as having potenial error and record the execution output: `scripts\check_hermes_output.sh` and `scripts\check_v8_output.sh`. Please update the path to the log file before executing these scripts.

### Fuzzing

Now you are ready to run `Fuzz4All` on all targets (with arbitrary inputs through autoprompting)! 

`Fuzz4All` is configured easily through config files. The one used for our experiment are store in `configs/`. 
The config file controls various aspects of `Fuzz4All` including the fuzzing language, time, autoprompting strategy, etc.
Please see any example config file in `configs/` for more detail. 

In general, you can run `Fuzz4All` with the following command:

```bash
python Fuzz4All/fuzz.py --config {config_file.yaml} main_with_config \ 
                        --folder outputs/fuzzing_outputs \
                        --batch_size {batch_size} \
                        --model_name {model_name} \
                        --target {target_name}
```

> [!Note]
> you will neede to build/download your own binary ({target_name}) for fuzzing

For targeted fuzzing (i.e., fuzzing a specific API or library of a language), you can modify the config file to point to the 
specific API/library documentation you want the model to generate prompts for. Please see `configs/targeted` for examples of such configs.

<details><summary>You should see similar outputs to the following: </summary> 

```
BATCH_SIZE: 5
MODEL_NAME: bigcode/starcoderbase 1b
DEVICE: gpu
...
=== Target Config ===
language: smt2
folder: outputs/full_run/cvc5/
...
====================
[INFO] Initializing ... this may take a while ...
[INFO] Loading model ...
=== Model Config ===
model_name: bigcode/starcoderbase
...
====================
[INFO] Model Loaded
[INFO] Use auto-prompting prompt ...
Generating prompts... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:07:30
[INFO] Done
 (resuming from 0)
[VERBOSE] ; SMT2 is an input language commonly used by SMT solvers, with its syntax based on S-expressions. The multi-sorted logic accommodates a simple type system to confirm that terms from contrasting sorts
aren't the equal. Uninterpreted functions can be declared, with the function symbol being an uninterpreted one. SMT2 supports various theories, including integer and real arithmetic, with basic logical
connectives, quantifiers, and attribute annotations. An SMT2 theory includes sort and function symbol declarations and assertions of facts about them. Terms can be checked against these theories to determine their
validity, with successful queries returning "unsat".
; Please create a short program which uses complex SMT2 logic for an SMT solver
(set-logic ALL)
...
(set-logic ALL)
(assert (forall ((n Int)) (=> (> n 0) (= n (* 2 n)))))
(check-sat)
(exit)
; Please create a short program which uses complex SMT2 logic for an SMT solver
(set-logic ALL)

Fuzzing •   0% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━     30/100000 • 0:02:26
```
</details>

After fuzzing, you can find the generated fuzzing programs in `outputs/full_run/{target}/`. 

<details>
<summary>Here is the structure of the output directory: </summary>

```
- outputs/full_run/{target}/
    - prompts 
        - best_prompt.txt: the best prompt found by `Fuzz4All` for the target.
        - greedy_prompt.txt
        - prompt_0.txt
        - prompt_1.txt
        - prompt_2.txt
        - scores.txt: keep track of the scores of each prompt (used to select the best prompt).
    - 0.fuzz
    - 1.fuzz
    ... # 
    - log.txt
    - log_generation.txt
    - log_validation.txt
```
</details>

Most notably, we log both the generation and validation process in `log_generation.txt` and `log_validation.txt` respectively. Furthermore, `log.txt` provides an overview of the fuzzing process (including any potential bugs found by `Fuzz4All`) 

Potential bugs will look like this in `log.txt`:

```
[VERBOSE] 2345.fuzz has potential error! # this indicates that file 2345.fuzz may have a potential bug
```


## ⚙️ Artifact

Please see [`README_artifact.md`](https://github.com/fuzz4all/fuzz4all/blob/master/README_artifact.md) and [Zenodo link](https://zenodo.org/records/10456883) for a more detailed explanation of Fuzz4All 
as well as how to produce the complete results from our paper 

## 🐛 Bugs Found

We have included some of our execution results: `\hermes_fuzz_executed`.

## 📝 Citation

```bibtex
@inproceedings{fuzz4all,
  title = {Fuzz4All: Universal Fuzzing with Large Language Models},
  author = {Xia, Chunqiu Steven and Paltenghi, Matteo and Tian, Jia Le and Pradel, Michael and Zhang, Lingming},
  booktitle = {Proceedings of the 46th International Conference on Software Engineering},
  series = {ICSE '24},
  year = {2024},
}
```

