from functools import lru_cache

from scipy.stats import binom, bernoulli

import matplotlib.pyplot as plt


# TODO: refactor the old code and transform it to OOP way
class FirstIssue:
    """
    Suppose a random variable Y represent number of successes in the three math exams
    (Y is a binomial random variable with n=3), A student pass an exam when his/her mark is greater or equal to 50.
    """

    def __int__(self, data: list[dict]):
        self.data = data

    def get_prob_avg_success(self) -> float:
        """
        Getting the probability of success avg in the exams.
        :return: float
        """
        students_data = self.data

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
        try:
            probability_avg_of_success_in_exam = scores_succeeded / number_of_students

            return probability_avg_of_success_in_exam

        except ZeroDivisionError:
            return "The number of students is zero!\n"
        except TypeError:
            return "The number of students must be integer!\n"

    @lru_cache(maxsize=128)
    def get_binomial_prob_of_success(self, trails: int) -> dict[int, float]:
        """
        Getting the binomial probability of each trail.
        :param trails: int
        :return: dict[int, float]
        """
        try:
            prob_avg_of_success_in_exam = self.get_prob_avg_success()

            random_variable_model = binom(trails, prob_avg_of_success_in_exam)

            random_variable_values = list(range(trails + 1))

            probs = [random_variable_model.pmf(y) for y in random_variable_values]

            binomial_prob_of_success = {}

            for prob in probs:
                binomial_prob_of_success[probs.index(prob)] = prob

            return binomial_prob_of_success

        except TypeError:
            return "The trails must be integer!\n"


class SecondIssue:
    """
    Assume a random variable X that defines the Gender of a student,
    We define a success when the student is a 'female'.
    """

    def __int__(self, data: list[dict]):
        self.data = data

    def get_prob_of_students_gender_is_female(self) -> float:
        """
        Getting the probability of the students is female.
        :return: float
        """
        students_data = self.data

        try:
            student_gender_is_female_counter = sum(student["gender"] == "female" for student in students_data)

            prob_of_students_gender_is_female = student_gender_is_female_counter / len(students_data)

        except ZeroDivisionError:
            return "The number of students is zero!\n"
        except TypeError:
            return "The number of students must be integer!\n"

        return prob_of_students_gender_is_female

    def get_bernoulli_pmf(self, random_variable: int) -> float:
        """
        Computing the probability of a bernoulli random variable.
        :param random_variable: int
        :return: float
        """
        try:
            if random_variable == 0:
                return 1 - self.get_prob_of_students_gender_is_female()
            elif random_variable == 1:
                return self.get_prob_of_students_gender_is_female()
            return None
        except (ValueError, TypeError):
            return "The random variable must be integer!\n"

    @lru_cache(maxsize=1)
    def get_plotting_distribution_of_the_random_variable(self) -> None:
        """
        Getting Plot the distribution of the random variable.
        :return: None
        """
        random_variable_model = bernoulli(self.get_prob_of_students_gender_is_female())

        random_variable_values = [0, 1]

        probabilities = [random_variable_model.pmf(x) for x in random_variable_values]

        plt.xlabel(xlabel="R.V (X)")
        plt.ylabel(ylabel="P(X=x)")
        plt.vlines(x=random_variable_values, ymin=0, ymax=probabilities, colors='k', linestyles='-', lw=1,
                   label='Bernoulli PMF     ')
        plt.legend(loc='best', frameon=False)
        plt.show()


class ThirdIssue:
    """
    Write a function that predicts the student mark given (Gender, Parent education, Test preparation).
    """

    def __int__(self, data: list[dict]):
        self.data = data

    def __get_student_information(self) -> dict:
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
        search_student = self.__get_student_information()

        students_data = self.data

        list_of_marks = [student["mark"] for student in students_data if student["gender"] == search_student["gender"]
                         and student["parent_education"] == search_student["parent_education"] and student[
                             "test_preperation"] == search_student["test_preperation"]]

        if len(list_of_marks) == 0:
            return f"None Student not found!\n"

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
            return "Not A nor B nor C"
