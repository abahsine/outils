#*******************
# Nom ......... : Exercice 3.14 (A Rendre)
# Rôle ........ : Comparaison de nombres en complément à deux pour déterminer lequel est le plus grand.
# Auteur ...... : Liubov Grabar
# Version ..... : V0.1 du 07/07/2023
# Licence ..... : réalisé dans le cadre du cours d'Architecture des ordinateurs
#********************/
def compare_complement_a_deux(num1, num2):
    # Vérifier les bits de signe
    signe1 = num1[0] 
    signe2 = num2[0]  

    if signe1 != signe2:
        # Les bits de signe sont différents
        if signe1 == '0':
            return f"{num1} est plus grand que {num2}"
        else:
            return f"{num2} est plus grand que {num1}"

    # Les bits de signe sont identiques, effectuer une comparaison bit par bit
    for bit1, bit2 in zip(num1[1:], num2[1:]):
        if bit1 != bit2:
            if bit1 == '1': 
                return f"{num1} est plus grand que {num2}"
            else:
                return f"{num2} est plus grand que {num1}"

    # Les nombres sont égaux
    return f"{num1} et {num2} sont égaux"

# Saisie des nombres par l'utilisateur
try:
    nombre1 = input("Entrez le premier nombre en complément à deux : ")
    int(nombre1,2)
    nombre2 = input("Entrez le deuxième nombre en complément à deux : ")
    int(nombre2,2)
    # Vérifier si les nombres ont la même longueur
    if len(nombre1) != len(nombre2):
        raise Error("Les nombres doivent être de même longueur") 
        
    resultat = compare_complement_a_deux(nombre1, nombre2)
    print(resultat)
except:
    # Gérer les erreurs d'entrée
    print("Vos deux nombres doivent être des compléments à deux de même longueur")
