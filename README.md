# EXIF Scrubber

A simple Python script to remove EXIF metadata from images. EXIF Scrubber does not modify your existing images.

## Installation
Just clone the repository or download the `exif-scrub.py` file.

To install requirements, run `pip install -r requirements.txt`, or manually install the requirements listed in that file.

## Usage
Give the script a [glob](https://docs.python.org/3/library/glob.html) of images to scrub EXIF data from.

```shell
$ python3 exif-scrub.py "GLOB" OPTIONS
```

### Options
#### -G, --gps
Remove all GPS related EXIF data.

```shell
$ python3 exif-scrub.py "protest/*.jpg" --gps

- gps_version_id
- gps_latitude_ref
- gps_latitude
- gps_longitude_ref
- gps_longitude
- gps_altitude_ref
- gps_altitude
- gps_timestamp
- gps_satellites
- gps_status
- gps_measure_mode
- gps_dop
- gps_speed_ref
- gps_speed
- gps_track_ref
- gps_track
- gps_img_direction_ref
- gps_img_direction
- gps_map_datum
- gps_dest_latitude_ref
- gps_dest_latitude
- gps_dest_longitude_ref
- gps_dest_longitude
- gps_dest_bearing_ref
- gps_dest_bearing
- gps_dest_distance_ref
- gps_dest_distance
- gps_processing_method
- gps_area_information
- gps_datestamp
- gps_differential
- gps_horizontal_positioning_error
```

#### -A, --all
Remove **all** EXIF data form the image.

#### -P, --pattern
Provide a Regex pattern to match. EXIF tags are converted to [snake_case](https://www.wikiwand.com/en/Snake_case), so your pattern should match.

```shell
$ python3 exif-scrub.py "protest/*.jpg" --pattern "datetime"

- datetime
- datetime_original
- datetime_digitized
```
