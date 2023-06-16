import os
from PIL import Image

def invert_image(image_path, output_directory):
    flips = [
        (Image.FLIP_LEFT_RIGHT, 'flipped_lr'),
        (Image.FLIP_TOP_BOTTOM, 'flipped_tb'),
        (Image.ROTATE_90, 'rotated_90'),
        (Image.ROTATE_180, 'rotated_180'),
        (Image.ROTATE_270, 'rotated_270')
    ]

    image = Image.open(image_path)
    image = image.convert("RGB")

    for flip, flip_name in flips:
        inverted_image = image.transpose(flip)
        output_path = os.path.join(output_directory, f'{flip_name}_{os.path.basename(image_path)}')
        inverted_image.save(output_path)
        print(f"Saved inverted image: {output_path}")

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.jpg', '.jpeg', '.png')):
                image_path = os.path.join(root, file)
                invert_image(image_path, root)

root_directory = r"dog\\images\\"

process_directory(root_directory)