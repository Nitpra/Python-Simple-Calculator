# This function Add two numbers
def add(a1, a2):
    return (a1+a2)
# This function Subtract two numbers
def subtract(a1, a2):
    return (a1-a2)
# This function Multipy two numbers
def multiply(a1, a2):
    return (a1*a2)
# This function Divide two numbers
def divide(a1, a2):
    return (a1/a2)



print('Select Operation')
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter Choice(1/2/3/4)")
    # Check if choice is one of the four options
    if choice in('1','2','3','4'):
        try:
            num1 = float(input('Enter num1: '))
            num2 = float(input('Enter num2: '))
        except ValueError:
            print('please check You have entered wrong number!')
            continue

        if choice == '1':
            print(num1, '+', num2, '=', add(num1,num2))

        if choice == '2':
            print(num1, '-', num2, '=', subtract(num1,num2))

        if choice == '3':
            print(num1, '*', num2, '=', multiply(num1,num2))

        if choice == '4':
            print(num1, '/', num2, '=', divide(num1,num2))

        new_calculation = input('You want to continue calculation(y/n): ')
        if new_calculation == 'n':
            break
    else:
        print('Invalid input')

