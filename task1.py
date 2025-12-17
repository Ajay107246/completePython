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
