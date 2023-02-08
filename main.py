import controler
import model
import view



class main: 

    """lancement du programme complet. Première phase d'inialisation du tournois puis déroulement du tournois"""
    def __init__(self, liste_de_joueurs, liste_de_tournois) -> None:
        self.liste_de_joueurs = liste_de_joueurs
        self.liste_de_tournois = liste_de_tournois

    def deroulement_du_programme(self):
        #ajout d'un joueur

        ajout_dun_joueur = view.AjouterUnJoueur().volonte_dajouter_un_joueur()
        while ajout_dun_joueur == "o":
            nouveau_joueur = view.AjouterUnJoueur().recuperation_infos_nouveau_joueur(ajout_dun_joueur)
            model.Joueur(nouveau_joueur).ajout_du_joueur(self.liste_de_joueurs)
            ajout_dun_joueur = view.AjouterUnJoueur().volonte_dajouter_un_joueur()

        #ajout d'un tournois   

        nouveau_tournoi = view.CreerUnTournois().recuperation_info_nouveau_tournois()
        model.tournoi(nouveau_tournoi, self.liste_de_tournois).ajout_dun_nouveau_tournois()
        

        

main('joueurs.json', 'tournois.json').deroulement_du_programme()