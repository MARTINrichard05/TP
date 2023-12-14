def nettoyer(phrase):
    for i in phrase:
        if not i.isalpha():
            phrase = phrase.replace(i, "")
    return phrase

def supprimerAccent(phrase):
    accents = "àâäéèêëîïôöùûüÿ"
    sansAccent = "aaaeeeeiioouuuy"
    for i in range(len(accents)):
        phrase = phrase.replace(accents[i], sansAccent[i])
    return phrase

def estPalindrome(phrase):
    phrase = phrase.lower()
    if phrase == phrase[::-1]:
        return True
    else:
        return False

phrase = input("Entrez un mot ou une phrase : ")
phrase = nettoyer(phrase)
phrase = supprimerAccent(phrase)
if estPalindrome(phrase):
    print("La phrase est un palindrome.")
else:
    print("La phrase n'est pas un palindrome.")
