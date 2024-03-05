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