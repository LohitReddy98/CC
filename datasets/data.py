import os
import requests

# List of Synset IDs
synset_ids = [
    "n02352591",
    "n02085936",
    "n02086646",
    "n02088238",
    "n02091467",
    "n02097130",
    "n02099601",
    "n02101388",
    "n02101556",
    "n02102177",
    "n02105056",
    "n02105412",
    "n02105855",
    "n02107142",
    "n02110958",
    "n02112137"
]

# Directory where you want to save the TAR files
download_dir = "datasets/imagenet-dogs"

# Create the directory if it doesn't exist
os.makedirs(download_dir, exist_ok=True)

# Base URL for Synset TAR files
base_url = "https://image-net.org/data/winter21_whole/"

# Download each Synset TAR file
for synset_id in synset_ids:
    url = f"{base_url}{synset_id}.tar"
    tar_filename = os.path.join(download_dir, f"{synset_id}.tar")

    # Download the TAR file
    response = requests.get(url)
    if response.status_code == 200:
        with open(tar_filename, 'wb') as tar_file:
            tar_file.write(response.content)
        print(f"Downloaded {synset_id}.tar")
    else:
        print(f"Failed to download {synset_id}.tar")

print("Download complete.")

import os
import requests

# List of Synset IDs
synset_ids = [
    "n02056570",
    "n02085936",
    "n02128757",
    "n02690373",
    "n02692877",
    "n03095699",
    "n04254680",
    "n04285008",
    "n04467665",
    "n07747607"
]


# Directory where you want to save the TAR files
download_dir = "datasets/imagenet-10"

# Create the directory if it doesn't exist
os.makedirs(download_dir, exist_ok=True)

# Base URL for Synset TAR files
base_url = "https://image-net.org/data/winter21_whole/"

# Download each Synset TAR file
for synset_id in synset_ids:
    url = f"{base_url}{synset_id}.tar"
    tar_filename = os.path.join(download_dir, f"{synset_id}.tar")

    # Download the TAR file
    response = requests.get(url)
    if response.status_code == 200:
        with open(tar_filename, 'wb') as tar_file:
            tar_file.write(response.content)
        print(f"Downloaded {synset_id}.tar")
    else:
        print(f"Failed to download {synset_id}.tar")

print("Download complete.")
