""" Game Guess the number
The computer takes the number itself and guesses the number """


import numpy as np


def random_predict(number: int=1) -> int:
    """Randomly guess the number

    Args:
        number (int, optional): The hidden number. Defaults to 1.

    Returns:
        int: Сount of attempts
    """
    count = 0
    down, up = 1, 101
    
    while True:
        count += 1
        predict_number = np.random.randint(down, up)
        
        if predict_number > number:
            up = predict_number
        elif predict_number < number:
            down = predict_number + 1
        else:
            break # predict_number == number
    
    return count


def score_game(random_predict) -> int:
    """ Determining the number of attempts to guess a number for 1000 times

    Args:
        random_predict ([type]): number guessing function

    Returns:
        int: average number of attempts
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=1000)
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    print(f'Your algorithm guesses the number on average for {score} attempts!')
    return score


if __name__ == "__main__":
    score_game(random_predict)

