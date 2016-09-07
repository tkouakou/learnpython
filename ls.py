# Utilisation d'une liste simple et de branchements conditionnels
print("Ce script recherche le plus grand de trois nombres")
print("Veuillez entrer trois nombres séparés par des virgules : ")
ch = input()

# L'association des fonctions eval() et list() permet de convertir
# en liste toute chaîne de valeurs séparés par des virgules
nn = list(eval(ch))
max, index = nn[0], 'premier'
if nn[1] > max:
    max = nn[1]
    index = 'second'
if nn[2] > max:
    max = nn[2]
    index = 'troisième'
print("Le plus grand de ces nombre est", max)
print("Ce nombre est le", index, "de votre liste.")
#print("test git")
