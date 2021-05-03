'''
# =============================================================================
#                        !!!52!!! - Classes, objects
# =============================================================================

class Car:
    #class variable Inside of class before other functions
    wheels = 4
    
    #instance variable beacuse inside of init
    def __init__(self):
        self.mil = 10
        self.com = 'BMW'
        
        
c1 = Car()
c2 = Car()

Car.wheels = 10

print(c1.mil, c1.com, c1.wheels)
print(c2.mil, c2.com, c2.wheels)
'''

# =============================================================================
#           !!!53!!! - Methods(instance, class, static)
# =============================================================================
'''
class Student:

    school = 'Telusko'

    
    def __init__(self, m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/ 3
            
    def get_m1(self):
        return self.m1
    #Instance mathod that Works with instances
    def set_m1(self,value):
        self.m1 = value
    #Class method that works with class
    @classmethod
    def Getschool(cls):
        return cls.school
     
    #STATIC METHOD *decorator required
    @staticmethod
    def info():
        print('This is student class... in abc module')        
        
        
        
s1 = Student(35,23,17)
s2 = Student(92,12,44)

# print(s1.avg())
# print(s2.avg())

print(s1.get_m1())
print(s1.Getschool())
print(s1.info())


'''

# =============================================================================
#                        !!!54!!! - Inner class (inside a class)
# =============================================================================
'''

class Student:
    
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        #WAZNE, ZEBY MIEC DOSTEP DO INNER CLASSY Z GŁOWNEJ
        self.lap = self.laptop()
        
    
    def show(self):
        print(self.name, self.rollno)
        self.lap.show()
    
    class laptop:
        
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8
        
        def show(self):
            print(self.brand,self.cpu,self.ram)

s1 = Student('Jakub', 35546)
s2 = Student('Sapura', 31242)

s1.show()



# print(s1.name, s1.rollno)
# print(s2.name, s2.rollno)

#ACCESS to the inner class

# lap1 = Student.laptop()
# lap2 = Student.laptop()

'''

# =============================================================================
#                        !!!55!!! - 
# =============================================================================

class Car:
    
    def __init__(self):
        self.brand = 'BMW'
        self.perfo = self.performance()
        
    def show(self):
        print(self.brand)
        self.perfo.show()
        
    class performance:
        
        def __init__(self):
            self.v_max = 330
            self.acceleraion = 5.4
            self.top_speed = 330
            self.interior = 3
        
        def show(self):
            print('v_max :' + str(self.v_max), 'top_speed :' + str(self.top_speed), 'interior :' + str(self.interior), 'acceleration :' + str(self.acceleraion))
            print('Car is interior ranges from 1 to 3, where 3 is the most exclusive interior. Your interior is {} '.format(self.interior))
            
        
    
# c1_per = Car.performance()
# c1_per.show()


c2 = Car()
c2.show()




# =============================================================================
#                           Class #55 - Inheritance
# =============================================================================

class A:
    
    def feature1(self):
        print('this is the feature number 1')
    def feature2(self):
        print('this is the feature number 2')
        
class B():
    
    def feature3(self):
        print('this is the feature number 3')
        
    def feature4(self):
        print('this is the feature number 4')

class C(A,B):
    
    def feature5(self):
        print('this is the feature number 3')
        

        

        

        
a1 = A()
b1 = B()
c1 = C()


c1.

# =============================================================================
#                           Class #56 Constructor in Inheritance
# =============================================================================



class A:
    
    def __init__(self):
        print('in A init')
    
    def feature1(self):
        print('this is the feature number 1')
        
    def feature2(self):
        print('this is the feature number 2')
        
class B():
    
    def __init__(self):
        print('in B init')
        super().__init__()
    
    def feature3(self):
        print('this is the feature number 3')
        
    def feature4(self):
        print('this is the feature number 4')
        
class C(A,B):
    
    def __init__(self):
        print('in C init')
        super().__init__()
    
    def feature5(self):
        print('this is the feature number 5')
        
    def feature6(self):
        print('this is the feature number 6')
        
    def feat(self):
        super().__init__()

