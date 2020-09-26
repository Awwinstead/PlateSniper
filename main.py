import os
import re
import cv2
from google.cloud import vision_v1p3beta1 as vision


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '.creds/PlateSniper-1c85303100a6.json'
SOURCE_PATH = 'tmp/'
states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "District of Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
states = [state.upper() for state in states]

def recognise_license_plate(img):

    height, width = img.shape[:2]
    img_scale = cv2.resize(img, (800, int((height*800)/width)))

    client = vision.ImageAnnotatorClient()

    err, arr = cv2.imencode(".png", img_scale)
    content = arr.tobytes()

    image = vision.types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    texts = [text.description for text in texts]
    licenses = []

    for text in texts[0].split('\n'):
        text = text.strip().replace(" ", "")
        result = re.search(r"^[A-Z0-9]{6,7}$", text)
        if result:
            # print(f"match: {result.group()}")
            licenses.append(result.group())
        else:
            # print(f"no match: {text}")
            pass

    return licenses


path = SOURCE_PATH + 'florida.jpg'
img = cv2.imread(path)

[print(plate) for plate in recognise_license_plate(img)]
