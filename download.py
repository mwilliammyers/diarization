import json
from pathlib import Path
from string import ascii_lowercase

import requests

base_url = "http://www.robots.ox.ac.uk/~vgg/data/voxceleb/vox1a/"

creds = json.loads(Path("creds.json").read_text())
username = creds["username"]
password = creds["password"]

for c in ascii_lowercase[:8]:
    r = requests.get(f"{base_url}/vox2_dev_aaca{c}", auth=(username, password))
    print(r)


r = requests.get(f"{base_url}/vox2_test_aac.zip", auth=(username, password))
print(r)
