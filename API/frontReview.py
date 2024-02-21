import streamlit as st
import requests
import csv
import os

modelResult = ["Shorts","Shirt","Socks","Coat","Dress","Boots","Handbag","Sunglasses","Hat","Belt","Backpack","Scarf","Jacket","Jeans","Gloves","Sneakers","Sweater","Pants","T-shirt","Jewelry","Skirt", "Blouse", "Sandals", "Hoodie","Shoes"]

SAVE_FILENAME = "predictionsReview.csv"

donneesFile = [["Age", "Genre", "Location", "Subscription Status", "Frequency of Purchases", 
               "Season", "Shipping Type", "Discount Applied", "Promo Code Used", "Payment Method",
               "Reco1", "Reco2", "Reco3"]]


def predict(data):
    url = "http://localhost:8080/predictknn"  # URL de l'endpoint de prédiction
    response = requests.post(url, json=data)  # Envoie de la requête POST avec les données
    prediction = response.json()  # Récupération de la prédiction depuis la réponse JSON
    return prediction


def getItemsToRecommend(uniqueProducts, idClient, prediction): 
    recommendedItems = []
    alreadyBought = []
    #On récupère les produits déjà achetés
    for i in range(len(reviews[idClient])):
        if reviews[idClient][i] > 0:
            print(uniqueProducts[i])
            alreadyBought.append(uniqueProducts[i])
            
    #On récupère les produits recommandés
    for j in range(len(prediction)):
        if prediction[j] > 0:
            #Si le produit n'est pas déjà acheté on l'ajoute à la liste des recommandations
            if uniqueProducts[j] not in alreadyBought:
                recommendedItems.append(uniqueProducts[j])
    return recommendedItems



values = ["Age", "Genre", "Location", "Subscription Status", "Frequency of Purchases"]
cols_cat_info = [1,2,3,4,5]
cols_data = [1,2,3,4,5, 11,13,14,15,17]

with open("../csv/shopping_behavior_updated.csv", mode='r', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        donnees = list(reader)
del donnees[0]

with open("../csv/review_table.csv", mode='r', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        reviews = list(reader)
        del reviews[0]
        for ligne in range(len(reviews)):
            for col in range(len(reviews[ligne])):
                reviews[ligne][col] = float(reviews[ligne][col])

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
        for ligne in donnees:
            if ligne[0] == id:
                person =  ligne
                break
        data = []
        for i in cols_data:
            data.append(person[i])
        
        # Appel de la fonction de prédiction avec les données saisies
        prediction = list(predict({"data": data})["predictions"].values())
        
        nouvelle_ligne = data
        
        st.write("Prédiction obtenue :")
        products = getItemsToRecommend(modelResult, int(id)-1, prediction)
        txt = ""
        for i in products:
            txt = txt + i + ", "
            nouvelle_ligne.append(i)
        txt = txt[:-2]
        st.write(txt)
        
        if len(donneesFile) > 1:
            donneesFile.remove(1)
        donneesFile.append(nouvelle_ligne)
        with open(SAVE_FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows(donneesFile)

# Appel de la fonction principale pour exécuter l'interface
if __name__ == "__main__":
    main()