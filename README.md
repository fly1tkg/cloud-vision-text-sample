# CloudVision API text recognition sample

python3 sample script of text recognition and JSON Format output file.

## Usage

### Install library

Install google-cloud-vision package using pip.

```
$ pip install --upgrade google-cloud-vision
```

### Export Credential Path

Specify credential file at the environment variable.

```
$ export GOOGLE_APPLICATION_CREDENTIALS=/path/to/credential.json
```

### Puts Images

Puts images into `resources` folder. (Only `*.jpg`)

### Execute script

```
$ python main.py
```

### Check output folder

You can see JSON file named same image name.
