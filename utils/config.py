from dataclasses import dataclass
from functools import lru_cache

from yaml import safe_load
import pandas as pd


@dataclass(frozen=True)
# TODO: find a better name for this class
class StudentPath:
    # TODO: find a better way to write the docs
    """
    Students path configurations
    """
    path: str


@dataclass(frozen=True)
# TODO: find a better name for this class
class StudentData:
    # TODO: find a better way to write the docs
    """
    Students data as a list of dict
    """
    data: list[dict]


@lru_cache(maxsize=1)
# TODO: find a better name for this func
def get_students_data() -> StudentData:
    # TODO: find a better way to write the docs
    """
    Getting students data as a list of dictionaries
    :return: StudentData
    """
    # TODO: find a better way to pass the file path
    with open("../config.yaml", "r") as file:
        config = safe_load(file)

        stu_path_cfg = StudentPath(path=config["STUDENTS_DATA_PATH"])

        data = pd.read_csv(stu_path_cfg.path).to_dict("records")

        stu_data_cfg = StudentData(data=data)

        return stu_data_cfg


students = get_students_data()

students_data = students.data
