import cv2
import face_recognition

class VideoCamera(object):
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
        success, image = self.video.read()
        small_image = cv2.resize(image, (0, 0), fx=0.25, fy=0.25)
        small_image = small_image[:, :, ::-1]

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