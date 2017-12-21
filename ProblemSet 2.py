'''
PROBLEM 1:
	Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by
	the credit card company each month.
	The following variables contain values as described below:
	    balance - the outstanding balance on the credit card
	    annualInterestRate - annual interest rate as a decimal
	    monthlyPaymentRate - minimum monthly payment rate as a decimal
	
	For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. 
	Be sure to print out no more than two decimal digits of accuracy - so print
		Remaining balance: 813.41
	instead of
		Remaining balance: 813.4141998135 
	
	So your program only prints out one thing: the remaining balance at the end of the year in the format:
		Remaining balance: 4784.0
	
	A summary of the required math is found below:
    	Monthly interest rate= (Annual interest rate) / 12.0
    	Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
    	Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
    	Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
'''
unpaid = 0

for i in range(13):
    #Gera um vetor de 13 posições (0 a 12)
    if i == 0:
        unpaid = balance - balance*monthlyPaymentRate
    else:
        balance = unpaid + (annualInterestRate/12.0)*unpaid
        unpaid = balance - balance*monthlyPaymentRate
        
print("Remaining balance: " + str(round(balance, 2)))



'''
PROBLEM 2:
	Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. 
	By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid
	each month.
	
	In this problem, we will not be dealing with a minimum monthly payment rate.
	The following variables contain values as described below:
	    balance - the outstanding balance on the credit card
	    annualInterestRate - annual interest rate as a decimal
	
	The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:
		Lowest Payment: 180 
	
	Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made).
	The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is possible for the balance to become negative
	using this payment scheme, which is okay. A summary of the required math is found below:
	    Monthly interest rate = (Annual interest rate) / 12.0
    	Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
    	Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
'''
lowest = 10

while True:
    in_bal = balance
    for i in range(12):
        if i == 0:
            unpaid = in_bal - lowest
        else:
            in_bal = (1 + annualInterestRate/12.0)*unpaid
            unpaid = in_bal - lowest
    if unpaid <= 0:
        break;
    lowest += 10

print("Lowest Payment: " + str(lowest))



'''
PROBLEM 3:
	You'll notice that in Problem 2, your monthly payment had to be a multiple of $10. Why did we make it that way? 
	You can try running your code locally so that the payment can be any dollar and cent amount (in other words, the monthly payment
	is a multiple of $0.01). Does your code still work? It should, but you may notice that your code runs more slowly, especially in cases with
	very large balances and interest rates. (Note: when your code is running on our servers, there are limits on the amount of computing time
	each submission is allowed, so your observations from running this experiment on the grading system might be limited to an error message
	complaining about too much time taken.)

	Well then, how can we calculate a more accurate fixed monthly payment than we did in Problem 2 without running into the problem of slow code?
	We can make this program run faster using a technique introduced in lecture - bisection search!
'''
m_rate = 0.2/12.0
upper = balance/12.0
lower = balance*((1+m_rate)**12)/12.0

while True:
    in_bal = balance
    guess = lower + (upper - lower)/2
    for i in range(12):
        if i == 0:
            unpaid = in_bal - guess
        else:
            in_bal = (1 + annualInterestRate/12.0)*unpaid
            unpaid = in_bal - guess
    if unpaid > 0.01:
        upper = guess
    elif unpaid < -0.01:
        lower = guess
    else:
        break
        
print("Lowest Payment: {:0.2f}".format(guess))