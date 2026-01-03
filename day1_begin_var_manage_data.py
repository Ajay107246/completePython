# Write your code below this line
print("Hello, World!")  # print simple string on console
print("\nHello, World!\n\nHello, World!")  # new line in string
print("Hello, Concatinate" + "Hello, World!")  # concatinate two string
print("Hello, Concatinate" + " " + "Hello, World with space!")  # concatinate two
# print("space before print - error: Unexpected indentation Pylance")
print ("With space after print!")  # space after print
print("   Hello, World with space before print!")  # space before print
print("Hello, World with space after print!   .")  # space after print

# print direct Input from user
print("Hello " + input("Enter your input: ")) #output> Hello <user input>
# Variable hold the input from user
name = input("Enter your input for variable: ")
print("Hello " + name)  # output> Hello <name>

# overwrite variable value with string
name = "New Value"
print("Hello " + name)  # output> Hello New Value

# Length of string using len() function for name variable
length = len(name)
print("Length of variable " + name + " is: " + str(length))  # output length of string
print(len(input("Enter your input for length: ")))  # output length of string

# Variables, reusability of code and reading code easily
username = "vscode_user"
length_username = len(username)
print("Username is: " + username)   # output username
print("Length of username is: " + str(length_username))  # output length of username

# Switch value of two variables
a = 5
b = 10
print("Before Swap: a =", a, ", b =", b)
a, b = b, a  # swap values
print("After Swap: a =", a, ", b =", b)

# Band name generator
print("Welcome to the Band Name Generator.")
city = input("What's name of the city you grew up in? \n") #nsk
pet = input("What's your pet's name? \n") #pip
band_name = city + " " + pet
print("Your band name could be " + band_name) #output band name: <city> <pet>
