import os
import sys
import logging
from tkinter import filedialog, messagebox
import traceback
import requests
import json
import tkinter as tk

# Set up API credentials for OpenAI
deepmind_api_key = os.getenv("DEEPAI_API_KEY")

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

# Check a string for emptiness and give error message if it is empty.
def check_valid_prompt(prompt: str):
    if not prompt:
        messagebox.showerror(title="ERROR", message="Please enter a prompt to generate an image from.")
        return False
    else:
        return True

def generate_deepai_image(prompt, save_url, picture_box):
    try:
        # Check for empty prompt.
        if not check_valid_prompt(prompt):
            return
        
        url = "https://api.deepai.org/api/text2img"
        data = {
            'text': prompt,
        }

        headers = {'api-key': deepmind_api_key}
        response = requests.post(url, data=data, headers=headers)

        if response.status_code == 200:
            result = json.loads(response.text)
            image_url = result['output_url']
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                with open(save_url, 'wb') as f:
                    f.write(image_response.content)
                picture_box.image = None
                picture_box.configure(image=None)
                picture_box.image = tk.PhotoImage(file=save_url)
                picture_box.configure(image=picture_box.image)
            else:
                raise Exception(f"Error occurred in generate_deepai_image() Failed to fetch image URL")
        else:
            raise Exception(f"Error occurred in generate_deepai_image() at line API request failed")
        
        logger.info(f"Generated deepai image for prompt: {prompt}")
    except Exception as e:
        tb = traceback.extract_tb(e.__traceback__)
        file, line, func, text = tb[-1]
        logger.error(f"Exception in File {file} and method {func}() at line {line}: {e}")
        messagebox.showerror("ERROR","Exception occured please check the log file for more details.")

def save_deepai_image(image_url, save_url_text):
    try:
        if image_url:
            file_types = [
                ('PNG Image', '*.png'),
                ('JPG Image', '*.jpg'),
                ('JPEG Image', '*.jpeg')
            ]
            file_name = filedialog.asksaveasfilename(defaultextension=".png", filetypes=file_types)
            if file_name:
                save_url_text.delete('1.0', tk.END)
                save_url_text.insert('1.0', file_name)
                response = requests.get(image_url)
                if response.status_code == 200:
                    with open(file_name, 'wb') as f:
                        f.write(response.content)
                else:
                    raise Exception(f"Error occurred in save_deepai_image() at line {sys.exc_info()[2].tb_lineno}: Failed to fetch image URL")
        else:
            raise Exception(f"Error occurred in save_deepai_image() at line {sys.exc_info()[2].tb_lineno}: No image URL to save")
    except Exception as e:
        tb = traceback.extract_tb(e.__traceback__)
        file, line, func, text = tb[-1]
        logger.error(f"Exception in File {file} and method {func}() at line {line}: {e}")
        messagebox.showerror("ERROR","Exception occured please check the log file for more details.")
        

# Create a button to clear the OpenAI Image section
def clear_deepai_image(openai_prompt_text, openai_picture_box, openai_url_text):
    openai_prompt_text.delete(0, tk.END)
    openai_picture_box.image = None
    openai_picture_box.configure(image=tk.PhotoImage())
    openai_url_text.delete('1.0', tk.END)

    logger.info("Cleared DeepAI image section")