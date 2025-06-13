from PIL import Image
def encrypt_image(image_path, key):
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size
    
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)
    
    image.save("encrypted_image.png")
    print("✅ Encrypted image saved as 'encrypted_image.png'")

def decrypt_image(image_path, key):
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)
    
    image.save("decrypted_image.png")
    print("✅ Decrypted image saved as 'decrypted_image.png'")

# Modify this to your image filename
key = 123
encrypt_image("sample_image.png", key)
decrypt_image("encrypted_image.png", key)
