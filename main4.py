"""
Creating OCR with QR scanner and bar code scanner project, using libraries EasyOCR and pyTorch

# install all Dependencies
>>> pip install torch torchvision torchaudio
>>> pip install easyocr
>>> pip install Pillow
>>> pip install opencv-python numpy pyzbar

"""

#************************************** Importing dependencies

import easyocr
import cv2
from matplotlib import pyplot as plt
import pyzbar.pyzbar as pyzbar

print("Service which we offer:\n 1) OCR Services\n 2) Bar Code Scanner\n 3) QR Code Scanner\n 4) Exit")
choice=int(input("Enter here\n"))


        
# Read in image, setting path of image and reading through easy-orc module
Image_path ="qpaper.jpg"
if(choice==1):
    reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext(Image_path)
    img = cv2.imread(Image_path)
    for detection in result:
      top_left = tuple([int(val) for val in detection[0][0]])
      bottom_right = tuple([int(val) for val in detection[0][2]])
      text = detection[1]
      font = cv2.FONT_HERSHEY_PLAIN
# Draws a green rectangle over text and also prints the text.
      img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 5)
      print(text)
    
# Opening the test file in both the reading and appending mode.
    with open('test.txt', 'a+') as file :
        file.write(text)
        file.write("\n")
 
         # the file will save and close after you exit this block scope
        
        
# cv. LINE_AA gives anti-aliased line which looks great for curves.
   # img = cv2.putText(img, text, top_left, font, 3, (0,0,0), 2, cv2.LINE_AA)

    plt.figure(figsize=(10, 10)) # increasing the size of image, makes us easier to see text
    plt.imshow(img)
    plt.show()
#img1=cv2.imwrite("NEWf.txt",text)

elif(choice==2):

    # Load an image or capture a video frame
    img = cv2.imread("barcode.png")
    # frame = cv2.VideoCapture(0).read()[1]  # for capturing a video frame

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Use ZBar to scan the barcode
    barcodes = pyzbar.decode(gray)

    # Loop through each barcode found
    for barcode in barcodes:
        # Extract the barcode data as a string
        barcode_data = barcode.data.decode("utf-8")
        print(f"Barcode data: {barcode_data}")
        
elif(choice==3):
    # Load an image or capture a video frame
    img = cv2.imread("code.jpg")
    # frame = cv2.VideoCapture(0).read()[1]  # for capturing a video frame

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Use pyzbar to scan the QR code
    qrcodes = pyzbar.decode(gray)

    # Loop through each QR code found
    for qr in qrcodes:
        # Extract the QR code data as a string
        qr_data = qr.data.decode("utf-8")
        print(f"QR code data: {qr_data}")
        
elif(choice==4):
    print("Thank You for using our system, Hoping that you liked our project..!")

else:
    print("Please select the correct option")



""" image will be in array formate
    [([[18, 18], [293, 18], [293, 145], [18, 145]], 'Text Here', 'someting called confidence')]
"""

"""
#************************************** Draw result for single line
# declaring some constants
top_left = tuple(result[0][0][0]) # [18, 18]
bottom_right = tuple(result[0][0][2]) # [298, 145]
text = result[0][1]
font = cv2.FONT_HERSHEY_PLAIN # Defining the font we gonna use

# draw a green color rectangle over text, and also print text on top_left out-side of rectange
img = cv2.imread(Image_path)
img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 5)
img = cv2.putText(img, text, top_left, font, .5, (255, 255, 255), cv2.LINE_AA)
plt.imshow(img)
plt.show()
"""

