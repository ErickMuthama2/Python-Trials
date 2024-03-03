class Team:
    def __init__(self,Name,Worth):
        self.Name=Name
        self.Worth=Worth
    def display(self):
        print(self.Name,self.Worth)

tm=Team('Manchester United',450000)
tm.display()

for i in range(1,10):
    area=3.14*i**2
    print(f'Area of circle is {area} cm squared')

class president:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print(self.name,self.id)

p=president('Erick Muthama',33805381)
p.display()        


