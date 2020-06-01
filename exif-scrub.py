import click
import glob
import datetime
import re
import exif
import os

@click.command()
@click.argument('file_glob', type=click.STRING)
@click.option('-G', '--gps', is_flag=True)
@click.option('-A', '--all', is_flag=True)
def exif_scrub(file_glob, gps, all):
  filepaths = glob.glob(file_glob)
  scrubbed = {}

  for filepath in filepaths:
    with open(filepath, 'rb') as image_file:
      image = exif.Image(image_file)
      if not image.has_exif:
        continue

      # Remove EXIF data.
      if gps:
        remove_gps(image)

      if all:
        remove_all(image)

      # Write new image file.
      filename, extension = os.path.splitext(filepath)
      scrubbed[f"{filename}_SCRUBBED{extension}"] = image.get_file()

  for name, image_bytes in scrubbed.items():
    with open(name, 'wb') as new_image_file:
      new_image_file.write(image_bytes)

def remove_gps(image):
  gps_attrs = [e_attr for e_attr in dir(image) if re.match('gps', e_attr)]
  remove_exif_attrs(image, gps_attrs)

def remove_all(image):
  remove_exif_attrs(image, dir(image))

def remove_exif_attrs(image, exif_attrs):
  for exif_attr in exif_attrs:
    delattr(image, exif_attr)

if __name__ == '__main__':
  exif_scrub()
