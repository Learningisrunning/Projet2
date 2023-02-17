import json
import time


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
