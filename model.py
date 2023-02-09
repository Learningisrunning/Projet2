import json
import time
import random
import pprint

# faire une class joueur sans s pour faire l'ajout d'un joueur dans le json / faire dans le controler une class qui vérif si un joueur existe
class Joueur: 
    "création d'un joueur et ajout du joueur au fichier json"
    def __init__(self, dict_dinfo_sur_le_joueur_a_ajouter) -> None:
        self.nouveau_joueur = dict_dinfo_sur_le_joueur_a_ajouter

    def ajout_du_joueur(self, fichier : json):

        with open(fichier, "r") as fichier_json: 
                dict_initial_joueurs =json.load(fichier_json)

        dict_initial_joueurs["Joueurs"].append(self.nouveau_joueur)
        print(dict_initial_joueurs)

        with open(fichier, "w") as fichier_json: 
            json.dump(dict_initial_joueurs, fichier_json, indent=4)


class Joueurs:


    "récupération des données des joueurs et création des joueurs"

    def __init__(self,fichier: json):

        self.fichier = fichier

    def creation_du_dict_de_joueurs_pour_le_tournois(self):

        dict_joueurs = {}
       
        with open(self.fichier, "r") as fichier_json: 
            lecture_json = json.load(fichier_json)

        for j in range (len(lecture_json['Joueurs'])):

            self.nom_de_famille = lecture_json['Joueurs'][j]["nom_de_famille"]
            self.prenom = lecture_json['Joueurs'][j]["prenom"]
            self.date_de_naissance = lecture_json['Joueurs'][j]["date_de_naissance"]
            self.identifiant_national_dechec = lecture_json['Joueurs'][j]["identifiant_national_dechec"]
            self.score = 0
            self.resultatM = " "
            dict_infos_joueurs = {

                "nom" : self.nom_de_famille,
                "prenom" : self.prenom,
                "date_de_naissance" : self.date_de_naissance,
                "identifiant_national_dechec" : self.identifiant_national_dechec,
                "score" : self.score,
                "resultatM" : self.resultatM

                }
            dict_joueurs[self.prenom +"." + self.nom_de_famille[0]] = dict_infos_joueurs
        self.joueurs_vf = dict_joueurs

        return self.joueurs_vf
    
    
class Tours : 
    "selection du nombre de tours"
    def __init__(self,fichier :json) -> None:

        self.fichier = fichier
    def initialisation_du_nombre_de_tour(self):
         with open(self.fichier, "r") as fichier_json: 
            dict_tournois = json.load(fichier_json)

            key = dict_tournois["Tournois"].keys()
            liste_des_cles_des_tournois = []
            for keys in key:
                liste_des_cles_des_tournois.append(keys)

            nombre_de_tours = dict_tournois["Tournois"][liste_des_cles_des_tournois[-1]]["nombre_de_tours"]

            return nombre_de_tours


class tournoi :
    def __init__(self, nouveau_tournois_data, fichier) -> None:

        self.nouveau_tournois_data = nouveau_tournois_data
        self.fichier = fichier

    def ajout_dun_nouveau_tournois(self):

        with open(self.fichier, "r") as fichier_json: 
            dict_initial_tournois =json.load(fichier_json)

        dict_initial_tournois["Tournois"][self.nouveau_tournois_data["nom_du_tournois"]] = (self.nouveau_tournois_data)

        with open(self.fichier, "w") as fichier_json: 
            json.dump(dict_initial_tournois, fichier_json, indent=4)


    
class Tournois: 

    def __init__(self, fichier, tour_actuel, liste_des_tours, liste_des_joueurs_enregistrees):

        self.fichier = fichier 
        self.tour_actuel = tour_actuel
        self.liste_des_tours = liste_des_tours
        self.liste_des_joueurs_enregistrees = liste_des_joueurs_enregistrees

        with open(self.fichier, "r") as fichier_json: 
            dict_tournois = json.load(fichier_json)

            key = dict_tournois["Tournois"].keys()
            liste_des_cles_des_tournois = []
            for keys in key:
                liste_des_cles_des_tournois.append(keys)

        self.nom_du_tournois = dict_tournois["Tournois"][liste_des_cles_des_tournois[-1]]["nom_du_tournois"]
    
    def ajout_des_donnee_du_tour_dun_tournois_dans_le_fichier_json(self):

        if  self.tour_actuel == 0 :
            self.date_debut = time.strftime("%Y-%m-%d %H:%M:%S")

            with open(self.fichier, "r") as fichier_json:
                fichier_infos_tournoi = json.load(fichier_json)

            
            fichier_infos_tournoi["Tournois"][self.nom_du_tournois]["date_de_debut_du_tournois"] = self.date_debut
        
            with open(self.fichier, "w") as fichier_json: 
                json.dump(fichier_infos_tournoi, fichier_json, indent=4)

        with open(self.fichier, "r") as fichier_json:
                fichier_infos_tournoi = json.load(fichier_json)

        if int(fichier_infos_tournoi["Tournois"][self.nom_du_tournois]["nombre_de_tours"]) == self.tour_actuel :

            self.date_fin= time.strftime("%Y-%m-%d %H:%M:%S")

            with open(self.fichier, "r") as fichier_json:
                fichier_infos_tournoi = json.load(fichier_json)

            fichier_infos_tournoi["Tournois"][self.nom_du_tournois]["liste_des_tours"] = self.liste_des_tours
            fichier_infos_tournoi["Tournois"][self.nom_du_tournois]["date_de_fin_du_tournois"] = self.date_fin
            fichier_infos_tournoi["Tournois"][self.nom_du_tournois]["liste_des_joueurs_enregistres"] = self.liste_des_joueurs_enregistrees

            with open(self.fichier, "w") as fichier_json: 
                json.dump(fichier_infos_tournoi, fichier_json, indent=4)


        with open(self.fichier, "r") as fichier_json:
                fichier_infos_tournoi = json.load(fichier_json)

        fichier_infos_tournoi["Tournois"][self.nom_du_tournois]["numero_tour_actuel"] = self.tour_actuel
        fichier_infos_tournoi["Tournois"][self.nom_du_tournois]["liste_des_joueurs_enregistres"] = self.liste_des_joueurs_enregistrees

        with open(self.fichier, "w") as fichier_json: 
            json.dump(fichier_infos_tournoi, fichier_json, indent=4)
 
def lecture_dun_fichier_json(fichier : json):

    with open(fichier, "r") as fichier_json: 
            dict_tournois = json.load(fichier_json)  
    return dict_tournois









