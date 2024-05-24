num1 = float(input('Enter 1st Number: '))

def adddition_(num1,num2):
    sum = num1 + num2
    return sum

def subtraction_(num1,num2):
    diff = num1 - num2
    return diff

def multiplication_(num1,num2):
    prod = num1 * num2
    return prod

def multiplication_per(num1,num_per):
    prod_per = num1 * (num_per/100)
    return prod_per

def division_(num1,num2):
    quot = num1 / num2
    return quot

while True:
    opp_input = input('Enter Operator: ')
    
    if opp_input == '+':
        num2 = float(input('Enter 2nd Number: '))
        answer = adddition_(num1,num2)
        print(answer)
        break
    elif opp_input == '-':
        num2 = float(input('Enter 2nd Number: '))
        answer = subtraction_(num1,num2)
        print(answer)
        break
    elif opp_input == '*':
        num2 = input('Enter 2nd Number: ')
        if '%' in num2:
            num_with_percentage = num2.strip('%')
            num_per = float(num_with_percentage)
            answer = multiplication_per(num1,num_per)
            print(answer)
            break
        else:
            num2 = float(num2)
            answer = multiplication_(num1,num2)
            print(answer)
            break
    elif opp_input == '/':
        num2 = float(input('Enter 2nd Number: '))
        answer = division_(num1,num2)
        print(answer)
        break
    else:
        print('Invalid Input, Pls. Input the appropriate opperator')
    

