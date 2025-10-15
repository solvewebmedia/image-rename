import os

def rename_image(
        image_path: str = False, 
        new_name: str = False,
        prefix: str = False,
        suffix: str = False
        ) -> str:
    """
    Rename an image file with options for new name, prefix, and suffix.
    Args:
    old_name (str): Current name of the image file.
    new_name (str): New name for the image file.
    prefix (str): Prefix to add to the current name.
    suffix (str): Suffix to add to the current name.
    """

    # Get original extension
    _, ext = os.path.splitext(image_path)

    # Build new name with prefix/suffix
    name = new_name
    if prefix:
        name = f"{prefix}{name}"
    if suffix:
        name = f"{name}{suffix}"

    # Add original extension
    name = f"{name}{ext}"
    new_path = os.path.join(os.path.dirname(image_path), name)

    os.rename(image_path, new_path)