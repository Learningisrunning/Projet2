import json
import view 
import model
import time
import pprint
import random

#diviser en package + flack 8 + commenter un peu plus mon code + résoudre le pb des infos pendant le tournois 

class VerifDoublonJoueurs:

    def verif_du_doublon(self, dict_des_joueurs, nouveau_joueur):

        nouvelle_identifiant_echec = nouveau_joueur["identifiant_national_dechec"]

        verification = bool
        for nb_joueurs in range(len(dict_des_joueurs["Joueurs"])):
            identifiants = dict_des_joueurs["Joueurs"][nb_joueurs]["identifiant_national_dechec"]
            if nouvelle_identifiant_echec == identifiants:
                verification = False
                break
            else: 
                verification = True

        return verification

class ClassementJoueurs: 
    "Classer les joueurs en fonction de leur score"
    def __init__(self, joueurs_enregistres: dict):
        self.joueurs_enregistres = joueurs_enregistres
    def classement_des_joueurs(self):

        self.cLassement_dict = sorted(self.joueurs_enregistres, key=lambda x: (self.joueurs_enregistres[x]["score"]), reverse=True)
        self.classement_et_score = {}
        for joueurs in self.cLassement_dict: 
            self.classement_et_score[joueurs] = self.joueurs_enregistres[joueurs]["score"]

        self.classement_tour = self.classement_et_score
        return self.classement_tour


class CreationPairesJoueurs: 
    "creation des paires pour les matchs"
    def __init__(self, joueurs, tours, liste_des_round):

        self.joueurs = joueurs
        self.tours = tours 
        self.liste_des_round = liste_des_round

    def creation_des_paire(self):
        
        self.liste_joueurs =[]

        if type(self.joueurs) == dict : 
            keys = self.joueurs.keys()
            

            for key in keys: 
                self.liste_joueurs.append(key)
        else:
            self.liste_joueurs = self.joueurs
        
        self.les_paires = {}
        c = 0

        if self.tours == 1:

            random.shuffle(self.liste_joueurs)
            for i in range(int(len(self.liste_joueurs)/2)) :
                for j in range(1):
                    self.les_paires["Paire N°" + str(i)] = self.liste_joueurs[c], self.liste_joueurs[c+1]
                    c = c+2
        else:
            for i in range(int(len(self.liste_joueurs)/2)) :
                c = 0
                for j in range(1):
                    self.les_paires["Paire N°" + str(i)] = self.liste_joueurs[c], self.liste_joueurs[c+1]
                    k = 0 
                    for round in range(len(self.liste_des_round)) : 
                        for paire in range (int(len(self.joueurs)/2)):
                            nombre_de_paire_identique = 0
                            if self.les_paires["Paire N°" + str(i)] == self.liste_des_round["Round N°" + str(round+1)][2]["Paire N°" + str(paire)] :
                                nombre_de_paire_identique = nombre_de_paire_identique +1
                                if nombre_de_paire_identique > 0 and len(self.liste_joueurs) > 2 and k+1>len(self.liste_joueurs) :
                                    k = k +1
                                    self.les_paires["Paire N°" + str(i)] = self.liste_joueurs[c], self.liste_joueurs[c+1+k]
                                    round = 0
                                    paire = 0

                index_du_premier_joueur = self.liste_joueurs.index(self.les_paires["Paire N°" + str(i)][0])
                #print(liste_joueurs)
                del self.liste_joueurs[index_du_premier_joueur]
                #print(liste_joueurs)
                index_du_second_joueur = self.liste_joueurs.index(self.les_paires["Paire N°" + str(i)][1])
                del self.liste_joueurs[index_du_second_joueur]
                #print(liste_joueurs)
                                         
        print(self.les_paires)
        self.paires= self.les_paires
        return self.paires 


class AjoutDuScore:
    """ ajout du scores obtenue pendant le tour à chaque joueurs """
    def __init__(self,liste_paires, joueurs_enregistres):
        self.liste_paires = liste_paires
        self.joueurs_enregistres = joueurs_enregistres
        

    def recuperer_les_resultats_du_tour(self, resultat_joueur_un_de_la_pair):
        resultat_du_tour =[]

        self.resultat_joueur_un_de_la_paire = resultat_joueur_un_de_la_pair

        if self.resultat_joueur_un_de_la_paire == "D":
            self.resultat_joueur_deux_de_la_paire = "D"
        elif self.resultat_joueur_un_de_la_paire == "W":
            self.resultat_joueur_deux_de_la_paire = "L"
        else:
            self.resultat_joueur_deux_de_la_paire = "W"

        
        resultat_du_tour.append(self.resultat_joueur_un_de_la_paire)
        resultat_du_tour.append(self.resultat_joueur_deux_de_la_paire)

        self.resultat_des_joueurs_sur_le_tour = resultat_du_tour

        return self.resultat_des_joueurs_sur_le_tour

    def resultats_des_matchs(self, resultat_du_tour):

        self.resultat_du_tour = resultat_du_tour

        self.stockage_des_resultats= []
        self.joueur_un = []
        self.joueur_deux =[]
        
        self.joueurs_enregistres[self.liste_paires[0]]["resultatM"] = self.resultat_du_tour[0]
        self.joueurs_enregistres[self.liste_paires[1]]["resultatM"] = self.resultat_du_tour[1]
            

        for i in range(2):

            if self.joueurs_enregistres[self.liste_paires[i]]["resultatM"] == "W":
                self.joueurs_enregistres[self.liste_paires[i]]["score"] = self.joueurs_enregistres[self.liste_paires[i]]["score"] + 1
            elif self.joueurs_enregistres[self.liste_paires[i]]["resultatM"] == "L":
                self.joueurs_enregistres[self.liste_paires[i]]["score"] = self.joueurs_enregistres[self.liste_paires[i]]["score"] + 0
            else: 
                self.joueurs_enregistres[self.liste_paires[i]]["score"] = self.joueurs_enregistres[self.liste_paires[i]]["score"] + 0.5

        
        joueur_un = [self.liste_paires[0]], [self.joueurs_enregistres[self.liste_paires[0]]["score"] ]
        joueur_deux = [self.liste_paires[1]], [self.joueurs_enregistres[self.liste_paires[1]]["score"] ]
       


        joueur_et_score =(joueur_un, joueur_deux)
        self.stockage_des_resultats.append(joueur_et_score)
        

        self.tuples_match = self.stockage_des_resultats
        return self.tuples_match 

