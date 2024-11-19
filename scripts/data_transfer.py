import os
import json
import paramiko  # For SFTP
from pathlib import Path

# Load configurations
with open('scripts/config.json') as config_file:
    config = json.load(config_file)

def setup_sftp_connection():
    """Establish an SFTP connection."""
    transport = paramiko.Transport((config['sftp']['host'], config['sftp']['port']))
    transport.connect(username=config['sftp']['username'], password=config['sftp']['password'])
    return paramiko.SFTPClient.from_transport(transport)

def transfer_files():
    """Transfer files from remote server to local directory."""
    sftp = setup_sftp_connection()
    remote_dir = config['sftp']['remote_dir']
    local_dir = config['local']['input_dir']

    for file in sftp.listdir(remote_dir):
        remote_file_path = f"{remote_dir}/{file}"
        local_file_path = os.path.join(local_dir, file)

        try:
            sftp.get(remote_file_path, local_file_path)
            log(f"Transferred: {file}")
        except Exception as e:
            log(f"Failed to transfer {file}: {e}")

    sftp.close()

def log(message):
    """Log messages to transfer.log."""
    with open('logs/transfer.log', 'a') as log_file:
        log_file.write(f"{message}\n")

if __name__ == "__main__":
    transfer_files()
