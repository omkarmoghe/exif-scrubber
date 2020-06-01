# EXIF Scrubber

A simple Python script to remove GPS or _all_ EXIF metadata from images.

## Usage
Give the script a [glob](https://docs.python.org/3/library/glob.html) of images to scrub EXIF data from.

```bash
python3 exif-scrub.py "protest/*.jpg" --gps
```

### Options
#### -G, --gps
Remove all EXIF data containing the phrase "gps".

#### -A, --all
Remove **all** EXIF data form the image.
