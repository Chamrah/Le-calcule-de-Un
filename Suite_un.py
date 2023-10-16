#Programme qui demande à l'utilisateur de taper un entier n et qui calcule Un
n=int(input("Veuillez entrer un entier : "))
ut=6
for i in range(1,n+1):
    u=4*ut+10
    ut=u
print(f"U{n} = {u}")