a1 = C()
a1.

a1.feat()


#supper class allows you to gain the access of the upper class method.
#, However it takes the left one as first in case of two.




# =============================================================================
#           Introduction to pylomorphism #57
            #Duck Typing  #58
# =============================================================================
class PyCharm:
    
    def execute(self):
        print('doing some shit1')
        print('doing some shit2')
        
class My_ide:
    
    def execute(self):

        print('doing some shit1')
        print('doing some shit2')  
        print('I jeszcze wincej')

class Laptop:
    
    def code(self, ide):
        ide.execute()
   
ide = My_ide()
     
x1 = Laptop()
x1.code(ide)
        

class Nissan:
    
    def execute(self):
        print('Nissan')

class BMW:
    
    def execute(self):
        print('BMW')

class Samochod:
    
    def car(self, model):
        model.execute()


model = Nissan()
c1 = Samochod()
c1.car(model)

# =============================================================================
#                       #59 Operator Overloading
# =============================================================================


class Student:
    
    def __init__(self, m1, m2):
        
        self.m1 = m1
        self.m2 = m2
        
    def __add__(self,other):
        
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
    
        return s3
    
    
s1 = Student(12,22)
s2 = Student(26,33)



s3 = s1 + s2
print(s3.m1)




class Car:
    
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
        
    def __add__(self, other):
        value1 = self.value1 + other.value1
        value2 = self.value2 + other.value2
        
        x3 = Car(value1,value2)
        
        return x3


c1 = Car(22,45)
c2 = Car(33,88)

x3 = c1 + c2
print(x3.value2+ x3.value1)



class Car2:
    
    def __init__(self, z1, z2):
        self.z1 = z1
        self.z2 = z2
        
    def __sub__(self, other):
        z1 = self.z1 - other.z1
        z2 = self.z2 - other.z2
        
        z3 = Car2(z1,z2)
        
        return z3
    
c1 = Car2(34,26)
c2 = Car2(22,11)
c3 = c2 - c1


print(c3.z1)

#mult

class Car3:
    
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        
    def __mul__(self, other):
        v1 = self.v1 * other.v1
        v2 = self.v2 * other.v2
        v3 = Car3(v1,v2)
        
        return v3

    def __gt__(self,other):
        v1 = self.v1 * other.v1
        v2 = self.v2 * other.v2
        
        if v1 > v2:
            True
        else:
            False
            
    def __str__(self):
        return self.v1, self.v2
    
    
        
c1 = Car3(2,5)
c2 = Car3(3,6)

x = c1.v1 * c1.v2
y = c2.v1 * c2.v2
if x > y:
    print(x)
    
a = 9
print(a)

print(c1.__str__())




    


c3 = c1 * c2


if c1 > c2:
    print('Car 1 wins')
else:
    print('Car 2 wins')
    


# =============================================================================
#                       #60 
# =============================================================================
    
class Student:
    
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    #METHOD OVERLOADING    
    def summ(self,a = None, b = None, c = None):
        
        s = 0

        
        if a!= None and b!= None and c!= None:
            s = a+b+c
        elif a!= None and b!= None:
            s = a+b
        else:
            s = a
            
        return s
  
s1 = Student(22,54)

print(s1.summ(2))



class A:
    
    def show(self):
        print('in A show')
class B(A):
    def show(self):
        print('in B show')
        

a1 = B()
a1.show()


# =============================================================================
#                   #61 Iterator 
# =============================================================================


class top10:

    def __init__(self):
        self.num = 1
        
    def __iter__(self):
        return self
    
    
    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num +=1

            return val
        else:
            raise StopIteration
    
values = top10()
print(values.__next__())

for i in values:
    print(i)
    

    

# =============================================================================
#               #62 Generators
# =============================================================================
    
def topten():
    n = 1
    while n <= 10:
        sq = n*n
        yield sq
        n +=1
        

values = topten()


for i in values:
    print(i)
    

