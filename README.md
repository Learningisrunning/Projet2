Guide pour lancer le programme de gestion des tournois d'échec. 

1- installer l'ensemble du code sur un ordinateur.  
2- Ajouter dans le fichier contenant tous les fichier .py les deux fichiers json (tournois.json et joueurs.json).  
3- Les deux fichiers json doivent suivre le format :  
{  
    "Joueurs":[  

    ]  
}  
et  
{  
    "Tournois":{  

    }  
}  
4- taper dans la console "python main.py" et suivez les indications données dans la console.  

Générer un flake8-report:  
1- installez flake8 avec la commande : "$ pip install flake8-html"  
2- Générez le fichier avec la commande : "$ flake8 --format=html --htmldir=flake-report"  
3- allez dans le dossier flak8-report qui vient d'être généré et cliquer sur le fichier .html  