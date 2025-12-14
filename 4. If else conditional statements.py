# if condition 


marks=20;
if marks>=20:
    print("pass");
else:
    print("fail")



# if elif else 



# score=int(input("enter the score:"));
# if score>=90:
#     print("grade A")
# elif score>=40 and score<90:
#     print("grade B")
# elif score>=20:
#     print("grade c")
# else:
#     print("fail grade")


# ternary operator ley chae eutae line ma if elif ko kaam gardinxa 

score=80
if score>=40: print("pass")


score = 50
result = "pass" if score >= 40 else "fail"


# python  match case statement 

# number = int(input())

# print(f"entered number is: {number}")

# if number % 2 == 0:
#     print("even")
# else:
#     print("odd")



# city = input("Enter the name of city: ")

# if city.lower() == 'delhi':
#     print("Monument of Delhi is: Red Fort")
# elif city.lower() == 'agra':
#     print("Monument of Agra is: Taj Mahal")
# elif city.lower() == 'odisha':
#     print("Monument of Odisha is: Puri Temple")
# elif city.lower() == 'kolkata':
#     print("Monument of Kolkata is: Howrah Bridge")
# else:
#     print("Enter the correct choice of the city")


'''
noOfDays=int(input("enter total numbe of working days")
)

noOfAbs=int(input("enter total number od days absent"))

percentage=(noOfDays-noOfAbs)/noOfDays*100

print("your attendance is",percentage)

if percentage<80:
    print("you are not able to sit in an examination ")
else:
    print("you are eligiible to attend the examination")

'''

'''
import math 

minx=min(4,5,10)
maxx=max(4,6,10)
print("minx value:",minx)
print("maxx value:",maxx)

miny=min(12,8,10)
maxy=max(12,8,10)

print("miny value:",miny)
print("maxy value:",maxy)


if minx==miny:
    print("equal")
elif max==maxy:
    print("equal")
else:
    print("not equal")

    '''


str=" this is python programming"

if "python" in str:
    print("the string contains the word 'python")
else:
    print("the string doesnot contain the word python")



# string operations 


# string length 
my_str="hello python"
length=len(my_str)
print(length)

# string upper and lower 
my_str="hello python"
uppertxt=my_str.upper()
lowertxt=my_str.lower()
print(uppertxt)
print(lowertxt)


# strip function 

my_str= "hello python"
# strip function ley extra space remove gardinxa
stripped_txt=my_str.strip()
print(stripped_txt)


my_str="hello python programming"
split_txt=my_str.split()
print(split_txt)



# join function 

word_list=["hello","python"]
joined_txt="".join(word_list)
print(joined_txt)


# replace function 

original= "I like python programming classes"
new= original.replace("prograaming", "coding")
print(new)


# find/index function 

txt=" i like pytho programming classes"
position=txt.find("py")
print("the position is :", position)

# startswith/endwith

filename="pythonFile.py"
fileendType=filename.endswith(".py")
filestartType=filename.startswith("Py")
print(fileendType)
print(filestartType)



# count function 


text= "pineApple"
count_text=text.count('p')
print(count_text)



# match case statement
month=7
match month:
    case 1:
        print("january")
    case 2:
        print("february")
    case 3:
        print("march")
    case 4:
        print("april")
    case 5:
        print("may")
    case 6:
        print("june")
    case 7:
        print("july")
    case 8:
        print("august")
    case 9:
        print("septemeber")
    case 10:
        print("october")
    case 11:
        print("november")
    case 12:
        print("december")


# case for default match case 

day=4
match day:
    case 6:
        print("today is saturday")
    case 7:
        print("today is sunday")
    case _:
        print("Looking for a weekend")

# using piping in match case 


day=4
match day:
    case 1|2|3|4|5:   #| bhaneko or ho
        print("today is weekday")
    case 6|7:
        print("i love weekeand")






class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

def describe_color(color_obj):
    match color_obj:
        case Color(r=255, g=0, b=0):
            return "pure red"
        case Color(r=0, g=255, b=0):
            return "pure green"
        case _:
            return "unknown color"

red = Color(255, 0, 0)
green = Color(0, 255, 0)

print(describe_color(red))
print(describe_color(green))


