abc = "abcdefghijklmnopqrstuvwxyz"
shift = input("Please enter the number of characters you would like to shift: ")
while shift.isdecimal() != True:
    print("The entered digit must be an integer")
    shift = input("Please enter the number of characters you would like to shift: ")
shift = int(shift)
sentence = input("Please enter the sentence to be encrypted: ")
sentence = sentence.lower()
new_sentece = ""


for char in sentence:
    if char in abc:
        index = abc.find(char)
        index = (index + shift) % 26
        char = abc[index]
        new_sentece += char
print(new_sentece)