import os
import argparse
from caption_func import create_captions, rename_image

def execute_captioning(image_folder):
    # Loop through folder of images and generate captions
    for image_file in os.listdir(image_folder):
        if image_file.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff")):
            image = os.path.join(image_folder, image_file)
            captions = create_captions(image_path=image).title()
            rename_image(
                image_path=image,
                new_name=captions,
                prefix="Solve - ",
                suffix=" - v1"
            )

def main():
    parser = argparse.ArgumentParser(description="Rename images in a folder using generated captions.")
    parser.add_argument(
        "folder",
        nargs="?",
        default="./images/",
        help="Path to the folder containing images (default: ./images/)"
    )
    args = parser.parse_args()
    execute_captioning(args.folder)

if __name__ == "__main__":
    main()