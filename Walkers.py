import cv2

# Crie nosso classificador de corpos
face_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# Inicie a captura de vídeo para o arquivo de vídeo
cap = cv2.VideoCapture('walking.avi')

# Faça o loop assim que o vídeo for carregado com sucesso
while True:
    
    # Leia o primeiro quadro
    ret, frame = cap.read()

    # Converta cada quadro em escala de cinza
    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    
    # Passe o quadro para nosso classificador de corpos
    for (x,y,w,h) in faces:
       cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    
    # Extraia as caixas delimitadoras para quaisquer corpos identificados
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) == 32: #32 é a barra de espaço
        break

cap.release()
cv2.destroyAllWindows()
