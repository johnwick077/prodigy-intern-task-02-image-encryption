# Image Encryption

This repository contains a Python script for encrypting and decrypting images. The script utilizes a simple encryption algorithm to secure image files.

## Functions

- **encrypt_image(input_file, output_file, key)**: Encrypts the specified input image and saves it to the output file using the provided key.
- **decrypt_image(input_file, output_file, key)**: Decrypts the specified input image and saves the original image to the output file using the provided key.

## Working

1. **Input**: The script reads an image file (e.g., `00.jpg`).
2. **Key Generation**: A cryptographic key is generated or specified for the encryption process.
3. **Encryption Process**:
   - The image data is processed pixel by pixel.
   - Each pixel's value is modified using the encryption algorithm with the key.
4. **Output**: The encrypted image is saved as `01.jpg`.

## Uses

- **Data Security**: Protect sensitive images by encrypting them.
- **Secure Transmission**: Encrypt images before sending them over insecure channels.
- **Storage**: Store images in an encrypted format to prevent unauthorized access.

## Example

### Input File
- `00.jpg`

### Output File
- `01.jpg`

