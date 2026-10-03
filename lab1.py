text = input()
text = [text[i] for i in range(0, len(text))]
new_text = ''
for letter in text:
    letter_ord = ord(letter)
    if letter_ord == 32:
        new_text += ' ' 
    elif(letter_ord in range(120, 123)):   
        new_text += chr(letter_ord - 23)
    else:
        new_text += chr(letter_ord + 3)
print(new_text)
