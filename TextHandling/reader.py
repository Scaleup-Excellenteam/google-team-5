from abc import ABC, abstractmethod
from typing import Generator, Any


class IReader(ABC):
    """Abstract class representing objects that yield lines of text from files."""
    
    @abstractmethod
    def read_lines(self, path: str, *args: Any, **kwargs: Any) -> Generator[str, None, None]:
        pass

    @abstractmethod
    def get_line(self, path: str, line_num: int, encoding: str = 'utf-8') -> str:
        pass


import os
from typing import Generator, Any


class TxtReader(IReader):
    """Class for yielding lines from .txt files in a directory."""

    def read_lines(self, path: str, encoding: str = 'utf-8', *args: Any, **kwargs: Any) -> Generator[str, None, None]:
        """Reads lines from all .txt files in the given directory or from a single file path.

        Args:
            path (str): Path to a directory containing .txt files or a single .txt file.

        Yields:
            Generator[str, None, None]: The file path first, then each line in the file.
        """
        try:
            if os.path.isdir(path):
                # Iterate over all files in the directory
                for file_name in os.listdir(path):
                    file_path = os.path.join(path, file_name)
                    if os.path.isfile(file_path):
                        # First yield the file path
                        yield file_path
                        # Then yield each line from the file
                        with open(file_path, 'r', encoding=encoding) as file:
                            for line in file:
                                yield line.strip()
            else:
                # If path is a single file
                yield path
                with open(path, 'r', encoding=encoding) as file:
                    for line in file:
                        yield line.strip()

        except FileNotFoundError:
            print(f"File not found in path: {path}")

        except IOError as e:
            print(f"Error reading file: {path}\n{e}")

    def get_line(self, path: str, line_num: int, encoding: str = 'utf-8') -> str:
        """Retrieve a specific line from a file with the specified encoding.

        Args:
            path (str): The path to the file from which to read the line.
            line_num (int): The line number to retrieve (1-based index).
            encoding (str, optional): The encoding to use when reading the file. Defaults to 'utf-8'.

        Returns:
            str: The content of the specified line without the newline character.

        Raises:
            FileNotFoundError: If the file at the specified path does not exist.
            ValueError: If the specified line number is out of range for the file.
            Exception: If any other error occurs during file processing.
        """
        try:
            with open(path, 'r', encoding=encoding) as file:
                for current_line_num, line in enumerate(file, start=1):
                    if current_line_num == line_num:
                        return line.strip()
            
            raise ValueError(f"Line number {line_num} is out of range for the file {path}.")
        
        except FileNotFoundError:
            raise FileNotFoundError(f"The file at {path} does not exist.")
        
        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")
