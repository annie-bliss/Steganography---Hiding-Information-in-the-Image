from PIL import Image
import numpy as np
from utils import binary_to_text, DELIMITER

def decode_image(image_path):
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        print(f"Error: File '{image_path}' not found.")
        return

    img_array = np.array(img)
    binary_data = ""

    for row in img_array:
        for pixel in row:
            for channel in range(3):  # R, G, B
                binary_data += str(pixel[channel] & 1)

    if DELIMITER not in binary_data:
        print("No hidden message found or image not properly encoded.")
        return

    message_bits = binary_data.split(DELIMITER)[0]
    message = binary_to_text(message_bits)
    print("Decoded message:", message)

if __name__ == "__main__":
    decode_image("encoded_image.png")
