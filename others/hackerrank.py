#Hacker Rank - Nested Lists
name = ['Harry','Berry','Tina','Akriti','Harsh','Kuba','Agata','Jacek','Grzegorz']
score = 37.21,37.21,37.2,41,39, 12, 24, 35, 77

dicto = dict(zip(name,score))
numbers = sorted(dicto.values())[:2]
names = []
count = 0

for number in numbers:
    for key,value in dicto.items():
        if number == value:
            names.append(key)
          
names = names[:2]
names.sort()
print(names)



ijput = 1,2,2

ijput = hash(tuple(ijput))
print(ijput)


text = 'HackerRank.com presents "Pythonist 2".'

def swap_case(s):
    chars = str()
    for char in s:
        if char.isupper():
            char = char.lower()
        else:
            char = char.upper()
        chars = chars + char
        
    return chars
a = 'Ross'
b = 'Taylor'

def print_full_name(a, b):
    print("Hello {} {}! You just delved into python.".format(a,b))


string = 'ASDASDASDASDASDDDDFSDGHGDGFHFGHFDFGDFGSDFS'
k = 2

def merge_the_tools(string, k):
    len_str = len(string)
    quehaches = k
    k = k
    #how manny in one list.
    x = len_str/k
    beginning = 0
    a = []
    b = []
    c = []
    #klocek "A"
    for i in range(beginning,k):
        if string[i] not in a:
            a.append(string[i])
    beginning = beginning + quehaches
    k = k + k
    for i in range(beginning,k):
        if string[i] not in b:
            b.append(string[i])
            
    beginning = beginning + quehaches
    k = k + quehaches
           
    for i in range(beginning,k):
        if string[i] not in c:
            c.append(string[i])
    #printing        
    
    a = ''.join(a)
    b = ''.join(b)
    c = ''.join(c)
    print(a)
    print(b)
    print(c)
'''https://www.hackerrank.com/challenges/merge-the-tools/problem'''

string = 'AABCAAADA'
k = 3

def merge_the_tools(string,k):
    beg = []
    end = []
    for i in range(0, len(string), k):
        chars = []
        for char in string[i:i+k]:
            if char not in chars:
                chars.append(char)
        chunk=''.join(chars)
        print(chunk)    
    
    
    
    
    


