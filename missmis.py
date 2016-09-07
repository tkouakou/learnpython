print("Veuillez saisir votre nom: ", end="")
nom = str(input())
print("Veuillez saisir votre sexe (M/F): ", end="")
sexe = str(input())
if sexe == 'M':
    print("Cher Monsieur",nom)
elif sexe == 'F':
    print("Chère Mademoiselle",nom)
