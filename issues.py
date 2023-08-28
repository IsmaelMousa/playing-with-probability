from functools import lru_cache
from typing import Union

from scipy.stats import binom, bernoulli
import matplotlib.pyplot as plt


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


class SecondIssue:
    """
    Assume a random variable X that defines the Gender of a student,
    We define a success when the student is a 'female'.
    """

    def __init__(self, data: list[dict]) -> None:
        self.__data = data

    def get_probability_of_students_gender_is_female(self) -> Union[float, str]:
        """
        Getting the probability of the students is female.
        :return: float
        """
        students_data = self.__data

        number_of_students = len(students_data)
        if number_of_students == 0:
            return "Students data is empty!\n"

        student_gender_is_female_count = sum(student["gender"] == "female" for student in students_data)

        prob_of_students_gender_is_female = student_gender_is_female_count / number_of_students

        return prob_of_students_gender_is_female

    def get_bernoulli_probability_mass_function(self, random_variable: int) -> Union[float, str]:
        """
        Computing the probability of a bernoulli random variable.
        :param random_variable: int
        :return: float
        """
        if random_variable not in [0, 1]:
            return "Invalid random variable!\n"

        elif random_variable == 0:
            return 1 - self.get_probability_of_students_gender_is_female()

        return self.get_probability_of_students_gender_is_female()

    def get_plotting_distribution_of_the_random_variable(self) -> None:
        """
        Getting Plot the distribution of the random variable.
        :return: None
        """
        random_variable_model = bernoulli(self.get_probability_of_students_gender_is_female())

        random_variable_values = [0, 1]

        probabilities = [random_variable_model.pmf(x) for x in random_variable_values]

        plt.xlabel(xlabel="R.V (X)")
        plt.ylabel(ylabel="P(X=x)")
        plt.vlines(x=random_variable_values, ymin=0, ymax=probabilities, colors='k', linestyles='-', lw=1,
                   label="Bernoulli PMF     ")
        plt.legend(loc="best", frameon=False)
        plt.show()


class ThirdIssue:
    """
    Predicts the student mark given (Gender, Parent education, Test preparation).
    """

    def __init__(self, data: list[dict]) -> None:
        self.__data = data

    @staticmethod
    def __get_student_information() -> dict[str, str]:
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

    def predict_mark(self) -> str:
        """
        Getting the most predict mark based on the inputs that were given.
        :returns: str
        """
        search_student = self.__get_student_information()
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
