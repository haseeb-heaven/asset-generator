# AI Assets Generator

<p align="center">
    <img src="https://raw.githubusercontent.com/haseeb-heaven/AI-Assets-Generator/main/resources/ai-assets-logo.png" alt="dall-e" width="800"/>
</p>

AI Assets Generator is tool for generating **A.I** powered images. This tool can also be used as an AI game Asset art generator with the Power of **DALL-E** and **Stable-Diffusion** you can generate high quality images for your Assets which can be used directly in your Game or Media.

## AI Assets Generator App.
<p align="center">
    <img src="https://raw.githubusercontent.com/haseeb-heaven/AI-Assets-Generator/main/resources/dalle-image.png" alt="dall-e" width="800"/>
</p>
<p align="center">
    <img src="https://raw.githubusercontent.com/haseeb-heaven/AI-Assets-Generator/main/resources/stablediffusion-image.png" alt="stability-ai" width="800"/>
</p>
<p align="center">
    <img src="https://raw.githubusercontent.com/haseeb-heaven/AI-Assets-Generator/main/resources/bing-image-search.png" alt="bing-search" width="800"/>
</p>


## Features

* Generate AI-generated images using powerful **DALL-E's** text-to-image API
* Generate AI-generated images using powerful and advanced **Stable Diffusion's** text-to-image API
* Generate AI-generated images using **DeepAI's** text-to-image API
* Search for images on Bing using the provided search query
* Advanced Logging with File logger to save all logs on error.
* Modular code structure for easy maintenance and expansion
* The OpenAI section of the tool allows users to generate images using the DALL-E API. This API uses a neural network to generate images based on user prompts. Users can enter a text prompt and the neural network will generate an image based on that prompt.
* The tool also includes a Bing Image Search section, which allows users to search for images on the internet using the Bing Search API. Users can enter a search query and the tool will display a list of images related to that query.
* The **DeepAI's** Image generate section also includes the ability to save images to the user's local filesystem. This can be useful for collecting a set of images for use in a project.
* The **Stable Diffusion's** Image generate section also includes advanced settings to generate high quality Images which can be saved directly to filesystem.


## Getting Started

To use this tool, follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install the required packages using the following command: 

```pip install -r requirements.txt```

4. To generate OpenAI images, you need to have an [OpenAI API key](https://platform.openai.com/account/api-keys) You can set the API key as an environment variable using the following command:

```export OPENAI_API_KEY=<your API key>```

For Windows, use the following command instead:

```set OPENAI_API_KEY=<your API key>```

4. To generate DeepAI images, you need to have an [DeepAI API key](https://deepai.org/dashboard/profile). You can set the API key as an environment variable using the following command:

```export DEEPAI_API_KEY=<your API key>```

For Windows, use the following command instead:

```set DEEPAI_API_KEY=<your API key>```

5. To generate Stable Diffusion images, you need to have an [Stable Diffusion API key](https://beta.dreamstudio.ai/membership?tab=apiKeys). You can set the API key as an environment variable using the following command:

```export STABILITY_KEY=<your API key>```

For Windows, use the following command instead:

```set STABILITY_KEY=<your API key>```

6. To run the program, execute the following command:

```python AIAssetsGenerator.py```

## Usage
Run the AIAssetsGenerator.py file to start the application.

The OpenAI tab allows you to generate AI-generated images using DALL-E. Enter your prompt text in the "Enter Prompt" textbox and click on "Generate Image" to see the generated image.</br>

The StableDiffusion tab allows you to generate Adavanced AI-generated images using Stability AI. Enter your prompt text in the "Enter Prompt" textbox and set your advanced settings and click on "Generate Image" to see the generated image.</br>

The DeepAI tab allows you to generate AI-generated images using DeepAI. Enter your prompt text in the "Enter Prompt" textbox and click on "Generate Image" to see the generated image.</br>

You can save the image using the "Save Image" button, and clear the prompt and image using the "Clear Image" button.
The Bing tab allows you to search for images using the Bing image search API.</br>

Enter your search query in the "Enter Search Query" textbox and click on "Search Images" to see the search results. Click on any image to see the full image, and save the image using the "Save Image" button. You can clear the search query, image, and URL using the "Clear Image" button.</br>

## Packages Used

* tkinter: Python's standard GUI package.
* requests: HTTP library for Python.
* Pillow: Python Imaging Library.
* python-dotenv: Python library to load environment variables from .env files.
* openai: Python Python SDK to use the OpenAI API.
* stablility_sdk : Python SDK for Stable diffustion.
* bing_image_urls:  Python SDK for the Bing image search API.

## Requirements

* Python 3.6 or higher
* tkinter
* openai
* bing_image_urls
* stablility_sdk

## Author

AI Assets Generator was developed by **HeavenHM**.
