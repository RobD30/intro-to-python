def convert_to_numeric(score):
    """
    Converts the scores into a numerical value
    """
    return float(score)


def sum_of_middle_three(score1, score2, score3, score4, score5):
    """
    Gives the sum
    """
    sum =
    return


def score_to_rating_string(score):
    """

    :return:
    """
    rating =
    return rating


def scores_to_rate(score1, score2, score3, score4, score5):
    """
    Turns 5 scores into a rating by averaging the middle 3.
    """
    # TODO convert scores into numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    # TODO: combined steps
    average_score = sum_of_middle_three(score1, score2, score3, score4, score5) / 3

    # TODO: Turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating
