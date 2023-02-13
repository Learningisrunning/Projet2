import pprint
Tournois_dict = {}


class AjouterUnJoueur:
    """ajout d'un joueur"""

    def volonte_dajouter_un_joueur(self):
        """verification de la volonté d'ajouter un joueur"""
        ajouterunjoueur = input("voulez-vous ajouter un joueur ? (n/o)")

        return ajouterunjoueur

    def recuperation_infos_nouveau_joueur(self, ajouter_un_joueur) -> None:
        """Récuperation des infos du nouveau joueur"""

        if ajouter_un_joueur == "n":
            print("aucun joueur ne sera ajouter" +
                  " à la liste précédement fournis")
        else:
            nom = input("Nom du joueur :")
            prenom = input("Prenom du joueur : ")
            date_de_naissance = input("Date de naissance du joueur : ")
            identifiant_national_dechec = (
                input("identifiant national d'echec du joueur :"))

        nouveau_joueur = {

                "nom_de_famille": nom,
                "prenom": prenom,
                "date_de_naissance": date_de_naissance,
                "identifiant_national_dechec": identifiant_national_dechec

            }

        return nouveau_joueur


class CreerUnTournois:
    """Creation d'un tournois"""

    def recuperation_info_nouveau_tournois(self) -> None:
        """recuperation des infos du nouveau tournois"""
        creer_un_tournois = input("Souhaitez-vous créer un tournois ? (o/n): ")

        if creer_un_tournois == "n":
            print("vous ne souhaitez pas créer de tournois")
        else:

            nom = input("indiquer le nom du tournois :")
            lieu = input("indiquer le lieu du tournois :")
            date_debut = " "
            date_fin = " "
            numero_tour_actuel = " "
            liste_des_tours = " "
            liste_joueurs_enregistres = (
                input("indiquer le fichier contenant" +
                      " la liste des joueurs enregistrés : "))
            remarque_directeur = input("indiquer les remarques du directeur: ")
            nombre_de_tours = input("indiquer le nombre de tours : ")

            nouveau_tournoi = {

                "nom_du_tournois": nom,
                "lieu_du_tournois": lieu,
                "date_de_debut_du_tournois": date_debut,
                "date_de_fin_du_tournois": date_fin,
                "numero_tour_actuel": numero_tour_actuel,
                "liste_des_tours": liste_des_tours,
                "liste_des_joueurs_enregistres": liste_joueurs_enregistres,
                "remarque_du_directeur": remarque_directeur,
                "nombre_de_tours": nombre_de_tours


                }

            return nouveau_tournoi

    def lancement_dun_tournois(self):
        """lancement d'un tournois"""

        lancer_le_tournois = input("souhaitez-vous" +
                                   " lancer le tournois ? (o/n): ")

        return lancer_le_tournois


class DonnerLesResultatsDunTour:
    "demander à l'utilisateur qui a gagné"

    def __init__(self, paire, numero_de_la_paire) -> None:

        self.paire = paire
        self.numero_de_la_paire = numero_de_la_paire

    def recuperer_les_resultats_du_tour(self):
        """recuperer les resultats du tour"""
        resultat_joueur_un_de_la_paire = (
            input("Pouvez-vous indiquer le résultat du joueur n°1 ("
                  + self.paire[0]
                  + ") pour le match N°"
                  + str(self.numero_de_la_paire) + " (W/L/D):"))

        return resultat_joueur_un_de_la_paire


class DonneesDuTournois:
    """ recuperation des données du tournois"""

    def __init__(self, fichier) -> None:
        self.fichier = fichier

    def recuperer_les_donnees_du_tournois_a_un_tour_t(self):
        """recuperation des données du tournois a un tour t"""

        charger_les_donnees = input("Souhaitez-vous charger" +
                                    "les données du tournois ? (o/n) : ")

        return charger_les_donnees

    def recuperation_des_joueurs_dun_tournois(self):
        """recuperation des joueurs d'un tournois"""
        recuperation_liste_joueurs = (
            input("Souhaitez-vous récupérer la liste des joueurs ? (o/n) : "))

        return recuperation_liste_joueurs

    def recuperation_liste_tournois(self):
        """recuperation de la liste des tournois"""
        recupration_liste_tournois = (
            input("Souhaitez-vous récupérer la liste des tournois ? (o/n) : "))

        return recupration_liste_tournois

    def recuperation_date_et_nom_dun_tournois(self):
        """recuperation de la date et du nom d'un tournois"""

        recuperation_date_et_nom_dun_tournois = (
            input("Souhaitez-vous récupérer le nom, la date," +
                  " la liste des joueurs et des" +
                  " tours d'un match précis ? (o/n) "))

        if recuperation_date_et_nom_dun_tournois == "o":
            numero_du_tournois = (
                input("Veuillez nous indiquer le numéro du tournoi concerné" +
                      " (cf : la liste du dessus) (1,2,3..) : "))
            numero_du_tournois = int(numero_du_tournois) - 1

        return numero_du_tournois


def affichage_des_donnees(data):
    """affichage des données avec pprint"""
    pprint.pprint(data)


def affichage_des_donnees_en_liste(data):
    """affichage des données en brut"""
    print(data)
