#!/usr/bin/bash
# This program is a wrapper installer for 'setup-workstation'

# Enable copr repo
sudo dnf copr enable rcallicotte/setup-workstation

# Install the rpm
sudo dnf install setup-workstation

# Call the setup script
sudo /opt/setup-workstation/dist/setup-workstation.sh
