## Project Shell, Basic

In this project we'll start to use command shell basic.

#### What is a Shell

 - he shell is a program that takes commands from the keyboard and gives them to the operating system to perform.

## Quiz 

### Question 0

What command would you use to list files on Linux?

 - ls

### Question 1

What does LTS stand for?

 - Long Term Support

### Question 2

How do you change directory on Linux?

 - cd

### Question 3

What does RTFM stand for?

 - Read The F\*\* Manual

# Tasks

### 0. Where am I? 

Write a script that prints the absolute path name of the current working directory.

Example:

```
[victorz@ManjaroKDE 0x00-shell_basics]$ ./0-current_working_directory 
/home/victorz/code/holberton-system_engineering-devops/0x00-shell_basics
[victorz@ManjaroKDE 0x00-shell_basics]$

```

### 1. What’s in there?

Display the contents list of your current directory.

Example:

```
[victorz@ManjaroKDE 0x00-shell_basics]$ ./1-listit 
0-current_working_directory  12-file_type      15-lets_move    18-commas        3-listfiles           6-firstdirectory  9-firstdirdeletion
10-back                      13-symbolic_link  16-clean_emacs  1-listit         4-listmorefiles       7-movethatfile    holberton.mgc
11-lists                     14-copy_html      17-tree         2-bring_me_home  5-listfilesdigitonly  8-firstdelete     README.md
[victorz@ManjaroKDE 0x00-shell_basics]$ 

```
### 2. There is no place like home

Write a script that changes the working directory to the user’s home directory.

 * You are not allowed to use any shell variables

```
[victorz@ManjaroKDE tmp]$ pwd
/tmp
[victorz@ManjaroKDE tmp]$ echo $HOME
/home/victorz
[victorz@ManjaroKDE tmp]$ source ./2-bring_me_home
[victorz@ManjaroKDE ~]$ pwd
/home/victorz
[victorz@ManjaroKDE ~]$ 

```

### 3. The long format

Display current directory contents in a long format

Example:

```
[victorz@ManjaroKDE 0x00-shell_basics]$ ./3-listfiles 
total 84
-rwxr-xr-x 1 victorz victorz  16 Jun  3 20:54 0-current_working_directory
-rwxr-xr-x 1 victorz victorz  17 Jun  3 20:54 10-back
-rwxr-xr-x 1 victorz victorz  30 Jun  3 20:54 11-lists
-rwxr-xr-x 1 victorz victorz  31 Jun  3 20:54 12-file_type
-rwxr-xr-x 1 victorz victorz  33 Jun  3 20:54 13-symbolic_link
-rwxr-xr-x 1 victorz victorz  28 Jun  3 20:54 14-copy_html
-rwxr-xr-x 1 victorz victorz  35 Jun  3 20:54 15-lets_move
-rwxr-xr-x 1 victorz victorz  18 Jun  3 20:54 16-clean_emacs
-rwxr-xr-x 1 victorz victorz  42 Jun  3 20:54 17-tree
-rwxr-xr-x 1 victorz victorz  20 Jun  3 20:54 18-commas
-rwxr-xr-x 1 victorz victorz  15 Jun  3 20:54 1-listit
-rwxr-xr-x 1 victorz victorz  15 Jun  3 20:54 2-bring_me_home
-rwxr-xr-x 1 victorz victorz  18 Jun  3 20:54 3-listfiles
-rwxr-xr-x 1 victorz victorz  19 Jun  3 20:54 4-listmorefiles
-rwxr-xr-x 1 victorz victorz  19 Jun  3 20:54 5-listfilesdigitonly
-rwxr-xr-x 1 victorz victorz  33 Jun  3 20:54 6-firstdirectory
-rwxr-xr-x 1 victorz victorz  42 Jun  3 20:54 7-movethatfile
-rwxr-xr-x 1 victorz victorz  39 Jun  3 20:54 8-firstdelete
-rwxr-xr-x 1 victorz victorz  33 Jun  3 20:54 9-firstdirdeletion
-rw-r--r-- 1 victorz victorz  51 Jun  3 20:54 holberton.mgc
-rw-r--r-- 1 victorz victorz 240 Jun  3 20:54 README.md
[victorz@ManjaroKDE 0x00-shell_basics]$ 

```

### 4. Hidden files

Display current directory contents, including hidden files (starting with .). Use the long format.

