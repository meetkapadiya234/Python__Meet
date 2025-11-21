# Example of reading and writing to a file in Python

# Opening the file in read mode
file = open("example.txt", "r")

# Reading the contents of the file
contents = file.read()

# Printing the contents
print("File contents:")
print(contents)

# Closing the file
file.close()


# /// Now, writing multiple strings to the file

# Opening a file in write mode
file = open("example.txt", "w")

# Writing multiple strings to the file
file.write("Hello, this is the first line.\n")
file.write("This is the second line.\n")
file.write("Python makes file handling easy!\n")

# Closing the file
file.close()

print("Multiple strings have been written to the file successfully.")
