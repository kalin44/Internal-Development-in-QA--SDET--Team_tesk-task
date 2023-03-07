import argparse
import subprocess
import time
import os


def synchronize_folders(source_folder, replica_folder, logfile):
    """
    Synchronize the source folder with replica folder using rsync
    """
    # Define rsync
    cmd = ["rsync", "-a", "--delete", source_folder, replica_folder]

    # Execute rsync command and log output
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    output = stdout.decode() + stderr.decode()
    with open(logfile, "a") as f:
        f.write(output)
    print(output)


def watch_folder(source_folder, replica_folder, logfile, interval):
    """
    Periodically check if source folder has been modified and synchronize with replica folde
    """
    # Get initial modification time of source folder
    last_modified = os.stat(source_folder).st_mtime

    while True:
        # Check if source folder has been modified
        if os.stat(source_folder).st_mtime > last_modified:
            print("Source folder modified, synchronizing...")
            synchronize_folders(source_folder, replica_folder, logfile)
            last_modified = os.stat(source_folder).st_mtime
        else:
            print("No changes in source folder.")

        # Wait for specified interval
        time.sleep(interval)


if __name__ == "__main__":
    # This is the main function where we parse command line arguments
    parser = argparse.ArgumentParser(description="Synchronize two folders.")
    parser.add_argument("--source", type=str, help="Path to source folder.")
    parser.add_argument("--replica", type=str, help="Path to replica folder.")
    parser.add_argument("--interval", type=int, default=60, help="Synchronization interval in seconds.")
    parser.add_argument("--logfile", type=str, default="sync.log", help="Path to log file.")
    args = parser.parse_args()

    # Watch source folder for changes and synchronize with replica folder
    watch_folder(args.source, args.replica, args.logfile, args.interval)
