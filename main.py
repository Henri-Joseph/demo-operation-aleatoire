import random

NBR_MIN = 1
NBR_MAX = 10
NBR_QUS = 4

# Creation de la fonction
def poser_qut():
    # creation des nombres aleatoires
    a = random.randint(NBR_MIN, NBR_MAX)
    b = random.randint(NBR_MIN, NBR_MAX)
    o = random.randint(0, 3)
    # Obtention du resultat
    if o == 0:
        opr = "*"
        resp_str = input(f"Quel est le resultat de l'opération suivante : {a} {opr} {b} ? ")
        res = a*b
    elif o == 1:
        opr = "+"
        resp_str = input(f"Quel est le resultat de l'opération suivante : {a} {opr} {b} ? ")
        res = a+b
    elif o == 2:
        opr = "/"
        resp_str = input(f"Quel est la partie entière de l'opération suivante : {a} {opr} {b} ? ")
        res = int(a/b)
    elif o == 3:
        opr = "-"
        resp_str = input(f"Quel est le resultat de l'opération suivante : {a} {opr} {b} ? ")
        res = a-b

    resp_int = int(resp_str)
    if resp_int == res:
        return True
    return False


# Poser plusieurs question
point = 0
for i in range(0, NBR_QUS):
    nq = i + 1
    print(f"Question N¤ {nq} sur {NBR_QUS}")
    if poser_qut():
        point += 1
        print("Reponse correct")
    else:
        print("Reponse incorrect")
    print()


# Affichage du score
print(f"Votre score est de {point}/{NBR_QUS}")

# Gestion des mentions
poucent_str = (point/NBR_QUS)*100
poucent = int(poucent_str)

if poucent == 100:
    print("Vous êtes excellent")
elif poucent == 0:
    print("Revisez vos maths")
elif 50 <= poucent < 100:
    print("Pas mal")
elif 0 < poucent < 50:
    print("Peut mieux faire")