# Jeu de Devinettes Coloré en Python

## Description

Ce projet est un petit jeu de devinettes où l'utilisateur doit deviner un nombre aléatoire choisi par le programme entre 1 et 100. Le jeu fournit des indices après chaque tentative, indiquant si le nombre deviné est trop petit ou trop grand. Lorsque l'utilisateur devine correctement, un message coloré apparaît, félicitant le joueur.

## Fonctionnalités

- Génération d'un nombre aléatoire entre 1 et 100.
- L'utilisateur fait des tentatives pour deviner ce nombre.
- Des indices colorés sont fournis après chaque essai :
  - **Bleu** pour "Trop petit".
  - **Rouge** pour "Trop grand".
  - **Vert** pour "Correct".
- Affichage du nombre de tentatives lorsque l'utilisateur trouve la bonne réponse.

## Technologies utilisées

- Python 3.x
- [termcolor](https://pypi.org/project/termcolor/) pour ajouter des couleurs aux messages affichés dans le terminal.

## Installation

1. Clonez ce dépôt sur votre machine locale :

   ```bash
   git clone https://github.com/votre-utilisateur/guess-game.git```

2. Accédez au répertoire du projet :
   ```bash
   cd guess-game```

3. Installez les dépendances :
   ```bash
   pip install termcolor```

4. Lancez le jeu :
   ```bash
   python guess_game.py```

## Améliorations possibles

- Ajouter un nombre limité de tentatives avant que le jeu ne se termine.
- Créer une interface graphique pour le jeu.
- Ajouter des niveaux de difficulté avec des plages de nombres différentes.

## Contribution

Si vous souhaitez contribuer à ce projet, veuillez suivre ces étapes :

1. Faites un fork de ce dépôt.
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/ma-fonctionnalité`).
3. Commitez vos changements (`git commit -am 'Ajout de ma fonctionnalité'`).
4. Poussez vos modifications (`git push origin feature/ma-fonctionnalité`).
5. Ouvrez une pull request.

## Licence

Ce projet est sous licence MIT.

```Ce format devrait maintenant fonctionner correctement pour un fichier `README.md`. Il contient des sections claires avec des instructions de mise en place, des fonctionnalités et une explication du projet, et tout est structuré avec le format Markdown approprié.```