# =============================================================================
#             #63  Execution handling
# =============================================================================
    
a = 5 
b = 2




try:
    print('resource open')
    print(a/b)
    k = int(input('Enter a number'))
    print(k)
except ZeroDivisionError as e:
    print('Hey, you cannot divide the number by 0, error is {}'.format(e))
    
except ValueError as e:
    print('Invalid input {} '.format(e))
    
except Exception as e:
    print('something went wrong, {}'.format(e))
    
    

finally:
    (print('resouce close'))
    
#finally execustes even if there is an error or not, no need to put it both sides


# =============================================================================
#               #64 -  #Multithreading
# =============================================================================

from threading import *
from time import sleep



class Hello(Thread):
    
    def run(self):
        for i in range(5):
            print('hello')
            sleep(0.5)
    
    
class Hi(Thread):
    
    def run(self):
        for i in range(5):
            print('Hi')
            sleep(0.5)

            
t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()

#Method must have a name of 'run' if we wish to use start function from threading class.
#join forces the processes to wait for eachother until they finish working, then executes the rest of the code.

print('bye')


# =============================================================================
#                   #65 File handling
# =============================================================================

f = open('blob.py', 'r')
f1 = open('abc', 'w')
for data in f:
    f1.write(data)

f2 = open('abc', 'r')
f2.readlines()

# =============================================================================
#                       #66,67 - LECTURES ABOUT THE COMMENTS
# =============================================================================

# =============================================================================
#               #68 Linear Search using Python
# =============================================================================
# pos = -1

# def search(list,number):
#     i = 0
#     while i < len(list):
#         if number == list[i]:
#             globals()['pos'] = i
#             return True
#         i += 1
#     return False

def search2(list,numer):
    for i in range(len(list)):
        if list[i] == number:
            return print(i)
    else:
        print('hwdp')
            

list = [1,2,3,4,5,6]
number = 2

# if search(list,number):
#     print('Found at ', pos+1)
# else:
#     print('Not fund')
    
search2(list,number)

# =============================================================================
#                   #69 Binary search 
# =============================================================================
list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
number = 14


pos = -1

def search(list,number):
    lower = 0
    upper = len(list)-1
    if number not in list:
        print('the number you are searching for is not in the list')
    else:
    
        while lower <= upper:
            mid = (lower + upper) // 2
            
            if number == list[mid]:
                globals() ['pos'] = mid
                return True
            else:
                if list[mid] < number:
                    lower = mid
                else:
                    upper = mid
        


#3,6
       
if search(list,number):
    print('found at {}'.format(pos+1))
else:
    print('index out of range')
    
    

# =============================================================================
#               Bubble sort using python #70 
# =============================================================================

# a  b
# a = t
# b = a
# b = t

list2 = []


def sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
                
    

list = [24,35,11,23,125,34,66,1,2,1245]



sort(list)
print(list)

#2

numbers = [154,23,2645,24,11,2,76,8,23]

def sort(numbers):
    for i in range(len(numbers)):
        min_val = i
        print('minimal_value set to {}'.format(i))
        for j in range(i,len(numbers)):
            print('comparing the lowest number in the sequence to the first one')
            if numbers[j] < numbers[min_val]:
                min_val = j
                print('minimalna wartość w rundzie {} to {}'.format(j,numbers[min_val]))
        #kopiowanie numbers[1] = 154
        temp = numbers[i]
        #ustawianie pierwszej liczby na najmniejsza czt.2,8,11 itd.
        numbers[i] = numbers[min_val]
        #ustawianie minimalnej vartości na liczbe pierwszą
        numbers[min_val] = temp
        
        
        
        print(numbers)




sort(numbers)



# =============================================================================
#                   Connecting ot MAriadB in Sub
# =============================================================================

import mysql.connector
mydb = mysql.connector.connect(host = '10.10.1.121', user= 'kuba', passwd = 'kalipso2')

mycursor = mydb.cursor()
mycursor.execute('show databases')

for i in mycursor:
    print(i)
    
































