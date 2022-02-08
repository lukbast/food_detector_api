def get_file_extension(file_path: str) -> str:
    """
        Simple utility function that returns extension of a file.

        Params:
            file_path (str) - path to the file
        Returns:
            extension (str) - extension of file that was passed as an argument.
    """
    extension = None
    for i, letter in enumerate(file_path[::-1]):
        if letter == ".":
            extension = file_path[len(file_path) - 1 - i:]
            break

    return extension
