import random


class VerifDoublonJoueurs:
    """Vérification des doublons"""

    def verif_du_doublon(self, dict_des_joueurs, nouveau_joueur):
        """Vérification des doublons de joueurs"""

        nouvelle_identifiant_echec = (
            nouveau_joueur["identifiant_national_dechec"])

        verification = bool

        for nb_joueurs in range(len(dict_des_joueurs["Joueurs"])):

            identifiants = (dict_des_joueurs["Joueurs"][nb_joueurs]
                            ["identifiant_national_dechec"])

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
        """Classement des joueurs"""

        classement_dict = (
            sorted(self.joueurs_enregistres,
                   key=lambda x: (self.joueurs_enregistres[x]["score"]),
                   reverse=True))

        classement_et_score = {}

        for joueurs in classement_dict:
            classement_et_score[joueurs] = (
                self.joueurs_enregistres[joueurs]["score"])

        classement_tour = classement_et_score

        return classement_tour


class CreationPairesJoueurs:
    "creation des paires pour les matchs"

    def __init__(self, joueurs, tours, liste_des_round):

        self.joueurs = joueurs
        self.tours = tours
        self.liste_des_round = liste_des_round

    def creation_des_paire(self):
        """Creation des paires pour les matchs"""

        liste_joueurs = []

        if type(self.joueurs) == dict:
            keys = self.joueurs.keys()

            for key in keys:
                liste_joueurs.append(key)
        else:
            liste_joueurs = self.joueurs

        les_paires = {}
        count = 0

        if self.tours == 1:
            random.shuffle(liste_joueurs)

            for i in range(int(len(liste_joueurs)/2)):
                for j in range(1):
                    les_paires["Paire N°" + str(i)] = (
                        liste_joueurs[count], liste_joueurs[count+1])
                    count = count+2
        else:
            for i in range(int(len(liste_joueurs)/2)):
                count = 0
                for j in range(1):
                    les_paires["Paire N°" + str(i)] = (
                        liste_joueurs[count], liste_joueurs[count+1])
                    count_bis = 0

                    for round in range(len(self.liste_des_round)):
                        for paire in range(int(len(self.joueurs)/2)):
                            nombre_de_paire_identique = 0

                            if les_paires["Paire N°" + str(i)] == (
                                    self.liste_des_round
                                    ["Round N°" + str(round+1)]
                                    [2]["Paire N°" + str(paire)]):

                                nombre_de_paire_identique = (
                                    nombre_de_paire_identique + 1)

                                if (nombre_de_paire_identique > 0 and
                                    len(liste_joueurs) > 2 and
                                        count_bis + 1 > len(liste_joueurs)):

                                    count_bis = count_bis + 1

                                    les_paires["Paire N°" + str(i)] = (
                                        liste_joueurs[count],
                                        liste_joueurs[count+1+count_bis])

                                    round = 0
                                    paire = 0

                index_du_premier_joueur = (
                    liste_joueurs.index(les_paires["Paire N°" + str(i)][0]))

                del liste_joueurs[index_du_premier_joueur]

                index_du_second_joueur = (
                    liste_joueurs.index(les_paires["Paire N°" + str(i)][1]))

                del liste_joueurs[index_du_second_joueur]

        print(les_paires)
        paires = les_paires

        return paires


class AjoutDuScore:
    """ ajout du scores obtenue pendant le tour à chaque joueurs """
    def __init__(self, liste_paires, joueurs_enregistres):
        self.liste_paires = liste_paires
        self.joueurs_enregistres = joueurs_enregistres

    def recuperer_les_resultats_du_tour(self, resultat_joueur_un_de_la_pair):
        """Recuperation des résultat du tour"""
        resultat_du_tour = []

        resultat_joueur_un_de_la_paire = resultat_joueur_un_de_la_pair

        if resultat_joueur_un_de_la_paire == "D":
            resultat_joueur_deux_de_la_paire = "D"
        elif resultat_joueur_un_de_la_paire == "W":
            resultat_joueur_deux_de_la_paire = "L"
        else:
            resultat_joueur_deux_de_la_paire = "W"

        resultat_du_tour.append(resultat_joueur_un_de_la_paire)
        resultat_du_tour.append(resultat_joueur_deux_de_la_paire)

        resultat_des_joueurs_sur_le_tour = resultat_du_tour

        return resultat_des_joueurs_sur_le_tour

    def resultats_des_matchs(self, resultat_du_tour):
        """resultats des matchs"""

        stockage_des_resultats = []
        joueur_un = []
        joueur_deux = []

        self.joueurs_enregistres[self.liste_paires[0]]["resultatM"] = (
            resultat_du_tour[0])

        self.joueurs_enregistres[self.liste_paires[1]]["resultatM"] = (
            resultat_du_tour[1])

        for i in range(2):

            if self.joueurs_enregistres[self.liste_paires[i]]["resultatM"] == (
                    "W"):
                self.joueurs_enregistres[self.liste_paires[i]]["score"] = (
                    self.joueurs_enregistres[self.liste_paires[i]]
                    ["score"] + 1)

            elif (self.joueurs_enregistres[self.liste_paires[i]]
                    ["resultatM"] == "L"):
                self.joueurs_enregistres[self.liste_paires[i]]["score"] = (
                    self.joueurs_enregistres[self.liste_paires[i]]
                    ["score"] + 0)

            else:
                self.joueurs_enregistres[self.liste_paires[i]]["score"] = (
                    self.joueurs_enregistres[self.liste_paires[i]]
                    ["score"] + 0.5)

        joueur_un = ([self.liste_paires[0]],
                     [self.joueurs_enregistres[self.liste_paires[0]]
                     ["score"]])

        joueur_deux = ([self.liste_paires[1]],
                       [self.joueurs_enregistres[self.liste_paires[1]]
                       ["score"]])

        joueur_et_score = (joueur_un, joueur_deux)
        stockage_des_resultats.append(joueur_et_score)

        tuples_match = stockage_des_resultats

        return tuples_match


