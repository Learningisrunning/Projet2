import json


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
