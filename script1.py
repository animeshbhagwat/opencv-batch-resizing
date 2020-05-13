import cv2
from pathlib import Path

for path in Path('src').rglob('*.jpg'):
    img = cv2.imread(f"src/{path.name}", 1)
    resized_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
    cv2.imwrite(f"resized/{path.name}_resized.jpg", resized_image)