import os
import argparse
from caption_func import create_captions, rename_image


IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff")


def execute_captioning(image_folder: str) -> None:
    """Generate captions and rename images in the given folder.

    Args:
        image_folder: Path to the folder with images. Use "." for current dir.
    """
    for entry in os.listdir(image_folder):
        if entry.lower().endswith(IMAGE_EXTENSIONS):
            image = os.path.join(image_folder, entry)
            captions = create_captions(image_path=image).title()
            rename_image(
                image_path=image,
                new_name=captions,
                prefix="Solve - ",
                suffix=" - v1",
            )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Rename images in a folder using generated captions."
    )
    parser.add_argument(
        "folder",
        nargs="?",
        default=".",
        help="Path to folder containing images (default: current directory)",
    )
    args = parser.parse_args()

    folder = os.path.abspath(args.folder)
    if not os.path.isdir(folder):
        raise SystemExit(f"Not a directory: {folder}")

    execute_captioning(folder)


if __name__ == "__main__":
    main()
