import gradio as gr
import os
import shutil
from generate import create_multiple_large_images

BASE_PATH = "./generated_images/"
ZIP_PATH = "./generated_images.zip"

def generate_images(size_mb, num_images):
    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH)

    for filename in os.listdir(BASE_PATH):
        file_path = os.path.join(BASE_PATH, filename)
        if os.path.isfile(file_path):
            os.unlink(file_path)

    created_image_paths = create_multiple_large_images(BASE_PATH, size_mb, num_images)

    if os.path.exists(ZIP_PATH):
        os.remove(ZIP_PATH)
    shutil.make_archive("generated_images", 'zip', BASE_PATH)

    return created_image_paths, ZIP_PATH

def create_ui():
    with gr.Blocks() as demo:
        gr.Markdown("# Test Image Generator")

        with gr.Row():
            size_input = gr.Slider(minimum=1, maximum=100, label="Target size of the images in MB")
            num_images_input = gr.Slider(minimum=1, maximum=100, step=1, label="Number of images to generate")

        generate_button = gr.Button("Generate")

        output_gallery = gr.Gallery(label="Generated Images", columns=3, height='400px')
        download_button = gr.File(label="Download All Images as ZIP")


        generate_button.click(
            fn=generate_images,
            inputs=[size_input, num_images_input],
            outputs=[output_gallery, download_button]
        )

    return demo

if __name__ == "__main__":
    ui = create_ui()
    ui.launch()
