import json


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
