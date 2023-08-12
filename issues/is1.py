from scipy.stats import binom
from utils.config import students_data
from functools import lru_cache


# a)
@lru_cache(maxsize=1)
def get_prob_avg_success() -> float:
    """
    Getting the probability of success avg in the exams
    :return: float
    """
    number_of_students = len(students_data)

    score_success_counter = 0

    for student in students_data:
        if student['score_1'] >= 50:
            score_success_counter += 1
        if student['score_2'] >= 50:
            score_success_counter += 1
        if student['score_3'] >= 50:
            score_success_counter += 1

    scores_succeeded = score_success_counter / 3

    probability_avg_of_success_in_exam = scores_succeeded / number_of_students

    return probability_avg_of_success_in_exam


# b)
@lru_cache(maxsize=5)
def get_binomial_prob_of_success(trails: int, probability_avg_of_success_in_exam: float) -> dict[int, float]:
    n = trails

    p = probability_avg_of_success_in_exam

    random_variable_model = binom(n, p)

    random_variable_values = list(range(n + 1))

    probabilities = [random_variable_model.pmf(y) for y in random_variable_values]

    binomial_prob_of_success = {}

    for probability in probabilities:
        binomial_prob_of_success[probabilities.index(probability)] = probability

    return binomial_prob_of_success
