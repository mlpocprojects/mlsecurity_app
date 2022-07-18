from Face_Recog.detectors import FaceDetector
import cv2

# # Link - https://google.github.io/mediapipe/solutions/face_detection

# def build_model():
#     import mediapipe as mp
#     mp_face_detection = mp.solutions.face_detection
#     # min_detection_confidence - "A filter to analyse the training photographs"
#     face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.4)
#     # Returns detected face
#     return face_detection


# def detect_face(face_detector, img, align=True):
#     import mediapipe as mp
#     import re
#     # Regular expressions
#     # mp_face_detection = mp.solutions.face_detection
#     resp = []
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     results = face_detector.process(img)
#     original_size = img.shape
#     target_size = (300, 300)
#     # First face , than eye
#     if results.detections:
#         for detection in results.detections:
#             # mp_drawing.draw_detection(img, detection)
#             # detected_face is the cropped image that is then passed forward to the Regognizer
#             '''
#             DETECTION - 
#             Collection of detected faces, where each face is represented as a detection proto message that contains 
#             a bounding box and 6 key points (right eye, left eye, nose tip, mouth center, right ear tragion, and left
#             ear tragion). The bounding box is composed of xmin and width (both normalized to [0.0, 1.0] by the
#             image width) and ymin and height (both normalized to [0.0, 1.0] by the image height). Each key point
#             is composed of x and y, which are normalized to [0.0, 1.0] by the image width and height
#             respectively.
#             '''
#             # Bounding Box
#             x = re.findall('xmin: (..*)', str(detection))
#             y = re.findall('ymin: (..*)', str(detection))
#             h = re.findall('height: (..*)', str(detection))
#             w = re.findall('width: (..*)', str(detection))
#             # Eye Locations
#             reye_x = re.findall('x: (..*)', str(detection))[0]
#             leye_x = re.findall('x: (..*)', str(detection))[1]
#             reye_y = re.findall('y: (..*)', str(detection))[0]
#             leye_y = re.findall('y: (..*)', str(detection))[1]
#             # Detections are normalized by the mediapipe API, thus they need to be multiplied
#             # Extra tweaking done to improve accuracy
#             x = (float(x[0]) * original_size[1])-10
#             y = (float(y[0]) * original_size[0])-40
#             h = (float(h[0]) * original_size[0])+30
#             w = (float(w[0]) * original_size[1])+20
#             reye_x = (float(reye_x) * original_size[1])
#             leye_x = (float(leye_x) * original_size[1])
#             reye_y = (float(reye_y) * original_size[0])
#             leye_y = (float(leye_y) * original_size[0])
#             if float(x) and float(y) > 0:
#                 detected_face = img[int(y):int(y + h), int(x):int(x + w)]
#                 img_region = [int(x), int(y), int(w), int(h)]
#                 if align:
#                     left_eye = (leye_x, leye_y)
#                     right_eye = (reye_x, reye_y)
#                     detected_face = FaceDetector.alignment_procedure(detected_face, left_eye, right_eye)
#                     imgCrop = cv2.resize(detected_face, (240,240))
#                 resp.append((imgCrop, img_region))
#             else:
#                 continue

#     # resp is a tuple containing the detected face and the area in the image the face exists
#     return resp,cv2.imwrite("img"+".jpg",imgCrop)

# from deepface.detectors import FaceDetector

# Link - https://google.github.io/mediapipe/solutions/face_detection

def build_model():
    import mediapipe as mp #this is not a must dependency. do not import it in the global level.
    mp_face_detection = mp.solutions.face_detection
    face_detection =  mp_face_detection.FaceDetection( min_detection_confidence=0.7)
    return face_detection

def detect_face(face_detector, img, align = True):
    import mediapipe as mp #this is not a must dependency. do not import it in the global level.
    resp = []
    
    img_width = img.shape[1]; img_height = img.shape[0]
    
    results = face_detector.process(img)
    
    if results.detections:
        for detection in results.detections:
            
            confidence = detection.score
            
            bounding_box = detection.location_data.relative_bounding_box
            landmarks = detection.location_data.relative_keypoints
            
            x = int(bounding_box.xmin * img_width)
            w = int(bounding_box.width * img_width)
            y = int(bounding_box.ymin * img_height)
            h = int(bounding_box.height * img_height)
            
            right_eye = (int(landmarks[0].x * img_width), int(landmarks[0].y * img_height))
            left_eye = (int(landmarks[1].x * img_width), int(landmarks[1].y * img_height))
            # nose = (int(landmarks[2].x * img_width), int(landmarks[2].y * img_height))
            # mouth = (int(landmarks[3].x * img_width), int(landmarks[3].y * img_height))
            # right_ear = (int(landmarks[4].x * img_width), int(landmarks[4].y * img_height))
            # left_ear = (int(landmarks[5].x * img_width), int(landmarks[5].y * img_height))
            
            if x > 0 and y > 0:
                detected_face = img[y:y+h, x:x+w]
                img_region = [x, y, w, h]
                
                if align:
                    detected_face = FaceDetector.alignment_procedure(detected_face, left_eye, right_eye)
                    imgCrop = cv2.resize(detected_face, (240,240))

                resp.append((imgCrop,img_region))
                
    return resp,cv2.imwrite("img"+".jpg",imgCrop)

