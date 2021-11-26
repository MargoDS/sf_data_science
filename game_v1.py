""" Game Guess the number"""

import numpy as np

number = np.random.randint(1, 101)

count = 0

while True:
    count += 1
    predict_number = int(input("Guess the number from 1 to 100: "))
    
    if predict_number > number:
        print("The number must be less then")
        
    elif predict_number < number:
        print("The number must be greater then")
    
    else:
        print(f"Congratulations! You guessed the number! Number = {number}, count of attempts - {count}")
        break
        

