def predict_mark(search_student: dict, students_data: list) -> str:
    list_of_marks = [student["mark"] for student in students_data if student["gender"] == search_student["gender"]
                     and student["parent_education"] == search_student["parent_education"] and student[
                         "test_preperation"] == search_student["test_preperation"]]

    if len(list_of_marks) == 0:
        return f"{None}, Student not found"

    mark_a_counter = list_of_marks.count("A")
    mark_b_counter = list_of_marks.count("B")
    mark_c_counter = list_of_marks.count("C")

    most_mark_found = max(mark_a_counter, mark_b_counter, mark_c_counter)

    if mark_a_counter == most_mark_found:
        return "The predicted mark is: A"
    elif mark_b_counter == most_mark_found:
        return "The predicted mark is: B"
    elif mark_c_counter == most_mark_found:
        return "The predicted mark is: C"
    else:
        return None


def get_student_information() -> dict:
    gender = input("Enter gender of the student (male / female): ").lower()

    parent_education = input(
        "Enter parent education (bachelor's degree / some college / master's degree / associate's degree / 'high school / some high school): ").lower()

    test_preperation = input(
        "Enter test preperation (completed / none): ").lower()

    while gender not in ["male", "female"]:
        print("Invalid gender\n")
        gender = input("Enter gender of the student (male / female): ").lower()

    while parent_education not in ["master's degree", "bachelor's degree", "high school", "some college",
                                   "associate's degree", "some high school", ]:
        print("Invalid parent education\n")
        parent_education = input(
            "Enter parent education (bachelor's degree / some college / master's degree / associate's degree / 'high school / some high school): ").lower()

    while test_preperation not in ["completed", "none"]:
        print("Invalid test preperation\n")
        test_preperation = input(
            "Enter test preparation (completed / none): ").lower()

    return {"gender": gender, "parent_education": parent_education, "test_preperation": test_preperation}
