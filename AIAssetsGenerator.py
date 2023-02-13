import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as filedialog
from Dalle import generate_openai_image, save_openai_image, clear_openai_image
from BingSearch import search_bing_images, save_bing_image, clear_bing_images
from DeepAI import generate_deepai_image, save_deepai_image, clear_deepai_image
from StableDiffusion import generate_stablediffusion_image, save_stablediffusion_image, clear_stablediffusion_image

# Define the Sampler options as a dictionary. STABLE_DIFFUSION_SAMPLERS
STABLE_DIFFUSION_SAMPLERS = {
    "SAMPLER_DDIM": 0,
    "SAMPLER_DDPM": 1,
    "SAMPLER_K_EULER": 2,
    "SAMPLER_K_EULER_ANCESTRAL": 3,
    "SAMPLER_K_HEUN": 4,
    "SAMPLER_K_DPM_2": 5,
    "SAMPLER_K_DPM_2_ANCESTRAL": 6,
    "SAMPLER_K_LMS": 7,
    "SAMPLER_K_DPMPP_2S_ANCESTRAL": 8,
    "SAMPLER_K_DPMPP_2M": 9,
}

# Define the engine options as a list.
STABLE_DIFFUSION_ENGINE = [
    "stable-diffusion-v1",
    "stable-diffusion-v1-5",
    "stable-diffusion-512-v2-0",
    "stable-diffusion-768-v2-0",
    "stable-diffusion-512-v2-1",
    "stable-diffusion-768-v2-1",
    "stable-inpainting-v1-0",
    "stable-inpainting-512-v2-0",
]

# Create the main window
window = tk.Tk()
window.title("AI Assets Generator")
window.geometry("800x600")

# Create a tabbed layout using ttk Notebook
tab_control = ttk.Notebook(window)
tab_control.pack(expand=True, fill='both')

#Frame for the OpenAI Image
def create_openai_section(openai_frame):
    openai_main_frame = tk.Frame(openai_frame)
    openai_main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create a label and text box for the OpenAI Image prompt
    prompt_label = tk.Label(openai_main_frame, text="Enter Prompt:")
    prompt_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
    prompt_text = tk.Entry(openai_main_frame, width=50)
    prompt_text.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky='ns')

    # Create a picture box for the OpenAI Image
    picture_box = tk.Label(openai_main_frame)
    picture_box.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky='ns')

    # Create a text box for the OpenAI Image URL
    url_text = tk.Text(openai_main_frame, height=2, width=50)
    url_text.grid(row=2, column=0, columnspan=4, padx=5, pady=5, sticky='ns')

    # Create a button to generate the OpenAI Image
    generate_button = tk.Button(openai_main_frame, text="Generate Image", command=lambda: generate_openai_image(prompt_text.get(), picture_box, url_text))
    generate_button.grid(row=3, column=0, padx=5, pady=5)

    save_button = tk.Button(openai_main_frame, text="Save Image", command=lambda: save_openai_image(url_text.get("1.0", "end").strip(), url_text))
    save_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(openai_main_frame, text="Clear Image", command=lambda: clear_openai_image(prompt_text, picture_box, url_text))
    clear_button.grid(row=3, column=2, padx=5, pady=5)

    # Center the buttons within the main frame
    openai_main_frame.grid_columnconfigure(0, weight=1)
    openai_main_frame.grid_columnconfigure(3, weight=1)

# Frame for the Bing Search
def create_bing_search_section(bing_search_frame):
    main_frame = tk.Frame(bing_search_frame)
    main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create a label and text box for the Bing Search query
    query_label = tk.Label(main_frame, text="Enter Query:")
    query_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
    query_text = tk.Entry(main_frame, width=50)
    query_text.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky='ns')

    # Create a picture box for the Bing Search Image
    bing_search_picture_box = tk.Label(main_frame)
    bing_search_picture_box.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky='ns')

    # Create a text box for the Bing Search Image URL
    search_url_text = tk.Text(main_frame, height=2, width=50)
    search_url_text.grid(row=2, column=0, columnspan=4, padx=5, pady=5, sticky='ns')

    # Create a button to search Bing and display the image
    search_button = tk.Button(main_frame, text="Search Bing", command=lambda: search_bing_images(query_text.get(), bing_search_picture_box, search_url_text))
    search_button.grid(row=3, column=0, padx=5, pady=5)

    save_button = tk.Button(main_frame, text="Save Image", command=lambda: save_bing_image(search_url_text.get("1.0", "end").strip()))
    save_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(main_frame, text="Clear Image", command=lambda: clear_bing_images(query_text,bing_search_picture_box, search_url_text))
    clear_button.grid(row=3, column=2, padx=5, pady=5)

    # Center the buttons within the main frame
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_columnconfigure(3, weight=1)


