print("Hello world")

#let variable = 21

variable = 21
last_name = "Chavez"
total = 12.99
age = 137
found = True
name = "Mauricio"

#if / else
# if (var == var2){
#logic
#}
#this is a test
if age < 100:
    print("dont worry your'e not that old")
    print("this is only a example")
elif age == 100:
    print("congrats your'e a century")
else:
    print("Sorry, seems that youre old!")

#function 

def say_hello():
    print("Hello")

def say_goodbye(name):
    print("Goodbye "+name)

#call function
say_hello()
say_goodbye("Mauricio")

#concatenation
print("Hello my name is "+name+" and i have "+str(age)+" years old")

print(f"hello my name is {name} and i have {age} years old")

#array
#list
color = ["white","red","black","blue"]
numberList = [1,2,3]
print(color)
#add
color.append("pink")
print(color)
#travel the list 

for temp in numberList:
    print(temp)
#for(int i = 0; i < color.length; i++)
    #let color = color[i]
    #console.log(color)
print(color[0])
#dictionary
me = {
    "name": "Mauricio",
    "last_name": "Chavez",
    "age": 21,
    "month":"june",
}
print(me["name"])

me["age"] = 22
me["color"] = "yellow"
print(me)