# appload
Simple FTP upload with python with credentials in keychain. Overrides the files specified. Supports folders.

## Installation

1. [Install pip](https://pip.pypa.io/en/stable/installing/)

2. Install **appload** using:

		sudo pip install https://github.com/buscarini/appload/archive/master.zip

## Usage

		appload "keychain_service" "keychain_account" "server" "port" "remote path" "file 1" "file 2" … "file n"