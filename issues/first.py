from functools import lru_cache
from typing import Union

from scipy.stats import binom


class FirstIssue:
    """
    Suppose a random variable Y represent number of successes in the three math exams
    (Y is a binomial random variable with n=3), A student pass an exam when his/her mark is greater or equal to 50.
    """

    def __init__(self, data: list[dict]) -> None:
        self.__data = data

    def get_average_success_probability(self) -> Union[float, str]:
        """
        Calculate the probability of success avg in the exams.

        :return: float
        """
        students_data = self.__data

        number_of_students = len(students_data)
        if number_of_students == 0:
            return "Students data is empty!\n"

        score_success_count = 0

        for student in students_data:
            if student["score_1"] >= 50:
                score_success_count += 1
            if student["score_2"] >= 50:
                score_success_count += 1
            if student["score_3"] >= 50:
                score_success_count += 1

        scores_succeeded = score_success_count / 3

        average_success_probability_in_exam = scores_succeeded / number_of_students

        return average_success_probability_in_exam

    @lru_cache(maxsize=128)
    def get_binomial_probability_of_success(self, trials: int) -> dict[int, float]:
        """
        Calculate the binomial probability of each trail.

        :param trials: int
        :return: dict[int, float]
        """
        if not isinstance(trials, int) or trials < 0:
            return {}

        average_success_probability_in_exam = self.get_average_success_probability()

        random_variable_model = binom(trials, average_success_probability_in_exam)

        random_variable_values = list(range(trials + 1))

        probabilities = [random_variable_model.pmf(y) for y in random_variable_values]

        binomial_success_probability = {}

        for probability in probabilities:
            binomial_success_probability[probabilities.index(probability)] = probability

        return binomial_success_probability
