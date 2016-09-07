# Année bissextile ou non à partir du millésime

print("Entrez le millésime: ", end="")
a = int(input())
if (a % 4 == 0) or ((a%100!=0) and (a % 400 == 0)):
    print("bissextile!")
else:
    print("non bissextile!")
