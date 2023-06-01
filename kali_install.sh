#!/bin/bash

# Update package lists
sudo apt update

# Install Python 3.11
sudo apt install python3.11

# Install pip for Python 3.11
sudo apt install python3.11-pip

# change into requirements dir
cd malware

# Install the requirements using pip
pip3 install -r requirements.txt