class ListeDesJoueurs:
    """Récuperation et tri des joueurs du tournois"""
    def __init__(self, joueurs, validation_recuperation_joueur) -> None:

        self.joueurs = joueurs
        self.validation_recuperation_joueur = validation_recuperation_joueur

    def recuperation_liste_des_joueurs_du_tournois(self):
        """recuperation de la liste des joueurs du tournois"""
        if self.validation_recuperation_joueur == "n":
            print("Vous ne souhaitez pas afficher la liste des joueurs")
        else:
            liste_des_joueurs = []

            keys = self.joueurs.keys()

            for key in keys:
                liste_des_joueurs.append(key)

            liste_des_joueurs.sort()

            return liste_des_joueurs


class ListeDesTournois:
    """Récuperation et tri des tournois"""
    def __init__(self, dict_tournois, validation_recuperation_tournois):

        self.dict_tournois = dict_tournois
        self.validation_recuperation_tournois = (
            validation_recuperation_tournois)

    def recuperation_liste_des_tournois(self):
        """recupeartion de la liste des tournosi"""

        if self.validation_recuperation_tournois == "n":
            print("vous ne souhaitez pas afficher la liste des tournois")
        else:
            liste_des_tournois = []

            keys = self.dict_tournois["Tournois"].keys()

            for key in keys:
                liste_des_tournois.append(key)

            return liste_des_tournois


class RecuperationDesDonneesDunTournois:
    """recuperation des donnees dun tournois"""
    def __init__(self, dict_de_lecture_du_json_tournois) -> None:

        self.dict_tournois = dict_de_lecture_du_json_tournois

    def recuperation_donnee_instant_t_tournois(self, validation):
        """recuperation des données d'un tournois à un instant t"""

        if validation == "o":

            key = self.dict_tournois["Tournois"].keys()
            liste_des_cles_des_tournois = []

            for keys in key:
                liste_des_cles_des_tournois.append(keys)

            info_du_tournois = (self.dict_tournois["Tournois"]
                                [liste_des_cles_des_tournois[-1]])

            return info_du_tournois

    def recuperation_date_et_nom_dun_tournois(self, liste_des_tournois,
                                              numero_tournois_souhaite):
        """recuperation de la date et du nom d'un tournois"""

        if numero_tournois_souhaite is None:
            print("vous ne souhaitez pas voir la date/le nom" +
                  " d'un tournois donné ? (o/n) : ")

        if numero_tournois_souhaite is not None:
            date_et_nom_dun_tournois = []

            (date_et_nom_dun_tournois.
                append((self.dict_tournois["Tournois"]
                        [liste_des_tournois[numero_tournois_souhaite]]
                        ["nom_du_tournois"])))
            (date_et_nom_dun_tournois.
                append((self.dict_tournois["Tournois"]
                        [liste_des_tournois[numero_tournois_souhaite]]
                        ["date_de_debut_du_tournois"])))
            (date_et_nom_dun_tournois.
                append((self.dict_tournois["Tournois"]
                        [liste_des_tournois[numero_tournois_souhaite]]
                        ["date_de_fin_du_tournois"])))

            return date_et_nom_dun_tournois

    def recuperation_des_joueurs_dun_tournois(self, liste_des_tournois,
                                              numero_tournois_souhaite):
        """recuperation des joueurs d'un tournois précis"""

        if numero_tournois_souhaite is None:
            pass

        if numero_tournois_souhaite is not None:

            liste_des_joueurs_dun_tournoi = []

            keys = (self.dict_tournois["Tournois"]
                    [liste_des_tournois[numero_tournois_souhaite]]
                    ["liste_des_joueurs_enregistres"].keys())

            for key in keys:
                liste_des_joueurs_dun_tournoi.append(key)

            liste_des_joueurs_dun_tournoi.sort()

            return liste_des_joueurs_dun_tournoi

    def recuperation_des_tours_dun_tournois(self, numero, liste_des_tournois):
        """recuperation des rounds d'un tournois"""

        numero_tournois_souhaite = numero

        if numero_tournois_souhaite is None:
            pass
        if numero_tournois_souhaite is not None:
            liste_des_tours_dun_tournoi = []

            (liste_des_tours_dun_tournoi.
                append((self.dict_tournois["Tournois"]
                        [liste_des_tournois[numero_tournois_souhaite]]
                        ["liste_des_tours"])))

        return liste_des_tours_dun_tournoi
