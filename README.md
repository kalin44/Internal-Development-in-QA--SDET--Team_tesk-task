# Internal Development in QA (SDET) Team_tesk task
 
This Python program that can synchronize two folders, source and replica, using the rsync algorithm. The program can be run from the command line and accepts the following arguments:

    --source: path to the source folder
    --replica: path to the replica folder
    --interval: synchronization interval in seconds
    --logfile: path to the log file

The program periodically checks if the source folder has been modified since the last synchronization, and if so, it synchronizes the source folder with the replica folder using the rsync algorithm. The program also logs all file creation/copying/removal operations to both the console output and the log file.

You can run this program from the command line with the following command:
python synchronize_folders.py --source /path/to/source/folder --replica /path/to/replica/folder --interval 60 --logfile sync.log

This will synchronize the source folder with the replica folder every 60 seconds, and log all file creation/copying/removal operations to the file sync.log.