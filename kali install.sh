#!/bin/bash

# Update package lists
sudo apt update

# Install Python 3.11
sudo apt install python3.11

# Install pip for Python 3.11
sudo apt install python3.11-pip

# Install the requirements using pip
pip install -r requirements.txt
