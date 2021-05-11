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



'''https://www.hackerrank.com/challenges/merge-the-tools/problem'''

#merge-the-tools
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
    
'''https://www.hackerrank.com/challenges/the-minion-game/problem'''
#The-Minion-Game

string = 'BANANA'
#players:
#Stuart has to make words starting with consotans.
#Kevin has to make words starting with vowels.
def Steuart(string):
    vowels = 'AEIOU' 
    characters = []
    words = []
    check_list = []
    score = 0
    for char in string:
        if char not in vowels:
            if char not in characters:
                characters.append(char)
    for x in characters:
        pos = string.find(x)
        numbers_left = len(string) - pos
        
        for i in range(numbers_left+1):
            y = string[pos: pos+i]string = 'BANANA'
#players:
#Stuart has to make words starting with consotans.
#Kevin has to make words starting with vowels.
def Steuart(string):
    vowels = 'AEIOU' 
    characters = []
    words = []
    check_list = []
    score = 0
    for char in string:
        if char not in vowels:
            if char not in characters:
                characters.append(char)
    for x in characters:
        pos = string.find(x)
        numbers_left = len(string) - pos
        
        for i in range(numbers_left+1):
            y = string[pos: pos+i]
            words.append(y)
    words = list(filter(lambda x : x != '', words))    
    
    for word in words[:len(string)]:
        x = len(word)
        for i in range(0,len(string)+1,x):
            if x > (len(string)/2):
                y = string[0:i]
                print(y)
                check_list.append(y)
                if i == 0 or i == 6:
                    pass
                else:
                    y = string[-i:]
                    print(y)
                    check_list.append(y)
            else:
                y = string[i:x+i]
                print(y)
                check_list.append(y)
                
    check_list = list(filter(lambda x : x != '', check_list))    
    
    for word in words:
        for i in range(len(check_list)):
            if word == check_list[i]:
                score = score +1
                print(score)
            
    return score
string = 'BANANA'
#players:
#Stuart has to make words starting with consotans.
#Kevin has to make words starting with vowels.
def Steuart(string):
    vowels = 'AEIOU' 
    characters = []
    words = []
    check_list = []
    score = 0
    for char in string:
        if char not in vowels:
            if char not in characters:
                characters.append(char)
    for x in characters:
        pos = string.find(x)
        numbers_left = len(string) - pos
        
        for i in range(numbers_left+1):
            y = string[pos: pos+i]
            words.append(y)
    words = list(filter(lambda x : x != '', words))    
    
    for word in words[:len(string)]:
        x = len(word)
        for i in range(0,len(string)+1,x):
            if x > (len(string)/2):
                y = string[0:i]
                print(y)
                check_list.append(y)
                if i == 0 or i == 6:
                    pass
                else:
                    y = string[-i:]
                    print(y)
                    check_list.append(y)
            else:
                y = string[i:x+i]
                print(y)
                check_list.append(y)
                
    check_list = list(filter(lambda x : x != '', check_list))    
    
    for word in words:
        for i in range(len(check_list)):
            if word == check_list[i]:
                score = score +1
                print(score)
            
    return score

            words.append(y)
    words = list(filter(lambda x : x != '', words))    
    
    for word in words[:len(string)]:
        x = len(word)
        for i in range(0,len(string)+1,x):
            if x > (len(string)/2):
                y = string[0:i]
                print(y)
                check_list.append(y)
                if i == 0 or i == 6:
                    pass
                else:
                    y = string[-i:]
                    print(y)
                    check_list.append(y)
            else:
                y = string[i:x+i]
                print(y)
                check_list.append(y)
                
    check_list = list(filter(lambda x : x != '', check_list))    
    
    for word in words:
        for i in range(len(check_list)):
            if word == check_list[i]:
                score = score +1
                print(score)
    return score



def minion_game(string):

    

print('{} '.format(name_of_the_winne), score)

#This one gave me headache
for word in words[:len(string)]:
    x = len(word)
    for i in range(0,len(string)+1,x):
        if x > (len(string)/2):
            y = string[0:i]
            print(y)
            if i == 0 or i == 6:
                pass
            else:
                y = string[-i:]
                print(y)
        else:
            y = string[i:x+i]
            print(y)
        
'''     
['B', 'BA', 'BAN', 'BANA', 
 'BANAN', 'BANANA', 'N', 
 'NA', 'NAN', 'NANA']  
'''
dictio = dict(enumerate(characters))

unique = []

for word in words:
    x = len(word)
    
    for i in range(string.find(characters[1]),len(string)+1,x):
        if x > (len(string)/2):
            y = string[0:i]
            unique.append(y)
            if i == 0 or i == 6:
                pass
            else:
                y = string[-i:]
                unique.append(y)
        else:
            y = string[i:x+i]
            unique.append(y)
            

S = 'BANANA'
n = len(S)

# consonents
stuart = 0

# vowels
kevin = 0

for i in range(n):
    if S[i] in ('A', 'E', 'I', 'O', 'U'):
        kevin += n - i
    else:
        stuart += n - i

if kevin > stuart:
    print('Kevin', kevin)
elif stuart > kevin:
    print('Stuart', stuart)
else:
    print('Draw')
    