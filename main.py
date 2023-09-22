from utils import students_data

from issues import FirstIssue, SecondIssue, ThirdIssue


def get_student_information() -> dict[str, str]:
    """
    Getting the students information as an input from the user.
    :return: dict
    """
    gender = input("Enter gender of the student (male / female): ").lower()

    parent_education = input(
        "Enter parent education (bachelor's degree / some college / master's degree"
        " / associate's degree / 'high school / some high school): ").lower()

    test_preperation = input(
        "Enter test preperation (completed / none): ").lower()

    while gender not in ["male", "female"]:
        print("Invalid gender\n")
        gender = input("Enter gender of the student (male / female): ").lower()

    while parent_education not in ["master's degree", "bachelor's degree", "high school", "some college",
                                   "associate's degree", "some high school", ]:
        print("Invalid parent education\n")
        parent_education = input(
            "Enter parent education (bachelor's degree / some college / master's degree"
            " / associate's degree / 'high school / some high school): ").lower()

    while test_preperation not in ["completed", "none"]:
        print("Invalid test preperation\n")
        test_preperation = input(
            "Enter test preparation (completed / none): ").lower()

    return {"gender": gender, "parent_education": parent_education, "test_preperation": test_preperation}


def main() -> None:
    first = FirstIssue(data=students_data)
    second = SecondIssue(data=students_data)
    third = ThirdIssue(data=students_data)

    a1 = first.get_average_success_probability()
    b1 = first.get_binomial_probability_of_success(trials=3)
    print(f"Question 1 \n{100 * '='}\na) {a1}\n{100 * '-'}\nb) {b1}\n{100 * '='}")

    a2 = second.get_probability_of_students_gender_is_female()
    b2 = second.get_bernoulli_probability_mass_function(
        random_variable=int(input(f"Question 2 \n{100 * '='}\nRandom variable: ")))
    print(f"{100 * '-'}\na) {a2}\n{100 * '-'}\nb) {b2}\n{100 * '='}")
    second.get_plotting_distribution_of_the_random_variable()

    print(f"Question 3\n{100 * '='}\n")
    p = third.predict_mark(search_student=get_student_information())
    print(f"\n{100 * '-'}\n{p}\n{100 * '-'}\n{100 * '='}")


if __name__ == '__main__':
    main()
