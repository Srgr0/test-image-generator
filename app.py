import gradio as gr
import os
from generate import create_multiple_large_images

BASE_PATH = "./generated_images/"

def generate_images(size_mb, num_images):
    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH)

    created_image_paths = create_multiple_large_images(BASE_PATH, size_mb, num_images)

    return created_image_paths

def create_ui():
    with gr.Blocks() as demo:
        gr.Markdown("# test-image-generator")
        size_input = gr.Slider(minimum=1, maximum=100, label="Target size of the images in MB")
        num_images_input = gr.Slider(minimum=1, maximum=10, step=1, label="Number of images to generate")
        generate_button = gr.Button("Generate")

        output = gr.Gallery(label="Generated images").style(grid=3)

        generate_button.click(
            fn=generate_images,
            inputs=[size_input, num_images_input],
            outputs=output
        )
    return demo

if __name__ == "__main__":
    ui = create_ui()
    ui.launch()
