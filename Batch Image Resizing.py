#This python file resizes all existing .jpg files in the same directory.
#Save this Python file in the same folder as the photos and run it.

import glob
import cv2

#glob finds certain files given certain path names
images = glob.glob("*.jpg")

for image in images:
    img = cv2.imread(image, 1) #0 (grey scale), 1 (color) or -1 (color with transparency)

    resized_img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

    #command that resizes the image to a particular size (might skew image though!)
    #resized_img = cv2.resize(img, (1000,1000))

    cv2.imwrite("resized_"+image, resized_img) #command that writes the image in a new file

    cv2.waitKey(2000) #closes window at a certain time (in ms) specified by the user, Type 0 to close window when user presses any button
    cv2.destroyAllWindows() #method that closes all windows
