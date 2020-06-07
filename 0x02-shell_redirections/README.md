#    Shell, I/O Redirection

This section to start working files redirection Input/Output Shell

## Quiz questions

#### Question #0

Which symbol should I use to redirect the standard output to a file (overwrite the file)?

 - \>

#### Question #1

Which symbol should I use to redirect the standard output to a file (appending to the file)?

 - \>\>

#### Question #2

Which symbol should I use to redirect the error output to the standard output?

 - 2\>\&1

#### Question #3

Which symbol should I use to start a comment?

 - \#

#### Question #4

Which command should I use to display the entire file content?

 - cat




#### Question #5

Which command should I use to display the last 11 lines of a file?

 - tail -n 11 my_file

#### Question #6

Which symbol should I use to escape a special character?

 - \\

## Tasks

#### 0. Hello World

Write a script that prints “Hello, World”, followed by a new line to the standard output.

```

julien@ubuntu:/tmp/h$ ./0-hello_world 
Hello, World
julien@ubuntu:/tmp/h$ ./0-hello_world | cat -e
Hello, World$
julien@ubuntu:/tmp/h$ 


```
















      
