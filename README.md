# image-rename

A tiny CLI to generate captions for images and rename them accordingly. Supports renaming a whole folder of images or a single image file, with optional prefix/suffix formatting.

## Install

1) Install `uv` (if you don't have it yet). See: https://docs.astral.sh/uv/getting-started/installation/

2) Install the tool directly from Git:

```sh
uv tool install https://github.com/ethbex/image-rename.git
```

- If the command is not found after installation, ensure the `uv` tools bin directory is on your PATH. Example for zsh:

```sh
# Replace with the path shown by `uv tool list --path`
export PATH="$HOME/.local/share/uv/tools/bin:$PATH"
```

Reload your shell:

```sh
source ~/.zshrc
```

## Usage

- Rename all images in a folder (default is current directory):

```sh
image-rename .
```

- Rename a specific image in the current directory:

```sh
image-rename example.jpg
```

- Customize the name with prefix/suffix:

```sh
image-rename /path/to/folder --prefix "Home - " --suffix " - v1"
image-rename example.jpg --prefix "Pic_" --suffix "_v2"
```

Supported image extensions: `.jpg, .jpeg, .png, .bmp, .gif, .tiff`.

## Update

```sh
uv tool update image-rename
```

## Uninstall

```sh
uv tool uninstall image-rename
```

## Troubleshooting

- Command not found after install:
  - Check tool location: `uv tool list --path`
  - Add its `bin` directory to PATH as shown above and reload your shell.
- Permissions issues on macOS:
  - You may need to allow terminal access to folders with images (System Settings > Privacy & Security > Files and Folders).
- Verbose warnings from libraries:
  - This tool suppresses most warnings and shows a progress bar. If you still see warnings, please open an issue with the log snippet.

## Notes

This utility depends on several ML/vision libraries (see `pyproject.toml`). When run the first time, model weights may be downloaded, which can take a while.
