from keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import json

def predict(file_path):
    model = load_model("models/dog_breed_classifier2.h5")
    test_image_path = file_path
    test_image = image.load_img(test_image_path, target_size=(299, 299))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    test_image = test_image / 255.0  # Normalize the pixel values

    predictions = model.predict(test_image)

    # Get the top 3 predicted class indices and probabilities
    top_classes_indices = np.argsort(predictions[0])[::-1][:3]
    top_classes_probabilities = predictions[0][top_classes_indices]

    # Get the class labels
    class_labels = {'n02085620-Chihuahua': 0, 'n02085782-Japanese_spaniel': 1, 'n02085936-Maltese_dog': 2, 'n02086079-Pekinese': 3, 'n02086240-Shih-Tzu': 4, 'n02086646-Blenheim_spaniel': 5, 'n02086910-papillon': 6, 'n02087046-toy_terrier': 7, 'n02087394-Rhodesian_ridgeback': 8, 'n02088094-Afghan_hound': 9, 'n02088238-basset': 10, 'n02088364-beagle': 11, 'n02088466-bloodhound': 12, 'n02088632-bluetick': 13, 'n02089078-black-and-tan_coonhound': 14, 'n02089867-Walker_hound': 15, 'n02089973-English_foxhound': 16, 'n02090379-redbone': 17, 'n02090622-borzoi': 18, 'n02090721-Irish_wolfhound': 19, 'n02091032-Italian_greyhound': 20, 'n02091134-whippet': 21, 'n02091244-Ibizan_hound': 22, 'n02091467-Norwegian_elkhound': 23, 'n02091635-otterhound': 24, 'n02091831-Saluki': 25, 'n02092002-Scottish_deerhound': 26, 'n02092339-Weimaraner': 27, 'n02093256-Staffordshire_bullterrier': 28, 'n02093428-American_Staffordshire_terrier': 29, 'n02093647-Bedlington_terrier': 30, 'n02093754-Border_terrier': 31, 'n02093859-Kerry_blue_terrier': 32, 'n02093991-Irish_terrier': 33, 'n02094114-Norfolk_terrier': 34, 'n02094258-Norwich_terrier': 35, 'n02094433-Yorkshire_terrier': 36, 'n02095314-wire-haired_fox_terrier': 37, 'n02095570-Lakeland_terrier': 38, 'n02095889-Sealyham_terrier': 39, 'n02096051-Airedale': 40, 'n02096177-cairn': 41, 'n02096294-Australian_terrier': 42, 'n02096437-Dandie_Dinmont': 43, 'n02096585-Boston_bull': 44, 'n02097047-miniature_schnauzer': 45, 'n02097130-giant_schnauzer': 46, 'n02097209-standard_schnauzer': 47, 'n02097298-Scotch_terrier': 48, 'n02097474-Tibetan_terrier': 49, 'n02097658-silky_terrier': 50, 'n02098105-soft-coated_wheaten_terrier': 51, 'n02098286-West_Highland_white_terrier': 52, 'n02098413-Lhasa': 53, 'n02099267-flat-coated_retriever': 54, 'n02099429-curly-coated_retriever': 55, 'n02099601-golden_retriever': 56, 'n02099712-Labrador_retriever': 57, 'n02099849-Chesapeake_Bay_retriever': 58, 'n02100236-German_short-haired_pointer': 59, 'n02100583-vizsla': 60, 'n02100735-English_setter': 61, 'n02100877-Irish_setter': 62, 'n02101006-Gordon_setter': 63, 'n02101388-Brittany_spaniel': 64, 'n02101556-clumber': 65, 'n02102040-English_springer': 66, 'n02102177-Welsh_springer_spaniel': 67, 'n02102318-cocker_spaniel': 68, 'n02102480-Sussex_spaniel': 69, 'n02102973-Irish_water_spaniel': 70, 'n02104029-kuvasz': 71, 'n02104365-schipperke': 72, 'n02105056-groenendael': 73, 'n02105162-malinois': 74, 'n02105251-briard': 75, 'n02105412-kelpie': 76, 'n02105505-komondor': 77, 'n02105641-Old_English_sheepdog': 78, 'n02105855-Shetland_sheepdog': 79, 'n02106030-collie': 80, 'n02106166-Border_collie': 81, 'n02106382-Bouvier_des_Flandres': 82, 'n02106550-Rottweiler': 83, 'n02106662-German_shepherd': 84, 'n02107142-Doberman': 85, 'n02107312-miniature_pinscher': 86, 'n02107574-Greater_Swiss_Mountain_dog': 87, 'n02107683-Bernese_mountain_dog': 88, 'n02107908-Appenzeller': 89, 'n02108000-EntleBucher': 90, 'n02108089-boxer': 91, 'n02108422-bull_mastiff': 92, 'n02108551-Tibetan_mastiff': 93, 'n02108915-French_bulldog': 94, 'n02109047-Great_Dane': 95, 'n02109525-Saint_Bernard': 96, 'n02109961-Eskimo_dog': 97, 'n02110063-malamute': 98, 'n02110185-Siberian_husky': 99, 'n02110627-affenpinscher': 100, 'n02110806-basenji': 101, 'n02110958-pug': 102, 'n02111129-Leonberg': 103, 'n02111277-Newfoundland': 104, 'n02111500-Great_Pyrenees': 105, 'n02111889-Samoyed': 106, 'n02112018-Pomeranian': 107, 'n02112137-chow': 108, 'n02112350-keeshond': 109, 'n02112706-Brabancon_griffon': 110, 'n02113023-Pembroke': 111, 'n02113186-Cardigan': 112, 'n02113624-toy_poodle': 113, 'n02113712-miniature_poodle': 114, 'n02113799-standard_poodle': 115, 'n02113978-Mexican_hairless': 116, 'n02115641-dingo': 117, 'n02115913-dhole': 118, 'n02116738-African_hunting_dog': 119}
   
    predictions_json = []
    for i in range(len(top_classes_indices)):
        class_index = top_classes_indices[i]
        class_label = [label for label, index in class_labels.items() if index == class_index][0]
        probability = top_classes_probabilities[i]
        prediction = {
            "class_label": class_label,
            "probability": probability.item() * 100
        }
        predictions_json.append(prediction)

    # Convert the list to a JSON string
    result_json = json.dumps(predictions_json)

    # Print the JSON result
    return result_json
