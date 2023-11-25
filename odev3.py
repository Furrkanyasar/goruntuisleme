import cv2
import numpy as np

def main():
    # Görüntüyü yükleme
    img = cv2.imread("D:/pirinc.jpg")

    # Gri tonlamaya dönüştürme
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Eşikleme işlemi
    _, threshold_img = cv2.threshold(gray_img, 220, 255, cv2.THRESH_BINARY)

    # Morfolojik işlemler
    kernel = np.ones((3, 3), np.uint8)
    threshold_img = cv2.morphologyEx(threshold_img, cv2.MORPH_OPEN, kernel)

    # Pirinç tanelerini sayma
    contours, _ = cv2.findContours(threshold_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    rice_count = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 100:
            rice_count += 1

    # Sonuçları kaydetme
    output_image_path = "D:/output_image.jpg"
    cv2.imwrite(output_image_path, img)

    threshold_image_path = "D:/threshold_image.jpg"
    cv2.imwrite(threshold_image_path, threshold_img)

    print(f"Pirinç sayısı: {rice_count}")

if __name__ == "__main__":
    main()
