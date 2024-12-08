from PIL import Image

def process_image(input_path, output_path, key, mode):
    try:
        image = Image.open(input_path)
        pixels = image.load()
        for x in range(image.width):
            for y in range(image.height):
                r, g, b = pixels[x, y]
                shift = key if mode == 'encrypt' else -key
                pixels[x, y] = ((r + shift) % 256, (g + shift) % 256, (b + shift) % 256)
        
        # Ensure the output file has a valid extension
        if not output_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            output_path += '.png'  # Default to PNG if no valid extension is provided
        image.save(output_path)
        print(f"Image {mode}ed and saved to {output_path}")
    except Exception as e:
        print(f"Error processing image: {e}")

def main():
    print("Image Encryption Tool")
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    if mode in ['encrypt', 'decrypt']:
        input_path = input("Enter input image path (include extension, e.g., input.png): ")
        output_path = input("Enter output image path (include extension, e.g., output.png): ")
        key = int(input("Enter key (integer): "))
        process_image(input_path, output_path, key, mode)
    else:
        print("Invalid mode! Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
