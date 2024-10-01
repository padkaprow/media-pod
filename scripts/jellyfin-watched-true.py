import os
import logging
from xml.etree import ElementTree as ET

# Configure logging with different levels
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

def set_watched(filepath, default_watched="false", watched_value="true"):
  """
  Marks a movie XML file as watched by setting the 'watched' element to the provided value.

  Args:
    filepath (str): Path to the XML file.
    default_watched (str, optional): Default value for the 'watched' element
      if it doesn't exist. Defaults to "false".
    watched_value (str, optional): Value to set for the "watched" element. Defaults to "true".

  Returns:
    bool: True on success, False on error.
  """
  errors = []  # List to store encountered errors
  try:
    tree = ET.parse(filepath)
  except FileNotFoundError:
    logging.error(f"File not found: {filepath}")
    errors.append(f"File not found: {filepath}")
    return False
  except ET.ParseError as e:
    logging.error(f"XML parsing error: {e}")
    errors.append(f"XML parsing error: {e}")
    return False

  root = tree.getroot()

  # Use XPath for more flexibility
  watched_element = root.find('.//watched')

  if watched_element is None:
    # Create the "watched" element if it doesn't exist
    watched_element = ET.Element('watched')
    root.append(watched_element)

  watched_element.text = watched_value

  try:
    tree.write(filepath)
    logging.info(f"Marked as watched: {filepath}")
  except (IOError, PermissionError) as e:
    logging.error(f"Error writing to file: {e}")
    errors.append(f"Error writing to file: {e}")
    return False

  if errors:
      logging.warning("Encountered errors while processing:")
      for error in errors:
          logging.warning(error)

  return True  # Indicate successful processing


def walk_directory(directory, extensions=["movie.nfo"], watched_value="true"):
  """
  Walks through a directory and marks all files with specified extensions as watched.

  Args:
    directory (str): Path to the directory to walk.
    extensions (list, optional): List of file extensions to target. Defaults to ["movie.nfo"].
    watched_value (str, optional): Value to set for the "watched" element. Defaults to "true".

  Returns:
    int: Number of successfully processed files.
  """
  processed_files = 0
  for root, dirs, files in os.walk(directory):
    for filename in files:
      if any(filename.lower().endswith(ext) for ext in extensions):
        filepath = os.path.join(root, filename)
        if set_watched(filepath, watched_value=watched_value):
          processed_files

if __name__ == "__main__":
  # Replace "path/to/your/directory" with the actual directory path
  directory = "/mnt/union/media/movies"
  walk_directory(directory)