import json
import view 
import model
import time
import pprint


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


class Matchs:
    """Définition des classements finaux (tant qu'il n'y a pas de view + stockage des résultats des matchs"""
    def __init__(self,liste_paires, joueurs_enregistres, resultat_du_tour):

        self.liste_paires = liste_paires
        self.joueurs_enregistres = joueurs_enregistres
        self.resultat_du_tour = resultat_du_tour

    def resultats_des_matchs(self):

        
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

            print(self.liste_des_joueurs)

































"""
class DeroulementDuProgramme :
    def __init__(self) -> None:

        view.AjouterUnJoueur("joueurs.json")
        Liste_des_joueurs_du_tournois = model.Joueurs("joueurs.json").joueurs_vf
        Recuperation_donnees_du_tournois = view.CreerUnTournois("tournois.json").tournois_cree
        LancementDuTournoi = view.LancerLeTournois().lancer_le_tournois
        nombre_de_tours = model.Tours(Recuperation_donnees_du_tournois["nombre_de_tours"]).nombre_de_tours


        if LancementDuTournoi == "n": 
            print("vous ne souhaitez pas lancer le tournois pour le moment")
            
        else :
            model.Tournois("tournois.json", 0, " ", Liste_des_joueurs_du_tournois, Recuperation_donnees_du_tournois["nom_du_tournois"])
            liste_des_tours = {}
            for tours in range(int(nombre_de_tours)):
                self.date_debut_de_tour = time.strftime("%Y-%m-%d %H:%M:%S")
                tours = tours +1
                print("debut du tours N°" + str(tours))
                if tours == 1:
                    Paire_du_tour = model.CreationPairesJoueurs(Liste_des_joueurs_du_tournois,tours, None).paires

                    for nombre_de_paires in range(len(Paire_du_tour)) :
                        resultat_du_tour = view.DonnerLesResultatsDunTour(Paire_du_tour["Paire N°" + str(nombre_de_paires)], nombre_de_paires ).resultat_des_joueurs_sur_le_tour
                        match = model.Matchs(Paire_du_tour["Paire N°" + str(nombre_de_paires)], Liste_des_joueurs_du_tournois, resultat_du_tour).tuples_match

                    classement_joueurs = model.ClassementJoueurs(Liste_des_joueurs_du_tournois).classement_tour
                    self.date_fin_de_tour = time.strftime("%Y-%m-%d %H:%M:%S")
                    liste_des_tours["Round N°" + str(tours)]= self.date_debut_de_tour, self.date_fin_de_tour, Paire_du_tour, classement_joueurs
                else: 

                    classement_joueurs = model.ClassementJoueurs(Liste_des_joueurs_du_tournois).classement_tour
                    Paire_du_tour = model.CreationPairesJoueurs(classement_joueurs,tours,liste_des_tours).paires

                    for nombre_de_paires in range(len(Paire_du_tour)) :
                        resultat_du_tour = view.DonnerLesResultatsDunTour(Paire_du_tour["Paire N°" + str(nombre_de_paires)], nombre_de_paires ).resultat_des_joueurs_sur_le_tour
                        match = model.Matchs(Paire_du_tour["Paire N°" + str(nombre_de_paires)], Liste_des_joueurs_du_tournois, resultat_du_tour).tuples_match
        
                    self.date_fin_de_tour = time.strftime("%Y-%m-%d %H:%M:%S")
                    liste_des_tours["Round N°" + str(tours)]= self.date_debut_de_tour, self.date_fin_de_tour, Paire_du_tour, classement_joueurs
                model.Tournois("tournois.json", tours, liste_des_tours, Liste_des_joueurs_du_tournois, Recuperation_donnees_du_tournois["nom_du_tournois"])
                view.DonneesDuTournois("tournois.json",Recuperation_donnees_du_tournois["nom_du_tournois"])


            self.resultat_final = classement_joueurs
            print(self.resultat_final)
            pprint.pprint(liste_des_tours)
            
class RecuperationDeData: 
    def __init__(self) -> None:

        Liste_des_joueurs_du_tournois = model.Joueurs("joueurs.json").joueurs_vf

        recuperation_des_joueurs = view.RecuperationDesJoueurs().recuperation_liste_joueurs

        model.ListeDesJoueurs(Liste_des_joueurs_du_tournois, recuperation_des_joueurs)

        recuperation_des_tournois = view.RecuperationDesTournois().recupration_liste_tournois     
        liste_nom_tournois = model.ListeDesTournois("tournois.json",recuperation_des_tournois).liste_des_tournois

        numero_du_tournois = view.RecuperationDateetNomDunTournois().numero_du_tournois
        model.RecuperationDuNomEtDateDunTournoiDonne(liste_nom_tournois,numero_du_tournois, "tournois.json")
        model.RecuperationDesJoueursDunTournoi(liste_nom_tournois,numero_du_tournois, "tournois.json")
        model.RecuperationDesToursDunTournoi(liste_nom_tournois,numero_du_tournois,"tournois.json")
        

"""



