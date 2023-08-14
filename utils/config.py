from dataclasses import dataclass
from functools import lru_cache

from yaml import safe_load
import pandas as pd


@dataclass(frozen=True)
class StudentsPath:
    """
    Students path configuration
    """
    path: str


@dataclass(frozen=True)
class StudentsData:
    """
    Students data store
    """
    data: list[dict]


@lru_cache(maxsize=1)
def get_stu_data() -> StudentsData:
    """
    Getting and loading students data as a list of dictionaries
    :return: StudentData
    """
    with open("config.yaml", "r") as file:
        config = safe_load(file)

        stu_path_cfg = StudentsPath(path=config["STUDENTS_DATA_PATH"])

        data = pd.read_csv(stu_path_cfg.path).to_dict("records")

        stu_data_cfg = StudentsData(data=data)

        return stu_data_cfg


students = get_stu_data()

students_data = students.data
