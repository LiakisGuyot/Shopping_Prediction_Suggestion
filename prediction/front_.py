import streamlit as st
import requests
import csv


def predict(data):
    url = "http://localhost:8080/predict"  # URL de l'endpoint de prédiction
    response = requests.post(url, json=data)  # Envoie de la requête POST avec les données
    prediction = response.json()  # Récupération de la prédiction depuis la réponse JSON
    return prediction


values = ["Age", "Genre", "Location", "Subscription Status", "Frequency of Purchases"]
cols_cat_info = [1,2,3,4,5]

with open("../csv/shopping_behavior_updated.csv", mode='r', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        donnees = list(reader)
del donnees[0]

with open("../csv/review_table.csv", mode='r', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        reviews = list(reader)

ids = [ligne[0] for ligne in donnees]

        
def main():
    st.title("Interface de prédiction pour des clients deja existant")

    # Champs de saisie manuelle pour les données de test
    id = st.selectbox("Sélectionnez l'id de la personne ", ids)
    if st.button("Rechercher"):
        st.write("Caractéristique de la personne :")
        for ligne in donnees:
            if ligne[0] == id:
                person =  ligne
                break
        txt = ""
        for i, val in enumerate(cols_cat_info):
            txt = txt + values[i] + ": " + person[val] + ", "
        txt = txt[:-2]
        st.write(txt)

        # Bouton pour faire la prédiction
        if st.button("Faire la prédiction"):
            # Création d'un dictionnaire avec les données saisies
            
            # Appel de la fonction de prédiction avec les données saisies
            prediction = predict(reviews[id])
            st.write("Prédiction obtenue :")
            st.write(prediction)

# Appel de la fonction principale pour exécuter l'interface
if __name__ == "__main__":
    main()