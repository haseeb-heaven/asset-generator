import os
import logging
from tkinter import filedialog, messagebox
import traceback
import requests
import tkinter as tk
from PIL import Image, ImageTk
import ssl
import io
import tkinter as tk
from PIL import Image, ImageTk
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

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
stability_api_key = os.environ.get('STABILITY_KEY')

# Set up SSL context to avoid SSL errors
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# Imagebox for saving the image.
output_image: Image = None

# Check a string for emptyness and give error message if it is empty.
def check_valid_prompt(prompt: str):
    if not prompt:
        messagebox.showerror(title="ERROR", message="Please enter a prompt to generate an image from.")
        return False
    else:
        return True

def generate_stablediffusion_image(prompt,engine,steps,scale:float,sampler,image_box,width:int,height:int):
    global output_image
    try:
        # Check for empty prompt.
        if not check_valid_prompt(prompt):
            return
        
        logger.info("Generating image from Stable Diffusion API")
        logger.info("Arguments provided are as follows prompt: %s, engine: %s, steps: %s, scale: %f, sampler: %s, width: %d, height: %d", prompt, engine, steps, scale, sampler, width, height)
        
        # Generate the image from Stable Diffustion API
        stability_api = client.StabilityInference(
            key=stability_api_key,
            verbose=True,
            engine=engine
        )
        
        answers = stability_api.generate(
            prompt=prompt,
            seed=992446758,# If a seed is provided, the resulting generated image will be deterministic.
            steps=steps, # Amount of inference steps performed on image generation. Defaults to 30. 
            cfg_scale=scale, # Influences how strongly your generation is guided to match your prompt.
            width=width,
            height=height,
            samples=1, # Number of images to generate, defaults to 1 if not included.
            sampler=getattr(generation, sampler) # Choose which sampler we want to denoise our generation with.
        )
        for resp in answers:
            for artifact in resp.artifacts:
                if artifact.finish_reason == generation.FILTER:
                    messagebox.showwarning("WARNING",
                        "Your request activated the API's safety filters and could not be processed.Please modify the prompt and try again."
                    )
                if artifact.type == generation.ARTIFACT_IMAGE:
                    image = output_image = Image.open(io.BytesIO(artifact.binary))
                    image = image.resize((300, 300))
                    img_tk = ImageTk.PhotoImage(image)
                    image_box.configure(image=img_tk)
                    image_box.image = img_tk
        # Log success message
        logging.info(f"Successfully generated StableDiffusion image from prompt: {prompt}")
    except Exception as e:
        tb = traceback.extract_tb(e.__traceback__)
        filename, line, func, text = tb[-1]
        messagebox.showerror("ERROR","Exception occured please check the log file for more details.")

        # Log error message
        logging.error(f"Exception in {func}() at line {line}: {e}")

def save_stablediffusion_image():
    global output_image
    try:
        # Ask the user for a filename to save the image to
        filetypes = [("PNG Files", "*.png"), ("JPEG Files", "*.jpeg"), ("JPG Files", "*.jpg"), ("All Files", "*.*")]
        filename = filedialog.asksaveasfilename(initialdir=".", title="Save Image", filetypes=filetypes)

        # If a filename was provided, save the image to the file
        if filename:
            if output_image is None:
                messagebox.showerror("Error", "Image not generated yet. Please generate an image first.")
                logger.error("Image not generated yet. Please generate an image first.")
                return
            else:
                output_image.save(filename, "PNG")
                # Display a success message
                messagebox.showinfo("Success", "Image saved to file")
                logging.info(f"Successfully saved image to file: {filename}")
    except Exception as e:
        tb = traceback.extract_tb(e.__traceback__)
        file, line, func, text = tb[-1]
        messagebox.showerror("ERROR","Exception occured please check the log file for more details.")
        # Log error message
        logging.error(f"Exception in {func}() at line {line}: {e}")
        
#Create a button to clear the OpenAI Image section
def clear_stablediffusion_image(prompt_text, picture_box):
    prompt_text.delete(0, tk.END)
    picture_box.image = None
    picture_box.configure(image=tk.PhotoImage())


