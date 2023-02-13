import json
import time


class Joueur:
    "création d'un joueur et ajout du joueur au fichier json"

    def __init__(self, dict_dinfo_sur_le_joueur_a_ajouter) -> None:
        self.nouveau_joueur = dict_dinfo_sur_le_joueur_a_ajouter

    def ajout_du_joueur(self, fichier: json):
        """Ajout d'un joueur"""
        with open(fichier, "r") as fichier_json:
            dict_initial_joueurs = json.load(fichier_json)

        dict_initial_joueurs["Joueurs"].append(self.nouveau_joueur)
        print(dict_initial_joueurs)

        with open(fichier, "w") as fichier_json:
            json.dump(dict_initial_joueurs, fichier_json, indent=4)


class Joueurs:

    "récupération des données des joueurs et création des joueurs"

    def __init__(self, fichier: json):

        self.fichier = fichier

    def creation_du_dict_de_joueurs_pour_le_tournois(self):
        """Creation du dictionnaire des joueurs pour le tournois"""

        dict_joueurs = {}

        with open(self.fichier, "r") as fichier_json:
            lecture_json = json.load(fichier_json)

        for j in range(len(lecture_json['Joueurs'])):

            nom_de_famille = lecture_json['Joueurs'][j]["nom_de_famille"]
            prenom = lecture_json['Joueurs'][j]["prenom"]
            date_de_naissance = lecture_json['Joueurs'][j]["date_de_naissance"]
            identifiant_national_dechec = (lecture_json['Joueurs'][j]
                                           ["identifiant_national_dechec"])
            score = 0
            resultatM = " "
            dict_infos_joueurs = {

                "nom": nom_de_famille,
                "prenom": prenom,
                "date_de_naissance": date_de_naissance,
                "identifiant_national_dechec": identifiant_national_dechec,
                "score": score,
                "resultatM": resultatM

                }
            dict_joueurs[prenom + "." + nom_de_famille[0]] = dict_infos_joueurs
        joueurs_vf = dict_joueurs

        return joueurs_vf


class Tours:
    "selection du nombre de tours"

    def __init__(self, fichier: json) -> None:

        self.fichier = fichier

    def initialisation_du_nombre_de_tour(self):
        """initialisation du nombre de tour du tournois"""

        with open(self.fichier, "r") as fichier_json:
            dict_tournois = json.load(fichier_json)

            key = dict_tournois["Tournois"].keys()
            liste_des_cles_des_tournois = []
            for keys in key:
                liste_des_cles_des_tournois.append(keys)

            nombre_de_tours = (dict_tournois["Tournois"]
                               [liste_des_cles_des_tournois[-1]]
                               ["nombre_de_tours"])

            return nombre_de_tours


class Tournoi:
    "ajout d'un nouveau tournois à la bdd"

    def __init__(self, nouveau_tournois_data, fichier) -> None:

        self.nouveau_tournois_data = nouveau_tournois_data
        self.fichier = fichier

    def ajout_dun_nouveau_tournois(self):
        """Ajout d'un tournois à la bdd"""

        with open(self.fichier, "r") as fichier_json:
            dict_initial_tournois = json.load(fichier_json)

        (dict_initial_tournois["Tournois"]
            [self.nouveau_tournois_data["nom_du_tournois"]]) = (
            self.nouveau_tournois_data)

        with open(self.fichier, "w") as fichier_json:
            json.dump(dict_initial_tournois, fichier_json, indent=4)


class Tournois:
    """mise à jour de la bdd des tournois"""

    def __init__(self, fichier, tour_actuel, liste_des_tours,
                 liste_des_joueurs_enregistrees):

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

        self.nom_du_tournois = (dict_tournois["Tournois"]
                                [liste_des_cles_des_tournois[-1]]
                                ["nom_du_tournois"])

    def ajout_des_donnee_du_tour_dun_tournois_dans_le_fichier_json(self):
        """Ajout des donnee du tour d'un tournois dans le fichier json"""

        if self.tour_actuel == 0:
            date_debut = time.strftime("%Y-%m-%d %H:%M:%S")

            with open(self.fichier, "r") as fichier_json:
                fichier_infos_tournoi = json.load(fichier_json)

            (fichier_infos_tournoi["Tournois"][self.nom_du_tournois]
                ["date_de_debut_du_tournois"]) = (date_debut)

            with open(self.fichier, "w") as fichier_json:
                json.dump(fichier_infos_tournoi, fichier_json, indent=4)

        with open(self.fichier, "r") as fichier_json:
            fichier_infos_tournoi = json.load(fichier_json)

        if (int(fichier_infos_tournoi["Tournois"]
                [self.nom_du_tournois]["nombre_de_tours"]) ==
                (self.tour_actuel)):

            date_fin = time.strftime("%Y-%m-%d %H:%M:%S")

            with open(self.fichier, "r") as fichier_json:
                fichier_infos_tournoi = json.load(fichier_json)

            (fichier_infos_tournoi["Tournois"]
                [self.nom_du_tournois]["liste_des_tours"]) = (
                    self.liste_des_tours)

            (fichier_infos_tournoi["Tournois"]
                [self.nom_du_tournois]["date_de_fin_du_tournois"]) = date_fin

            (fichier_infos_tournoi["Tournois"]
                [self.nom_du_tournois]["liste_des_joueurs_enregistres"]) = (
                    self.liste_des_joueurs_enregistrees)

            with open(self.fichier, "w") as fichier_json:
                json.dump(fichier_infos_tournoi, fichier_json, indent=4)

        with open(self.fichier, "r") as fichier_json:
            fichier_infos_tournoi = json.load(fichier_json)

        (fichier_infos_tournoi["Tournois"]
            [self.nom_du_tournois]["numero_tour_actuel"]) = self.tour_actuel
        (fichier_infos_tournoi["Tournois"]
            [self.nom_du_tournois]["liste_des_joueurs_enregistres"]) = (
                self.liste_des_joueurs_enregistrees)

        with open(self.fichier, "w") as fichier_json:
            json.dump(fichier_infos_tournoi, fichier_json, indent=4)


def lecture_dun_fichier_json(fichier: json):
    """Lecture d'un fichier json et transformation en dictionnaire"""

    with open(fichier, "r") as fichier_json:
        dict_tournois = json.load(fichier_json)
    return dict_tournois
