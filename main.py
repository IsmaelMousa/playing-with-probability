from utils.config import students_data

from issues.first import FirstIssue
from issues.second import SecondIssue
from issues.third import ThirdIssue


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


if __name__ == '__main__':
    F = FirstIssue(data=students_data)
    S = SecondIssue(data=students_data)
    T = ThirdIssue(data=students_data)

    a1 = F.get_average_success_probability()
    b1 = F.get_binomial_probability_of_success(trials=3)
    print(f"{100 * '-'}\n{a1}\n{b1}\n{100 * '-'}")

    a2 = S.get_probability_of_students_gender_is_female()
    b2 = S.get_bernoulli_probability_mass_function(random_variable=int(input("Random variable: ")))
    print(f"{100 * '-'}\n{a2}\n{b2}\n{100 * '-'}")
    S.get_plotting_distribution_of_the_random_variable()

    p = T.predict_mark(search_student=get_student_information())
    print(f"{100 * '-'}\n{p}\n{100 * '-'}")
