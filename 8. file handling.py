"""File opening and reading content"""
f = open("summary.txt", "r")
content = f.read()
print(content)
print("                                     ")
"""properties of file handling"""
print("Filename:", f.name)
print("Mode:", f.mode)
print("File opened or closed??",f.closed)







"""Read particular lines from file"""
def file_read_any_text(fname, lines):

        from itertools import islice

        with open(fname) as f:
                for line in islice(f, lines):
                        print(line)
"""It prints the lines till 2nd lines"""
file_read_any_text('summary.txt',2)





"""With statement file opening and reading content"""
with open("summary.txt", "r") as file:
    content = file.read()
    print(content)




"""With statement file opening and reading content"""
with open("summary.txt", "w") as file:
   file.write("\nAdding another line for Python as it is interpreter friendly")
   #file.seek(0)
with open("summary.txt", "r") as f:
        content = f.read()
        print(content)
file.close()





"""With statement file opening and reading content"""
with open("summary.txt", "a") as file:
   file.write("\nAdding another line for Python as it is interpreter friendly")
   #file.seek(0)
with open("summary.txt", "r") as f:
        content = f.read()
        print(content)
file.close()









with open("summary.txt", "r+") as f:
      f.write("This is Python file handling class.\n")
      f.write("This is very helpful.")
      # seek() function is used if read/write mode of file and acts as file pointer.
      # If file is already written the pointer always stays at end of the line, seek () helps to reposition.
      f.seek(0)
      content = f.read()
      print(content)
     





with open("summary1.txt", "w+") as f:
      f.write("This is Python file handling class.\n")
      f.write("This is very helpful.")
      # seek() function is used if read/write mode of file and acts as file pointer.
      # If file is already written the pointer always stays at end of the line, seek () helps to reposition.
      f.seek(0)
      content = f.read()
      print(content)






with open("summary.txt", "a+") as f:
      f.write("This is Python file handling class.\n")
      f.write("This is very helpful.")
      # seek() function is used if read/write mode of file and acts as file pointer.
      # If file is already written the pointer always stays at end of the line, seek () helps to reposition.
      f.seek(0)
      content = f.read()
      print(content)
     
