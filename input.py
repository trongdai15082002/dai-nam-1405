age = input("How old are you?")
name = input("What your name?")

message = "I am {}. I am {} years old."
#print("I am " + name + ". I am 20" + age +" years old.")
print(message.format(name, age))