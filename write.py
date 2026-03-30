f=open("one.txt", "w") 
f.write("Hello Students\n")
f.write("Welcome to Python file handling.\n")
f.write("Learning is fun!\n")
f.close()

f=open("one.txt", "a")
f.write("This line is added at the end.\n")
f.close()

f=open("topics.txt", "w")
lines = [
"Python Programming\n",
"File Handling\n",
"Error Handling\n",
"Exception Handling\n"
]
f.writelines(lines)
f.close()

