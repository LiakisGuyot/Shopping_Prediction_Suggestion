from fastapi import FastAPI
import csv
import os
from sklearn.preprocessing import LabelEncoder
from fctUtils import predict, load, dataFromJson


MODEL_FILENAME = "../pickles/predictionModelTest.pkl"
MODEL_FILENAME2 = "../pickles/knn_recommandation.pkl"
SAVE_FILENAME = "predictions.csv"

ENCODER_FILENAME = "../pickles/label_encoders_info_test.pkl"

app = FastAPI()
pipeline = load(MODEL_FILENAME)
encoder = load(ENCODER_FILENAME)

pipelineknn = load(MODEL_FILENAME2)

modelResult = ["Shorts","Shirt","Socks","Coat","Dress","Boots","Handbag","Sunglasses","Hat","Belt","Backpack","Scarf","Jacket","Jeans","Gloves","Sneakers","Sweater","Pants","T-shirt","Jewelry","Skirt", "Blouse", "Sandals", "Hoodie","Shoes"]
cols_cat_info = [1,2,3,4,5,6,7,8,9]
    
if os.path.exists(SAVE_FILENAME):
    # Si le fichier existe, on le lit et on stocke les données dans une liste
    with open(SAVE_FILENAME, mode='r', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        donnees = list(reader)
else:
    # Si le fichier n'existe pas, on initialise une liste vide
    donnees = [["Age", "Genre", "Location", "Subscription Status", "Frequency of Purchases", 
               "Season", "Shipping Type", "Discount Applied", "Promo Code Used", "Payment Method",
               "Shorts","Shirt","Socks","Coat","Dress","Boots","Handbag","Sunglasses","Hat","Belt",
               "Backpack","Scarf","Jacket","Jeans","Gloves","Sneakers","Sweater","Pants","T-shirt",
               "Jewelry","Skirt", "Blouse", "Sandals", "Hoodie","Shoes"]]

@app.post("/predict")
async def predictApi(data: dict):
    """
    Predict model output with contact datas. (POST)
    :param data: data to predict (JSON)
    :return: predictions (JSON)
    """
    df = dataFromJson(data)
    nouvelle_ligne = df.iloc[0].tolist()
    x = df.iloc[0].tolist()
    
    for i, val in enumerate(cols_cat_info):
        x[val] = encoder[i].transform([x[val]])[0]
    
    y_pred = predict(pipeline, [x])
    
    # Ajouter une nouvelle ligne à la liste de données
    for i in y_pred[0]:
        nouvelle_ligne.append(i)
    donnees.append(nouvelle_ligne)
    
    # Triez la liste en fonction de ses éléments et récupérez les indices correspondants
    indices_tries = sorted(range(len(y_pred[0])), key=lambda i: y_pred[0][i], reverse=True)

    # Récupérez les 5 premiers indices
    top5_indices = indices_tries[:5]

    # Sauvegarder les données dans le fichier CSV
    with open(SAVE_FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(donnees)
        
    prediction = {}
    for i in top5_indices:
        prediction[modelResult[i]] = y_pred[0][i]
    
    
    return {"predictions": prediction}


@app.post("/predictknn")
async def predictReviewApi(data: dict):
    
    x = data["data"]
    x[0] = int(x[0])

    for i, val in enumerate(cols_cat_info):
        x[val] = encoder[i].transform([x[val]])[0]
    
    predict = pipelineknn.predict([x])
    prediction = {}
    for i, val in enumerate(predict[0]):
        prediction[modelResult[i]] = val
    
    return {"predictions": prediction}