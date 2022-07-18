import cv2
from Face_Recog.detectors import FaceDetector
from cv2 import dnn_superres


def build_model():
	from mtcnn import MTCNN
	face_detector = MTCNN()
	return face_detector

def detect_face(face_detector, img, align = True):

	resp = []

	detected_face = None
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

			# sr = dnn_superres.DnnSuperResImpl_create()
			# sr.readModel(path = "MlSecurity/Face_Recog/basemodels/FSRCNN-small_x3.pb")
			# sr.setModel("edsr", 3)
			imgCrop = cv2.resize(detected_face,(600,600))
			# imgCro = sr.upsample(imgCrop)
			resp.append((imgCrop, img_region))

	return resp#,cv2.imwrite("img"+".jpg",imgCrop)
