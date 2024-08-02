import cv2
import glob

# read the haarcascade to detect cat faces
cat_cascade = cv2.CascadeClassifier('classifier/haarcascade_frontalcatface.xml')  # noqa

for file_path in glob.glob("images/*.jpg"):
    # read the input image
    img = cv2.imread(file_path)

    # convert the input image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detects cat faces in the input image
    faces = cat_cascade.detectMultiScale(gray, 1.1, 3)
    print(f'{file_path} - Number of detected cat faces: {len(faces)}')

    # if atleast one cat face id detected
    if len(faces) > 0:
        print("Cat face detected")
        for (x, y, w, h) in faces:
            # To draw a rectangle in a face
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 2)
            cv2.putText(img, 'cat face', (x, y-3),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    else:
        print("No cat face detected")

    # Display an image in a window
    cv2.imshow('Cat Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
