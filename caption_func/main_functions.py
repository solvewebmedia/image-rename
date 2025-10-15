from transformers import pipeline
import os

try:
    import torch
except ImportError:
    torch = None

os.environ["TRANSFORMERS_VERBOSITY"] = "error"

def create_captions(
        image_path: str = False
        ) -> list:
    """
    Generate a caption for the given image using BLIP and return the raw response from the transformer.
    Args:
        image_path (str): Path to the image file.
    Returns:
        list: The raw response from the Hugging Face pipeline (list of dicts).
    """
    device = -1
    if torch is not None and torch.cuda.is_available():
        device = 0
    captioner = pipeline(
        task="image-to-text",
        model="Salesforce/blip-image-captioning-base",
        device=device,
        use_fast=True,
    )
    # Use image_path as the path to the image
    return captioner(image_path)[0]['generated_text']