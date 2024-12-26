# function
def greet(firstName, lastName): # parameter
    print(f'Hey {firstName} {lastName}') # formatting string
    print('Welcome aboard')


greet(firstName = 'John',lastName = 'Cena') # arguments
greet(lastName='Marry',firstName='Don') 


def square(number):
    return number * number 


print(square(number=2))