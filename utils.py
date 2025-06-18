def text_to_binary(text):
    """Convert a string into binary representation."""
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary_str):
    """Convert binary string to readable text."""
    chars = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    return ''.join(chr(int(b, 2)) for b in chars if len(b) == 8)

# Custom delimiter to indicate end of message
DELIMITER = '1111111111111110'  # 16 bits unlikely to occur in normal text
