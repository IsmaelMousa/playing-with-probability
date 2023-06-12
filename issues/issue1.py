from scipy.stats import binom
from data.students import DATA

# a)
number_of_students = len(DATA)

score_success_counter = 0

for student in DATA:
    if student['score_1'] >= 50:
        score_success_counter += 1
    if student['score_2'] >= 50:
        score_success_counter += 1
    if student['score_3'] >= 50:
        score_success_counter += 1

scores_successed = score_success_counter / 3

probability_of_success_in_exam = scores_successed / number_of_students

print(f"The probability of success (p): {probability_of_success_in_exam}")

# b)

n = 3

p = probability_of_success_in_exam

random_variable_model = binom(n, p)

random_variable_values = list(range(n+1))

probabilities = [random_variable_model.pmf(y) for y in random_variable_values]

for probability in probabilities:
    print(f"P(Y={probabilities.index(probability)}) = {probability}")
