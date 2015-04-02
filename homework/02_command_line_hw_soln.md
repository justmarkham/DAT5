## Command Line Homework Solution
#### The following solution assumes you are working from the class "DAT5" directory. 
* How many text messages are there?
	* Answer:  5574
	* Code:  `wc data/SMSSpamCollection.txt` gives you the line count, word count, and character count

* What is the average number of words per text?  What is the average number of characters per text?
	* Answer:  Words per text: 15.6 or 16.6 (see below for explanation); Characters per text: 85.7 or 81.9 (see below)
	* Code:  
		* `wc data/SMSSpamCollection.txt` gives you the line count, word count, and character count.  You can divide the word count by the line count (so the number of words in each line which represents one text) to get 92482/5574 = 16.6 words per text.  However, if you want to be more technical about it, each line contains an extra word that is not part of the text, the "spam" or "ham" label.  You could remove the number of "spam"/"ham" labels (one per line) from the total word count to get (92482 - 5574)/5574 = 15.6.  
		* Similarly, using the line count and character count from the `wc` command, you can divide the character count by the line count to get 477907/5574 = 85.7.  If you remove the characters counted for the "spam" and "ham" labels, you get (477907 - 4*(# of hams) - 5*(# of spams) )/5574 = (477907 - 4*(4827) - 5*(747) )/5574 = 81.9.  **Note**:  The point of this wasn't to necessarily get the exact numbers but to identify that you can use `wc` to get a quick idea of features and labels in your data without having to open it.


* How many messages are spam?  How many are ham?
	* Answer:  Spam: 4827  Ham: 747
	* Code:
		* `grep -w 'ham' data/SMSSpamCollection.txt | wc` gives you the line count of lines labeled 'ham' in the file.  
		* `grep -w 'spam' data/SMSSpamCollection.txt | wc` gives you the line count of lines labeled 'spam' in the file.

* Is there a difference between the number of words per text and characters per text in messages that are spam vs. those that are ham?  What are these numbers?
	* Answer: Yes, there is a difference.  It seems that the "spam" texts have a much higher words per text and characters per text.  Using the simplified calculations (i.e. not remove the "spam" and "ham" from the word counts), we get the following numbers.
```
        Words per Text   Char per Text
Ham:         15.3            76.6
Spam:        24.9           145.12
```
	* Code: 
		* `grep -w 'ham' data/SMSSpamCollection.txt | wc` gives the line, word, and character count for all of the lines labeled 'ham'.  You can divide the word count by line count to get the 'Words per Text' and divide the character count by line count to get the 'Characters per Text'.  
		* `grep -w 'spam' data/SMSSpamCollection.txt | wc` gives the line, word, and character count for all of the lines labeled 'spam'.  You can divide the word count by line count to get the 'Words per Text' and divide the character count by line count to get the 'Characters per Text'.  

* **Bonus**: If you feel that this is too easy, research the `awk` command to learn how to calculate and print out these averages in the console.
	* Answer: See below
	* Code: 
		* `grep -w 'spam' data/SMSSpamCollection.txt | wc | awk '{print "Words per text: "$2/$1}'` will give you the words per text.  Notice the format of `awk` here.  You are telling it to print something and pass it column number labels.  `wc` prints out three columns:  lines, words, and characters.  For the words per text (i.e. line) we want to divide the second column by the first.
		* `grep -w 'spam' data/SMSSpamCollection.txt | wc | awk '{print "Characters per text: "$3/$1}'` will give you the character per text.

* Separate the spam and ham messages into files "spam_messages.txt" and "ham_messages.txt".
	* Answer: The code below accomplishes this.
	* Code: 
		* `grep -w 'ham' data/SMSSpamCollection.txt > ham.txt` takes the output of the `grep`, which is all of the lines that have a label ham, and puts it into a file called `ham.txt` using the `>` operator.
		* `grep -w 'spam' data/SMSSpamCollection.txt > spam.txt` takes the output of the `grep`, which is all of the lines that have a label spam, and puts it into a file called `spam.txt` using the `>` operator.
