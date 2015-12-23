# appload
Simple FTP upload with python with credentials in keychain. Overrides the files specified. Supports folders.

## Installation

1. [Install pip](https://pip.pypa.io/en/stable/installing/)

2. Install **appload** using:

		sudo pip install https://github.com/buscarini/appload/archive/master.zip

## Upgrade

	sudo pip install --upgrade https://github.com/buscarini/appload/archive/master.zip
	

## Usage

		appload.py "keychain service" "username" "server" "port" "remote path" "file 1" "file 2" … "file n"
		
**"keychain service"** is just the name or identifier you want to use for this service. You can put anything you want there (like "company_ftp").
**"keychain account"** is the ftp username.
