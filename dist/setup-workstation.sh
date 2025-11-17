#!/usr/bin/bash
# Executes the ansible playbook

echo "[ INFO ] Starting setup-workstation..."
sudo ansible-playbook /opt/setup-workstation/default.yml -i /opt/setup-workstation/hosts

if [ $? -ne 0 ]; then
	echo "[ ERROR ] Generic error detected.  Sleeping for 60s."
	sleep 60
	exit 1
else
	echo "[ INFO ] setup-workstation completed successfully."
	echo "***** Window will self-terminate in 10s *****"
	sleep 10
fi
exit 0
