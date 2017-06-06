# What is this for?
This .py program displays by file-size the files that stills haves the file descriptor open, after deleting the file.

# When to use it?
Sometimes when you delete a file that a program is using, when this occurs, the file system space stills the same and you need to restart the program to free that space, but restarting it´s not always the best idea on a production environment, so the best option is truncating the file descriptor.

With this, you will see where is located the descriptor of the file, to truncate it and free the space.
:> /proc/PID/fd/fd_id  (with this you could truncate the file, but take care!!!! you will need to be sure what you are doing)

# How to avoid the problem?
In the first step, always truncate the file and then you can remove it.
- :> file (truncate file)
- rm file (delete file)



# REQUIREMENTS:
You need to have lsof installed previously.
DELETED_FILES.py works with python 2.7 or 3.x and DELETED_FILES_py2.4.py with Python 2.4.x
