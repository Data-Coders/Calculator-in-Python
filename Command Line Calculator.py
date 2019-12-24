print('--- Alex\'s Calculator ---')
print('1. ADDition')
print('2. SUBstraction')
print('3. MULtiply')
print('4. DIVide')
print('5. EXIT')
x = int(input())

command = ' Enter Your Two numbers To Perform The Operation : '
def ini():
    a = int(input())
    b = int(input())
    return a, b
def resultoo():
    result = ' Your Result after Performing The Operation from {} and {} is {}'
    print(result.format(a,b,c))
    print(' Want To Continue If Yes then Enter Your Choice else Press any number exept 1 - 4')
    x = int(input())
    return x

while x < 5:
    if x == 1:
        print(command)
        a, b = ini()
        c = a + b
        x = resultoo()
    elif x == 2:
        print(command)
        a, b = ini()
        c = a - b
        x = resultoo()
    elif x == 3:
        print(command)
        a, b = ini()
        c = a * b
        x = resultoo()
    elif x == 4:
        print(command)
        a, b = ini()
        c = a / b
        x = resultoo()
    elif x < 5:
        break