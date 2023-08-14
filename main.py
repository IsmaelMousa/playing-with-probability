import issues.is1

if __name__ == '__main__':
    # Question 1:
    # A)
    prob_avg_of_success = issues.is1.get_prob_avg_success()
    print(prob_avg_of_success)

    # B)
    try:
        trails = int(input("Number of Trails: "))
        binomial_prob_of_success = issues.is1.get_binomial_prob_of_success(trails=trails,
                                                                           prob_avg_of_success_in_exam=prob_avg_of_success)
        print(binomial_prob_of_success)

    except ValueError:
        print("Invalid input!")

