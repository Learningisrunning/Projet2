import json


def lecture_dun_fichier_json(fichier: json):
    """Lecture d'un fichier json et transformation en dictionnaire"""

    with open(fichier, "r") as fichier_json:
        dict_tournois = json.load(fichier_json)
    return dict_tournois
