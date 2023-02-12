import os
import sys
import logging
from tkinter import filedialog, messagebox
import traceback
import urllib.request
import requests
import tkinter as tk
from io import BytesIO
from PIL import Image, ImageTk
import openai
import ssl

# Set up logging
# Create a logger and set the log level
logger = logging.getLogger('AiAssetsGenerator')
logger.setLevel(logging.DEBUG)

# Setup logs for basic logging
logging.basicConfig(filename='AiAssetsGenerator.log', level=logging.INFO)

# Create a file handler and set the log level
log_file = os.path.join(os.getcwd(), 'AiAssetsGenerator.log')
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)

# Create a formatter and add it to the file handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

# Set up API credentials for OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set up SSL context to avoid SSL errors
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# Check a string for emptyness and give error message if it is empty.
def check_valid_prompt(prompt: str):
    if not prompt:
        messagebox.showerror(title="ERROR", message="Please enter a prompt to generate an image from.")
        return False
    else:
        return True

def generate_openai_image(prompt, openai_picture_box, openai_url_text):
    try:
        # Check for empty prompt.
        if not check_valid_prompt(prompt):
            return
        
        # Generate the image from OpenAI API
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512",
            api_key=openai.api_key,
        )

        # Display the image in the picture box
        img_url = response['data'][0]['url']
        with urllib.request.urlopen(img_url, context=ssl_context) as url:
            image_bytes = url.read()
        image = Image.open(BytesIO(image_bytes))
        image = image.resize((300, 300), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        openai_picture_box.configure(image=photo)
        openai_picture_box.image = photo

        # Display the image URL in the text box
        openai_url_text.delete('1.0', tk.END)
        openai_url_text.insert(tk.END, img_url)

        # Log success message
        logging.info(f"Successfully generated DALL-E image from prompt: {prompt}")
    except Exception as e:
        tb = traceback.extract_tb(e.__traceback__)
        filename, line, func, text = tb[-1]
        messagebox.showerror("ERROR","Exception occured please check the log file for more details.")

        # Log error message
        logging.error(f"Exception in {func}() at line {line}: {e}")

def save_openai_image(url, openai_url_text):
    try:
        # Make a GET request to download the image
        response = requests.get(url, verify=False)

        # Ask the user for a filename to save the image to
        filetypes = [("PNG Files", "*.png"), ("JPEG Files", "*.jpeg"), ("JPG Files", "*.jpg"), ("All Files", "*.*")]
        filename = filedialog.asksaveasfilename(initialdir=".", title="Save Image", filetypes=filetypes)

        # If a filename was provided, save the image to the file
        if filename:
            with open(filename, "wb") as f:
                f.write(response.content)

            # Display a success message
            messagebox.showinfo("Success", "Image saved to file")
            
            # Clear the image URL text box
            openai_url_text.delete('1.0', tk.END)
    except Exception as e:
        tb = traceback.extract_tb(e.__traceback__)
        file, line, func, text = tb[-1]
        messagebox.showerror("ERROR","Exception occured please check the log file for more details.")
        # Log error message
        logging.error(f"Exception in {func}() at line {line}: {e}")
        
#Create a button to clear the OpenAI Image section
def clear_openai_image(openai_prompt_text, openai_picture_box, openai_url_text):
    openai_prompt_text.delete(0, tk.END)
    openai_picture_box.image = None
    openai_picture_box.configure(image=tk.PhotoImage())
    openai_url_text.delete('1.0', tk.END)


