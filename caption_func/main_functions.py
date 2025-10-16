from transformers import pipeline

try:
    import torch
except ImportError:
    torch = None

def create_captions(
        image_path: str = False,
        context: str | None = None,
        ) -> str:
    """
    Generate a caption for the given image using BLIP and return the generated text.

    Args:
        image_path (str): Path to the image file.
        context (str | None): Optional bias/context text to provide to the captioner
            to make captions less generic. Passed as the `text` argument to the
            Hugging Face pipeline when supported by the model.

    Returns:
        str: The generated caption text.
    """
    device = -1
    if torch is not None and torch.cuda.is_available():
        device = 0
    captioner = pipeline(
        task="image-to-text",
        model="Salesforce/blip-image-captioning-base",
        device=device,
    )
    # Pass context as the `text` argument when provided to bias the caption
    if context:
        return captioner(image_path, text=context)[0]["generated_text"]
    return captioner(image_path)[0]["generated_text"]