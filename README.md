# Steganography---Hiding-Information-in-the-Image
A simple Python-based project that hides secret messages inside PNG images using the Least Significant Bit (LSB) technique. Includes both encoding and decoding scripts with support for text embedding, message extraction, and lossless image processing. 

## 🔍 Features

- Hide secret text messages inside images
- Extract hidden messages from encoded images
- Lossless data hiding using LSB method
- CLI-based tool for simplicity and portability
- Lightweight and easy to use

## 🧰 Technologies Used

- **Programming Language**: Python  
- **Libraries**:  
  - [`Pillow`](https://pillow.readthedocs.io/) – for image processing  
  - [`NumPy`](https://numpy.org/) – for pixel-level manipulation  

## ⚙️ How It Works

- **Encoding**: The script reads a message, converts it into binary, and embeds each bit into the least significant bit of RGB values in an image.
- **Decoding**: The script reads the LSBs from an image, reconstructs the binary message, and converts it back to text.

## 📦 Project Structure

steganography/
├── encode.py # Script to encode message into image
├── decode.py # Script to decode message from image
├── utils.py # Helper functions (binary conversion, delimiters)
├── sample_image.png # Input image used for hiding message
├── encoded_image.png # Output image with hidden message
└── message.txt # Text file containing the secret message

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/steganography.git
cd steganography


### 2. Install Requirements
bash
Copy code
pip install pillow numpy

### 3. Encode a Message
Place your message in message.txt and run:

bash
Copy code
python encode.py

### 4. Decode the Message
Make sure encoded_image.png exists and run:

bash
Copy code
python decode.py

### Output
The encoded_image.png will look just like the original.
The decoder retrieves the exact message embedded, if not tampered.

**👩‍💻 Created By**
Ankita Kumari
A simple project demonstrating how image steganography can be implemented using Python.

📄 License
This project is open-source under the MIT License.

yaml
Copy code
