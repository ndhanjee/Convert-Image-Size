import glob
import cv2

#glob finds certain files given certain path names
images = glob.glob("*.jpg")

for image in images:
    img = cv2.imread(image, 0)

    resized_img = cv2.resize(img, (100,100))

    cv2.imwrite("resized_"+image, resized_img)

    cv2.waitKey(2000)
    cv2.destroyAllWindows()
