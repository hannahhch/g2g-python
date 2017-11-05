#first argument is always "self", a bit like "this"
class Greeter:
    def __init__(self, greeting):
        self.greeting = greeting

    def greet(self, name):
        print(self.greeting + ", " + name + "!")

#JS example: new Greeter("Hello")
#Ruby example: Greeter.new("Hello")

english_greeter = Greeter("Hello")
spanish_greeter = Greeter("Hola")

spanish_greeter.greet("Remy")
