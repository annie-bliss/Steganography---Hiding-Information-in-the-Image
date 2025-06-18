from PIL import Image
import numpy as np
from utils import text_to_binary, DELIMITER

def encode_image(image_path, message, output_path='encoded_image.png'):
    print("Opening image...")
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        print(f"Error: File '{image_path}' not found.")
        return

    img_array = np.array(img)
    print("Image loaded successfully!")

    binary_msg = text_to_binary(message) + DELIMITER
    data_index = 0

    print("Encoding message...")
    for row in img_array:
        for pixel in row:
            for channel in range(3):  # RGB
                if data_index < len(binary_msg):
                    pixel[channel] = np.uint8((pixel[channel] & 0b11111110) | int(binary_msg[data_index]))
                    data_index += 1
                else:
                    break

    encoded_img = Image.fromarray(img_array)
    encoded_img.save(output_path)
    print(f"Message encoded and saved as '{output_path}'")

if __name__ == "__main__":
    print("Reading message.txt...")
    try:
        with open("message.txt", "r") as f:
            secret_message = f.read()
        print("Message loaded!")
    except FileNotFoundError:
        print("Error: 'message.txt' not found.")
        exit()

    encode_image("sample_image.png", secret_message)