Example:
```
[victorz@ManjaroKDE 0x00-shell_basics]$ ./4-listmorefiles 
total 92
drwxr-xr-x 2 victorz victorz 4096 Jun  3 20:54 .
drwxr-xr-x 4 victorz victorz 4096 Jun  3 20:54 ..
-rwxr-xr-x 1 victorz victorz   16 Jun  3 20:54 0-current_working_directory
-rwxr-xr-x 1 victorz victorz   17 Jun  3 20:54 10-back
-rwxr-xr-x 1 victorz victorz   30 Jun  3 20:54 11-lists
-rwxr-xr-x 1 victorz victorz   31 Jun  3 20:54 12-file_type
-rwxr-xr-x 1 victorz victorz   33 Jun  3 20:54 13-symbolic_link
-rwxr-xr-x 1 victorz victorz   28 Jun  3 20:54 14-copy_html
-rwxr-xr-x 1 victorz victorz   35 Jun  3 20:54 15-lets_move
-rwxr-xr-x 1 victorz victorz   18 Jun  3 20:54 16-clean_emacs
-rwxr-xr-x 1 victorz victorz   42 Jun  3 20:54 17-tree
-rwxr-xr-x 1 victorz victorz   20 Jun  3 20:54 18-commas
-rwxr-xr-x 1 victorz victorz   15 Jun  3 20:54 1-listit
-rwxr-xr-x 1 victorz victorz   15 Jun  3 20:54 2-bring_me_home
-rwxr-xr-x 1 victorz victorz   18 Jun  3 20:54 3-listfiles
-rwxr-xr-x 1 victorz victorz   19 Jun  3 20:54 4-listmorefiles
-rwxr-xr-x 1 victorz victorz   19 Jun  3 20:54 5-listfilesdigitonly
-rwxr-xr-x 1 victorz victorz   33 Jun  3 20:54 6-firstdirectory
-rwxr-xr-x 1 victorz victorz   42 Jun  3 20:54 7-movethatfile
-rwxr-xr-x 1 victorz victorz   39 Jun  3 20:54 8-firstdelete
-rwxr-xr-x 1 victorz victorz   33 Jun  3 20:54 9-firstdirdeletion
-rw-r--r-- 1 victorz victorz   51 Jun  3 20:54 holberton.mgc
-rw-r--r-- 1 victorz victorz  240 Jun  3 20:54 README.md
[victorz@ManjaroKDE 0x00-shell_basics]$ 

```

### 5. I love numbers

Display current directory contents.

   - Long format
   - with user and group IDs displayed numerically
   - And hidden files \(starting with .\)

```
[victorz@ManjaroKDE 0x00-shell_basics]$ ./5-listfilesdigitonly | head -10
total 92
drwxr-xr-x 2 victorz victorz 4096 Jun  3 20:54 .
drwxr-xr-x 4 victorz victorz 4096 Jun  3 20:54 ..
-rwxr-xr-x 1 victorz victorz   16 Jun  3 20:54 0-current_working_directory
-rwxr-xr-x 1 victorz victorz   17 Jun  3 20:54 10-back
-rwxr-xr-x 1 victorz victorz   30 Jun  3 20:54 11-lists
-rwxr-xr-x 1 victorz victorz   31 Jun  3 20:54 12-file_type
-rwxr-xr-x 1 victorz victorz   33 Jun  3 20:54 13-symbolic_link
-rwxr-xr-x 1 victorz victorz   28 Jun  3 20:54 14-copy_html
-rwxr-xr-x 1 victorz victorz   35 Jun  3 20:54 15-lets_move
[victorz@ManjaroKDE 0x00-shell_basics]$

```

### 6. Welcome holberton 

Create a script that creates a directory named holberton in the /tmp/ directory.

Example:

```
$ ./6-firstdirectory
$ file /tmp/holberton/
/tmp/holberton/: directory
$
```

### 7. Betty in Holberton

Move the file betty from /tmp/ to /tmp/holberton.

Example:

```
$ ./7-movethatfile
$ ls /tmp/holberton/
betty
$
```

### 8. Bye bye Betty

Delete the file betty.

 - The file betty is in /tmp/holberton

Example:

```
$ ./8-firstdelete
$ ls /tmp/holberton/
$
```

### 9. Bye bye Holberton

Delete the directory holberton that is in the /tmp directory.

Example:

```
$ ./9-firstdirdeletion
$ file /tmp/holberton
/tmp/holberton: cannot open `/tmp/holberton' (No such file or directory)
$
```

### 10. Back to the future 

Write a script that changes the working directory to the previous one.

### 11. Lists 

Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.

### 12. File type

Write a script that prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script.

### 13. We are symbols, and inhabit symbols 

Create a symbolic link to /bin/ls, named \_\_ls\_\_. The symbolic link should be created in the current working directory.

### 14. Copy HTML files

Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.

You can consider that all HTML files have the extension .html

### 15. Let’s move

Create a script that moves all files beginning with an uppercase letter to the directory /tmp/u.

You can assume that the directory /tmp/u will exist when we will run your script

### 16. Clean Emacs 

Create a script that deletes all files in the current working directory that end with the character ~.

### 17. Tree

Create a script that creates the directories welcome/, welcome/to/ and welcome/to/holberton in the current directory.

You are only allowed to use two spaces in your script, not more.


### 18. Life is a series of commas, not periods

Write a command that lists all the files and directories of the current directory, separated by commas (,).

  - Directory names should end with a slash \(/\)
  - Files and directories starting with a dot (.) should be listed
  - The listing should be alpha ordered, except for the directories . and .. which should be listed at the very beginning
  - Only digits and letters are used to sort; Digits should come first
  - You can assume that all the files we will test with will have at least one letter or one digit
  - The listing should end with a new line



































