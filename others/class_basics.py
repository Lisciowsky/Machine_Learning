'''
class Robot:
    def __init__(self,g_name,g_color,g_weight):
        self.g_name = g_name
        self.g_color = g_color
        self.g_name = g_name
    
    def introduceSelf(self):
        print('My name is {}'.format(self.g_name))
        
r1 = Robot(g_name = "Tom", g_color = "blue", g_weight = "30")
r2 = Robot("Jerry", "Blue", 40)

# r1.introduceSelf()
# r2.introduceSelf()

class Person:
    def __init__(self, n, p, i):
        self.name = n
        self.personality = p
        self.is_sitting = i
        
    def sit_down(self):
        self.is_sitting = True
    def stand_up(self):
        self.is_sitting = False
        
p1 = Person("Alice", "agressive", False)
p2 = Person("Becky","talkative", True)

p1.robot_owned = r2
p2.robot_owned = r1


class Student:
    
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def introduce_self(self):
        print('I am {}'.format(self.name))
        
    def get_grade(self):
        return self.grade
        
    
class Course:
    import numpy as np
    
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        else:
            return False
        
    def add_average_grade(self):
        grade_number = 0
        for student in self.students:
            grade_number += student.get_grade()
        return f"{np.round(grade_number/len(self.students),2)}"    

s1 = Student("Jakub", 24, 95)
s2 = Student("Agata",29, 85)
s3 = Student("Paweł", 30, 70)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

for i in course.students:
    print(i.name)
print(course.add_average_grade())
'''
'''

class Pet:
    def __init__(self,name,age, bio):
        self.name = name
        self.age = age
        self.bio = bio
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.bio}")
        


class Cat(Pet):
    def __init__(self, name, age, color, bio):
        super().__init__(name,age, bio)
        self.color = color
       
    def speak(self):
        print("Meow")
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old, and I am {self.color} and I am {self.bio}")

        
class Dog(Pet):
    def speak(self):
        print("Bark")
        
p = Pet("Tim", 19, "Human")
c = Cat("Bill", 34, "black", "Cat")
d = Dog("jill",25, "Dog")


p.show()
c.show()
d.show()

'''
'''
class Person:
    number_of_people = 0
    
    def __init__(self,name):
        self.name = name
        Person.add_person()
    @classmethod
    def number_of_people_function(cls):
        return cls.number_of_people
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1
        
print(Person.number_of_people_function())
Person.add_person()
print(Person.number_of_people_function())

'''

class Math:
    
    @staticmethod
    def add5(x):
        return x+5
    
    @staticmethod
    def add10(x):
        return x+10
print(Math.add5(5) * Math.add10(10))
        
        




    

    


