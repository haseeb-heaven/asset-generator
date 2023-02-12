# AI Assets Generator

<p align="center">
    <img src="https://raw.githubusercontent.com/haseeb-heaven/AI-Assets-Generator/main/resources/ai-assets-logo.png" alt="dall-e" width="800"/>
</p>

AI Assets Generator is a Python-based tool for generating artificial intelligence-powered images and searching for images on Bing. This tool can also be used as an AI game asset art generator.

## AI Assets Generator App.
<p align="center">
    <img src="https://raw.githubusercontent.com/haseeb-heaven/AI-Assets-Generator/main/resources/dalle-image-search.png" alt="dall-e" width="800"/>
</p>
<p align="center">
    <img src="https://raw.githubusercontent.com/haseeb-heaven/AI-Assets-Generator/main/resources/bing-image-search.png" alt="dall-e" width="800"/>
</p>



## Features

* Generate OpenAI images with the provided prompt text
* Save OpenAI-generated images
* Clear OpenAI-generated images
* Search for images on Bing using the provided search query
* Modular code structure for easy maintenance and expansion
* The OpenAI section of the tool allows users to generate images using the DALL-E API. This API uses a neural network to generate images based on user prompts. Users can enter a text prompt and the neural network will generate an image based on that prompt.
* The tool also includes a Bing Image Search section, which allows users to search for images on the internet using the Bing Search API. Users can enter a search query and the tool will display a list of images related to that query.
* The Bing Image Search section also includes the ability to save images to the user's local filesystem. This can be useful for collecting a set of images for use in a project.
* The tool includes error handling and validation for user inputs, so if the user enters an invalid prompt or search query, they will be notified with a message.
* The code is modular and organized into different files for each section of the tool. This makes it easy to modify or extend the tool in the future.


## Getting Started

To use this tool, follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install the required packages using the following command: 

```pip install -r requirements.txt```

4. To generate OpenAI images, you need to have an OpenAI API key. You can set the API key as an environment variable using the following command:

```export OPENAI_API_KEY=<your API key>```

For Windows, use the following command instead:

```set OPENAI_API_KEY=<your API key>```

5. To run the program, execute the following command:

```python AIAssetsGenerator.py```

## Usage
Run the ImageAIGenerator.py file to start the application.

The OpenAI tab allows you to generate AI-generated images using DALL-E. Enter your prompt text in the "Enter Prompt" textbox and click on "Generate Image" to see the generated image.</br>

You can save the image using the "Save Image" button, and clear the prompt and image using the "Clear Image" button.
The Bing tab allows you to search for images using the Bing image search API.</br>

Enter your search query in the "Enter Search Query" textbox and click on "Search Images" to see the search results. Click on any image to see the full image, and save the image using the "Save Image" button. You can clear the search query, image, and URL using the "Clear Image" button.</br>

## Packages Used
* tkinter: Python's standard GUI package.
* requests: HTTP library for Python.
* Pillow: Python Imaging Library.
* python-dotenv: Python library to load environment variables from .env files.
* openai: Python library to use the OpenAI API.
* python-bing-image-search: Python SDK for the Bing image search API.

## Requirements

* Python 3.6 or higher
* tkinter
* openai
* bing_image_downloader

## Author

AI Assets Generator was developed by HeavenHM.
