'''

age = 20

if age < 21:
    print('no beer for you! ')

name = 'ludan'

if name is 'lucy':
    print ('hey there lucy')
elif name is 'bruce':
    print ('hows going?')
elif name is 'lingling':
    print('i miss you')
else:
    print ('please sign up for the site!')

foods = ['egg', 'noodles', 'gas', 'oil']

for f in foods[1:]:
    print(f)
    print(len(f))

for b in range(5, 100, 3):
    print(b)

cup = 6

while cup < 10:
    print(cup)
    cup += 1
    cup = cup+1
'''

# comments

'''
magicnumber = 14

print('bruce', 9)

for n in range(101):
    if n is magicnumber:
        print(n, 'is a magic number!')
        break
    else:
        print(n)
'''
# homework

'''
for q in range(1, 100, 1):
    if q % 4 is 0:
        print(q)
'''

# continue:

'''
numbertaken = [2, 5, 6, 23, 6]

print('numbers that r still available:')

for a in range(1, 6):
    if a in numbertaken:
        continue
    print(a)
'''

# functions

'''
def bruce():
    print('dayum, functions are cool!')

bruce()

def coffee_drinking(cof):
    amount = cof / 6.468
    print(amount)

coffee_drinking(23)
coffee_drinking(0)

'''

# return values

'''
def allowed_dating_age(my_age):
    girls_age = my_age/2 + 7
    return girls_age

bruce_limit = allowed_dating_age(23)
chenmai_limit = allowed_dating_age(21)
print('bruce can date girl', bruce_limit, 'or older')
print('chenmai can date girl', chenmai_limit, 'or older')

'''

# default values for argument

'''
def get_gender(sex = 'unknown'):
    if sex is 'm':
        sex = 'male'
    elif sex is 'f':
        sex = 'female'
    print(sex)

get_gender('f')
get_gender('m')
get_gender()

'''

# variable scope

'''
a = 923

def corn():
    print(a)

def okay():
    print(a)

corn()
okay()

'''


# keyword arguments

'''
def cat (name='crystal', action='eat', food='bacon'):
    print(name, action, food)

cat()
cat('happy', 'made', 'by you')
cat( food= 'ertsdf', action='hit')

'''

# flexible number of argument

'''
def add_number(*args):
# we gona take a bunch of arguments but we dont know how many yet
    total = 0
    for a in args:
        total += a
    print(total)

add_number(3, 534, -243, 34)
add_number(34)
add_number(523)

'''

# unpacking arguments

'''
def health_calculator(age, noodles_ate, water_drunk):
    answer = (100-age) + (noodles_ate * 8) + water_drunk ** 2
    print(answer)

bruce = [21, 3, 10]

health_calculator(bruce[0], bruce[1], bruce[2])
health_calculator(*bruce)
'''

# a good story?? talking about sets

'''
groceries = {'cereal', 'milk', 'beer', 'lotion', 'beer'}
print(groceries)

if 'milk' in groceries:
    print('you already have milk hoss!')
else:
    print('oh yeah, you need milk!')
'''

# dictionary

'''
classmates = {'tony': ' cool but smells', 'happy': ' i think its part of life', '100': ' 123'}

print(classmates)
print(classmates['100'])

for k, c in classmates.items():
    print(k + c)
'''

# modules

'''
import tuna
import random

x = random.randrange(1, 1000)
print(x)
tuna.bruce()

'''

# download an image from the web

'''
import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + '.jpg'
    urllib.request.urlretrieve(url, full_name)

download_web_image('https://scontent-dfw1-1.xx.fbcdn.net/v/t1.0-0/p206x206/12141659_534556766703054_4133181235712795920_n.jpg?oh=78035bbc4b98724108035ce70d72b0a0&oe=57734044')

'''

# how to read and write files

'''
fw = open('bruce.txt', 'w')
# open a file and write to it
fw.write('writing some stuff in my text file\n')
fw.write('lets dance\n')
fw.close()

fr = open('bruce.txt', "r")
text = fr.read()
print(text)
fr.close()

'''

# download files from the web

'''

from urllib import request

goog_url = 'http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=3&e=12&f=2016&g=d&a=7&b=19&c=2004&ignore=.csv'

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    # connect
    csv = response.read()
    csv_str = str(csv)
    # make sure the data import is string, or save as string
    lines = csv_str.split('\\n')
    # seperate data into different lines
    dest_url = r'goog.csv'
    # save file to goog.csv file name on the computer
    fx = open(dest_url, 'w')
    # make a file in the computer
    for line in lines:
        fx.write(line + '\n')
    # write to the file
    fx.close()

download_stock_data(goog_url)


'''

# class and objects

'''

class Enemy:
    life = 3

    def attack(self):
        print('ouch!')
        self.life -= 1

    def checklife(self):
        if self.life <= 0:
            print('I am dead.')
        else:
            print(str(self.life) + ' life left.')


# object: a way to access to sth inside class

enemy1 = Enemy()
enemy2 = Enemy()

enemy1.attack()
enemy1.attack()
enemy1.checklife()
enemy2.checklife()

'''

# init


'''
class tuna:

    def __init__(self):
        print('okay lets do it!')

    def swim(self):
        print('lets swim!')

flipper = tuna()
flipper.swim()


class enemy:

    def __init__(self, x):
        self.energy = x

    def get_energy(self):
         print(self.energy)

jason = enemy(5)
sandy = enemy(30)


jason.get_energy()
sandy.get_energy()

'''

# class variable and

'''
class girl:

    gender = 'female' # default within class

    def __init__(self, name):
        self.name = name

r = girl('rachel')
s = girl('stanky')
print(r.gender)
print(s.gender)

print(r.name)


'''

# inheritance (getting sth from someone else)


'''
class parent():

    def print_last_name(self):
        print('roberts')

class child(parent):
    # look for parent class and get everything from that class.

    def print_frist_name(self):
        print('bucky')

    def print_last_name(self):
        # change last name to bruce other than roberts. (over writing)
        # replace old name from parent class to new class name which is bruce.
        print('bruce')


bruce = child()
bruce.print_frist_name()
bruce.print_last_name()


'''

