#!/bin/bash
# Executes the ansible playbook


sudo ansible-playbook /opt/setup-workstation/default.yml -i /opt/setup-workstation/hosts
