print("Creating a text file with the write() method.")
print('')
print("Reading the newly created file.")

text_file = open("write_it.txt", "w")
text_file.write("Line 1\n")
text_file.write("This is line 2\n")
text_file.write("That makes this line 3\n")
text_file.close()

text_file = open("write_it.txt", "r")
read_file = text_file.read()
print(read_file)
print("And that would make this third line.")
print('')
print('')
text_file.close()

print("Creating a text file with the writelines() method.")
print('')
print("Reading the newly created file.")

text_file = open("write_it.txt", "w")
lines = ["Line 1\n", "This is line 2\n", "That makes this line 3\n"]
text_file.writelines(lines)
text_file.close()

text_file = open("write_it.txt", "r")
read_file = text_file.read()
print(read_file)
