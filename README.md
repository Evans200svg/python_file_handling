# File Read & Write Challenge 🖋️

This Python program demonstrates basic file handling and error management:

## Features
- Prompts the user for a filename to read.
- Handles errors if the file does not exist or cannot be read.
- Reads the file's contents.
- Modifies the contents (converts all text to uppercase).
- Writes the modified contents to a new file prefixed with `modified_`.
- Prints messages for success or errors.

## Usage
1. Run the program:
	 ```powershell
	 python index.py
	 ```
2. Enter the filename you want to read (e.g., `input.txt`).
3. If the file exists and is readable, a new file named `modified_input.txt` will be created with the modified content.

## Error Handling
- If the file does not exist, you will see:
	> Error: File 'filename' not found.
- If the file cannot be read or written, you will see an appropriate error message.

## Example
Suppose you have a file called `example.txt` containing:
```
Hello World!
This is a test.
```
After running the program and entering `example.txt`, a new file `modified_example.txt` will be created containing:
```
HELLO WORLD!
THIS IS A TEST.
```

---
Created for the File Read & Write Challenge and Error Handling Lab.

