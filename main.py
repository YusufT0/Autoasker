from PIL import ImageGrab
from PIL import Image
import keyboard
import pyautogui
import pytesseract
import cv2
import openai
import tkinter as tk
from tkinter import ttk
    
def mousePoint(): 
    while True:
        if keyboard.read_key() == "a": # You can change these keys with anything you want
            position1 = pyautogui.position()
            print(position1)
        elif keyboard.read_key() == "b":
            position2 = pyautogui.position()
            print(position2)
        if keyboard.read_key() == "c":
            return (position1[0],position1[1],position2[0],position2[1])
def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=("Helvetica", 10))
    label.pack(side="top", fill="x", pady=10)
    popup.attributes('-topmost',True)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.after(5000, popup.destroy)
    popup.mainloop()
            


def preprosses():
    img=cv2.imread("cropped_screenshot.png")
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh, im_bw = cv2.threshold(gray_image, 200,255, cv2.THRESH_BINARY) # If the output data is too broken you can change these values.
    cv2.imwrite("output.png", im_bw)


def askchat(text):
    openai.api_key = open("key.txt", "r").read().strip("\n")
    content = text # You can add to this string text
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": content}]
    )
    reply_content = completion.choices[0].message.content
    return reply_content

box = mousePoint() 
im = ImageGrab.grab(bbox=box)
im.save("cropped_screenshot.png")
preprosses()
image = Image.open("cropped_screenshot.png")
text = pytesseract.image_to_string(image, lang="eng")
print(text)
popupmsg(askchat(text))



