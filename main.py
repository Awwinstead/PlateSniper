import os
import cv2
from google.cloud import vision_v1p3beta1 as vision


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '.creds/PlateSniper-1c85303100a6.json'
SOURCE_PATH = 'tmp/'


def recognise_license_plate(img):

    height, width = img.shape[:2]
    img_scale = cv2.resize(img, (800, int((height*800)/width)))

    client = vision.ImageAnnotatorClient()

    err, arr = cv2.imencode(".png", img_scale)
    content = arr.tobytes()

    image = vision.types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    return [text.description for text in texts]


path = SOURCE_PATH + 'florida.jpg'
img = cv2.imread(path)

[print(plate) for plate in recognise_license_plate(img)]
