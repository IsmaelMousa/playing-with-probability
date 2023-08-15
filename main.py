# TODO: EDIT MAIN FILE
from issues import is1, is2

"""
def question_1(part: str):
    prob_avg_of_success = is1.get_prob_avg_success()
    if part == 'a' or part == 'A':
        print(prob_avg_of_success)
    elif part == 'b' or part == 'B':
        try:
            trails = int(input("Number of Trails: "))
            binomial_prob_of_success = is1.get_binomial_prob_of_success(trails=trails,
                                                                        prob_avg_of_success_in_exam=prob_avg_of_success)
            print(binomial_prob_of_success)

        except ValueError:
            print("Invalid input Trails!")
    return None


def question_2(part: str):
    prob_of_students_gender_is_female = is2.get_prob_of_students_gender_is_female()
    if part == 'a' or part == 'A':
        print(prob_of_students_gender_is_female)
    elif part == 'b' or part == 'B':
        try:
            random_variable = int(input("Enter R.V: "))
            bernoulli_pmf = is2.get_bernoulli_pmf(random_variable=random_variable,
                                                  prob_of_success=prob_of_students_gender_is_female)
            print(bernoulli_pmf)
        except (ValueError, TypeError):
            print("Invalid input R.V")
    elif part == 'c' or part == 'C':
        is2.get_plotting_distribution_of_the_random_variable(
            prob_of_students_gender_is_female=prob_of_students_gender_is_female)
    return None

"""
if __name__ == '__main__':
    """
    for part in ['a', 'b']:
        question_1(part=part)

    for part in ['a', 'b', 'c']:
        question_2(part=part)
    """
