
import json


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
