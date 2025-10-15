from transformers import pipeline
import os
from io import StringIO 
import contextlib
import sys

try:
    import torch
except ImportError:
    torch = None

@contextlib.contextmanager
def suppress_output():
    with StringIO() as buf, contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
        yield

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

    with suppress_output():
        captioner = pipeline(
            task="image-to-text",
            model="Salesforce/blip-image-captioning-base",
            device=device,
            use_fast=True,
        )
    # Use image_path as the path to the image
    return captioner(image_path)[0]['generated_text']