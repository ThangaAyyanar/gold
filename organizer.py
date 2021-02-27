# Organize unorganized folder ex: downloads

from pathlib import Path

path = Path('/Users/thanga-6745/Downloads')
image_extension = ["jpg","jpeg","png"]
document_extension = ["pdf","epub","png","rtf","txt","csv"]
video_extension = ["mp4","avi"]

def make_dirs():
  print(f'Current working directory {Path.cwd()}')
  dir_list = ['Books','Videos','Image','Trash']
  for dir in dir_list:
    Path.mkdir(Path(dir),exist_ok=True)

def getFiles():
    for path_object in path.iterdir():
      if path_object.is_file():
        extension = path_object.name.split('.')[-1]
        if extension in image_extension:
          new_path = f'Image/{path_object.name}'
          path_object.rename(new_path)
        elif extension in document_extension:
          new_path = f'Books/{path_object.name}'
          path_object.rename(new_path)
        elif extension in video_extension:
          new_path = f'Videos/{path_object.name}'
          path_object.rename(new_path)
        else:
          new_path = f'Trash/{path_object.name}'
          path_object.rename(new_path)


getFiles()