class ListeDesJoueurs:
    def __init__(self, joueurs, validation_recuperation_joueur) -> None:

        self.joueurs = joueurs 
        self.validation_recuperation_joueur = validation_recuperation_joueur

    def recuperation_liste_des_joueurs_du_tournois (self):
        
        if self.validation_recuperation_joueur == "n": 
            print("Vous ne souhaitez pas afficher la liste des joueurs")
        else:
            self.liste_des_joueurs = []

            keys = self.joueurs.keys()

            for key in keys: 
                self.liste_des_joueurs.append(key)

            self.liste_des_joueurs.sort()

            return self.liste_des_joueurs

class ListeDesTournois : 
    def __init__(self, dict_tournois, validation_recuperation_tournois) -> None:

        self.dict_tournois = dict_tournois
        self.validation_recuperation_tournois = validation_recuperation_tournois

    def recuperation_liste_des_tournois(self):

        if self.validation_recuperation_tournois == "n":
            print("vous ne souhaitez pas afficher la liste des tournois")
        else : 
            liste_des_tournois = []

            keys = self.dict_tournois["Tournois"].keys()

            for key in keys : 
                liste_des_tournois.append(key)

            return liste_des_tournois

class RecuperationDesDonneesDunTournois : 
    def __init__(self,dict_de_lecture_du_json_tournois) -> None:

        self.dict_tournois = dict_de_lecture_du_json_tournois
    
    def recuperation_donnee_instant_t_tournois(self, validation):

        if validation == "o":


            key = self.dict_tournois["Tournois"].keys()
            liste_des_cles_des_tournois = []
            for keys in key:
                liste_des_cles_des_tournois.append(keys)

            info_du_tournois = self.dict_tournois["Tournois"][liste_des_cles_des_tournois[-1]]

            return info_du_tournois


    def recuperation_date_et_nom_dun_tournois(self,liste_des_tournois, numero_tournois_souhaite):
        self.numero_tournois_souhaite = numero_tournois_souhaite
        

        if self.numero_tournois_souhaite == None:
                print("vous ne souhaitez pas voir la date/le nom d'un tournois donné ? (o/n) : ")
        if self.numero_tournois_souhaite != None:
                date_et_nom_dun_tournois = []
                
                date_et_nom_dun_tournois.append(self.dict_tournois["Tournois"][liste_des_tournois[self.numero_tournois_souhaite]]["nom_du_tournois"])
                date_et_nom_dun_tournois.append(self.dict_tournois["Tournois"][liste_des_tournois[self.numero_tournois_souhaite]]["date_de_debut_du_tournois"])
                date_et_nom_dun_tournois.append(self.dict_tournois["Tournois"][liste_des_tournois[self.numero_tournois_souhaite]]["date_de_fin_du_tournois"])

                return date_et_nom_dun_tournois

    def recuperation_des_joueurs_dun_tournois(self,liste_des_tournois, numero_tournois_souhaite):

            self.numero_tournois_souhaite = numero_tournois_souhaite

            if self.numero_tournois_souhaite == None:
                pass
            if self.numero_tournois_souhaite != None:

                liste_des_joueurs_dun_tournoi = []


                Keys = self.dict_tournois["Tournois"][liste_des_tournois[self.numero_tournois_souhaite]]["liste_des_joueurs_enregistres"].keys()
                
                for key in Keys :
                    liste_des_joueurs_dun_tournoi.append(key)
                
                liste_des_joueurs_dun_tournoi.sort()

                return liste_des_joueurs_dun_tournoi

    def recuperation_des_tours_dun_tournois(self, numero, liste_des_tournois):
        self.numero_tournois_souhaite = numero
        self.liste_des_tournois = liste_des_tournois
        if self.numero_tournois_souhaite == None:
            pass
        if self.numero_tournois_souhaite != None:
            liste_des_tours_dun_tournoi = []


            liste_des_tours_dun_tournoi.append(self.dict_tournois["Tournois"][self.liste_des_tournois[self.numero_tournois_souhaite]]["liste_des_tours"])  

            return liste_des_tours_dun_tournoi

