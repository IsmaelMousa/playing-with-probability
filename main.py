from utils import students_data

from issues import FirstIssue, SecondIssue, ThirdIssue


def main():
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
    get_student_information = third.get_student_information()
    p = third.predict_mark(search_student=get_student_information)
    print(f"\n{100 * '-'}\n{p}\n{100 * '-'}\n{100 * '='}")


if __name__ == '__main__':
    main()
