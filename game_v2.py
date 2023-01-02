"""Game guess a number"""

import numpy as np

def random_predict(number:int=1) -> int:
    """random guessing a number

    Args:
        number (int, optional): guessed number. Defaults to 1.

    Returns:
        int: count of tries
    """
    
    count = 0
    
    while True:
        count+=1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
    return count
print(f'Number of tries: {random_predict()}')

def score_game(random_predict) -> int:
    """_summary_

    Args:
        random_predict ([type]): guessing function

    Returns:
        int: middle number og tries
    """
    
    count_is = [] # list for saving number of tries
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_is.append(random_predict(number))
        
    score = int(np.mean(count_is))
    
    print(f'your algoryyhm guesses a number for: {score} tries!')
    return(score)
score_game(random_predict)

if __name__ == '__main__':
    score_game(random_predict)