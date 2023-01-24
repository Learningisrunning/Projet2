import json


class AjouterUnJoueur:
    def __init__(self, fichier : json) -> None:
        
        

        self.ajouterunjoueur = input("voulez-vous ajouter un joueur ? (n/o)")

        if self.ajouterunjoueur == "n":
            print("aucun joueur ne sera ajouter à la liste précédement fournis")
        else: 
            self.nom = input("Nom du joueur :")
            self.prenom = input("Prenom du joueur : ")
            self.date_de_naissance = input("Date de naissance du joueur : ")
            self.identifiant_national_dechec = input("identifiant national d'echec du joueur :")

            nouveau_joueur= {

                "nom_de_famille" : self.nom,
                "prenom" : self.prenom,
                "date_de_naissance" : self.date_de_naissance,
                "identifiant_national_dechec" : self.identifiant_national_dechec

            }

           
            with open(fichier, "r") as fichier_json: 
                dict_initial =json.load(fichier_json)

            dict_initial["Joueurs"].append(nouveau_joueur)
            print(dict_initial)

            with open(fichier, "w") as fichier_json: 
                json.dump(dict_initial, fichier_json, indent=4)

            print("le joueur " + self.nom +" "+ self.prenom + " né le " + self.date_de_naissance + " qui a pour identifiant national " + self.identifiant_national_dechec + " à bien été ajouté")

class CreerUnTournois:
    def __init__(self,joueurs_enregistres, nombre_de_tours) -> None:
        self.creer_un_tournois = input("Souhaitez-vous créer un tournois ? (o/n")

        if self.creer_un_tournois == "n":
            print("vous ne souhaitez pas créer de tournois")
        else : 

            self.nom = input("indiquer le nom du tournois :")
            self.lieu = input("indiquer le lieu du tournois :")
            #self.date_debut = date_debut
            #self.date_fin= date_fin
            #self.numero_tour_actuel = numero_tour_actuel
            #self.liste_des_tours = liste_des_tours
            self.liste_joueurs_enregistres = joueurs_enregistres
            self.remarque_directeur = input("indiquer les remarques du directeur : ")
            self.nombre_de_tours = nombre_de_tours

class LancerLeTournois: 
    def __init__(self) -> None:
        self.lancer_le_tournois : input("souhaitez-vous lancer le tournois ? (o/n)")

class DonneesDuTournois: 
    def __init__(self) -> None:
        self.charger_les_donnees = input("Souhaitez-vous charger les données du tournois ? (o/n) : ")
decision = AjouterUnJoueur("joueurs.json").ajouterunjoueur
print(decision)

