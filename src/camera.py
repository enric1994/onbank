import os
import cv2
import face_recognition
from find import predict_user
import json

# ENCODINGS
ENCODINGS_NAME = 'enric_david_pierre.pickle'
data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'data')
encodings_path = os.path.join(data_path, 'encodings', ENCODINGS_NAME)

# CUSTOMERS
customers_path = os.path.join(data_path, 'customers.json')
with open(customers_path) as f:
    customers = json.load(f)

# COLORS
white = (255, 255, 255)
blue = (20, 20, 20)
black = (0, 0, 0)

class VideoCameraPhoto(object):
    
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        # Read video stream
        success, image = self.video.read()
        # Save image
        # image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'img', 'face.png')
        # cv2.imwrite(image_path, image)
        # Resize
        small_image = cv2.resize(image, (0, 0), fx=0.25, fy=0.25)
        small_image = small_image[:, :, ::-1]
        # Face landmarks
        face_landmarks_list = face_recognition.face_landmarks(small_image)
        for face_landmarks in face_landmarks_list:
            color = (0,255,0)
            radius = 5
            thickness = 2
            resize = 4

            cv2.circle(image, (face_landmarks['left_eyebrow'][0][0]*resize, face_landmarks['left_eyebrow'][0][1]*resize), radius, color,thickness)
            cv2.circle(image, (face_landmarks['left_eyebrow'][1][0]*resize, face_landmarks['left_eyebrow'][1][1]*resize), radius, color,thickness)
            cv2.circle(image, (face_landmarks['left_eyebrow'][2][0]*resize, face_landmarks['left_eyebrow'][2][1]*resize), radius, color,thickness)
            cv2.circle(image, (face_landmarks['left_eyebrow'][3][0]*resize, face_landmarks['left_eyebrow'][3][1]*resize), radius, color,thickness)
            cv2.circle(image, (face_landmarks['left_eyebrow'][4][0]*resize, face_landmarks['left_eyebrow'][4][1]*resize), radius, color,thickness)

            cv2.circle(image, (face_landmarks['right_eyebrow'][0][0]*resize, face_landmarks['right_eyebrow'][0][1]*resize), radius, color,thickness)
            cv2.circle(image, (face_landmarks['right_eyebrow'][1][0]*resize, face_landmarks['right_eyebrow'][1][1]*resize), radius, color,thickness)
            cv2.circle(image, (face_landmarks['right_eyebrow'][2][0]*resize, face_landmarks['right_eyebrow'][2][1]*resize), radius, color,thickness)
            cv2.circle(image, (face_landmarks['right_eyebrow'][3][0]*resize, face_landmarks['right_eyebrow'][3][1]*resize), radius, color,thickness)
            cv2.circle(image, (face_landmarks['right_eyebrow'][4][0]*resize, face_landmarks['right_eyebrow'][4][1]*resize), radius, color,thickness)

            cv2.circle(image, (face_landmarks['nose_tip'][0][0]*resize, face_landmarks['nose_tip'][0][1]*resize), radius, color,thickness)
            cv2.circle(image, (face_landmarks['nose_tip'][1][0]*resize, face_landmarks['nose_tip'][1][1]*resize), radius, color,thickness)
            cv2.circle(image, (face_landmarks['nose_tip'][2][0]*resize, face_landmarks['nose_tip'][2][1]*resize), radius, color,thickness)
            cv2.circle(image, (face_landmarks['nose_tip'][3][0]*resize, face_landmarks['nose_tip'][3][1]*resize), radius, color,thickness)
            cv2.circle(image, (face_landmarks['nose_tip'][4][0]*resize, face_landmarks['nose_tip'][4][1]*resize), radius, color,thickness)

            cv2.circle(image, (face_landmarks['top_lip'][0][0]*resize, face_landmarks['top_lip'][0][1]*resize), radius, color,thickness)
            cv2.circle(image, (face_landmarks['top_lip'][1][0]*resize, face_landmarks['top_lip'][1][1]*resize), radius, color,thickness)
            cv2.circle(image, (face_landmarks['top_lip'][5][0]*resize, face_landmarks['top_lip'][5][1]*resize), radius, color,thickness)
            cv2.circle(image, (face_landmarks['top_lip'][6][0]*resize, face_landmarks['top_lip'][6][1]*resize), radius, color,thickness)


            cv2.circle(image, (face_landmarks['bottom_lip'][0][0]*resize, face_landmarks['bottom_lip'][0][1]*resize), radius, color,thickness)
            cv2.circle(image, (face_landmarks['bottom_lip'][1][0]*resize, face_landmarks['bottom_lip'][1][1]*resize), radius, color,thickness)
            cv2.circle(image, (face_landmarks['bottom_lip'][5][0]*resize, face_landmarks['bottom_lip'][5][1]*resize), radius, color,thickness)
            cv2.circle(image, (face_landmarks['bottom_lip'][6][0]*resize, face_landmarks['bottom_lip'][6][1]*resize), radius, color,thickness)

        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


