# mini project on Calculator

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def true_div (a,b):
    if b==0:
        return "Error! Division by Zero"
    else:
        return a/b
def floor_div (a,b):
    if b==0:
        return "Error! Division by Zero"
    else:
        return a//b
def exponentiate(x, y):
    return x ** y
def mod (a,b):
    if b==0:
        return"Error! Division by Zero"
    else: 
        return a%b
def fact():
    a=int(input('Enter the value : '))
    fact=1
    for i in range(1,a+1):
        fact*=i
    return fact
def sqrt ():
    a=int(input('Enter the valeu : '))
    return a**(1/2)


print("Select operation:")
print("1. Addition")
print("2. Subtract")
print("3. Multiply")
print("4. TrueDivision")
print("5. FloorDivision")
print("6. Exponentiate")
print("7. Modulus")
print("8. Factorial ")
print("9. Square Root")

while True:
    choice = input("Enter choice (1/2/3/4/5/6/7/8/9): ")

    if choice in ('1', '2', '3', '4', '5','6','7'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", sub(num1, num2))
        elif choice == '3':
            print("Result:", mul(num1, num2))
        elif choice == '4':
            print("Result:", true_div(num1, num2))
        elif choice == '5':
            print("Result:", floor_div(num1, num2))
        elif choice == '6':
            print("Result:", exponentiate(num1, num2))
        elif choice == '7':
            print("Result:", mod(num1, num2))

    elif choice in ('8', '9'):
        

        if choice == '8':
            print("Result:", fact())
        elif choice == '9':
            print("Result:", sqrt())

    else:
        print("Invalid Input")

    another_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() not in 'yes':
        break
