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


















