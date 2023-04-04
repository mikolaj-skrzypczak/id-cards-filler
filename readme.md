## GHOST-ids
Project created to automatically fill in ~350 ID cards of GHOST Day: Applied Machine Learning Conference 2023
which I had the pleasure to co-organize with my colleagues from GHOST student research group.

More information about the conference can be found here: https://ghostday.pl/.

## Configuration
- Rename the [config.yaml.sample](ids_filler/config/config.yaml.sample) file to `config.yaml` and adjust the configuration.
- Put appropriate template images in the [clear_cards](ids_filler/resources/clear_cards) directory.
- Put csv files with the list of participants in the [csv_files](ids_filler/resources/attendees) directory. The csv files
should have the following structure: `name surname, affiliation\n`
For the program to work the names in attendees fields of config.yaml should match the names of the csv and png files.

## Installation & Running
The project uses [poetry](https://python-poetry.org/) to manage dependencies. To install poetry, run:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
(The above command is taken from the official poetry installation guide, refer to it in case of any issues.)

To install the project dependencies, run:
```bash
poetry install
```

To run the project, run:
```bash
poetry run ids_filler
```

## What it does :)
With given config:
```yaml
name_y_offset: 850
surname_y_offset: 950
affiliation_y_offset: 1100

attendees:
  gold:
    color: "#FFA63F"
```
gold.csv file with the following content:
```csv
Jan A Kowalski, Senior Research Scientist at GHOST, some other stuff & that is a really long affiliation
```
template of ID card (gold.png):
![Screenshot 1](ids_filler/resources/clear_cards/gold.png)

The program will create a new image with the following content:
![Screenshot 2](ids_filler/resources/readme_pictures/gold.png)

All the images are put in `ids_filler/results` directory.