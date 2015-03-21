# Introduction to the Command Line
This document outlines some basic commands for the Unix command line.  For Linux and OS X users, these should work in **Terminal**.  For Windows users, most of these will work in **Git Bash**.  
**Note**: Most of these commands will not work in the Windows Command Prompt.

### General Command Format
`<command> -<options> <arguments>`
* `<command>` is the actual command
* `<options>` (AKA “flags”) specify different ways of executing the command
* `<arguments>` are things that go “into” the command to be operated on

### General Tips
* If there are spaces in file/folder names, use a “\” to “escape” the space characters or put the entire file path in quotes
* Type the first few letters of the file or folder name, then hit tab to autocomplete the file or folder name.  This often auto escapes spaces for you.
* Use the up and down arrow keys to navigate old commands

### Getting Help With a Command
`<command> --help` prints out the "help" page about a particular command.

For Linux/Mac users, the `man` command will give much more detailed information about a command.  To use it type `man <command>` where `<command>` is any command line command.

## File Paths
##### Relative File Paths
A relative file path specifies a path to a file taking into account what your current working directory is.  For example, if you were to give someone directions from their house to your house, you would give the directions with context of leaving their house (the relative path from where they are to where you are).
##### Absolute File Paths
An absolute file path specifies a path to a file assuming there is no knowledge of what your current working directory is.  This means the file path starts at the root directory.  For example, if you were to give someone directions from their house to your house, you would start by telling them to be on earth, then go to your continent, then go to your country, then go to your region, etc.

## Basic Commands
##### `pwd`
* **P**rints **w**orking **d**irectory (the directory/folder you are currently in)
* Lets you see where you are in your file system
* Try it out; type `pwd` into your command line.

##### `ls`
* `ls` **l**i**s**ts files/folders in your current directory
* Can list files in a specific directory (file path) with `ls <file path>`
* Optional arguments
    * `ls -a` lists **a**ll files, including the hidden files
    * `ls -l` lists the files in a **l**ist with extra information
        * File permissions (owner, group, all users)
        * Number of links
        * Owner name
        * Owner group
        * File size
        * Created/Last modified date
        * File/Folder name
* `ls *` will list all files and the contents of all folders in your current working directory.

##### `clear`
* **Clear**s all output from your console

##### `cd`
* `cd <path>` **c**hanges **d**irectory to the path you specify.  You can use a relative path or an absolute path.
* `cd ..` moves your working directory "up" one directory.
* `cd` moves your working directory to your "home" directory.
* Using `cd` and `ls` to navigate and look at your files at the command line is like clicking folders in Finder/Document Explorer.

##### `mkdir `
* `mkdir <name>` **m**a**k**es/creates a new **dir**ectory/folder with the title <name>

##### `touch`
* `touch <file>` creates an empty file with the name <file>.
* This is useful for creating empty files to be edited at a later time.

##### `rm -i`
* `rm -i <file>` **r**e**m**oves a file.  The -i flag prompts you to confirm that you really want to delete the file.
* **NOTE**: Be careful with `rm`.  Once you `rm` a file, it is gone forever.  That's why it's smart to always use `rm -i`. 
* `rm -ir <folder>` removes a folder and everything within it.
* **Note**: The `-r` option means **r**ecursive.  It's often needed for operations on a folder.

##### `mv`
* `mv <current file location> <new file location>` will **m**o**v**e a file from its <current file location> to a <new file location>.
* This is the same as dragging and dropping a file from one place to another.
* `mv <current file name> <new file name>` renames a file.  You "move" it from one location, <current file name>, to another location, <new file name>, though it doesn't actually move locations.

##### `cp`
* `cp <current file location> <new file location>` will **c**o**p**y a file from it's <current file location> to a <new file location>, leaving the original file untouched.  
* This is different from `mv` in that you are creating a new file and putting it somewhere rather than just moving the current file.

##### `zip`/`unzip`
* `zip <zipped file> <original file>` will zip/compress the <original file> into a <zipped file>.
* `zip -r <zipped file> <original folder>` will zip/compress the <original folder> and all of its files into a <zipped file>.
* **Note**:  A list of files and folders, separated by spaces, can be zipped into one zipped file with `zip -r <zipped file> <original file 1> <original folder 2> ...`.
* `unzip <file>` will unzip/uncompress a file.

## Exercise One
* Create an empty directory called `test`.
* Change your working directory to this new `test` directory.
* Create *three* empty files in your `test` directory using `touch`.
* Remove *one* of the previously created files.
* Go up one directory and remove the `test` directory with the empty files in it.  **NOTE**:  Be careful and make sure you are removing the correct files! 
* Create an empty file called `test.txt`.  
* Change the name to `data_science_is_cool.txt`.
* Create an empty file called `my_secrets.txt`.
* Create a new directory called `my_diary`.  
* Move the two previously created files into this directory.
* Create a new directory called `my_blog`.  Copy the file `data_science_is_cool.txt` from `my_diary` to `my_blog`.
* Zip the folders `my_diary` and `my_blog` into a new file called `writings.zip`.
* Delete the folders `my_diary` and `my_blog`.
* Unzip `writings.zip` to get your folders back.
* Once you finish, you can delete everything:  `writings.zip`, `my_diary`, and `my_blog`.

