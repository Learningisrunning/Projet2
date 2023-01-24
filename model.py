import json
import random

class Joueurs:

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
        self.joueurs = dict_joueurs
    
class Tours:

    def __init__(self,joueurs_enregistrés, nombre_de_tours = 4):

        liste_des_tours = {}
        self.nombre_de_tours = nombre_de_tours
        for tours in range(nombre_de_tours-1):
            if tours < 1:
                Paires_du_tour = CreationPairesJoueurs(joueurs_enregistrés)
            else:

                classement_joueurs = ClassementJoueurs(joueurs_enregistrés).classement_tour
                Paires_du_tour = CreationPairesJoueurs(classement_joueurs).paires
                Match = Matchs(Paires_du_tour, joueurs_enregistrés)
                liste_des_tours["Round N°" + str(tours)] = Paires_du_tour, classement_joueurs

        self.resultat_final = classement_joueurs
        print(liste_des_tours)
    
class ClassementJoueurs: 

    def __init__(self, joueurs_enregistres: dict):
        
        cLassement_dict = sorted(joueurs_enregistres, key=lambda x: (joueurs_enregistres[x]["score"]), reverse=True)
        
        self.classement_tour = cLassement_dict
        

class CreationPairesJoueurs: 

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
    def __init__(self,liste_paires, joueurs_enregistres):

        stockage_des_resultats= []
        joueur_un = []
        joueur_deux =[]
        score_possible = ["W", "L", "D"]
        
     

        for j in range(len(liste_paires)):
            random.shuffle(score_possible)
            joueurs_enregistres[liste_paires["Paire N°" + str(j)][0]]["resultatM"] = score_possible[0]

            if joueurs_enregistres[liste_paires["Paire N°" + str(j) ][0]]["resultatM"] == "D":
                joueurs_enregistres[liste_paires["Paire N°" + str(j) ][1]]["resultatM"] = score_possible [0] 
            elif score_possible[1] != "D": 
                joueurs_enregistres[liste_paires["Paire N°" + str(j) ][1]]["resultatM"] = score_possible [1] 
            else:
                joueurs_enregistres[liste_paires["Paire N°" + str(j) ][1]]["resultatM"] = score_possible [2]

            for i in range(2):

                if joueurs_enregistres[liste_paires["Paire N°" + str(j) ][i]]["resultatM"] == "W":
                    joueurs_enregistres[liste_paires["Paire N°" + str(j) ][i]]["score"] = joueurs_enregistres[liste_paires["Paire N°" + str(j) ][i]]["score"] + 1
                elif joueurs_enregistres[liste_paires["Paire N°" + str(j) ][i]]["resultatM"] == "L":
                    joueurs_enregistres[liste_paires["Paire N°" + str(j) ][i]]["score"] = joueurs_enregistres[liste_paires["Paire N°" + str(j) ][i]]["score"] + 0
                else: 
                    joueurs_enregistres[liste_paires["Paire N°" + str(j) ][i]]["score"] = joueurs_enregistres[liste_paires["Paire N°" + str(j) ][i]]["score"] + 0.5


        for j in range(len(liste_paires)):
            joueur_un = [liste_paires["Paire N°" + str(j) ][0]], [joueurs_enregistres[liste_paires["Paire N°" + str(j) ][0]]["score"] ]
            joueur_deux = [liste_paires["Paire N°" + str(j) ][1]], [joueurs_enregistres[liste_paires["Paire N°" + str(j) ][1]]["score"] ]

            joueur_et_score =(joueur_un, joueur_deux )
            stockage_des_resultats.append(joueur_et_score)

        self.tuples_match = stockage_des_resultats
    
class Tournois: 

    def __init__(self, nom, lieu, date_debut, date_fin , numero_tour_actuel, liste_des_tours, liste_joueurs_enregistres, remarques_directeur, nombre_de_tours=4):
        
        self.nom = nom 
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin= date_fin
        self.numero_tour_actuel = numero_tour_actuel
        self.liste_des_tours = liste_des_tours
        self.liste_joueurs_enregistres = liste_joueurs_enregistres
        self.remarque_directeur = remarques_directeur
        self.nombre_de_tours = nombre_de_tours


joueurs = Joueurs("joueurs.json").joueurs
#paires = CreationPairesJoueurs(joueurs).paires
#tuples_matchs = Matchs(paires,joueurs).tuples_match
#classement_des_joueurs = ClassementJoueurs(joueurs)
tours = Tours(joueurs, 6).resultat_final
print(tours)




