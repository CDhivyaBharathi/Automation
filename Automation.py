import cv2
import time
import random


startTime = time.time()

def take_snapshot():
       number = random.randint(0,100)
    captureObject = cv2.VideoCapture(0)
    result = True
    while (result):
        ret,frame = captureObject.read()
        cv2.imwrite("NewPicture1.jpg", frame)
        result = False
    
    captureObject.release()
    cv2.destroyAllWindows()


def main():
    password = 'qwerty'
    userPassword = input('Enter the password : ')
    if (userPassword!=password):
      print("Incorrect password")
      take_snapshot()
    
    if (userPassword == password):
        print("Password is correct")

   



main() 


        


 
