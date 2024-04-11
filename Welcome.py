welcome = input("Please type your first name: ")

print("Hello", welcome + " to my first vs code .py file")

while True:
    hello = input("Please input a number: \n1 - Who are you?\n2 - How are you?\n3 - Where are you?\n4 - End program.\n\t")
    if hello == "1":
     print("I am a Student from NFH\n")
    elif hello == "2":
     print("Im at school that should say enough..\n")
    elif hello == "3":
     print("Why you asking?\n")
    else:
      break

print("Bye bye\n")