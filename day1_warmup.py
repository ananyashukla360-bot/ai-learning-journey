#Function refresher : 

#To enter numbers in list and print avg
from symtable import Class


L=list(map(int, input("Enter the numbers: ").split()))

def avg(l):
    return sum(l)/len(l)

#to enter a word and reverse it
S=list(map(str, input("Enter the words: ").split()))

def reverse(s):
    return s[::-1]
reverse_word = [reverse(word) for word in S]


#to create a func with default arg
#name = input("Enter your name: ") 
def greet(name,greeting = "fuck off"):
    return greeting + " " + name




#Dicts and lists refresher : 

people = []
n =int(input("Enter the number of people: "))   
for _ in range(n):
    name = str(input("Enter your name: "))
    age = int(input("Enter your age: "))
    skill = str(input("Enter your skill: "))
    person = dict(name=name, age=age, skill=skill)
    people.append(person)

t_skill = "ai"
print ([person['name'] for person in people if person['skill'] == t_skill])



#class refresher
class Note :
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def summary(self):
        return self.content[:50]

n = Note("Meeting Notes", "We discussed the project timeline and assigned tasks to each team member.")
print(n.title)      
print(n.summary())  

    
    
    
