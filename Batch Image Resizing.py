#This python file resizes all existing .jpg files in the same directory: 

import glob
import cv2

#glob finds certain files given certain path names
images = glob.glob("*.jpg")

for image in images:
    img = cv2.imread(image, 0) #this line also converts image to 0 (grey scale), 1 (color) or -1 (color with transparency) 

    resized_img = cv2.resize(img, (100, 100)) #command that resizes the image to 100 x 100 pixels

    cv2.imwrite("resized_"+image, resized_img) #command that writes the image in a new file

    cv2.waitKey(2000) #closes window at a certain time (in ms) specified by the user, 0-> closes widow when user presses any button
    cv2.destroyAllWindows() #method that closes all windows