## Advanced Commands

##### `find`
* `find -name <name>` will search the current working directory (`pwd`) and **find** files and folders of the given <name>.
* `find <path to search> -name <name>` will search the specified path for files and folders of the given <name>.
* <name> can be the full name, but it can also be a partial match using wild card characters.
    * \* specifies any number of any characters
        * `find -name '*.csv'` will find all of the CSV files in your current directory.
    * ? specifies one character
        * `find -name '0?_submission.csv'` would find the following files in your current working directory:  `01_submission.csv`, `02_submission.csv`, and `03_submission.csv` but not `10_submission.csv`. 
* This is a very useful and powerful command.

##### `head`
* `head <file>` prints the **head** (first ten lines) of the <file>
* This is useful for looking at the beginning of a large file before performing a command on it.

##### `tail`
* `tail <file>` prints the **tail** (last ten lines) of the <file>
* This is useful for looking at the end of a large file before performing a command on it.

##### `cat`
* `cat <file>` prints the entire <file>
* This is useful sending the contents of the file into another command (more on that below).

##### `less`
* `less <file>` prints out enough of the file to fill up the console window and allows you to "scroll" through the file.
* Type `q` or `:q` to get out of the file and return to the command line.

##### `grep`
* `grep <pattern>` **g**lobally searches for a **r**egular **e**xpression and **p**rints the matches to the console.
* Returns partial matches
* Returns the line that matched.
* `grep <pattern> <file>` searches a <file> for the <patter> and prints the matching lines to the console.

##### `wc`
* `wc <file>` returns the **c**ount of lines, **w**ords, and characters in a file.
* **Note**: A word is any set of characters delimited by space.
* Combining `wc` and `grep` is a useful way of determining how many occurences of a specific word there are in a file.

##### `wget`
* `wget <url>` will go to the **w**eb and **get** the resources at the specified <url>.
* **Note**:  This doesn't work in **Git Bash**.

##### `|`
* Let’s you **pipe** commands into each other
* `<command 1> | <command 2> | <command 3>` pipes these three commands into each other.  `<command 1>` completes and the results of it are piped into `<command 2>`.  `<command 2>` completes and the results of it are pipe into `<command 3>`.  `<command 3>` completes and the results of it are printed to the console.
* This concept is a very powerful one on the command line.  This allows you to do complex things all from the command line.

##### `>`
* `<command> > <file>` takes the output of the <command> and saves it in a <file>.
* This is useful for saving the results of a command to a file.

## Exercise Two
* Navigate to the directory where you cloned the DAT5 repository.
* Find all of the CSV files in the `data` directory.  How many are there?
* How many Markdown files are there in the DAT5 directory?
* How many lines are in the `airline_safety.csv` data?
* Using `airline_safety.csv`, return a list of the airlines that have a '\*' in the name. Write these airlines to a file called `starred_airlines.csv`. **Note**: Make sure to put the \* in quotes.
* Using `chipotle_orders.tsv`, how many 'Steak Burrito's contain 'Black Beans'?  Are there more 'Steak Burrito's with 'Pinto Beans'?

## Command Line Utilities

##### `sudo`
* `sudo <command>` runs the <command> with admin access.
* Stands for **S**per **u**ser **d**o
* Use with caution as this gives your computer unrestricted access when performing the command that follows.  This is sometimes necessary to install software or access certain, restricted directories.

##### `nano`
* `nano <file>` will open the file in the NANO text editor.
* `Ctrl + X` will e**x**it the editor and prompt you to save the file or exit without saving.
* I would not recommend doing a lot of work in NANO, though it is useful to be aware of.

##### `vim`
* `vim <file>` will open the file in the VIM text editor.  But you can't start typing right away.
* Type `i` to enable **i**nsert mode and start typing.
* Use `:` to start a command
* `:w` to **w**rite/save a file
* `:x` to write/save the file you are working on and e**x**it the text editor
* `:q` to quit/exit the text editor.
* I would not recommend doing a lot of work in VIM, though it is useful to be aware of.

## Homework
* Using the command line, look at the file `SMSSpamCollection.txt` in the `data` directory.  It contains text messages that are labeled as spam or ham (the opposite of spam).  Answer the following questions:
    * How many text messages are there?
    * What is the average number of words per text?  What is the average number of characters per text?
    * How many messages are spam?  How many are ham?
    * Is there a difference between the number of words per text and characters per text in messages that are spam vs. those that are ham?  What are these numbers?
    * **Hint**: Many commands only return
* Separate the spam and ham messages into files "spam_messages.txt" and "ham_messages.txt".