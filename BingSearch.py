import logging
import tkinter as tk
from tkinter import filedialog, messagebox
import traceback
import urllib.request
from io import BytesIO
from PIL import Image, ImageTk
from bing_image_urls import bing_image_urls
import requests
import ssl
import os

#setting image box size for this UI application.
dalle_imagebox_width = 480
dalle_imagebox_height = 480

# Disable SSL verification
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# Configure the logging module
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
# Check a string for emptyness and give error message if it is empty.
def check_valid_query(prompt: str):
    if not prompt:
        logging.error("Query string is empty")
        tk.messagebox.showerror("ERROR", "Please enter a query to search an image from.")
        return False
    else:
        return True

def search_bing_images(query, bing_picture_box, bing_url_text):
    try:
        # Check for empty prompt.
        if not check_valid_query(query):
            return

        # Download and display the search results
        image_urls = bing_image_urls(query, limit=1, adult_filter_off=False)
        image_url = image_urls[0]
        logging.info("Image URL: %s Query: %s", image_url, query)
        
        # Download the images and display them in the picture boxes
        with urllib.request.urlopen(image_url,context=ssl_context) as url:
            image_data = url.read()
        image = Image.open(BytesIO(image_data))
        image = image.resize((dalle_imagebox_width, dalle_imagebox_height))
        photo = ImageTk.PhotoImage(image)
        bing_picture_box.configure(image=photo)
        bing_picture_box.image = photo

        # Display the image URL in the text box
        bing_url_text.delete('1.0', tk.END)
        bing_url_text.insert(tk.END, image_url)
        
        logger.info(f"Searched image for query: {query}")
    except Exception as e:
        tb = traceback.extract_tb(e.__traceback__)
        file, line, func, text = tb[-1]
        logging.error("Exception in File %s and method %s() at line %s: %s", file, func, line, e)
        messagebox.showerror("ERROR","Exception occured please check the log file for more details.")

def save_bing_image(url):
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
    except Exception as e:
        tb = traceback.extract_tb(e.__traceback__)
        file, line, func, text = tb[-1]
        logging.error("Exception in File %s and method %s() at line %s: %s", file, func, line, e)
        messagebox.showerror("ERROR","Exception occured please check the log file for more details.")
        
def clear_bing_images(bing_query_text, bing_picture_box, bing_url_text):
    bing_query_text.delete(0, tk.END)
    bing_picture_box.image = None
    bing_picture_box.configure(image=tk.PhotoImage())
    bing_url_text.delete('1.0', tk.END)
