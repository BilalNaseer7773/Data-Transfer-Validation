# Data Transfer and Validation System

## Overview
This project facilitates secure data transfer and validation of files. It uses SFTP for secure file transfer and validates data formats (e.g., JSON).

## Features
- Secure file transfer using SFTP.
- Automated validation of JSON files.
- Logs all actions for debugging and traceability.

## Directory Structure
- `scripts/`: Python scripts for transfer and validation.
- `data/`: Input, processed, and error files.
- `logs/`: Logs for all actions.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Update `config.json` with your SFTP and directory details.
3. Run `data_transfer.py` to fetch files, and `data_validation.py` to validate them.

## Requirements
- Python 3.x
- `paramiko` for SFTP.
