<<<<<<< HEAD
# import tkinter as tk
# from tkinter import messagebox
# import cv2
# import requests
# import numpy as np
# from PIL import Image, ImageTk
# import io

# def capture_image():
#     cap = cv2.VideoCapture(0)
#     if not cap.isOpened():
#         print("Cannot access the webcam.")
#         return None
    
#     ret, frame = cap.read()
#     cap.release()
    
#     if not ret:
#         print("Failed to capture image.")
#         return None
    
#     frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
#     img = Image.fromarray(frame_rgb)
#     img.show()
    
#     send_image_to_server(frame)
    
# def send_image_to_server(image):
#     _, img_encoded = cv2.imencode('.jpg', image)
#     img_bytes = img_encoded.tobytes()
    
#     server_url = 'http://localhost:3000/upload'  # Corrected URL for local server
#     try:
#         response = requests.post(server_url, files={'file': ('image.jpg', img_bytes, 'image/jpeg')})
#         print(f"Image sent to server. Response: {response.status_code}")
#     except Exception as e:
#         print(f"Error sending image to server: {e}")

# def show_ad():
#     ad_window = tk.Toplevel(app)
#     ad_window.title("Advertisement")
#     ad_window.geometry("400x300")
    
#     ad_label = tk.Label(ad_window, text="This is a random advertisement!\nClick Close to capture your image!", font=("Arial", 14))
#     ad_label.pack(pady=20)
    
#     close_button = tk.Button(ad_window, text="Close", command=lambda: [ad_window.destroy(), capture_image()])
#     close_button.pack(pady=10)

# app = tk.Tk()
# app.title("Ad-Supported Application")

# ad_button = tk.Button(app, text="Show Advertisement", command=show_ad, font=("Arial", 14))
# ad_button.pack(pady=20)

# app.mainloop()

import tkinter as tk
import cv2
import requests
from PIL import Image, ImageTk

def capture_image():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot access the webcam.")
        return
    
    ret, frame = cap.read()
    cap.release()
    if not ret:
        print("Failed to capture image.")
        return
    send_image_to_server(frame)

def send_image_to_server(image):
    _, img_encoded = cv2.imencode('.jpg', image)
    img_bytes = img_encoded.tobytes()
    server_url = 'http://localhost:3000/upload'
    try:
        response = requests.post(server_url, files={'file': ('image.jpg', img_bytes, 'image/jpeg')})
        print(f"Image sent to server. Response: {response.status_code}")
    except Exception as e:
        print(f"Error sending image to server: {e}")

def show_ad_and_capture():
    ad_image = Image.open("ad_image.png")
    ad_image = ad_image.resize((375, 140))
    ad_photo = ImageTk.PhotoImage(ad_image)
    
    ad_label = tk.Label(app, image=ad_photo)
    ad_label.image = ad_photo
    ad_label.pack()
    app.after(400, capture_image)

app = tk.Tk()
app.title("Ad-Supported Application")
app.geometry("400x300")

show_ad_and_capture()

app.mainloop()
=======
# import tkinter as tk
# from tkinter import messagebox
# import cv2
# import requests
# import numpy as np
# from PIL import Image, ImageTk
# import io

# def capture_image():
#     cap = cv2.VideoCapture(0)
#     if not cap.isOpened():
#         print("Cannot access the webcam.")
#         return None
    
#     ret, frame = cap.read()
#     cap.release()
    
#     if not ret:
#         print("Failed to capture image.")
#         return None
    
#     frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
#     img = Image.fromarray(frame_rgb)
#     img.show()
    
#     send_image_to_server(frame)
    
# def send_image_to_server(image):
#     _, img_encoded = cv2.imencode('.jpg', image)
#     img_bytes = img_encoded.tobytes()
    
#     server_url = 'http://localhost:3000/upload'  # Corrected URL for local server
#     try:
#         response = requests.post(server_url, files={'file': ('image.jpg', img_bytes, 'image/jpeg')})
#         print(f"Image sent to server. Response: {response.status_code}")
#     except Exception as e:
#         print(f"Error sending image to server: {e}")

# def show_ad():
#     ad_window = tk.Toplevel(app)
#     ad_window.title("Advertisement")
#     ad_window.geometry("400x300")
    
#     ad_label = tk.Label(ad_window, text="This is a random advertisement!\nClick Close to capture your image!", font=("Arial", 14))
#     ad_label.pack(pady=20)
    
#     close_button = tk.Button(ad_window, text="Close", command=lambda: [ad_window.destroy(), capture_image()])
#     close_button.pack(pady=10)

# app = tk.Tk()
# app.title("Ad-Supported Application")

# ad_button = tk.Button(app, text="Show Advertisement", command=show_ad, font=("Arial", 14))
# ad_button.pack(pady=20)

# app.mainloop()

import tkinter as tk
import cv2
import requests
from PIL import Image, ImageTk

def capture_image():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot access the webcam.")
        return
    
    ret, frame = cap.read()
    cap.release()
    if not ret:
        print("Failed to capture image.")
        return
    send_image_to_server(frame)

def send_image_to_server(image):
    _, img_encoded = cv2.imencode('.jpg', image)
    img_bytes = img_encoded.tobytes()
    server_url = 'http://localhost:3000/upload'
    try:
        response = requests.post(server_url, files={'file': ('image.jpg', img_bytes, 'image/jpeg')})
        print(f"Image sent to server. Response: {response.status_code}")
    except Exception as e:
        print(f"Error sending image to server: {e}")

def show_ad_and_capture():
    ad_image = Image.open("ad_image.png")
    ad_image = ad_image.resize((375, 140))
    ad_photo = ImageTk.PhotoImage(ad_image)
    
    ad_label = tk.Label(app, image=ad_photo)
    ad_label.image = ad_photo
    ad_label.pack()
    app.after(400, capture_image)

app = tk.Tk()
app.title("Ad-Supported Application")
app.geometry("400x300")

show_ad_and_capture()

app.mainloop()
>>>>>>> 3673686cb54a75b1ccf6bf382fba74822597e31b
