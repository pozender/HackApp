@echo off

REM Ajouter tous les fichiers modifiés
git add .

REM Effectuer un commit avec le message spécifié
git commit -m "ceci est une update"

REM Pousser les modifications vers le dépôt distant
git push
