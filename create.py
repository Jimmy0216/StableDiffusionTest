import os
import torch
from transformers import CLIPTextModel, CLIPTokenizer
from diffusers import StableDiffusionPipeline

print("Running script")

# img 폴더 경로 설정
output_dir = "C:\\Users\\user\\dev\\project\\test\\img"

# img 폴더가 없으면 생성
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Created directory {output_dir}")

# Tokenizer and model loading
tokenizer = CLIPTokenizer.from_pretrained("openai/clip-vit-large-patch14")
text_encoder = CLIPTextModel.from_pretrained("openai/clip-vit-large-patch14")

print("Tokenizer and text encoder loaded")

# Stable Diffusion Pipeline Loading
model_id = "runwayml/stable-diffusion-v1-5"
pipeline = StableDiffusionPipeline.from_pretrained(model_id, low_cpu_mem_usage=True)

print("Pipeline load complete")

# Function to create images with text prompts
def generate_images(prompts, num_images_per_prompt=4):
    for prompt in prompts:
        print(f"Creating {num_images_per_prompt} images for prompt:", prompt)
        # Create images
        with torch.no_grad():
            images = pipeline([prompt] * num_images_per_prompt).images

        # Save the images
        for i in range(num_images_per_prompt):
            index = 0
            while True:
                filename = os.path.join(output_dir, f"{prompt.replace(' ', '_')}_{index}.png")
                if not os.path.exists(filename):
                    break
                index += 1

            # Save the image
            images[i].save(filename)
            print(f"Image {i+1} has been created and saved as '{filename}'.")

# Example usage with different prompts
prompts = [
    "A woman flying in space in marvel style."
]

# Generate 4 images for each prompt
generate_images(prompts, num_images_per_prompt=4)
