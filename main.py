import cv2
import traceback
import os
import sys
import numpy as np
from mail import sendEmail # extra: send an image to my email
classificador = cv2.CascadeClassifier("models/haarcascade-frontalface-default.xml")
camera = cv2.VideoCapture(0) #indica para utilizar o 1o device neste caso a webcam
counter = 0

while (True):
    try:
        conectado, imagem = camera.read()
        #print(conectado)
        imagem=cv2.flip(imagem,0)
        imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) # face cinza obrigatorio pelo modelo de deteccao
        facesDetectadas = classificador.detectMultiScale(imagemCinza,scaleFactor=1.5,minSize=(50,50)) # chamar classificador q detecta ja as faces
        for (x, y, largura, altura) in facesDetectadas:
            cv2.rectangle(imagem, (x,y), (x + largura, y + altura), (0, 0, 255), 2) # colocar rectangulo a volta da face
            cv2.imwrite('tempCapturedImgEmail.jpg', imagem)
            #counter = counter + 1
            #print(counter)
            sendEmail(imagem)
            os.remove('tempCapturedImgEmail.jpg')

        cv2.imshow("Camera View", imagem)
        cv2.waitKey(1)
    except:
        traceback.print_exc()
        sys.exit()

camera.release()
cv2.destroyAllWindows()
