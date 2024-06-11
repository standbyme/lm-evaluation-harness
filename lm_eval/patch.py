import time
from typing import List
import pickle
from pathlib import Path


def dump_prompts(task):

    prompts: List[str] = list(map(lambda inst: inst.args[0], task.instances))
    task_name = task.config.task

    result_path = Path().cwd() / "prompts"
    result_path.mkdir(parents=True, exist_ok=True)

    # get the current timestamp in seconds
    timestamp = int(time.time())

    # dump prompts to a file named task_name.pkl in the pickle format
    with open(result_path / f"{task_name}.{timestamp}.pkl", "wb") as f:
        pickle.dump(prompts, f)
