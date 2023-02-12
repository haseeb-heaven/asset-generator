import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as filedialog
from Dalle import generate_openai_image, save_openai_image, clear_openai_image
from BingSearch import search_bing_images, save_bing_image, clear_bing_images

# Create the main window
window = tk.Tk()
window.title("AI Assets Generator")
window.geometry("800x600")

# Create a tabbed layout using ttk Notebook
tab_control = ttk.Notebook(window)
tab_control.pack(expand=True, fill='both')

def create_openai_section(openai_frame):
    openai_left_frame = tk.Frame(openai_frame)
    openai_left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create a label and text box for the OpenAI Image prompt
    openai_prompt_label = tk.Label(openai_left_frame, text="Enter Prompt:")
    openai_prompt_label.pack(side=tk.TOP, padx=5, pady=5)
    openai_prompt_text = tk.Entry(openai_left_frame, width=50)
    openai_prompt_text.pack(side=tk.TOP, padx=5, pady=5)

    # Create a picture box for the OpenAI Image
    openai_picture_box = tk.Label(openai_left_frame)
    openai_picture_box.pack(side=tk.TOP, padx=5, pady=5)

    # Create a text box for the OpenAI Image URL
    openai_url_text = tk.Text(openai_left_frame, height=2, width=50)
    openai_url_text.pack(side=tk.TOP, padx=5, pady=5)

    # Create a button to generate the OpenAI Image
    openai_generate_button = tk.Button(openai_left_frame, text="Generate Image", command=lambda: generate_openai_image(openai_prompt_text.get(), openai_picture_box, openai_url_text))
    openai_generate_button.pack(side=tk.TOP, padx=5, pady=5)

    openai_save_button = tk.Button(openai_left_frame, text="Save Image", command=lambda: save_openai_image(openai_url_text.get("1.0", "end").strip(), openai_url_text))
    openai_save_button.pack(side=tk.TOP, padx=5, pady=5)

    openai_clear_button = tk.Button(openai_left_frame, text="Clear Image", command=lambda: clear_openai_image(openai_prompt_text, openai_picture_box, openai_url_text))
    openai_clear_button.pack(side=tk.TOP, padx=5, pady=5)
                            
def create_bing_section(bing_frame):
    bing_left_frame = tk.Frame(bing_frame)
    bing_left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    bing_query_label = tk.Label(bing_left_frame, text="Enter Search Query:")
    bing_query_label.pack(side=tk.TOP, padx=5, pady=5)

    bing_query_text = tk.Entry(bing_left_frame, width=50)
    bing_query_text.pack(side=tk.TOP, padx=5, pady=5)

    bing_picture_box = tk.Label(bing_left_frame)
    bing_picture_box.pack(side=tk.TOP, padx=5, pady=5)
    
    bing_search_button = tk.Button(bing_left_frame, text="Search Images", command=lambda: search_bing_images(bing_query_text.get(),bing_picture_box, bing_url_text))
    bing_search_button.pack(side=tk.TOP, padx=5, pady=5)

    bing_url_text = tk.Text(bing_left_frame, height=2, width=50)
    bing_url_text.pack(side=tk.TOP, padx=5, pady=5)

    bing_save_button = tk.Button(bing_left_frame, text="Save Image", command=lambda: save_bing_image(bing_url_text.get("1.0", "end").strip()))
    bing_save_button.pack(side=tk.TOP, padx=5, pady=5)

    bing_clear_button = tk.Button(bing_left_frame, text="Clear Image", command=lambda: clear_bing_images(bing_query_text, bing_picture_box, bing_url_text))
    bing_clear_button.pack(side=tk.TOP, padx=5, pady=5)

# Main method for the application.
if __name__ == "__main__":
    
    openai_tab = ttk.Frame(tab_control)
    tab_control.add(openai_tab, text="DALL-E")
    create_openai_section(openai_tab)

    bing_tab = ttk.Frame(tab_control)
    tab_control.add(bing_tab, text="Bing")
    create_bing_section(bing_tab)

    # Start the main event loop
    window.mainloop()