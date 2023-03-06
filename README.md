# Create Image

This script takes two input images and concatenates them horizontally to create a new image. The new image is saved to the specified output directory with the specified filename.

## Prerequisites

This script requires Python 3.x and the Python Imaging Library (PIL) to be installed. You can install PIL using pip:

```
pip install pillow
```

## Compile .exe file

- `python -m venv venv`
- `venv\Scripts\activate`
- It is required to have already installed PyInstaller: `pip install pyinstaller`
- Run the following comand in the `create-image.py` location:
  ```
  python -m PyInstaller create-image.py --onefile
  ```

## Usage

To run the script, open a terminal or command prompt and navigate to the directory containing the .exe file. Then, run the following command:

```
create-image.exe <first-image-file> <second-image-file> <output-directory> <output-file-name>
```

Replace `<first-image-file>` with the path to the first input image file, `<second-image-file>` with the path to the second input image file, `<output-directory>` with the path to the output directory where the new image will be saved, and `<output-file-name>` with the desired name for the new image file.

For example:

```
create-image.exe input1.jpg input2.jpg output/ concatenated.jpg
```

This will concatenate the `input1.jpg` and `input2.jpg` files horizontally and save the resulting image as `concatenated.jpg` in the `output/` directory.

## Error Handling

The script currently assumes that the input files are valid image files and that the output directory exists or can be created. If the script encounters any errors, it will print an error message to the console.

## Potential Improvements

- Add error handling for invalid file paths or file types: The script currently assumes that the input files are valid image files and that the output directory exists or can be created. You could add error handling to check that the input files exist and are valid image files, and that the output directory is valid and can be created.
- Allow the user to specify the output image format: The current implementation saves the output image as a JPEG file by default. You could modify the script to allow the user to specify the output file format (e.g. JPEG, PNG, GIF) as a command-line argument.
- Add support for vertical concatenation: The current implementation concatenates the images horizontally. You could modify the script to allow the user to specify whether to concatenate the images horizontally or vertically.
- Improve the command-line argument parsing: The script currently uses simple positional arguments to parse the input and output file paths. You could consider using a more robust argument parser library, such as argparse, to provide better error messages, handle optional arguments, and allow the user to specify arguments in any order.
- Improve the output filename handling: The current implementation requires the user to specify the output filename, including the file extension. You could modify the script to automatically append the appropriate file extension based on the chosen output format, or allow the user to specify just the output filename without the extension.
- Add logging or verbose output: The script currently has no logging or output beyond the initial argument parsing and error messages. You could add logging or verbose output to indicate the progress of the script (e.g. "Loading input images...", "Creating output image...", "Saving output file...").

## Contributing

If you find a bug or have a feature request, please open an issue or submit a pull request on GitHub.
