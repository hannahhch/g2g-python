a = 1

if a == 2:
    print("a is equal to 2")
elif a == 1:
    print("a is equal to 1")
else:
    print("a is not equal to 2")

for x in [1, 2, 3]:
    print("x = " + str(x))

def hello(name):
    print("Hello, " + name)

hello("Phoenix")
hello("Sage")

def print_even_or_odd(num):
    if num == 0:
        print("0 is zero")
    elif num % 2 == 0:
        print(str(num) + " is even")
    else:
        print(str(num) + " is odd")

print_even_or_odd(0)
