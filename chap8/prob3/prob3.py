inputString = ''

text_file = open("write_it.txt", "w")
print("Input your string...")

while True :
    inputString = input(">> ")
    if inputString == 'Q' :
        break
    text_file.write(inputString + "\n")
text_file.close()
print("Write process has been finished")

print('')
print('')
print('')
print("Your inputs are below..")
text_file = open("write_it.txt", "r")
read_text = text_file.read()
print(read_text)

