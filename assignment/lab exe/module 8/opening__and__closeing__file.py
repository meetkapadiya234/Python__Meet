# Example of opening and closing a file in Python

# Opening a file in write mode
file = open("example.txt", "w")

# Writing text to the file
file.write("Hello, this is a sample text.\n")
file.write("Python file handling is easy!")

# Closing the file
file.close()

print("Text has been written to the file successfully.")
