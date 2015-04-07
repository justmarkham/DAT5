## DAT5 Course Repository

Course materials for [General Assembly's Data Science course](https://generalassemb.ly/education/data-science/washington-dc/) in Washington, DC (3/18/15 - 6/3/15).

**Instructors:** Kevin Markham and Brandon Burroughs

Monday | Wednesday
--- | ---
 | 3/18: Introduction and Python
3/23: Git and Command Line | 3/25: Exploratory Data Analysis
**3/30:** Visualization and APIs | 4/1: Machine Learning and KNN
**4/6:** Bias-Variance and Model Evaluation | 4/8: Kaggle Titanic (Part 1)
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
* Python exercises with [Chipotle order data](https://github.com/TheUpshot/chipotle) (listed at bottom of [code](code/01_reading_files.py) file) ([solution](code/01_chipotle_homework_solution.py))
* Work through GA's excellent introductory [command line tutorial](http://generalassembly.github.io/prework/command-line/#/) and then take this brief [quiz](https://gahub.typeform.com/to/J6xirf).
* Read through the [course project requirements](other/project.md) and start thinking about your own project!

**Optional:**
* If we discovered any setup issues with your laptop, please resolve them before Monday.
* If you're not feeling comfortable in Python, keep practicing using the resources above!


-----

### Class 2: Git and Command Line
* Any questions about the course project?
* Command line ([slides](slides/02_Introduction_to_the_Command_Line.md))
* Git and GitHub ([slides](slides/02_git_github.pdf))

**Homework:**
* Command line exercises with [SMS Spam Data](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection) (listed at the bottom of [Introduction to the Command Line](slides/02_Introduction_to_the_Command_Line.md)) ([solution](homework/02_command_line_hw_soln.md))
* **Note**: This homework is not due until Monday. You might want to create a GitHub repo for your homework instead of using Gist!

**Optional:**
* Browse through some [example student projects](https://github.com/justmarkham/DAT-project-examples) to stimulate your thinking and give you a sense of project scope.

**Resources:**
* This [Command Line Primer](http://lifehacker.com/5633909/who-needs-a-mouse-learn-to-use-the-command-line-for-almost-anything) goes a bit more into command line scripting.
* Read the first two chapters of [Pro Git](http://git-scm.com/book/en/v2) to gain a much deeper understanding of version control and basic Git commands.
* Watch [Introduction to Git and GitHub](https://www.youtube.com/playlist?list=PL5-da3qGB5IBLMp7LtN8Nc3Efd4hJq0kD) (36 minutes) for a quick review of a lot of today's material.
* [GitRef](http://gitref.org/) is an excellent reference guide for Git commands, and [Git quick reference for beginners](http://www.dataschool.io/git-quick-reference-for-beginners/) is a shorter guide with commands grouped by workflow.
* The [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) covers standard Markdown and a bit of "[GitHub Flavored Markdown](https://help.github.com/articles/github-flavored-markdown/)."


-----

### Class 3: Pandas
* Pandas for data exploration, analysis, and visualization ([code](code/03_exploratory_analysis_pandas.py))
    * [Split-Apply-Combine](http://i.imgur.com/yjNkiwL.png) pattern
    * Simple examples of [joins in Pandas](http://www.gregreda.com/2013/10/26/working-with-pandas-dataframes/#joining)

**Homework:**
* Pandas practice with [Automobile MPG Data](https://archive.ics.uci.edu/ml/datasets/Auto+MPG) (listed at the bottom of [Exploratory Analysis in Pandas](code/03_exploratory_analysis_pandas.py)) ([solution](homework/03_pandas_hw_soln.py))
* Talk to an instructor about your project
* Don't forget about the Command line exercises (listed at the bottom of [Introduction to the Command Line](slides/02_Introduction_to_the_Command_Line.md))

**Optional:**
* To learn more Pandas, review this [three-part tutorial](http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/), or review these two excellent (but extremely long) notebooks on Pandas: [introduction](http://nbviewer.ipython.org/github/fonnesbeck/Bios366/blob/master/notebooks/Section2_5-Introduction-to-Pandas.ipynb) and [data wrangling](http://nbviewer.ipython.org/github/fonnesbeck/Bios366/blob/master/notebooks/Section2_6-Data-Wrangling-with-Pandas.ipynb).
* Read [How Software in Half of NYC Cabs Generates $5.2 Million a Year in Extra Tips](http://iquantny.tumblr.com/post/107245431809/how-software-in-half-of-nyc-cabs-generates-5-2) for an excellent example of exploratory data analysis.


-----

### Class 4: Visualization and APIs
* Visualization ([slides](slides/04_visualization.pdf) and [code](code/04_visualization.py))
* APIs ([slides](slides/04_apis.pdf) and [code](code/04_apis.py))

**Homework:**
* Visualization practice with [Automobile MPG Data](https://archive.ics.uci.edu/ml/datasets/Auto+MPG) (listed at the bottom of [the visualization code](code/04_visualization.py))
* **Note**:  This homework isn't due until Monday.

**Optional:**
* Watch [Look at Your Data](https://www.youtube.com/watch?v=coNDCIMH8bk) (18 minutes) for an excellent example of why visualization is useful for understanding your data.

**Resources:**
* For more on Pandas plotting, read this [notebook](http://nbviewer.ipython.org/github/fonnesbeck/Bios366/blob/master/notebooks/Section2_7-Plotting-with-Pandas.ipynb) or the [visualization page](http://pandas.pydata.org/pandas-docs/stable/visualization.html) from the official Pandas documentation.
* To learn how to customize your plots further, browse through this [notebook on matplotlib](http://nbviewer.ipython.org/github/fonnesbeck/Bios366/blob/master/notebooks/Section2_4-Matplotlib.ipynb) or this [similar notebook](http://nbviewer.ipython.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb).
* To explore different types of visualizations and when to use them, [Choosing a Good Chart](http://extremepresentation.typepad.com/files/choosing-a-good-chart-09.pdf) and [The Graphic Continuum](http://www.coolinfographics.com/storage/post-images/The-Graphic-Continuum-POSTER.jpg) are handy one-page references, or check out the [R Graph Catalog](http://shinyapps.stat.ubc.ca/r-graph-catalog/).
* For a more in-depth introduction to visualization, browse through these [PowerPoint slides](http://www2.research.att.com/~volinsky/DataMining/Columbia2011/Slides/Topic2-EDAViz.ppt) from Columbia's Data Mining class.
* [Mashape](https://www.mashape.com/explore) and [Apigee](https://apigee.com/providers) allow you to explore tons of different APIs. Alternatively, a [Python API wrapper](http://www.pythonforbeginners.com/api/list-of-python-apis) is available for many popular APIs.


-----

### Class 5: Data Science Workflow, Machine Learning, KNN
* Iris dataset
    * [What does an iris look like?](http://sebastianraschka.com/Images/2014_python_lda/iris_petal_sepal.png)
    * [Data](http://archive.ics.uci.edu/ml/datasets/Iris) hosted by the UCI Machine Learning Repository
    * "Human learning" exercise ([solution](code/05_iris_exercise.py))
* Introduction to data science ([slides](slides/05_intro_to_data_science.pdf))
    * [Quora: What is data science?](https://www.quora.com/What-is-data-science/answer/Michael-Hochster)
    * [Data science Venn diagram](http://drewconway.com/zia/2013/3/26/the-data-science-venn-diagram)
    * [Quora: What is the workflow of a data scientist?](http://www.quora.com/What-is-the-work-flow-or-process-of-a-data-scientist/answer/Ryan-Fox-Squire)
    * Example student project: [MetroMetric](https://github.com/justmarkham/DAT-project-examples/blob/master/pdf/bus_presentation.pdf)
* Machine learning and KNN ([slides](slides/05_machine_learning_knn.pdf))
    * [Reddit AMA with Yann LeCun](http://www.reddit.com/r/MachineLearning/comments/25lnbt/ama_yann_lecun)
    * [Characteristics of your zip code](http://www.esri.com/landing-pages/tapestry/)
* Introduction to scikit-learn ([code](code/05_sklearn_knn.py))
    * Documentation: [user guide](http://scikit-learn.org/stable/modules/neighbors.html), [module reference](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.neighbors), [class documentation](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)

**Homework:**
* Complete your visualization homework assigned in class 4
* [Reading assignment on the bias-variance tradeoff](homework/05_bias_variance.md)
* A write-up about your [project question and dataset](other/project.md) is due on Monday! ([example one](https://github.com/justmarkham/DAT4-students/blob/master/jason/jk_project_idea.md), [example two](https://github.com/justmarkham/DAT4-students/blob/master/alexlee/project_question.md))

**Optional:**
* For a useful look at the different types of data scientists, read [Analyzing the Analyzers](http://cdn.oreillystatic.com/oreilly/radarreport/0636920029014/Analyzing_the_Analyzers.pdf) (32 pages).
* For some thoughts on what it's like to be a data scientist, read these short posts from [Win-Vector](http://www.win-vector.com/blog/2012/09/on-being-a-data-scientist/) and [Datascope Analytics](http://datascopeanalytics.com/what-we-think/2014/07/31/six-qualities-of-a-great-data-scientist).
* For a fun (yet enlightening) look at the data science workflow, read [What I do when I get a new data set as told through tweets](http://simplystatistics.org/2014/06/13/what-i-do-when-i-get-a-new-data-set-as-told-through-tweets/).
* For a more in-depth introduction to data science, browse through these [PowerPoint slides](http://www2.research.att.com/~volinsky/DataMining/Columbia2011/Slides/Topic1-DMIntro.ppt) from Columbia's Data Mining class.
* For a more in-depth introduction to machine learning, read section 2.1 (14 pages) of Hastie and Tibshirani's excellent book, [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/). (It's a free PDF download!)
* For a really nice comparison of supervised versus unsupervised learning, plus an introduction to reinforcement learning, watch this [video](http://work.caltech.edu/library/014.html) (13 minutes) from Caltech's [Learning From Data](http://work.caltech.edu/telecourse.html) course.

**Resources:**
* Quora has a [data science topic FAQ](https://www.quora.com/What-is-the-Data-Science-topic-FAQ) with lots of interesting Q&A.
* Keep up with local data-related events through the Data Community DC [event calendar](http://www.datacommunitydc.org/calendar) or [weekly newsletter](http://www.datacommunitydc.org/thenewsletter/).


-----

### Class 6: Bias-Variance Tradeoff and Model Evaluation
* Brief introduction to the IPython Notebook
* Exploring the bias-variance tradeoff ([notebook](http://nbviewer.ipython.org/github/justmarkham/DAT5/blob/master/notebooks/06_bias_variance.ipynb))
* Discussion of the [assigned reading](homework/05_bias_variance.md) on the bias-variance tradeoff
* Model evaluation procedures ([notebook](http://nbviewer.ipython.org/github/justmarkham/DAT5/blob/master/notebooks/06_model_evaluation_procedures.ipynb))

**Resources:**
* If you would like to learn the IPython Notebook, the official [Notebook tutorials](http://nbviewer.ipython.org/github/ipython/ipython/blob/master/examples/Notebook/Index.ipynb) are useful.
* To get started with Seaborn for visualization, the official website has a series of [tutorials](http://web.stanford.edu/~mwaskom/software/seaborn/tutorial.html) and an [example gallery](http://web.stanford.edu/~mwaskom/software/seaborn/examples/index.html).
* Hastie and Tibshirani have an excellent [video](https://www.youtube.com/watch?v=_2ij6eaaSl0&t=2m34s) (12 minutes, starting at 2:34) that covers training error versus testing error, the bias-variance tradeoff, and train/test split (which they call the "validation set approach").
* Caltech's Learning From Data course includes a fantastic [video](http://work.caltech.edu/library/081.html) (15 minutes) that may help you to visualize bias and variance.


-----

### Class 7: Kaggle Titanic (Part 1)
* Guest instructor: [Josiah Davis](https://generalassemb.ly/instructors/josiah-davis/3315)
* Participate in Kaggle's [Titanic competition](http://www.kaggle.com/c/titanic-gettingStarted)
    * Work in pairs, but the goal is for every person to make at least one submission by the end of the class period!

**Homework:**
* Option 1 is to do the [Glass identification homework](homework/07_glass_identification.md). This is a good option if you are still getting comfortable with what we have learned so far, and prefer a very structured assignment.
* Option 2 is to keep working on the Titanic competition, and see if you can make some additional progress! This is a good assignment if you are feeling comfortable with the material and want to learn a bit more on your own.
* In either case, please submit your code as usual, and include lots of code comments!
