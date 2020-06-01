import click
import glob
import datetime
import re
import exif
import os

EXIF_ATTRS = exif._constants.ATTRIBUTE_ID_MAP

@click.command()
@click.argument('file_glob', type=click.STRING)
@click.option('-G', '--gps', is_flag=True)
@click.option('-A', '--all', is_flag=True)
@click.option('-P', '--pattern', type=click.STRING)
def exif_scrub(file_glob, gps, all, pattern):
  filepaths = glob.glob(file_glob)
  scrubbed = {}

  for filepath in filepaths:
    with open(filepath, 'rb') as image_file:
      image = exif.Image(image_file)
      if not image.has_exif:
        continue

      # Remove EXIF data.
      if gps:
        remove_match(image, '^gps')

      if pattern:
        remove_match(image, pattern)

      if all:
        remove_all(image)

      # Write new image file.
      filename, extension = os.path.splitext(filepath)
      scrubbed[f"{filename}_SCRUBBED{extension}"] = image.get_file()

  for name, image_bytes in scrubbed.items():
    with open(name, 'wb') as new_image_file:
      new_image_file.write(image_bytes)

def remove_all(image):
  all_attrs = [e_attr for e_attr in EXIF_ATTRS if re.match('^(?!_).*', e_attr)]
  remove_exif_attrs(image, all_attrs)

def remove_match(image, pattern):
  attrs_to_remove = [e_attr for e_attr in EXIF_ATTRS if re.match(pattern, e_attr)]
  remove_exif_attrs(image, attrs_to_remove)

def remove_exif_attrs(image, exif_attrs):
  for exif_attr in exif_attrs:
    try:
      image.delete(exif_attr)
      click.echo(f"- {exif_attr}")
    except AttributeError:
      pass

if __name__ == '__main__':
  exif_scrub()
