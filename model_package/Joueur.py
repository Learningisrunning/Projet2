import json


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
