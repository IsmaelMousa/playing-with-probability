# TODO: refactor this code and make it more pythonic
from scipy.stats import bernoulli
import matplotlib.pyplot as plt

from utils.config import students_data

# a)
student_gender_is_female_counter = sum(student["gender"] == "female" for student in students_data)

probability_of_student_gender_is_female = student_gender_is_female_counter / len(students_data)

print(f"The probability of success (p): {probability_of_student_gender_is_female} ")


# b)
def bernoulli_pmf(x: int, p: float) -> float:
    if x == 0 and (0 <= p <= 1):
        return f"P(X={x}) = {1 - p}"

    elif x == 1 and (0 <= p <= 1):
        return f"P(X={x}) = {p}"

    else:
        return f"{None}, as values of bernoulli random variable should be 0 or 1"


x = int(input("Enter the value of R.V: "))

p = float(input("Enter the probability: "))

print(f"The Probability (p): {bernoulli_pmf(x, p)}")

# c)

probability_of_success = probability_of_student_gender_is_female

random_variable_model = bernoulli(probability_of_success)

random_variable_values = list(range(2))

probabilities = [random_variable_model.pmf(x) for x in random_variable_values]

plt.xlabel("R.V (X)")
plt.ylabel("P(X=x)")
plt.vlines(random_variable_values, 0, probabilities, colors='k', linestyles='-', lw=1, label='Bernoulli PMF     ')
plt.legend(loc='best', frameon=False)
plt.show()
