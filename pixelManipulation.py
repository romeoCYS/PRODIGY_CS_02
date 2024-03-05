from tkinter import filedialog
from tkinter import Tk
from PIL import Image

def select_image_file():
    
    root = Tk()
    root.withdraw()   
    file_path = filedialog.askopenfilename()
    return file_path

def encrypt_image(input_image_path, output_image_path, key):
    
    input_image = Image.open(input_image_path)
    width, height = input_image.size
    rgb_image = input_image.convert('RGB')
    encrypted_image = Image.new('RGB', (width, height))
    
    for x in range(width):
        for y in range(height):        
            r, g, b = rgb_image.getpixel((x, y))
       
            r = r ^ key
            g = g ^ key
            b = b ^ key
             
            encrypted_image.putpixel((x, y), (r, g, b))
    
    encrypted_image.save(output_image_path)
    print("Image encrypted successfully!")

def decrypt_image(input_image_path, output_image_path, key):
    
    encrypted_image = Image.open(input_image_path)
    width, height = encrypted_image.size
    
    decrypted_image = Image.new('RGB', (width, height))
     
    for x in range(width):
        for y in range(height):
            r, g, b = encrypted_image.getpixel((x, y))
            
            r = r ^ key
            g = g ^ key
            b = b ^ key
            
            decrypted_image.putpixel((x, y), (r, g, b))
    
    decrypted_image.save(output_image_path)
    print("Image decrypted successfully!")

def main():
    
    input_image_path = select_image_file()
    if not input_image_path:
        print("No file selected.")
        return
    
    output_encrypted_image_path = "encrypted_image.png"
    output_decrypted_image_path = "decrypted_image.png"
    
    encryption_key = 123
    
    encrypt_image(input_image_path, output_encrypted_image_path, encryption_key)
    
    decrypt_image(output_encrypted_image_path, output_decrypted_image_path, encryption_key)

if __name__ == "__main__":
    main()
