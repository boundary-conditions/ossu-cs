notes

file permissions are written as [d]rwxrwxrwx the optional d is for directory. Read, Write Execute. Execute in a directory allows a user to enter the directory and search its contents.

rm removes a file, -r makes this recursive, so directories and their contents can be removed.
rmdir removes an empty directory
cp copies a file, cp takes a filename and a filepath, so cp file1.txt ./other_directory/file1.txt
mv works like cp but moves instead of making a copy.
--help and man provide documentation, man takes a program name as the argument, --help follows a program name.
cat displays the contents of a file
pwd is print working drive
cd changes directories, cd ~ goes to home directory, . is current, .. is parent, - goes back to the previous directory (not parent, previous)
echo returns input
take output from one program and send to another using >, <. These overwrite contents. >> appends input to current contents.
cat < hello.txt > hello2.txt - cat reads the output from hello.txt and and then returns it, and then the > takes the output from the 'cat < hello.txt' and uses it as input for hello2.txt.
The | pipe operator takes the output from the program on the left and uses it as input for the program on the right.
tail prints the tail end of a file (ie: tail ../notes.md)
sudo means do as superuser, sudo su will switch the shell from the user shell (identified by the $) to the root shell (identified by the #).




curl

