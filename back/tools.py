from keras.models import load_model
import numpy as np
import os
import cv2
import imutils
from imutils import contours

def predict(file_path):
    model = load_model("models/modelbest_V1.h5")
    img = cv2.imread(file_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(img, (5, 5), 0)
    blurred = blurred.astype(np.uint8)
    edged = cv2.Canny(blurred, 30, 150)
    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    min_contour_area = 100
    cnts = [c for c in cnts if cv2.contourArea(c) > min_contour_area]
    cnts = contours.sort_contours(cnts, method="left-to-right")[0]
    image_with_rectangles = img.copy()
    class_labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'add', 'div', 'sub', 'times',]
    predictions = []

    for i, c in enumerate(cnts):
    # Récupérer les coordonnées du rectangle englobant du contour
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(image_with_rectangles, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image_with_rectangles, str(i+1), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        roi = img[y:y + h, x:x + w]
        cv2.imwrite(f'uploads/roi_{i}.jpg', roi)

    for i in range(len(cnts)):
        roi = cv2.imread(f'uploads/roi_{i}.jpg')
        roi_resized = cv2.resize(roi, (28, 28))
        roi_gray = cv2.cvtColor(roi_resized, cv2.COLOR_BGR2GRAY)
        roi_normalized = roi_gray / 255.0
        roi_input = roi_normalized.reshape(28, 28, 1)
        prediction = model.predict(np.expand_dims(roi_input, axis=0))
        pred = np.argmax(prediction, axis=1)
        predictions.append(pred[0])
    
    # match the predictions with the class labels
    operation = []

    for i in range(len(predictions)):
        for j in range(len(class_labels)):
            if predictions[i] == j:
                operation.append(class_labels[j])

    # check if the first element is a number
    if operation[0] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        result = "Error"
    else: 
        print(operation)
        for i in range(len(operation)):
            if operation[i] == 'add':
                operation[i] = '+'
            elif operation[i] == 'sub':
                operation[i] = '-'
            elif operation[i] == 'times':
                operation[i] = '*'
            elif operation[i] == 'div':
                operation[i] = '/'
        result = eval(''.join(operation))
    
    # delete the roi images
    for i in range(len(cnts)):
        os.remove(f'uploads/roi_{i}.jpg')

   
    return {"operation predicted": ''.join(operation), "result": result}
