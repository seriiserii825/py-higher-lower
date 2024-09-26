def compareAnswer(answer, question_1, question_2):
    if answer == 'a':
        if question_1['follower_count'] > question_2['follower_count']:
            return True
        else:
            return False
    elif answer == 'b':
        if question_2['follower_count'] > question_1['follower_count']:
            return True
        else:
            return False
    else:
        return False
