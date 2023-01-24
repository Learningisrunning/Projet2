import json
Tournois_dict = {}

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
                dict_initial_joueurs =json.load(fichier_json)

            dict_initial_joueurs["Joueurs"].append(nouveau_joueur)
            print(dict_initial_joueurs)

            with open(fichier, "w") as fichier_json: 
                json.dump(dict_initial_joueurs, fichier_json, indent=4)

            print("le joueur " + self.nom +" "+ self.prenom + " né le " + self.date_de_naissance + " qui a pour identifiant national " + self.identifiant_national_dechec + " à bien été ajouté")

class CreerUnTournois:
    def __init__(self, fichier) -> None:
        self.creer_un_tournois = input("Souhaitez-vous créer un tournois ? (o/n) : ")

        if self.creer_un_tournois == "n":
            print("vous ne souhaitez pas créer de tournois")
        else : 

            self.nom = input("indiquer le nom du tournois :")
            self.lieu = input("indiquer le lieu du tournois :")
            self.date_debut = " "
            self.date_fin= " "
            self.numero_tour_actuel = " "
            self.liste_des_tours = " "
            self.liste_joueurs_enregistres = input("indiquer le fichier contenant la liste des joueurs enregistrés : ")
            self.remarque_directeur = input("indiquer les remarques du directeur : ")
            self.nombre_de_tours = input("indiquer le nombre de tours : ")


            nouveau_tournoi = {

                "lieu_du_tournois" : self.lieu,
                "date_de_debut_du_tournois " : self.date_debut,
                "date_de_fin_du_tournois" : self.date_fin,
                "numero_tour_actuel" : self.numero_tour_actuel,
                "liste_des_tours" : self.liste_des_tours,
                "liste_des_joueurs_enregistres" : self.liste_joueurs_enregistres,
                "remarque_du_directeur" : self.remarque_directeur,
                "nombre_de_tours" : self.nombre_de_tours


                }
            
            Tournois_dict[self.nom] = nouveau_tournoi
            
            

            with open(fichier, "r") as fichier_json: 
                dict_initial_tournois =json.load(fichier_json)

            dict_initial_tournois["Tournois"].append(Tournois_dict)

            with open(fichier, "w") as fichier_json: 
                json.dump(dict_initial_tournois, fichier_json, indent=4)
            
           
        

class LancerLeTournois: 
    def __init__(self) -> None:

        self.lancer_le_tournois = input("souhaitez-vous lancer le tournois ? (o/n) : ")

class DonneesDuTournois: 

    def __init__(self) -> None:
        self.charger_les_donnees = input("Souhaitez-vous charger les données du tournois ? (o/n) : ")


