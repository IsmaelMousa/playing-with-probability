from utils.config import students_data
from issues import is1, is2, is3

if __name__ == '__main__':
    first_question_a = is1.get_prob_avg_success(students_data=students_data)
    first_question_b = is1.get_binomial_prob_of_success(trails=3, prob_avg_of_success_in_exam=first_question_a)

    print(first_question_a)
    print(first_question_b)

    second_question_a = is2.get_prob_of_students_gender_is_female(students_data=students_data)
    second_question_b = is2.get_bernoulli_pmf(random_variable=int(input("Enter R.V: ")),
                                              prob_of_success=second_question_a)
    is2.get_plotting_distribution_of_the_random_variable(prob_of_students_gender_is_female=second_question_a)

    print(second_question_a)
    print(second_question_b)

    third_question_set = is3.get_student_information()
    third_question_get = is3.predict_mark(third_question_set, students_data=students_data)

    print(third_question_get)
