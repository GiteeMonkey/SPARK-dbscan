#!/usr/bin/env bash

# ~/aws.sh

# Removed user's cached credentials
# This script might be run with .dots, which uses elevated privileges
sudo -K

echo "------------------------------"
echo "Setting up AWS."
echo "This script re