import os

def delete_movie_xml(directory):
  """Recursively searches for and deletes 'movie.xml' files in the given directory."""

  for root, dirs, files in os.walk(directory):
    if 'movie.xml' in files:
      file_path = os.path.join(root, 'movie.xml')
      os.remove(file_path)
      print(f"Deleted movie.xml from {file_path}")

# Replace 'your_directory_path' with the actual path to the directory you want to search
directory_path = '/mnt/union/media/movies'

delete_movie_xml(directory_path)