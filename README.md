# PythonYGOScanner
Scans Yu-Gi-Oh cards and gets price info using Python

and data provided by ygoprodeck.com

Requires Python module "requests" to be installed

Can search for cards by name or set code

## Downloading and running

`git clone https://github.com/CDelgado-dev/PythonYGOScanner`

`cd PythonYGOScanner`

`python3 YGOAPI.py`

You can also pass the card or set code as a CLI argument

For example: 

`python3 YGOAPI.py Dark Magician`

or, 

`python3 YGOAPI.py BP01-EN017`

## Dependenancies
On Debian/Ubuntu/Mint/Pop

`sudo apt install python3-pip`

On RHEL/Fedora/CentOS

`sudo dnf install python3-pip`

Then:

`pip3 install requests`