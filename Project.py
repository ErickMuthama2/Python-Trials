class car:
    def __init__(self,modelname,year):
        self.modelname = modelname
        self.year = year
    def display(self):
        print(self.modelname,self.year)

cl=car("Toyota",2016)
cl.display()

class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print(self.name,self.id)

ni=employee("Erick Muthama",33805381)
ni.display()

class team:
    def __init__(self,teamname,position):
        self.teamname=teamname
        self.position=position
    def display(self):
        print(self.teamname,self.position)

tm=team("Manchester United",2)
tm.display()

print("Enter 1 for Circle")
print("Enter 2 for Rectangle")
print("Enter 3 for Triangle")
ch=int(input("Enter your choice: "))
if ch==1:
    r=int(input("Enter your radius in cm:"))
    area=3.14*r**2
    print(f"area of the circle is {area} cm squared")
elif ch==2:
    l=int(input("Enter your length in cm:"))
    w=int(input("Enter your width in cm:"))
    area=l*w
    print(f"Your area of rectangle is {area} cm squared")
elif ch==3:
    b=int(input("Enter your base in cm:"))
    h=int(input("Enter your height in cm:"))
    area=0.5*b*h
    print(f"Your area of Triangle is {area}")
elif ch!=(1,2,3):
    print(f"invalid choice kindly retry again ")

while True:
    user_input = input("Enter a valid input: ")

    if user_input.isnumeric():
        # Check if the input is a valid number
        user_input = int(user_input)
        break  # Exit the loop if valid input is provided
    else:
        print("Invalid input. Please try again.")

class teacher:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print(self.name,self.id)

tch=teacher('Fredrick Musyoki',33805381)
tch.display()        



