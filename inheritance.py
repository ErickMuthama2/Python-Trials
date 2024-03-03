class pet:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak(self):
        print('I dont know what I am saying')

class Dog(pet):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color=color

    def speak(self):
        print('Bark')

    def show(self):
        print(f'I am {self.name} and {self.age} years old and I am {self.color} color')

class cat(pet):
    def speak(self):
        print('meow')

p=Dog("Tim",24,"Black")
p.show()
p.speak()
