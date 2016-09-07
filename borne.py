# soient deux bornes entières a et b, additionner les nombres
# mutliple de 3 et 5 compris entre ces bornes

print("Entrer la valeur de la borne inférieur: ", end="" )
a = int(input())
print("Entrer la valeur de la borne supérieur: ", end="")
b = int(input())

s = 0 # somme recherchée nulle au départ
# Nombre en cours de traitement
n = a
while n <= b:
    if n % 3 == 0 or n % 5 == 0:
        s = s + n
    n = n + 1
print('La somme recherchée est:', s)
