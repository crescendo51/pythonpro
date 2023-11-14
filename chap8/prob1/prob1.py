print("Opening and closing the file.")
print('')
print("Reading characters from the file.")
text_file = open("read_it.txt", "r")
print(text_file.read(1))
print(text_file.read(5))
print('')
text_file.close()

print("Reading the entire file at once.")
text_file = open("read_it.txt", "r")
print(text_file.read())
print('')
text_file.close()

print("Reading characters from a line.")
text_file = open("read_it.txt", "r")
print(text_file.readline(1))
print(text_file.readline(5))
print('')
text_file.close()

print("Reading one line at a time.")
text_file = open("read_it.txt", "r")
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
print('')
text_file.close()

print("Reading the entire file into a list.")
text_file = open("read_it.txt", "r")
lines = text_file.readlines()
print(lines)
print(len(lines))
for line in lines:
    print(line)
print('')
text_file.close()

print("Looping through the file, line by line.")
text_file = open("read_it.txt", "r")
for line in text_file:
    print(line)
text_file.close()