# Frame for the DeepAI Image section
def create_deepai_section(deepai_frame):
    main_frame = tk.Frame(deepai_frame)
    main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create a label and text box for the DeepAI Image prompt
    prompt_label = tk.Label(main_frame, text="Enter Prompt:")
    prompt_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
    prompt_text = tk.Entry(main_frame, width=50)
    prompt_text.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky='ns')

    # Create a picture box for the DeepAI Image
    picture_box = tk.Label(main_frame)
    picture_box.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky='ns')

    # Create a text box for the DeepAI Image URL
    deepai_url_text = tk.Text(main_frame, height=2, width=50)
    deepai_url_text.grid(row=2, column=0, columnspan=4, padx=5, pady=5, sticky='ns')

    # Create a button to generate the DeepAI Image
    generate_button = tk.Button(main_frame, text="Generate Image", command=lambda: generate_deepai_image(prompt_text.get(), picture_box, deepai_url_text))
    generate_button.grid(row=3, column=0, padx=5, pady=5)

    save_button = tk.Button(main_frame, text="Save Image", command=lambda: save_deepai_image(deepai_url_text.get("1.0", "end").strip(), deepai_url_text))
    save_button.grid(row=3, column=1, padx=5, pady=5)

    clear_button = tk.Button(main_frame, text="Clear Image", command=lambda: clear_deepai_image(prompt_text, picture_box, deepai_url_text))
    clear_button.grid(row=3, column=2, padx=5, pady=5)

    # Center the buttons within the main frame
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_columnconfigure(3, weight=1)


# Frame for Stable Diffusion.
def create_stable_diffusion_section(stable_diffusion_frame):
    main_frame = tk.Frame(stable_diffusion_frame)
    main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Create a label and dropdown for the engine selection
    engine_label = tk.Label(main_frame, text="Engine:")
    engine_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
    engine_var = tk.StringVar(main_frame, value=STABLE_DIFFUSION_ENGINE[0])
    engine_dropdown = tk.OptionMenu(main_frame, engine_var, *STABLE_DIFFUSION_ENGINE)
    engine_dropdown.grid(row=1, column=0, padx=5, pady=5, sticky='w')

    # Create a label and dropdown for the sampler selection
    sampler_label = tk.Label(main_frame, text="Sampler:")
    sampler_label.grid(row=0, column=1, padx=5, pady=5, sticky='w')
    sampler_options = list(STABLE_DIFFUSION_SAMPLERS.keys())
    sampler_var = tk.StringVar(main_frame, value=sampler_options[0])
    sampler_dropdown = tk.OptionMenu(main_frame, sampler_var, *sampler_options)
    sampler_dropdown.grid(row=1, column=1, padx=5, pady=5, sticky='w')

    # Create a label and text box for the number of steps
    steps_label = tk.Label(main_frame, text="Steps:")
    steps_label.grid(row=0, column=2, padx=5, pady=5, sticky='w')
    steps_var = tk.IntVar(main_frame)
    steps_var.set(30)
    steps_entry = tk.Entry(main_frame, textvariable=steps_var)
    steps_entry.grid(row=1, column=2, padx=5, pady=5, sticky='w')

    # Create a label and text box for the scale option
    scale_label = tk.Label(main_frame, text="Scale:")
    scale_label.grid(row=0, column=3, padx=5, pady=5, sticky='w')
    scale_var = tk.StringVar(main_frame)
    scale_var.set("8.0")
    scale_entry = tk.Entry(main_frame, textvariable=scale_var)
    scale_entry.grid(row=1, column=3, padx=5, pady=5, sticky='w')
    
    # Create inputs for Stable Diffusion resolution
    resolution_label = tk.Label(main_frame, text="Resolution:")
    resolution_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')
    width_text_var = tk.IntVar(main_frame)
    width_text_var.set(512)
    width_text = tk.Entry(main_frame, width=10,textvariable=width_text_var)
    width_text.grid(row=2, column=1, padx=5, pady=5, sticky='w')
    
    height_text_var = tk.IntVar(main_frame)
    height_text_var.set(512)
    height_text = tk.Entry(main_frame, width=10,textvariable=height_text_var)
    height_text.grid(row=2, column=2, padx=5, pady=5, sticky='w')
    
    prompt_label = tk.Label(main_frame, text="Enter Prompt:")
    prompt_label.grid(row=4, column=0, padx=5, pady=5, sticky='w')
    stable_diffusion_prompt_text = tk.Entry(main_frame, width=50)
    stable_diffusion_prompt_text.grid(row=4, column=0, columnspan=4, padx=5, pady=5, sticky='ns')

    # Create a picture box for the Stable Diffusion Image
    stable_diffusion_picture_box = tk.Label(main_frame)
    stable_diffusion_picture_box.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky='ns')

    # Create a button to generate the Stable Diffusion Image
    generate_button = tk.Button(main_frame, text="Generate Image", command=lambda: generate_stablediffusion_image(stable_diffusion_prompt_text.get(), engine_var.get(), steps_var.get(), float(scale_var.get()), sampler_var.get(),stable_diffusion_picture_box,width_text_var.get(),height_text_var.get()))
    generate_button.grid(row=6, column=0,columnspan=2, padx=5, pady=5, sticky='ns')

    save_button = tk.Button(main_frame, text="Save Image", command=lambda: save_stablediffusion_image())
    save_button.grid(row=6, column=1,columnspan=2, padx=5, pady=5, sticky='ns')

    clear_button = tk.Button(main_frame, text="Clear Image", command=lambda: clear_stablediffusion_image(stable_diffusion_prompt_text, stable_diffusion_picture_box))
    clear_button.grid(row=6, column=2,columnspan=2, padx=5, pady=5, sticky='ns')

    # Center the buttons within the main frame
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_columnconfigure(4, weight=1)

