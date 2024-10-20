import os
import easyocr

reader = easyocr.Reader(["en"], gpu=True)
print("The current working directory is: ", os.getcwd().replace("\\", "\\\\"))
print(
    "C:\\Users\\ASUS ROG ALFRED\\Documents\\ECE\\ING3\\New York\\Courses\\Intelligent Robotics\\Project_SmartFridge\\Smart_Fridge_Project_Code\\src\\opencv\\test.png"
)

result = reader.readtext(
    "C:\\Users\\ASUS ROG ALFRED\\Documents\\ECE\\ING3\\New York\\Courses\\Intelligent Robotics\\Project_SmartFridge\\Smart_Fridge_Project_Code\\src\\opencv\\test.png"
)

for bbox, text, prob in result:
    print(f"Text: {text}, Probability: {prob}")

print(" The current working directory is: ", os.getcwd())
