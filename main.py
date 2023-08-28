from utils.config import students_data
from issues import *

if __name__ == '__main__':
    F, S, T = FirstIssue(students_data), SecondIssue(students_data), ThirdIssue(students_data)

    a1 = F.get_average_success_probability()
    b1 = F.get_binomial_probability_of_success(trials=int(input("Trails: ")))
    print(a1, b1)

    a2 = S.get_probability_of_students_gender_is_female()
    b2 = S.get_bernoulli_probability_mass_function(random_variable=int(input("Random variable: ")))
    S.get_plotting_distribution_of_the_random_variable()
    print(a2, b2)

    p = T.predict_mark()
    print(p)
