import cv2
import face_recognition

img = cv2.imread("WIN_20230927_14_33_26_Pro.jpg")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding = face_recognition.face_encodings(rgb_img)[0]

img2 = cv2.imread("images/Messi.webp")
rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

result = face_recognition.compare_faces([img_encoding], img_encoding2)
print("Result: ", result)

sfr = SimpleFacerec()
sfr.load_encoding_images("images/")


import cv2

video_cap = cv2.VideoCapture(0)
while True :
    ret , video_data = video_cap.read()
    cv2.imshow("video_live", video_data)
    if cv2.waitKey(10) == ord("a") :
        break
    
video_cap.release()    
    