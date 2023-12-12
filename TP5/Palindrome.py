phrase = input("Entrez un mot ou une phrase : ")

for i in phrase:
    if not i.isalpha():
        phrase = phrase.replace(i, "")

phrase = phrase.lower()
if phrase == phrase[::-1]:
    print("La phrase est un palindrome.")
else:
    print("La phrase n'est pas un palindrome.")