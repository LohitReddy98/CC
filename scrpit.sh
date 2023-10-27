#!/bin/bash

# Set the directory where the tar files are located
tar_directory="/datasets/imagenet-10"

# Ensure the directory exists
if [ ! -d "$tar_directory" ]; then
    echo "Directory not found: $tar_directory"
    exit 1
fi

# Loop through all the tar files in the directory
for tar_file in "$tar_directory"/*.tar; do
    if [ -f "$tar_file" ]; then
        # Get the tar file name (excluding the ".tar" extension)
        tar_filename=$(basename "$tar_file" .tar)

        # Create a subfolder with the tar file name
        subfolder="$tar_directory/$tar_filename"
        mkdir -p "$subfolder"

        # Extract the tar file contents into the subfolder
        tar -xf "$tar_file" -C "$subfolder"
        echo "Extracted $tar_file to $subfolder"
    fi
done
