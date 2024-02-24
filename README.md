## Utilisation de l'API

Pour lancer l'API, ouvrez un terminal dans le dossier "API" du projet
Exécutez les commandes suivantes : 
- uvicorn api:app --host 0.0.0.0 --port 8080
- streamlit run frontReview.py --server.port 8081
- streamlit run front.py --server.port 8082

L'API écrit les résultats des prédictions dans des fichiers csv : 
-  "prediction.csv" correspond aux prédictions réalisées pour un nouvel utilisateur.
-  "predictionReview.csv" correspond aux prédictions réalisées pour un utilisateur déjà client du site.


## Dashboard PowerBI
Il est nécessaire de refaire les liens avec les différents excels pour assurer le sourcing.

Les prédictions doivent pointer sur les fichiers présents dans le dossier api.
Il faut donc que l'élément présentant la prédiction pour un nouvel utilisateur pointe sur "prediction.csv" du dossier API.
Il faut que l'élément présentant la prédiction sur un utilisateur déjà présent dans la base de donnée pointe sur "predictionReview.csv" du dossier API.
  

