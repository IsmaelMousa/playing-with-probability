from typing import Union

from scipy.stats import bernoulli
import matplotlib.pyplot as plt


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
