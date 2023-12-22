class ThirdIssue:
    """
    Predicts the student mark given (Gender, Parent education, Test preparation).
    """

    def __init__(self, data: list[dict]) -> None:
        self.__data = data

    def predict_mark(self, search_student: dict[str, str]) -> str:
        """
        Getting the most predict mark based on the inputs that were given.
        :returns: str
        """
        students_data = self.__data

        marks = [student["mark"] for student in students_data if student["gender"] == search_student["gender"]
                 and student["parent_education"] == search_student["parent_education"] and student[
                     "test_preperation"] == search_student["test_preperation"]]
        if len(marks) == 0:
            return "No match between the students information and your inputs!\n"

        mark_a_count = marks.count("A")
        mark_b_count = marks.count("B")
        mark_c_count = marks.count("C")

        counts = {"A": mark_a_count, "B": mark_b_count, "C": mark_c_count}
        max_count = max(counts.values())

        predicted_marks = [mark for mark, count in counts.items() if count == max_count]

        if len(predicted_marks) == 1:
            return f"The predicted mark is: {predicted_marks[0]}"

        return " & ".join(predicted_marks)

    @staticmethod
    def get_student_information() -> dict[str, str]:
        """
        Getting the students information as an input from the user.
        :return: dict
        """
        gender = input("Enter gender of the student (male / female): ").lower()

        while gender not in ["male", "female"]:
            print("Invalid gender\n")
            gender = input("Enter gender of the student (male / female): ").lower()

        parent_education = input(
            "Enter parent education (bachelor's degree / some college / master's degree"
            " / associate's degree / high school / some high school): ").lower()

        while parent_education not in ["master's degree", "bachelor's degree", "high school", "some college",
                                       "associate's degree", "some high school", ]:
            print("Invalid parent education\n")
            parent_education = input(
                "Enter parent education (bachelor's degree / some college / master's degree"
                " / associate's degree / 'high school / some high school): ").lower()

        test_preperation = input(
            "Enter test preperation (completed / none): ").lower()

        while test_preperation not in ["completed", "none"]:
            print("Invalid test preperation\n")
            test_preperation = input(
                "Enter test preparation (completed / none): ").lower()

        return {"gender": gender, "parent_education": parent_education, "test_preperation": test_preperation}
