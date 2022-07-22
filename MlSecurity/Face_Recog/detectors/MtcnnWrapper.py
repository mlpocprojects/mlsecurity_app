import cv2
from Face_Recog.detectors import FaceDetector
from skimage.transform import resize
from PIL import Image as im
import numpy as np


def build_model():
	from mtcnn import MTCNN
	face_detector = MTCNN()
	return face_detector

def detect_face(face_detector, img, align = True):

	resp = []

	detected_face = None
	# img = cv2.resize(img,(1920,1080))
	img_region = [0, 0, img.shape[0], img.shape[1]]

	img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #mtcnn expects RGB but OpenCV read BGR
	detections = face_detector.detect_faces(img_rgb)

	if len(detections) > 0:

		for detection in detections:
			x, y, w, h = detection["box"]
			detected_face = img[int(y):int(y+h), int(x):int(x+w)]
			img_region = [x, y, w, h]

			if align:
				keypoints = detection["keypoints"]
				left_eye = keypoints["left_eye"]
				right_eye = keypoints["right_eye"]
				detected_face = FaceDetector.alignment_procedure(detected_face, left_eye, right_eye)

			detected_face = cv2.resize(detected_face, (480,480))
			resp.append((detected_face,img_region))	

	return resp#,cv2.imwrite("img"+".jpg",detected_face)


	'''
# import cv2
# from Face_Recog.detectors import FaceDetector
# import numpy as np


# def build_model():
# 	from mtcnn import MTCNN
# 	face_detector = MTCNN()
# 	return face_detector

# def detect_face(face_detector, img, align = True):

# 	resp = []

# 	detected_face = None
# 	img_region = [0, 0, img.shape[0], img.shape[1]]

# 	img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #mtcnn expects RGB but OpenCV read BGR
# 	detections = face_detector.detect_faces(img_rgb)

# 	if len(detections) > 0:

# 		for detection in detections:
# 			detected_face = img
# 			if align:
# 				keypoints = detection["keypoints"]
# 				left_eye = keypoints["left_eye"]
# 				right_eye = keypoints["right_eye"]
# 				detected_face = FaceDetector.alignment_procedure(detected_face, left_eye, right_eye)
# 				detections_1 = face_detector.detect_faces(img_rgb)
# 				for detection in detections_1:
# 					x, y, w, h = detection["box"]
# 					detected_face_1 = detected_face[int(y):int(y+h), int(x):int(x+w)]
# 					img_region = [x, y, w, h]

# 		norm_img = np.zeros((300, 300))
# 		norm_img = cv2.normalize(detected_face_1, norm_img, 0, 255, cv2.NORM_MINMAX)
# 		norm_img = cv2.resize(norm_img, (800,800))
# 		resp.append((norm_img,img_region))

# 	return resp#,cv2.imwrite("img"+".jpg",norm_img)
	'''
