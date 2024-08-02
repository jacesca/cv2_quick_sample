# Importing the required libraries.
import cv2
import glob

# The haarcascade_frontalcatface.xml and dog.xml files are cascade classifiers
# that are used by the OpenCV library to detect objects in images. These can be
# found in the following locations:
# https://github.com/opencv/opencv/blob/master/data/haarcascades
# https://github.com/metinozkan/DogAndCat-Face-Opencv/tree/master/Cat_dog_face

# Load the cascade classifiers for cats and dogs
cat_cascade = cv2.CascadeClassifier('classifier/haarcascade_frontalcatface.xml')  # noqa
# dog_cascade = cv2.CascadeClassifier('classifier/dog_face.xml')

for file_path in glob.glob("images/*.jpg"):
    # Read the image
    img = cv2.imread(file_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect cats and dogs in the image
    cats = cat_cascade.detectMultiScale(gray, 1.1, 3)
    # dogs = dog_cascade.detectMultiScale(gray, 1.1, 3)

    # Print the number of cats and dogs detected
    print(f"{file_path} - Cats detected: {len(cats)}")
    # print(f"{file_path} - Dogs detected: {len(dogs)}")
