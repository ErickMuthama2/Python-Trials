class student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade    #0-100
    def get_grade(self):
        return self.grade
    
class course:
    def __init__(self,name,max_students):
        self.name=name
        self.max_students=max_students
        self.students=[]

    def add_student(self,student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False   
        
    def get_average_grade(self):
        value=0
        for student in self.students:
            value += student.get_grade()

        return value/len(self.students) 

s1=student("Erick",24,89)
s2=student("Tim",22,67)
s3=student("Brayo",25,78)
s4=student("Fred",20,80)
s5=student("Timo",27,90)
cr=course("Statistics",5)
cr.add_student(s1)
cr.add_student(s2)
cr.add_student(s3)
cr.add_student(s4)
print(cr.add_student(s5))
print(cr.get_average_grade())
