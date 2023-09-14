# Clean Text Utility

This utility is designed to process plain text files by removing commas and
converting spaces to newlines. The processed file will be saved with
the `.cleaned.txt` extension in an `output` directory.

## Usage

Open a terminal, change into the directory where this script is located, and run
the following command:

```bash
python clean-text.py <path_to_file>
```

Where `<path_to_file>` is the path to the plain text file you want to process.

## Features

- **File Validation**: The program first ensures that the file you've specified
  exists and is a plain text file.
- **Comma Removal**: Removes all commas from the given file.
- **Space to Newline Conversion**: Converts all spaces to newline characters.

## Function Descriptions

- `validate_file_path(file_path: str)`: Validates that the given file exists and
  is a plain text file.
- `get_dest_path(file_path: str) -> str`: Determines the destination path where
  the processed file should be saved.
- `process_file(source_file: str, dest_file: str)`: Processes the source file to
  remove commas and convert spaces to newlines, and then saves the processed
  content to the destination file.

## Dependencies

- `sys`: For command-line arguments.
- `os`: For file and path operations.
- `mimetypes`: For guessing the MIME type of the file.

## Error Codes

- `1`: The file doesn't exist or the wrong number of arguments were provided.
- `2`: The provided file is not a plain text file.
- `3`: An error occurred while processing the file.

---