class VideoCameraRecognition(object):
    
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        # Read video stream
        success, image = self.video.read()
        # Resize
        small_image = cv2.resize(image, (0, 0), fx=0.25, fy=0.25)
        small_image = small_image[:, :, ::-1]
        # Predict
        user_ids, boxes = predict_user(small_image, encodings_path)
        # Only one user at a time
        if len(user_ids) == 1:
            # Name
            user_id = user_ids[0]
            if user_id in customers:
                customer = customers[user_id]
                for ((top, right, bottom, left), name) in zip(boxes, user_ids):
                    # Resize back
                    left *= 4
                    top *= 4
                    right *= 4
                    bottom *= 4
                    # draw the predicted face name on the image
                    # cv2.rectangle(image, (left, top), (right, bottom,), (210, 100, 50), 2)
                    centerX = left + (right-left)/2
                    centerY = top + (bottom-top)/2
                    sizeX = (right - left)*0.5
                    sizeY = (bottom-top) *0.7
                    cv2.ellipse(image,(int(centerX), int(centerY)),(int(sizeX),int(sizeY)),0,0,360,255,2)
                    # Normalized Y
                    y = top - 15 if top - 15 > 15 else top + 15
                    # Name
                    cv2.putText(image, customer['name'], (left + 50, y - 50), cv2.FONT_HERSHEY_TRIPLEX, 1, black, 4)
                    cv2.putText(image, customer['name'], (left + 50, y - 50), cv2.FONT_HERSHEY_TRIPLEX, 1, white, 2)
                    # account balance, credit card balance
                    balances = 'Balance: {} GBP'.format(customer['account balance'])
                    cv2.putText(image, balances, (left + 50, bottom + 80), cv2.FONT_HERSHEY_TRIPLEX, 0.75, black, 4)
                    cv2.putText(image, balances, (left + 50, bottom + 80), cv2.FONT_HERSHEY_TRIPLEX, 0.75, white, 2)
                    # direct debits
                    position = y + 50
                    cv2.putText(image, 'Direct Debits:', (right + 30, position), cv2.FONT_HERSHEY_TRIPLEX, 0.75, black, 4)
                    cv2.putText(image, 'Direct Debits:', (right + 30, position), cv2.FONT_HERSHEY_TRIPLEX, 0.75, white, 2)
                    position += 40
                    orders = [ '{}: {} GBP'.format(k, v) for k, v in customer['standing orders'].items() ]
                    for order in orders:
                        cv2.putText(image, order, (right + 30, position), cv2.FONT_HERSHEY_TRIPLEX, 0.75, black, 4)
                        cv2.putText(image, order, (right + 30, position), cv2.FONT_HERSHEY_TRIPLEX, 0.75, white, 2)
                        position += 40
                    # Credit Score
                    position = y + 100
                    cv2.putText(image, 'Credit Score:', (left - 175, position), cv2.FONT_HERSHEY_TRIPLEX, 0.75, black, 4)
                    cv2.putText(image, 'Credit Score:', (left - 175, position), cv2.FONT_HERSHEY_TRIPLEX, 0.75, white, 2)
                    position += 40
                    cv2.putText(image, str(customer['credit score']), (left - 100, position), cv2.FONT_HERSHEY_TRIPLEX, 0.75, black, 4)
                    cv2.putText(image, str(customer['credit score']), (left - 100, position), cv2.FONT_HERSHEY_TRIPLEX, 0.75, white, 2)
        elif len(user_ids) > 1:
            cv2.putText(image, 'Watch out! You might have company', (10, 30), cv2.FONT_HERSHEY_TRIPLEX, 0.75, black, 4)
            cv2.putText(image, 'Watch out! You might have company', (10, 30), cv2.FONT_HERSHEY_TRIPLEX, 0.75, white, 2)
        # Encode the new image
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()