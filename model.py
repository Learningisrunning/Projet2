import controler
import json
import random

class Joueurs:


    "récupération des données des joueurs et création des joueurs"

    def __init__(self,fichier: json):


        dict_joueurs = {}
       
        with open(fichier, "r") as fichier_json: 
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
            dict_joueurs["joueur N°" + str(j)] = dict_infos_joueurs
        self.joueurs_vf = dict_joueurs
    
class Tours : 
    "selection du nombre de tours"
    def __init__(self,tours = 4) -> None:
        self.nombre_de_tours = tours


class ClassementJoueurs: 

    def __init__(self, joueurs_enregistres: dict):
        
        cLassement_dict = sorted(joueurs_enregistres, key=lambda x: (joueurs_enregistres[x]["score"]), reverse=True)
        classement_et_score = {}
        for joueurs in cLassement_dict: 
            classement_et_score[joueurs] = joueurs_enregistres[joueurs]["score"]

        self.classement_tour = classement_et_score
        

class CreationPairesJoueurs: 
    "creation des paires pour les matchs"
    def __init__(self, joueurs):
        
        liste_joueurs =[]

        if type(joueurs) == dict : 
            keys = joueurs.keys()
            

            for key in keys: 
                liste_joueurs.append(key)
        else:
            liste_joueurs = joueurs

        les_paires = {}
        c = 0

        for i in range(int(len(liste_joueurs)/2)) :
            for j in range(1):
                les_paires["Paire N°" + str(i)] = liste_joueurs[c], liste_joueurs[c+1]
                c = c+2
        
        self.paires= les_paires  
        
    
class Matchs:
    """Définition des classements finaux (tant qu'il n'y a pas de view + stockage des résultats des matchs"""
    def __init__(self,liste_paires, joueurs_enregistres, resultat_du_tour):

        stockage_des_resultats= []
        joueur_un = []
        joueur_deux =[]
        
        joueurs_enregistres[liste_paires[0]]["resultatM"] = resultat_du_tour[0]
        joueurs_enregistres[liste_paires[1]]["resultatM"] = resultat_du_tour[1]
            

        for i in range(2):

            if joueurs_enregistres[liste_paires[i]]["resultatM"] == "W":
                joueurs_enregistres[liste_paires[i]]["score"] = joueurs_enregistres[liste_paires[i]]["score"] + 1
            elif joueurs_enregistres[liste_paires[i]]["resultatM"] == "L":
                joueurs_enregistres[liste_paires[i]]["score"] = joueurs_enregistres[liste_paires[i]]["score"] + 0
            else: 
                joueurs_enregistres[liste_paires[i]]["score"] = joueurs_enregistres[liste_paires[i]]["score"] + 0.5


        
            joueur_un = [liste_paires[0]], [joueurs_enregistres[liste_paires[0]]["score"] ]
            joueur_deux = [liste_paires[1]], [joueurs_enregistres[liste_paires[1]]["score"] ]

            joueur_et_score =(joueur_un, joueur_deux )
            stockage_des_resultats.append(joueur_et_score)

        self.tuples_match = stockage_des_resultats
    
class Tournois: 

    def __init__(self):
        

        self.nom = controler.PreparationDuTournois().creer_un_tournois.nom 
        self.lieu = controler.PreparationDuTournois().creer_un_tournois.lieu
        self.date_debut = controler.PreparationDuTournois().creer_un_tournois.date_debut
        self.date_fin= controler.PreparationDuTournois().creer_un_tournois.date_fin
        self.numero_tour_actuel = controler.PreparationDuTournois().creer_un_tournois.numero_tour_actuel
        self.liste_des_tours = controler.PreparationDuTournois().creer_un_tournois.liste_des_tours
        self.liste_joueurs_enregistres = controler.PreparationDuTournois().creer_un_tournois.liste_joueurs_enregistres
        self.remarque_directeur = controler.PreparationDuTournois().creer_un_tournois.remarque_directeur
        self.nombre_de_tours = controler.PreparationDuTournois().creer_un_tournois.nombre_de_tours


"""
joueurs = Joueurs("joueurs.json").joueurs
#paires = CreationPairesJoueurs(joueurs).paires
#tuples_matchs = Matchs(paires,joueurs).tuples_match
#classement_des_joueurs = ClassementJoueurs(joueurs)
tours = Tours(joueurs, 6).resultat_final
print(tours)
"""



