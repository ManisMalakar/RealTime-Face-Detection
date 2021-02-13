import cv2 

#Loading pretrained data on face frontals from opencv
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Choosing an image to detect faces in
webcam=cv2.VideoCapture(0)

#Run through the frame
while True:
    #From frame
    frame_read,frame=webcam.read()

    #Converting the image to greyscale
    grayscaled_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #Detect Faces
    face_coordinates=trained_face_data.detectMultiScale(grayscaled_img)
    
    #Draw rectanges around the faces
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y), (x+w,y+h),(0,255,0),2)

    cv2.imshow('Real Time Face Check',frame)
    key=cv2.waitKey(1)

    #Stoo if Q key is pressed
    if key==81 or key==113:
        break


print("Code Completed.")