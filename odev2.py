import cv2
import numpy as np
# Kamerayı açma
cap = cv2.VideoCapture(0)

while True:
    # Kameradan çerçeve okuma
    ret, frame = cap.read()

    # Çerçeve yoksa döngüden çıkma
    if not ret:
        break

    # Çerçeve boyutlarını alma
    height, width, _ = frame.shape

    # Çerçeve rengini HSV'ye dönüştürme
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Kırmızı renk aralığını tanımlama
    lower_red = np.array([0, 120, 120])
    upper_red = np.array([10, 255, 255])

    # HSV görüntüsünde kırmızı renk aralığını maskeleme
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Orijinal görüntü üzerine maskeyi uygulama
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Görüntüleri ekrana gösterme
    cv2.imshow('Original', frame)
    cv2.imshow('Result', result)

    # 'q' tuşuna basıldığında döngüden çıkma
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera kapatma
cap.release()
cv2.destroyAllWindows()
