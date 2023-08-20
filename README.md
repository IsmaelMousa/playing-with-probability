# Playing with the Probabilities

## Table of contents

* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Issues](#issues)
    * [First Issue](#first-issue)
        * [a](#a-compute-probability-of-success-p)
        * [b](#b-compute-probability-of-every-value-of-the-random-variable-y)
    * [Second Issue](#second-issue)
        * [a](#a-compute-the-probability-of-success-using-the-data)
        * [b](#b-write-a-function-that-computes-the-probability-of-a-bernoulli-random-variable)
        * [c](#c-plot-the-distribution-of-the-random-variable-x)
    * [Third Issue](#third-issue)
        * [Input](#input)
        * [Output](#output)
* [Contact](#contact)

## General info

This project is intended only for training and learning to solve probabilistic issues using the Python language.

The project was simple and not very good in terms of codes, files, etc...
Where the project was basically just about providing solutions without using that much code (the project was just one
file),
But I decided to incorporate the things and additions that I learned myself through my scientific and training
experience in this project so that it is more advanced.

## Technologies

Project is created with:

* Python 3.11.2

## Setup

To run this project:

1) install dependencies run `pip install -r requirements.txt`
2) run main file `python main.py` or using code editor(Pycharm or VS code)

## Issues:

### First Issue

Suppose a random variable Y represent number of successes in the three math exams, (Y is a binomial random variable with
n=3).
A student pass an exam when his/her mark is greater or equal to 50.

##### a) Compute probability of success (p).

##### b) Compute probability of every value of the random variable Y.

### Second Issue

Assume a random variable X that defines the Gender of a student. We define a success when the student is a 'female'.

##### a) Compute the probability of success using the data.

##### b) Write a function that computes the probability of a bernoulli random variable.

##### c) Plot the distribution of the random variable X.

### Third Issue

Write a function that predicts the student mark given (Gender, Parent education, Test preparation).

#### Input:

##### 1) The historical data as a list of dictionaries.

##### 2) Information of the unseen student as a dictionary.

#### Output:

The predicted mark for that student, (The predicted mark is the mark with the maximum conditional probability).

## Contact

Created by [@Ismael Mousa](https://www.linkedin.com/in/ismaelmousa/) - feel free to contact me!
