import time
import controler
import view
from model_package import (Joueur, Joueurs,
                           lecture_dun_fichier_json, Tournoi, Tours, Tournois)


class Main:
    """Phase d'inialisation du tournois puis déroulement du tournois"""
    def __init__(self, liste_de_joueurs, liste_de_tournois) -> None:
        self.liste_de_joueurs = liste_de_joueurs
        self.liste_de_tournois = liste_de_tournois

    def deroulement_du_programme(self):
        """ajout d'un joueur"""
        dict_des_joueurs = lecture_dun_fichier_json.lecture_dun_fichier_json(
            self.liste_de_joueurs)
        ajout_dun_joueur = view.AjouterUnJoueur().volonte_dajouter_un_joueur()
        while ajout_dun_joueur == "o":
            nouveau_joueur = (view.AjouterUnJoueur().
                              recuperation_infos_nouveau_joueur(
                                ajout_dun_joueur))

            verif = (controler.VerifDoublonJoueurs().
                     verif_du_doublon(dict_des_joueurs, nouveau_joueur))

            if verif is True:
                Joueur.Joueur(nouveau_joueur).ajout_du_joueur(
                    self.liste_de_joueurs)
            else:
                print("joueur déjà enregistré")

            ajout_dun_joueur = (view.AjouterUnJoueur().
                                volonte_dajouter_un_joueur())

        """ajout d'un tournois"""

        nouveau_tournoi = (view.CreerUnTournois().
                           recuperation_info_nouveau_tournois())

        (Tournoi.Tournoi(nouveau_tournoi,
                         self.liste_de_tournois).ajout_dun_nouveau_tournois())

        """creation de la list des joueurs du tournoi"""

        joueurs_du_tournois = (Joueurs.Joueurs(self.liste_de_joueurs).
                               creation_du_dict_de_joueurs_pour_le_tournois())

        """initialisation du nombre de tours"""

        nombre_de_tours = (Tours.Tours(self.liste_de_tournois).
                           initialisation_du_nombre_de_tour())

        """Déroulement d'un tour"""

        (Tournois.Tournois(self.liste_de_tournois,
                           0,
                           " ",
                           joueurs_du_tournois).
         ajout_des_donnee_du_tour_dun_tournois_dans_le_fichier_json())

        liste_des_tours = {}

        for tours_actuel in range(int(nombre_de_tours)):
            """Lancement d'un tour"""

            date_debut_de_tour = time.strftime("%Y-%m-%d %H:%M:%S")
            tours_actuel = tours_actuel + 1

            if tours_actuel == 1:

                paires_du_tour = (controler.
                                  CreationPairesJoueurs(joueurs_du_tournois,
                                                        tours_actuel, None).
                                  creation_des_paire())

                """Déroulement des matchs et ajout du score"""

                for nb_paires in range(len(paires_du_tour)):

                    resultat_du_tour = (view.DonnerLesResultatsDunTour
                                        (paires_du_tour["Paire N°" +
                                                        str(nb_paires)],
                                         nb_paires).
                                        recuperer_les_resultats_du_tour())

                    resultat_joueurs_tour = (controler.
                                             AjoutDuScore(
                                                paires_du_tour["Paire N°" +
                                                               str(nb_paires)],
                                                joueurs_du_tournois).
                                             recuperer_les_resultats_du_tour(
                                                resultat_du_tour))

                    (controler.
                     AjoutDuScore(paires_du_tour["Paire N°" + str(nb_paires)],
                                  joueurs_du_tournois).resultats_des_matchs(
                                    resultat_joueurs_tour))

                """Classement des joueurs, ajout des infos des rounds"""

                classement_des_joueurs = (controler.
                                          ClassementJoueurs(
                                            joueurs_du_tournois).
                                          classement_des_joueurs())

                date_fin_de_tour = time.strftime("%Y-%m-%d %H:%M:%S")

                liste_des_tours["Round N°" + str(tours_actuel)] = (

                    date_debut_de_tour,
                    date_fin_de_tour,
                    paires_du_tour,
                    classement_des_joueurs)

            else:

                """CLassement des joueurs et création des paires"""

                classement_des_joueurs = (controler.
                                          ClassementJoueurs(
                                            joueurs_du_tournois).
                                          classement_des_joueurs())

                paires_du_tour = (controler.
                                  CreationPairesJoueurs(joueurs_du_tournois,
                                                        tours_actuel,
                                                        liste_des_tours).
                                  creation_des_paire())

                for nb_paires in range(len(paires_du_tour)):

                    resultat_du_tour = (view.
                                        DonnerLesResultatsDunTour(
                                            paires_du_tour["Paire N°" +
                                                           str(nb_paires)],
                                            nb_paires).
                                        recuperer_les_resultats_du_tour())

                    resultat_joueurs_tour = (controler.
                                             AjoutDuScore(
                                                paires_du_tour["Paire N°" +
                                                               str(nb_paires)],
                                                joueurs_du_tournois).
                                             recuperer_les_resultats_du_tour(
                                                resultat_du_tour))

                    (controler.AjoutDuScore(paires_du_tour["Paire N°" +
                                                           str(nb_paires)],
                                            joueurs_du_tournois).
                     resultats_des_matchs(resultat_joueurs_tour))

                date_fin_de_tour = time.strftime("%Y-%m-%d %H:%M:%S")

                liste_des_tours["Round N°" + str(tours_actuel)] = (
                    date_debut_de_tour,
                    date_fin_de_tour,
                    paires_du_tour,
                    classement_des_joueurs)

            (Tournois.Tournois(self.liste_de_tournois,
                               tours_actuel,
                               liste_des_tours,
                               joueurs_du_tournois).
             ajout_des_donnee_du_tour_dun_tournois_dans_le_fichier_json())

            recuperer_les_donnees = (
                view.DonneesDuTournois(self.liste_de_tournois).
                recuperer_les_donnees_du_tournois_a_un_tour_t())

            """Récupération des données du tour"""

            if recuperer_les_donnees == "o":

                dict_des_tournois = (lecture_dun_fichier_json.
                                     lecture_dun_fichier_json(
                                      self.liste_de_tournois))

                donnees_au_tour_t = (
                    controler.RecuperationDesDonneesDunTournois(
                        dict_des_tournois).
                    recuperation_donnee_instant_t_tournois(
                        recuperer_les_donnees))

                view.affichage_des_donnees(donnees_au_tour_t)

        return joueurs_du_tournois

    def recuperation_de_data(self, liste_joueurs_du_tournoi) -> None:

        """Récuperation des différentes données"""

        dict_tournois = (lecture_dun_fichier_json.
                         lecture_dun_fichier_json(self.liste_de_tournois))

        """affichage de la liste des joueurs du tournoi"""

        recuperer_la_liste_des_joueurs = (
            view.DonneesDuTournois(self.liste_de_tournois).
            recuperation_des_joueurs_dun_tournois())

        liste_des_joueurs = (
            controler.ListeDesJoueurs(liste_joueurs_du_tournoi,
                                      recuperer_la_liste_des_joueurs).
            recuperation_liste_des_joueurs_du_tournois())

        view.affichage_des_donnees_en_liste(liste_des_joueurs)

        """affichage de la liste des tournois"""

        recuperer_la_liste_des_tournois = (
            view.DonneesDuTournois(self.liste_de_tournois).
            recuperation_liste_tournois())

        liste_des_tournois = (
            controler.ListeDesTournois(dict_tournois,
                                       recuperer_la_liste_des_tournois).
            recuperation_liste_des_tournois())

        view.affichage_des_donnees_en_liste(liste_des_tournois)

        """affichage des infos d'un tournoi sélectionné (date, nom ...)"""

        numero_du_tournois_souhaite = (
            view.DonneesDuTournois(self.liste_de_tournois).
            recuperation_date_et_nom_dun_tournois())

        date_et_nom_dun_tournoi_souhaite = (
            controler.RecuperationDesDonneesDunTournois(dict_tournois).
            recuperation_date_et_nom_dun_tournois(liste_des_tournois,
                                                  numero_du_tournois_souhaite))

        view.affichage_des_donnees_en_liste(date_et_nom_dun_tournoi_souhaite)

        joueurs_dun_tournoi_souhaite = (
            controler.RecuperationDesDonneesDunTournois(dict_tournois).
            recuperation_des_joueurs_dun_tournois(liste_des_tournois,
                                                  numero_du_tournois_souhaite))

        view.affichage_des_donnees_en_liste(joueurs_dun_tournoi_souhaite)

        liste_des_tours_et_matchs = (
            controler.RecuperationDesDonneesDunTournois(dict_tournois).
            recuperation_des_tours_dun_tournois(numero_du_tournois_souhaite,
                                                liste_des_tournois))

        view.affichage_des_donnees(liste_des_tours_et_matchs)


liste_joueurs_du_tournois = (
    Main('joueurs.json', 'tournois.json').
    deroulement_du_programme())

(Main('joueurs.json', 'tournois.json').
 recuperation_de_data(liste_joueurs_du_tournois))
