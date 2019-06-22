import os
import cv2
import face_recognition

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
        image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'img', 'face.png')
        cv2.imwrite(image_path, image)
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
        # Predict
        
        for ((top, right, bottom, left), name) in zip(boxes, names):
		    # draw the predicted face name on the image
            cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
            y = top - 15 if top - 15 > 15 else top + 15
            cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
        # Encode the new image
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()