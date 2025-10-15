import os
import argparse
import warnings
from tqdm import tqdm
from caption_func import create_captions, rename_image


IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff")

# Suppress FutureWarnings and UserWarnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)


def execute_captioning(image_folder: str, prefix: str, suffix: str) -> None:
    """Generate captions and rename images in the given folder.

    Args:
        image_folder: Path to the folder with images. Use "." for current dir.
        prefix: Prefix to add to the new image name.
        suffix: Suffix to add to the new image name.
    """
    images = [entry for entry in os.listdir(image_folder) if entry.lower().endswith(IMAGE_EXTENSIONS)]
    for entry in tqdm(images, desc="Processing images", unit="img"):
        image = os.path.join(image_folder, entry)
        captions = create_captions(image_path=image).title()
        rename_image(
            image_path=image,
            new_name=captions,
            prefix=prefix,
            suffix=suffix,
        )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Rename images in a folder or a single image using generated captions."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Path to folder or image (default: current directory)",
    )
    parser.add_argument(
        "--prefix",
        type=str,
        default="Solve - ",
        help="Prefix to add to the new image name (default: 'Solve - ')",
    )
    parser.add_argument(
        "--suffix",
        type=str,
        default=" - v1",
        help="Suffix to add to the new image name (default: ' - v1')",
    )
    args = parser.parse_args()

    path = os.path.abspath(args.path)
    prefix = args.prefix
    suffix = args.suffix
    if os.path.isdir(path):
        execute_captioning(path, prefix, suffix)
    elif os.path.isfile(path) and path.lower().endswith(IMAGE_EXTENSIONS):
        print("Processing image...")
        captions = create_captions(image_path=path).title()
        rename_image(
            image_path=path,
            new_name=captions,
            prefix=prefix,
            suffix=suffix,
        )
    else:
        raise SystemExit(f"Not a valid image or directory: {path}")


if __name__ == "__main__":
    main()
