from abc import ABC, abstractmethod
from typing import Generator, Any


class IReader(ABC):
    """Abstract class representing objects that yield lines of text from files."""
    
    @abstractmethod
    def read_lines(self, path: str, *args: Any, **kwargs: Any) -> Generator[str, None, None]:
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