# This is method to show the help window.
def show_help():
    help_window = tk.Toplevel(window)
    help_window.title("Help")
    help_window.geometry("400x300")

    help_text = tk.Text(help_window, font=("Helvetica", 12))
    help_text.pack()

    help_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
    help_text.insert(tk.END, "Welcome to the AI Assets Generator!\n\n")
    help_text.insert(tk.END, "This application allows you to generate images using the OpenAI DALL-E API, DeepAI, and Bing Search.\n\n")
    help_text.insert(tk.END, "OpenAI DALL-E:\n")
    help_text.insert(tk.END, "Enter a prompt for the image you want to generate and click 'Generate Image'. The generated image will appear in the picture box.\n\n")
    help_text.insert(tk.END, "DeepAI:\n")
    help_text.insert(tk.END, "Enter the desired parameters and click 'Generate Image'. The generated image will appear in the picture box.\n\n")
    help_text.insert(tk.END, "Bing Search:\n")
    help_text.insert(tk.END, "Enter a search query and click 'Search Images'. The search results will appear in the picture box. Click on a picture to select it, and click 'Save Image' to save the selected image.\n\n")

    help_text.config(state=tk.DISABLED)

    ok_button = tk.Button(help_window, text="OK", command=help_window.destroy)
    ok_button.pack(pady=10)


if __name__ == "__main__":

    openai_tab = ttk.Frame(tab_control)
    tab_control.add(openai_tab, text="DALL-E")
    create_openai_section(openai_tab)

    stable_diffustion_tab = ttk.Frame(tab_control)
    tab_control.add(stable_diffustion_tab, text="Stable Diffusion")
    create_stable_diffusion_section(stable_diffustion_tab)

    deepai_tab = ttk.Frame(tab_control)
    tab_control.add(deepai_tab, text="DeepAI")
    create_deepai_section(deepai_tab)

    bing_tab = ttk.Frame(tab_control)
    tab_control.add(bing_tab, text="Bing")
    create_bing_search_section(bing_tab)

    help_button = tk.Button(window, text="Help", command=show_help)
    help_button.pack()

    # Start the main event loop
    window.mainloop()
