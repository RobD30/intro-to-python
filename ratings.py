def scores_to_rate(score1,score2,score3,score4,score5):
    """
    Turns 5 scores into a rating by averaging the middle 3.
    """
    #TODO convert scores into numbers
    score1 = convert_tonumeric(score1)
    score2 = convert_tonumeric(score2)
    score3 = convert_tonumeric(score3)
    score4 = convert_tonumeric(score4)
    score5 = convert_tonumeric(score5)

    #TODO: Find the middle three scores

    #TODO: Take average of middle three scores
    average_score = #((score1 + score2 + score3) / 3)

    #TODO: Turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating