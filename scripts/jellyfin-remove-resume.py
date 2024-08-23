import os
from xml.etree import ElementTree as ET


def remove_resume_element(filepath):
  """
  Removes the "resume" element from the given movie.xml file.

  Args:
    filepath: Path to the movie.xml file.
  """
  try:
    tree = ET.parse(filepath)
    root = tree.getroot()
    for child in root:
      if child.tag == "resume":
        root.remove(child)
        break  # Only remove the first occurrence
    tree.write(filepath)
    print(f"Successfully removed resume element from {filepath}")
  except FileNotFoundError:
    print(f"File not found: {filepath}")
  except ET.ParseError as e:
    print(f"Error parsing XML file {filepath}: {e}")


def walk_directory(directory):
  """
  Walks through a directory recursively and searches for movie.xml files.

  Args:
    directory: Path to the directory to search.
  """
  for root, dirs, files in os.walk(directory):
    for filename in files:
      if filename.lower() == "movie.xml":
        filepath = os.path.join(root, filename)
        remove_resume_element(filepath)


if __name__ == "__main__":
  # Replace "path/to/your/directory" with the actual directory path
  directory = "/mnt/union/media/movies"
  walk_directory(directory)