import os
import sys
from dataclasses import dataclass
from functools import lru_cache

from yaml import safe_load, YAMLError
import pandas as pd


@dataclass(frozen=True)
class StudentsPath:
    """
    Students path configuration.
    """
    path: str


@dataclass(frozen=True)
class StudentsData:
    """
    Students data store.
    """
    data: list[dict]


@lru_cache(maxsize=1)
def get_stu_data() -> StudentsData:
    """
    Getting and loading students data as a list of dictionaries.
    :return: StudentData
    """
    base_path = os.path.dirname(os.path.abspath(__file__))
    cfg_path = os.path.join(base_path, "../config.yaml")

    print(cfg_path)
    try:
        with open(cfg_path, "r") as cfg_file:
            config: dict = safe_load(cfg_file)

            stu_path_cfg = StudentsPath(path=config.get("STUDENTS_DATA_PATH", "Not Found"))

            data = pd.read_csv(stu_path_cfg.path).to_dict("records")

            stu_data_cfg = StudentsData(data=data)

            return stu_data_cfg

    except IOError:
        print(f"Unable to open the config file with path: {cfg_path}")
        sys.exit(os.EX_IOERR)

    except YAMLError:
        print("Unable to parse the config file.")
        sys.exit(os.EX_IOERR)


students = get_stu_data()

students_data = students.data
