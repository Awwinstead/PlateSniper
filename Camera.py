import cv2
import time




def get_image_path():

    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()

    if not ret:
        print("unable to capture image")
        return None

    millis = int(round(time.time() * 1000))

    img_name = "tmp/{}.png".format(millis)
    cv2.imwrite(img_name, frame)
    camera.release()
    return img_name


if __name__ == "__main__" :

    print(get_image_path())

