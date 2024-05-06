# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("I am learning python as a programming language\n")
        file.write(" This is week 5. \n")
        file.write("Today's date is 06/05/2024\n")
    print("File created successfully.")
except Exception as e:
    print("Error creating file:", e)

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to read the file.")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Appending line 1\n")
        file.write("Appending line 2\n")
        file.write("Appending line 3\n")
    print("File appended successfully.")
except Exception as e:
    print("Error appending to file:", e)
finally:
    print("File handling completed.")