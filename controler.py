import json
import view 
import model


class LancerLeProgramme :
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
                tours = tours +1
                print("debut du tours N°" + str(tours))
                if tours == 0:
                    Paire_du_tour = model.CreationPairesJoueurs(Liste_des_joueurs_du_tournois).paires

                    for nombre_de_paires in range(len(Paire_du_tour)) :
                        resultat_du_tour = view.DonnerLesResultatsDunTour(Paire_du_tour["Paire N°" + str(nombre_de_paires)]).resultat_des_joueurs_sur_le_tour
                        match = model.Matchs(Paire_du_tour["Paire N°" + str(nombre_de_paires)], Liste_des_joueurs_du_tournois, resultat_du_tour)

                    classement_joueurs = model.ClassementJoueurs(Liste_des_joueurs_du_tournois).classement_tour
                    liste_des_tours["Round N°" + str(tours)]= Paire_du_tour, classement_joueurs
                else: 

                    classement_joueurs = model.ClassementJoueurs(Liste_des_joueurs_du_tournois).classement_tour
                    Paire_du_tour = model.CreationPairesJoueurs(classement_joueurs).paires

                    for nombre_de_paires in range(len(Paire_du_tour)) :
                        resultat_du_tour = view.DonnerLesResultatsDunTour(Paire_du_tour["Paire N°" + str(nombre_de_paires)]).resultat_des_joueurs_sur_le_tour
                        match = model.Matchs(Paire_du_tour["Paire N°" + str(nombre_de_paires)], Liste_des_joueurs_du_tournois, resultat_du_tour)
        
                    liste_des_tours["Round N°" + str(tours)]= Paire_du_tour, classement_joueurs
                model.Tournois("tournois.json", tours, liste_des_tours, Liste_des_joueurs_du_tournois, Recuperation_donnees_du_tournois["nom_du_tournois"])

            self.resultat_final = classement_joueurs
            print(self.resultat_final)
            #print(liste_des_tours)





