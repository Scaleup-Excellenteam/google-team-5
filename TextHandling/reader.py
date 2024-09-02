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


class TxtReader(IReader):
    """Class for yielding lines from .txt files"""
    
    def read_lines(self, path: str, encoding: str = 'utf-8', *args: Any, **kwargs: Any) -> Generator[str, None, None]:
        """Reads lines from a given .txt file path and yields one line at a time.

        Args:
            path (str): path to .txt file.

        Yields:
            Generator[str, None, None]: next line in the file.
        """
        try:
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
