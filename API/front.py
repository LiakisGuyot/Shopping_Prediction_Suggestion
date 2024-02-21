import streamlit as st
import requests

def predict(data):
    url = "http://localhost:8080/predict"  # URL de l'endpoint de prédiction
    response = requests.post(url, json=data)  # Envoie de la requête POST avec les données
    prediction = response.json()  # Récupération de la prédiction depuis la réponse JSON
    return prediction

loc = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado',
       'Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois',
       'Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland'
       ,'Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana'
       ,'Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York'
       ,'North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania'
       ,'Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah'
       ,'Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']
freq = ['Annually','Bi-Weekly','Every 3 Months','Fortnightly','Monthly','Quarterly','Weekly']
sizeList = ['L', 'M', 'S', 'XL']
colors = ['Beige', 'Black', 'Blue', 'Brown', 'Charcoal', 'Cyan', 'Gold', 'Gray', 'Green',
 'Indigo', 'Lavender', 'Magenta', 'Maroon', 'Olive', 'Orange', 'Peach', 'Pink',
 'Purple', 'Red', 'Silver', 'Teal', 'Turquoise', 'Violet', 'White', 'Yellow']
seasons = ['Fall', 'Spring', 'Summer', 'Winter']
shippingList = ['2-Day Shipping', 'Express', 'Free Shipping', 'Next Day Air', 'Standard', 'Store Pickup']
YesNo = ['No', 'Yes']
paymentMethod = ['Bank Transfer', 'Cash', 'Credit Card', 'Debit Card', 'PayPal', 'Venmo']

def main():
    st.title("Interface de prédiction")

    # Champs de saisie manuelle pour les données de test
    st.subheader("Saisie manuelle des données de test")
    age = st.number_input("Age", min_value=0, max_value=150, value=18, step=1)
    genre = st.radio("Choisissez votre genre", ('Male', 'Female'))
    location = st.selectbox("Choisissez une ville", loc)
    subscription = st.radio("Est il inscrit ", ('No', 'Yes'))
    frequency = st.selectbox("Choisissez une fréquence d'achat", freq)
    #size = st.selectbox("Choisissez votre taille", sizeList)
    #color = st.selectbox("Choisissez votre couleur favorite", colors)
    season = st.selectbox("Choisissez la saison de l'achat", seasons)
    #review = st.number_input("Review", min_value=0, max_value=5, value=3)
    shipping = st.selectbox("Choisissez votre moyen de livraison", shippingList)
    discount = st.selectbox("Choisissez si vous avez une réduction", YesNo)
    promo = st.selectbox("Choisissez si vous avez un code promo", YesNo)
    payment = st.selectbox("Choisissez votre moyen de payment favorie", paymentMethod)
    

    # Bouton pour faire la prédiction
    if st.button("Faire la prédiction"):
        # Création d'un dictionnaire avec les données saisies
        data = {
            "Age": age,
            "Genre": genre,
            "Location": location,
            "Subscription Status": subscription,
            "Frequency of Purchases": frequency,
            #"Size": size,
            #"Color": color,
            "Season": season,
            #"Review Rating": review,
            "Shipping Type": shipping,
            "Discount Applied": discount,
            "Promo Code Used": promo,
            "Payment Method": payment
        }
        # Appel de la fonction de prédiction avec les données saisies
        prediction = predict(data)["predictions"]
        st.write("Prédiction obtenue :")
        for cle, valeur in prediction.items():
            st.write(cle + " : " + str(valeur) + " unité achetée")

# Appel de la fonction principale pour exécuter l'interface
if __name__ == "__main__":
    main()