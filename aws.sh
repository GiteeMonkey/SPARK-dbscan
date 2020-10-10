#!/usr/bin/env bash

# ~/aws.sh

# Removed user's cached credentials
# This script might be run with .dots, which uses elevated privileges
sudo -K

echo "------------------------------"
echo "Setting up AWS."
echo "This script requires pip and virtualenvwrapper to be installed."
echo "See the pydata.sh script."

echo "------------------------------"
echo "Source virtualenvwrapper from ~/.extra"
source ~/.extra

###############################################################################
# Python 2 Virtual Enviroment                                                 #
###############################################################################

echo "------------------------------"
echo "Updating py2-data virtual environment with AWS modules."

# Create a Python2 data environment
# If this environment already exists from running pydata.sh,
# it will not be overwritten
mkvirtualenv py2-data
workon py2-data

pip install boto
pip install awscli
pip install mrjob
pip install s3cmd

EXTRA_PATH=~/.extra
echo $EXTRA_PATH
echo "" >> $EXTRA_