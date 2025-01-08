from cryptography.fernet import Fernet
from PIL import Image
import base64
import hashlib
import os

def generate_key(password):
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

def hide_text_in_image(image_path, text_file_path, output_image_path):
    with open(text_file_path, "rb") as file:
        data = file.read()

    img = Image.open(image_path)
    img = img.convert("RGBA")
    pixels = img.getdata()

    binary_data = ''.join(format(byte, '08b') for byte in data)
    binary_data += "1111111111111110"

    new_pixels = []
    data_index = 0

    for pixel in pixels:
        if data_index < len(binary_data):
            r, g, b, a = pixel
            new_pixel = (
                (r & ~1) | int(binary_data[data_index]),
                (g & ~1) | int(binary_data[data_index + 1]) if data_index + 1 < len(binary_data) else g,
                (b & ~1) | int(binary_data[data_index + 2]) if data_index + 2 < len(binary_data) else b,
                a
            )
            new_pixels.append(new_pixel)
            data_index += 3
        else:
            new_pixels.append(pixel)

    img.putdata(new_pixels)
    img.save(output_image_path)

def extract_text_from_image(image_path, output_file_path):
    img = Image.open(image_path)
    img = img.convert("RGBA")
    pixels = img.getdata()
    binary_data = ""
    for pixel in pixels:
        r, g, b, a = pixel
        binary_data += f"{r & 1}{g & 1}{b & 1}"
    end_marker = "1111111111111110"
    data_index = binary_data.find(end_marker)
    if data_index == -1:
        raise ValueError("No hidden text found in the image.")
    binary_data = binary_data[:data_index]
    bytes_data = bytes(int(binary_data[i:i + 8], 2) for i in range(0, len(binary_data), 8))
    with open(output_file_path, "wb") as file:
        file.write(bytes_data)

def lock_file_with_image(file_path, password, image_path):
    if not os.path.exists(file_path):
        print("Text file does not exist.")
        return
    if not os.path.exists(image_path):
        print("Image file does not exist.")
        return
    key = generate_key(password)
    cipher = Fernet(key)
    with open(file_path, "rb") as file:
        content = file.read()
    encrypted_content = cipher.encrypt(content)
    encrypted_file_path = file_path + ".locked"
    with open(encrypted_file_path, "wb") as locked_file:
        locked_file.write(encrypted_content)
    output_image_path = os.path.join(os.path.dirname(image_path), "pendrive_hidden.png")
    hide_text_in_image(image_path, encrypted_file_path, output_image_path)

    os.remove(file_path)
    os.remove(encrypted_file_path)
    print(f"File locked and hidden in image '{output_image_path}'.")


def unlock_file_from_image(image_path, password):
    hidden_file_path = "hidden_file.locked"

    try:
        extract_text_from_image(image_path, hidden_file_path)
    except ValueError:
        print("No hidden file found in the image.")
        return

    key = generate_key(password)
    cipher = Fernet(key)

    try:
        with open(hidden_file_path, "rb") as file:
            encrypted_content = file.read()

        decrypted_content = cipher.decrypt(encrypted_content)
        original_file_path = "unlocked_file.txt"

        with open(original_file_path, "wb") as unlocked_file:
            unlocked_file.write(decrypted_content)

        os.remove(hidden_file_path)
        print(f"File unlocked and saved as '{original_file_path}'.")
    except Exception as e:
        print("Incorrect password or corrupted file. File remains locked.")
        os.remove(hidden_file_path)
if __name__ == "__main__":
    print("1. Lock a file and hide it in an image")
    print("2. Unlock a file from an image")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        file_path = input("Enter the path of the text file to lock: ")
        password = input("Enter the password to lock the file: ")
        image_path = input("Enter the path of the image to hide the file in: ")
        lock_file_with_image(file_path, password, image_path)
    elif choice == "2":
        image_path = input("Enter the path of the image to unlock the file from: ")
        password = input("Enter the password to unlock the file: ")
        unlock_file_from_image(image_path, password)
    else:
        print("Invalid choice.")
