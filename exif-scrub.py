import click
import glob
import datetime
import re
import exif
import os

@click.command()
@click.argument('file_glob', type=click.STRING)
@click.option('-G', '--gps', type=click.BOOL, default=False)
@click.option('-A', '--all', type=click.BOOL, default=False)
def exif_scrub(file_glob, gps, all):
  filepaths = glob.glob(file_glob)
  modified = []

  for filepath in filepaths:
    with open(filepath, 'rb') as image_file:
      image = exif.Image(image_file)
      if !image.has_exif:
        continue

      # Remove EXIF data.
      if gps:
        remove_gps(image)

      if all:
        remove_all(image)

      # Write new image file.
      filename, extension = os.path.splitext(filepath)
      with open(f"{filename}_{get_postfix()}.{extension}", 'wb') as new_image_file:
        new_image_file.write(image.get_file())

def remove_gps(image):
  gps_attrs = [e_attr for e_attr in dir(image) if re.match('gps', e_attr)]
  remove_exif_attrs(image, gps_attrs)

def remove_all(image):
  remove_exif_attrs(image, dir(image))

def remove_exif_attrs(image, exif_attrs):
  for exif_attr in exif_attrs:
    delattr(image, exif_attr)

def get_postfix():
  f"SCRUBBED_{datetime.datetime.now().replace(microsecond=0).isoformat()}"

if __name__ == '__main__':
  exif_scrub()
