import json
import pprint
Tournois_dict = {}

class AjouterUnJoueur:

    def volonte_dajouter_un_joueur(self):

        self.ajouterunjoueur = input("voulez-vous ajouter un joueur ? (n/o)")

        return self.ajouterunjoueur

    def recuperation_infos_nouveau_joueur(self, ajouter_un_joueur) -> None:

        if  ajouter_un_joueur == "n":
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
        return nouveau_joueur

class CreerUnTournois:
    def recuperation_info_nouveau_tournois(self) -> None:
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

                "nom_du_tournois" : self.nom,
                "lieu_du_tournois" : self.lieu,
                "date_de_debut_du_tournois" : self.date_debut,
                "date_de_fin_du_tournois" : self.date_fin,
                "numero_tour_actuel" : self.numero_tour_actuel,
                "liste_des_tours" : self.liste_des_tours,
                "liste_des_joueurs_enregistres" : self.liste_joueurs_enregistres,
                "remarque_du_directeur" : self.remarque_directeur,
                "nombre_de_tours" : self.nombre_de_tours


                }

            return nouveau_tournoi

    def lancement_dun_tournois(self):

        self.lancer_le_tournois = input("souhaitez-vous lancer le tournois ? (o/n) : ")

        return self.lancer_le_tournois
            

class DonnerLesResultatsDunTour: 
    "demander à l'utilisateur qui a gagné"
    def __init__(self,paire, numero_de_la_paire) -> None:

        self.paire = paire 
        self.numero_de_la_paire = numero_de_la_paire

    def recuperer_les_resultats_du_tour(self):

        resultat_du_tour = []
        self.resultat_joueur_un_de_la_paire = input("Pouvez-vous indiquer le résultat du joueur n°1 (" + self.paire[0] + ") pour le match N°" + str(self.numero_de_la_paire) + " (W/L/D):" )

        if self.resultat_joueur_un_de_la_paire == "D":
            self.resultat_joueur_deux_de_la_paire = "D"
        elif self.resultat_joueur_un_de_la_paire == "W":
            self.resultat_joueur_deux_de_la_paire = "L"
        else:
            self.resultat_joueur_deux_de_la_paire = "W"

        
        resultat_du_tour.append(self.resultat_joueur_un_de_la_paire)
        resultat_du_tour.append(self.resultat_joueur_deux_de_la_paire)

        self.resultat_des_joueurs_sur_le_tour = resultat_du_tour

        return self.resultat_des_joueurs_sur_le_tour



class DonneesDuTournois: 

    def __init__(self, fichier, nom_du_tournoi) -> None:
        self.fichier = fichier 
        self.nom_du_tournois = nom_du_tournoi

    def recuperer_les_donnees_du_tournois_a_un_tour_t(self):

        self.charger_les_donnees = input("Souhaitez-vous charger les données du tournois ? (o/n) : ")

        if self.charger_les_donnees == "o":
             with open(self.fichier, "r") as fichier_json: 
                donnee_a_linstant_t = json.load(fichier_json)

             pprint.pprint(donnee_a_linstant_t["Tournois"][self.nom_du_tournoi])

    def recuperation_des_joueurs_dun_tournois(self):
        self.recuperation_liste_joueurs  = input("Souhaitez-vous récupérer la liste des joueurs ? (o/n) : ")
    def recuperation_liste_tournois(self):
        self.recupration_liste_tournois = input("Souhaitez-vous récupérer la liste des tournois ? (o/n) : ")
    def recuperation_date_et_nom_dun_tournois(self):
        self.recuperation_date_et_nom_dun_tournois = input("Souhaitez-vous récupérer le nom, la date, la liste des joueurs et des tours d'un match précis ? (o/n) ")

        if self.recuperation_date_et_nom_dun_tournois == "o": 
            self.numero_du_tournois = input("Veuillez nous indiquer le numéro du tournoi concerné (cf : la liste du dessus) (1,2,3..) : ")
            self.numero_du_tournois = int(self.numero_du_tournois) - 1




