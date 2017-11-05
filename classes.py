#first argument is always "self", a bit like "this"
class Greeter:
    """
    The Greeter class privdes a multi-lingual way to greet people.
    """
    def __init__(self, greeting="Hello", excited=True):
        self.greeting = greeting
        self.excited = excited

    def greet(self, name):
        punctuation = "."
        if self.excited:
            punctuation = "!"
        print(self.greeting + ", " + name + punctuation)



#JS example: new Greeter("Hello")
#Ruby example: Greeter.new("Hello")

english_greeter = Greeter()
spanish_greeter = Greeter("Hola")
french_greeter = Greeter(excited=False, greeting="Bonjour")

english_greeter.greet("Dorian")
spanish_greeter.greet("Remy")
french_greeter.greet("Kerry")

# multi-line string example
output = """
Rowan says, "Hello!"

Sawyer returns the greeting.
"""
print(output)
