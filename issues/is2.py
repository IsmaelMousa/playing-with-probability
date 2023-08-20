from functools import lru_cache

from scipy.stats import bernoulli
import matplotlib.pyplot as plt


# a)
def get_prob_of_students_gender_is_female(students_data) -> float:
    """
    Getting the probability of the students is female.
    :return: float
    """
    student_gender_is_female_counter = sum(student["gender"] == "female" for student in students_data)

    prob_of_students_gender_is_female = student_gender_is_female_counter / len(students_data)

    return prob_of_students_gender_is_female


# b)
def get_bernoulli_pmf(random_variable: int, prob_of_success: float) -> float:
    """
    Computing the probability of a bernoulli random variable.
    :param random_variable: int
    :param prob_of_success: float
    :return: float
    """
    try:
        if 0 <= prob_of_success <= 1:
            if random_variable == 0:
                return 1 - prob_of_success
            elif random_variable == 1:
                return prob_of_success
        return None
    except (ValueError, TypeError):
        return None


# c)
@lru_cache(maxsize=1)
def get_plotting_distribution_of_the_random_variable(prob_of_students_gender_is_female: float) -> None:
    """
    Getting Plot the distribution of the random variable.
    :param prob_of_students_gender_is_female: float
    :return: function
    """
    prob_of_success = prob_of_students_gender_is_female

    random_variable_model = bernoulli(prob_of_success)

    random_variable_values = [0, 1]

    probabilities = [random_variable_model.pmf(x) for x in random_variable_values]

    plt.xlabel(xlabel="R.V (X)")
    plt.ylabel(ylabel="P(X=x)")
    plt.vlines(x=random_variable_values, ymin=0, ymax=probabilities, colors='k', linestyles='-', lw=1,
               label='Bernoulli PMF     ')
    plt.legend(loc='best', frameon=False)
    plt.show()
