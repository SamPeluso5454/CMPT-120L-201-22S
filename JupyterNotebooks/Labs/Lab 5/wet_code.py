# We're looking to find out how much money we have after a day with friends on Saturday. 
# Our code does the trick but we learned about keeping out code DRY recently and want to make it more efficent by making it DRY.
# I want you to accomplish this by making functions where you see repeated code. 
# Some things to note. When we have a positive number that gets split up and 85% goes into checking and 15% goes into savings. 
# All negative numbers gets taken out of the checking account.


from typing import Tuple


def saturdays_bank_transactions(transations) -> Tuple[float, float]:
    savings = 1096.25
    checking = 1590.80

    checking += (transations[0] * 0.85)
    savings += (transations[0] * 0.15)
    
    checking += transations[1]
    
    checking += transations[2]
    
    checking += transations[3]

    checking += (transations[4] * 0.85)
    savings += (transations[4] * 0.15)
    
    checking += (transations[5] * 0.85)
    savings += (transations[5] * 0.15)

    checking += transations[6]
    
    checking += transations[7]
    
    checking += transations[8]
    
    checking += transations[9]
    
    checking += transations[10]

    return checking, savings

if __name__ == "__main__":
    transations = [300.00, -50.00, -5.00, -20, 15.72, 2083.93, -1034.00, -420.00, -5.23, -15.93, -72.90]
    new_balance = saturdays_bank_transactions(transations)
    print("Your new checking balance is:", '${:.2f}'.format(round(new_balance[0], 2)), "\nYour new savings balance is: ", '${:.2f}'.format(round(new_balance[1], 2)))