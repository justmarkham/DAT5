## DAT5 Course Repository

Course materials for [General Assembly's Data Science course](https://generalassemb.ly/education/data-science/washington-dc/) in Washington, DC (3/18/15 - 6/3/15).

**Instructors:** Kevin Markham and Brandon Burroughs

Monday | Wednesday
--- | ---
 | 3/18: Introduction and Python
3/23: Git and Command Line | 3/25: Exploratory Data Analysis
**3/30:** Visualization and APIs | 4/1: Machine Learning and KNN
**4/6:** Bias-Variance and Train/Test Split | 4/8: Kaggle Titanic (Part 1)
4/13: Web Scraping, Tidy Data, Reproducibility | 4/15: Linear Regression
4/20: Logistic Regression and Confusion Matrix | 4/22: ROC and Cross-Validation
**4/27:** Project Presentation #1 | 4/29: Kaggle Titanic (Part 2)
5/4: Naive Bayes | 5/6: Natural Language Processing
5/11: Decision Trees | 5/13: Ensembles
**5/18:** Clustering and Regularization | 5/20: Advanced scikit-learn
**5/25:** *No Class* | 5/27: Databases and SQL
6/1: Course Review | **6/3:** Project Presentation #2


### Key Project Dates
* **3/30:** Deadline for discussing your project idea(s) with an instructor
* **4/6:** Project question and dataset (write-up)
* **4/27:** Project presentation #1 (slides, code, visualizations)
* **5/18:** First draft due (draft of project paper, code, visualizations)
* **5/25:** Peer review due
* **6/3:** Project presentation #2 (project paper, slides, code, visualizations, data, data dictionary)


### Key Project Links
* [Course project requirements](other/project.md)
* [Public data sources](other/public_data.md)
* [Kaggle competitions](http://www.kaggle.com/)
* [Examples of student projects](https://github.com/justmarkham/DAT-project-examples)
* [Peer review guidelines](other/peer_review.md)


### Logistics
* Office hours will take place every Saturday and Sunday.
* Homework will be assigned every Wednesday and due on Monday, and you'll receive feedback by Wednesday.
* Our primary tool for out-of-class communication will be a private chat room through [Slack](https://slack.com/).


### Submission Forms
* [Homework submission form](http://bit.ly/dat5homework) (also for project submissions)
    * [Gist](https://gist.github.com/) is an easy way to put your homework online
* [Feedback submission form](http://bit.ly/dat5feedback) (at the end of every class)


### Before the Course Begins
* Install the [Anaconda distribution](http://continuum.io/downloads) of Python 2.7x.
* Install [Git](http://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and create a [GitHub](https://github.com/) account.
* Once you receive an email invitation from Slack, join our "DAT5 team" and add your photo.
* Choose a [Python workshop](https://generalassemb.ly/education?format=classes-workshops) to attend, depending upon your current skill level:
    * Beginner: [Saturday 3/7 10am-2pm](https://generalassemb.ly/education/introduction-to-python-programming/washington-dc/11137) or [Thursday 3/12 6:30pm-9pm](https://generalassemb.ly/education/introduction-to-python-programming/washington-dc/11136)
    * Intermediate: [Saturday 3/14 10am-2pm](https://generalassemb.ly/education/python-for-data-science-intermediate/washington-dc/11167)
* Practice your Python using the resources below.


### Python Resources
* [Codecademy's Python course](http://www.codecademy.com/en/tracks/python): Good beginner material, including tons of in-browser exercises.
* [DataQuest](https://dataquest.io/missions): Similar interface to Codecademy, but focused on teaching Python in the context of data science.
* [Google's Python Class](https://developers.google.com/edu/python/): Slightly more advanced, including hours of useful lecture videos and downloadable exercises (with solutions).
* [A Crash Course in Python for Scientists](http://nbviewer.ipython.org/gist/rpmuller/5920182): Read through the Overview section for a quick introduction to Python.
* [Python for Informatics](http://www.pythonlearn.com/book.php): A very beginner-oriented book, with associated [slides](https://drive.google.com/folderview?id=0B7X1ycQalUnyal9yeUx3VW81VDg&usp=sharing) and [videos](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj4JXIwMwN1_ss1Tk8wZShEJ).
* Code from our [beginner](code/00_python_beginner_workshop.py) and [intermediate](code/00_python_intermediate_workshop.py) workshops: Useful for review and reference.


-----

### Class 1: Introduction and Python
* Introduction to General Assembly
* Course overview ([slides](slides/01_course_overview.pdf))
* Brief tour of Slack
* Checking the setup of your laptop
* Python lesson with [airline safety data](https://github.com/fivethirtyeight/data/tree/master/airline-safety) ([code](code/01_reading_files.py))

**Homework:**
* Python exercises with [Chipotle order data](https://github.com/TheUpshot/chipotle) (listed at bottom of [code](code/01_reading_files.py) file)
* Work through GA's excellent introductory [command line tutorial](http://generalassembly.github.io/prework/command-line/#/) and then take this brief [quiz](https://gahub.typeform.com/to/J6xirf).
* Read through the [course project requirements](other/project.md) and start thinking about your own project!

**Optional:**
* If we discovered any setup issues with your laptop, please resolve them before Monday.
* If you're not feeling comfortable in Python, keep practicing using the resources above!


-----

### Class 2: Git and Command Line
* Command line ([slides](https://github.com/justmarkham/DAT5/blob/master/slides/02_Introduction_to_the_Command_Line.md))
* Git and GitHub ([slides](https://github.com/justmarkham/DAT5/blob/master/slides/02_git_github.pdf))
* Any initial questions about the course project?

**Homework:**
* **Note**:  This homework is not due until Monday.
* Command line exercises with [SMS Spam Data](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection) (listed at the bottom of [Introduction to the command Line](https://github.com/justmarkham/DAT5/blob/master/slides/02_Introduction_to_the_Command_Line.md)

**Optional:**
* Browse through some [example student projects](https://github.com/justmarkham/DAT-project-examples) to stimulate your thinking and give you a sense of project scope.

**Resources:**
* This [Command Line Primer[(http://lifehacker.com/5633909/who-needs-a-mouse-learn-to-use-the-command-line-for-almost-anything) goes a bit more into command line scripting.
* Read the first two chapters of [Pro Git](http://git-scm.com/book/en/v2) to gain a much deeper understanding of version control and basic Git commands.
* Watch [Introduction to Git and GitHub](https://www.youtube.com/playlist?list=PL5-da3qGB5IBLMp7LtN8Nc3Efd4hJq0kD) (36 minutes) for a quick review of a lot of today's material.
* [GitRef](http://gitref.org/) is an excellent reference guide for Git commands, and [Git quick reference for beginners](http://www.dataschool.io/git-quick-reference-for-beginners/) is a shorter guide with commands grouped by workflow.
* The [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) covers standard Markdown and a bit of "[GitHub Flavored Markdown](https://help.github.com/articles/github-flavored-markdown/)."
