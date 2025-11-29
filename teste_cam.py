import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
ret, frame = cap.read()
if ret:
    cv2.imwrite("teste.jpg", frame)
    print("✅ Imagem capturada como teste.jpg")
else:
    print("❌ Erro ao capturar imagem.")
cap.release()