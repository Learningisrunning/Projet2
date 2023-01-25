import controler
import json
import time

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
    def __init__(self, joueurs, tours, liste_des_round):
        
        liste_joueurs =[]

        if type(joueurs) == dict : 
            keys = joueurs.keys()
            

            for key in keys: 
                liste_joueurs.append(key)
        else:
            liste_joueurs = joueurs

        les_paires = {}
        c = 0

        if tours == 1:
            for i in range(int(len(liste_joueurs)/2)) :
                for j in range(1):
                    les_paires["Paire N°" + str(i)] = liste_joueurs[c], liste_joueurs[c+1]
                    c = c+2
        else:
            for i in range(int(len(liste_joueurs)/2)) :
                c = 0
                for j in range(1):
                    les_paires["Paire N°" + str(i)] = liste_joueurs[c], liste_joueurs[c+1]
                    k = 0 
                    for round in range(len(liste_des_round)) : 
                        for paire in range (int(len(joueurs)/2)):
                            nombre_de_paire_identique = 0
                            if les_paires["Paire N°" + str(i)] == liste_des_round["Round N°" + str(round+1)][0]["Paire N°" + str(paire)] :
                                nombre_de_paire_identique = nombre_de_paire_identique +1
                                if nombre_de_paire_identique > 0 and len(liste_joueurs) > 2 :
                                    k = k +1
                                    les_paires["Paire N°" + str(i)] = liste_joueurs[c], liste_joueurs[c+1+k]
                                    round = 0
                                    paire = 0

                index_du_premier_joueur = liste_joueurs.index(les_paires["Paire N°" + str(i)][0])
                print(liste_joueurs)
                del liste_joueurs[index_du_premier_joueur]
                print(liste_joueurs)
                index_du_second_joueur = liste_joueurs.index(les_paires["Paire N°" + str(i)][1])
                del liste_joueurs[index_du_second_joueur]
                print(liste_joueurs)
                                   


                    

        

        
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

    def __init__(self, fichier, tour_actuel, liste_des_tours, liste_des_joueurs_enregistree, nom_du_tournois ):
        
        self.numero_tour_actuel = tour_actuel
        self.liste_des_tours = liste_des_tours
        self.liste_joueurs_enregistres = liste_des_joueurs_enregistree

        if  self.numero_tour_actuel == 0 :
            self.date_debut = time.strftime("%Y-%m-%d %H:%M:%S")

            with open(fichier, "r") as fichier_json:
                fichier_infos_tournoi = json.load(fichier_json)

            fichier_infos_tournoi["Tournois"][-1][nom_du_tournois]["liste_des_joueurs_enregistres"] = liste_des_joueurs_enregistree
            fichier_infos_tournoi["Tournois"][-1][nom_du_tournois]["date_de_debut_du_tournois"] = self.date_debut
        
            with open(fichier, "w") as fichier_json: 
                json.dump(fichier_infos_tournoi, fichier_json, indent=4)

        with open(fichier, "r") as fichier_json:
                fichier_infos_tournoi = json.load(fichier_json)

        if int(fichier_infos_tournoi["Tournois"][-1][nom_du_tournois]["nombre_de_tours"]) == self.numero_tour_actuel :

            self.date_fin= time.strftime("%Y-%m-%d %H:%M:%S")

            with open(fichier, "r") as fichier_json:
                fichier_infos_tournoi = json.load(fichier_json)

            fichier_infos_tournoi["Tournois"][-1][nom_du_tournois]["liste_des_tours"] = self.liste_des_tours
            fichier_infos_tournoi["Tournois"][-1][nom_du_tournois]["date_de_fin_du_tournois"] = self.date_fin

            with open(fichier, "w") as fichier_json: 
                json.dump(fichier_infos_tournoi, fichier_json, indent=4)


        with open(fichier, "r") as fichier_json:
                fichier_infos_tournoi = json.load(fichier_json)

        fichier_infos_tournoi["Tournois"][-1][nom_du_tournois]["numero_tour_actuel"] = self.numero_tour_actuel

        with open(fichier, "w") as fichier_json: 
            json.dump(fichier_infos_tournoi, fichier_json, indent=4)
            


        


"""
joueurs = Joueurs("joueurs.json").joueurs
#paires = CreationPairesJoueurs(joueurs).paires
#tuples_matchs = Matchs(paires,joueurs).tuples_match
#classement_des_joueurs = ClassementJoueurs(joueurs)
tours = Tours(joueurs, 6).resultat_final
print(tours)
"""



