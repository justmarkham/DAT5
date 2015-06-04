## DAT5 Course Repository

Course materials for [General Assembly's Data Science course](https://generalassemb.ly/education/data-science/washington-dc/) in Washington, DC (3/18/15 - 6/3/15).

**Instructors:** Kevin Markham and Brandon Burroughs

Monday | Wednesday
--- | ---
 | 3/18: Introduction and Python
3/23: Git and Command Line | 3/25: Exploratory Data Analysis
**3/30:** Visualization and APIs | 4/1: Machine Learning and KNN
**4/6:** Bias-Variance and Model Evaluation | 4/8: Kaggle Titanic
4/13: Web Scraping, Tidy Data, Reproducibility | 4/15: Linear Regression
4/20: Logistic Regression and Confusion Matrices | 4/22: ROC and Cross-Validation
**4/27:** Project Presentation #1 | 4/29: Naive Bayes
5/4: Natural Language Processing | 5/6: Kaggle Stack Overflow
5/11: Decision Trees | 5/13: Ensembles
**5/18:** Clustering and Regularization | 5/20: Advanced scikit-learn and Regex
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
* To learn more Pandas, review this [three-part tutorial](http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/), or review these two excellent (but extremely long) notebooks on Pandas: [introduction](http://nbviewer.ipython.org/github/fonnesbeck/Bios8366/blob/master/notebooks/Section2_5-Introduction-to-Pandas.ipynb) and [data wrangling](http://nbviewer.ipython.org/github/fonnesbeck/Bios8366/blob/master/notebooks/Section2_6-Data-Wrangling-with-Pandas.ipynb).
* Read [How Software in Half of NYC Cabs Generates $5.2 Million a Year in Extra Tips](http://iquantny.tumblr.com/post/107245431809/how-software-in-half-of-nyc-cabs-generates-5-2) for an excellent example of exploratory data analysis.


-----

### Class 4: Visualization and APIs
* Visualization ([slides](slides/04_visualization.pdf) and [code](code/04_visualization.py))
* APIs ([slides](slides/04_apis.pdf) and [code](code/04_apis.py))

**Homework:**
* Visualization practice with [Automobile MPG Data](https://archive.ics.uci.edu/ml/datasets/Auto+MPG) (listed at the bottom of [the visualization code](code/04_visualization.py)) ([solution](homework/04_visualization_hw_soln.py))
* **Note**:  This homework isn't due until Monday.

**Optional:**
* Watch [Look at Your Data](https://www.youtube.com/watch?v=coNDCIMH8bk) (18 minutes) for an excellent example of why visualization is useful for understanding your data.

**Resources:**
* For more on Pandas plotting, read this [notebook](http://nbviewer.ipython.org/github/fonnesbeck/Bios8366/blob/master/notebooks/Section2_7-Plotting-with-Pandas.ipynb) or the [visualization page](http://pandas.pydata.org/pandas-docs/stable/visualization.html) from the official Pandas documentation.
* To learn how to customize your plots further, browse through this [notebook on matplotlib](http://nbviewer.ipython.org/github/fonnesbeck/Bios8366/blob/master/notebooks/Section2_4-Matplotlib.ipynb) or this [similar notebook](http://nbviewer.ipython.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb).
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
* [Reading assignment on the bias-variance tradeoff](homework/06_bias_variance.md)
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
* Exploring the bias-variance tradeoff ([notebook](notebooks/06_bias_variance.ipynb))
* Discussion of the [assigned reading](homework/06_bias_variance.md) on the bias-variance tradeoff
* Model evaluation procedures ([notebook](notebooks/06_model_evaluation_procedures.ipynb))

**Resources:**
* If you would like to learn the IPython Notebook, the official [Notebook tutorials](http://nbviewer.ipython.org/github/ipython/ipython/blob/master/examples/Notebook/Index.ipynb) are useful.
* To get started with Seaborn for visualization, the official website has a series of [tutorials](http://web.stanford.edu/~mwaskom/software/seaborn/tutorial.html) and an [example gallery](http://web.stanford.edu/~mwaskom/software/seaborn/examples/index.html).
* Hastie and Tibshirani have an excellent [video](https://www.youtube.com/watch?v=_2ij6eaaSl0&t=2m34s) (12 minutes, starting at 2:34) that covers training error versus testing error, the bias-variance tradeoff, and train/test split (which they call the "validation set approach").
* Caltech's Learning From Data course includes a fantastic [video](http://work.caltech.edu/library/081.html) (15 minutes) that may help you to visualize bias and variance.


-----

### Class 7: Kaggle Titanic
* Guest instructor: [Josiah Davis](https://generalassemb.ly/instructors/josiah-davis/3315)
* Participate in Kaggle's [Titanic competition](http://www.kaggle.com/c/titanic-gettingStarted)
    * Work in pairs, but the goal is for every person to make at least one submission by the end of the class period!

**Homework:**
* Option 1 is to do the [Glass identification homework](homework/07_glass_identification.md). This is a good option if you are still getting comfortable with what we have learned so far, and prefer a very structured assignment. ([solution](code/07_glass_id_homework_solution.py))
* Option 2 is to keep working on the Titanic competition, and see if you can make some additional progress! This is a good assignment if you are feeling comfortable with the material and want to learn a bit more on your own.
* In either case, please submit your code as usual, and include lots of code comments!


-----

### Class 8: Web Scraping, Tidy Data, Reproducibility
* Web scraping ([slides](slides/08_web_scraping.pdf) and [code](code/08_web_scraping.py))
    * [HTML Tree](http://www.openbookproject.net/tutorials/getdown/css/images/lesson4/HTMLDOMTree.png)
* Tidy data:
    * [Introduction](http://stat405.had.co.nz/lectures/18-tidy-data.pdf)
    * Example datasets: [Bob Ross](https://github.com/fivethirtyeight/data/blob/master/bob-ross/elements-by-episode.csv), [NFL ticket prices](https://github.com/fivethirtyeight/data/blob/master/nfl-ticket-prices/2014-average-ticket-price.csv), [airline safety](https://github.com/fivethirtyeight/data/blob/master/airline-safety/airline-safety.csv), [Jets ticket prices](https://github.com/fivethirtyeight/data/blob/master/nfl-ticket-prices/jets-buyer.csv), [Chipotle orders](https://github.com/TheUpshot/chipotle/blob/master/orders.tsv)
* Reproducibility:
    * [Introduction](http://www.dataschool.io/reproducibility-is-not-just-for-researchers/), [Tweet](https://twitter.com/jakevdp/status/519563939177197571)
    * [Components of reproducible analysis](https://github.com/jtleek/datasharing)
    * Examples: [Classic rock](https://github.com/fivethirtyeight/data/tree/master/classic-rock), [student project 1](https://github.com/jwknobloch/DAT4_final_project), [student project 2](https://github.com/justmarkham/DAT4-students/tree/master/Jonathan_Bryan/Project_Files)

**Resources:**
* This [web scraping tutorial from Stanford](http://web.stanford.edu/~zlotnick/TextAsData/Web_Scraping_with_Beautiful_Soup.html) provides an example of getting a list of items.
* If you want to learn more about tidy data, [Hadley Wickham's paper](http://www.jstatsoft.org/v59/i10/paper) has a lot of nice examples.
* If your co-workers tend to create spreadsheets that are [unreadable by computers](https://bosker.wordpress.com/2014/12/05/the-government-statistical-services-terrible-spreadsheet-advice/), perhaps they would benefit from reading this list of [tips for releasing data in spreadsheets](http://www.clean-sheet.org/). (There are some additional suggestions in this [answer](http://stats.stackexchange.com/questions/83614/best-practices-for-creating-tidy-data/83711#83711) from Cross Validated.)
* Here's [Colbert on reproducibility](http://thecolbertreport.cc.com/videos/dcyvro/austerity-s-spreadsheet-error) (8 minutes).


-----

### Class 9: Linear Regression
* Linear regression ([notebook](notebooks/09_linear_regression.ipynb))
    * Simple linear regression
    * Estimating and interpreting model coefficients
    * Confidence intervals
    * Hypothesis testing and p-values
    * R-squared
    * Multiple linear regression
    * Feature selection
    * Model evaluation metrics for regression
    * Handling categorical predictors

**Homework:**
* If you're behind on homework, use this time to catch up.
* Keep working on your project... your first presentation is in less than two weeks!!

**Resources:**
* To go much more in-depth on linear regression, read Chapter 3 of [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/), from which this lesson was adapted. Alternatively, watch the [related videos](http://www.dataschool.io/15-hours-of-expert-machine-learning-videos/) or read my [quick reference guide](http://www.dataschool.io/applying-and-interpreting-linear-regression/) to the key points in that chapter.
* To learn more about Statsmodels and how to interpret the output, DataRobot has some decent posts on [simple linear regression](http://www.datarobot.com/blog/ordinary-least-squares-in-python/) and [multiple linear regression](http://www.datarobot.com/blog/multiple-regression-using-statsmodels/).
* This [introduction to linear regression](http://people.duke.edu/~rnau/regintro.htm) is much more detailed and mathematically thorough, and includes lots of good advice.
* This is a relatively quick post on the [assumptions of linear regression](http://pareonline.net/getvn.asp?n=2&v=8).


-----

### Class 10: Logistic Regression and Confusion Matrices
* Logistic regression ([slides](slides/10_logistic_regression_confusion_matrix.pdf) and [code](code/10_logistic_regression_confusion_matrix.py))
* Confusion matrices (same links as above)

**Homework:**
* Video assignment on [ROC Curves and Area Under the Curve](homework/11_roc_auc.md)
* Review the notebook from class 6 on [model evaluation procedures](notebooks/06_model_evaluation_procedures.ipynb)

**Resources:**
* For more on logistic regression, watch the [first three videos](https://www.youtube.com/playlist?list=PL5-da3qGB5IC4vaDba5ClatUmFppXLAhE) (30 minutes total) from Chapter 4 of An Introduction to Statistical Learning.
* UCLA's IDRE has a handy table to help you remember the [relationship between probability, odds, and log-odds](http://www.ats.ucla.edu/stat/mult_pkg/faq/general/odds_ratio.htm).
* Better Explained has a very friendly introduction (with lots of examples) to the [intuition behind "e"](http://betterexplained.com/articles/an-intuitive-guide-to-exponential-functions-e/).
* Here are some useful lecture notes on [interpreting logistic regression coefficients](http://www.unm.edu/~schrader/biostat/bio2/Spr06/lec11.pdf).
* Kevin wrote a [simple guide to confusion matrix terminology](http://www.dataschool.io/simple-guide-to-confusion-matrix-terminology/) that you can use as a reference guide.


-----

### Class 11: ROC Curves and Cross-Validation
* ROC curves and Area Under the Curve
    * Discuss the [video assignment](homework/11_roc_auc.md)
    * Exercise: [drawing an ROC curve](slides/11_drawing_roc.pdf)
    * Calculating AUC and plotting an ROC curve ([notebook](notebooks/11_roc_auc.ipynb))
* Cross-validation ([notebook](notebooks/11_cross_validation.ipynb))
* Discuss this article on [Smart Autofill for Google Sheets](http://googleresearch.blogspot.com/2014/10/smart-autofill-harnessing-predictive.html)

**Homework:**
* Your first [project presentation](other/project.md) is on Monday! Please submit a link to your project repository (with slides, code, and visualizations) before class using the homework submission form.

**Optional:**
* Titanic exercise ([notebook](notebooks/11_titanic_exercise.ipynb))

**Resources:**
* scikit-learn has extensive documentation on [model evaluation](http://scikit-learn.org/stable/modules/model_evaluation.html).
* For more on cross-validation, read section 5.1 of [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/) (11 pages) or watch the related videos: [K-fold and leave-one-out cross-validation](https://www.youtube.com/watch?v=nZAM5OXrktY) (14 minutes), [cross-validation the right and wrong ways](https://www.youtube.com/watch?v=S06JpVoNaA0) (10 minutes).


-----

### Class 12: Project Presentation #1
* Project presentations!

**Homework:**
* Read these [Introduction to Probability](https://docs.google.com/presentation/d/1cM2dVbJgTWMkHoVNmYlB9df6P2H8BrjaqAcZTaLe9dA/edit#slide=id.gfc3caad2_00) slides (from the [OpenIntro Statistics textbook](https://www.openintro.org/stat/textbook.php)) and try the included quizzes. Pay specific attention to the following terms: probability, sample space, mutually exclusive, independent.
* Reading assignment on [spam filtering](homework/13_spam_filtering.md).


-----

### Class 13: Naive Bayes
* Conditional probability and Bayes' theorem
    * [Slides](slides/13_bayes_theorem.pdf) (adapted from [Visualizing Bayes' theorem](http://oscarbonilla.com/2009/05/visualizing-bayes-theorem/))
    * [Visualization of conditional probability](http://setosa.io/conditional/)
    * Applying Bayes' theorem to iris classification ([notebook](notebooks/13_bayes_iris.ipynb))
* Naive Bayes classification
    * [Slides](slides/13_naive_bayes.pdf)
    * Example with spam email ([notebook](notebooks/13_naive_bayes_spam.ipynb))
    * Discuss the reading assignment on [spam filtering](homework/13_spam_filtering.md)
    * [Airport security example](http://www.quora.com/In-laymans-terms-how-does-Naive-Bayes-work/answer/Konstantin-Tt)
    * Classifying [SMS messages](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection) ([code](code/13_naive_bayes.py))

**Homework:**
* Please download/install the following for the NLP class on Monday
    * In Spyder, `import nltk` and run `nltk.download('all')`.  This downloads all of the necessary resources for the Natural Language Tool Kit.
    * We'll be using two new packages/modules for this class:  textblob and lda.  Please install them.  **Hint**:  In the Terminal (Mac) or Git Bash (Windows), run `pip install textblob` and `pip install lda`.

**Resources:**
* For other intuitive introductions to Bayes' theorem, here are two good blog posts that use [ducks](https://planspacedotorg.wordpress.com/2014/02/23/bayes-rule-for-ducks/) and [legos](http://www.countbayesie.com/blog/2015/2/18/bayes-theorem-with-lego).
* For more on conditional probability, these [slides](https://docs.google.com/presentation/d/1psUIyig6OxHQngGEHr3TMkCvhdLInnKnclQoNUr4G4U/edit#slide=id.gfc69f484_00) may be useful.
* For more details on Naive Bayes classification, Wikipedia has two excellent articles ([Naive Bayes classifier](http://en.wikipedia.org/wiki/Naive_Bayes_classifier) and [Naive Bayes spam filtering](http://en.wikipedia.org/wiki/Naive_Bayes_spam_filtering)), and Cross Validated has a good [Q&A](http://stats.stackexchange.com/questions/21822/understanding-naive-bayes).
* If you enjoyed Paul Graham's article, you can read [his follow-up article](http://www.paulgraham.com/better.html) on how he improved his spam filter and this [related paper](http://www.merl.com/publications/docs/TR2004-091.pdf) about state-of-the-art spam filtering in 2004.
* If you're planning on using text features in your project, it's worth exploring the different types of [Naive Bayes](http://scikit-learn.org/stable/modules/naive_bayes.html) and the many options for [CountVectorizer](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html).


-----

### Class 14: Natural Language Processing
* Natural Language Processing ([notebook](notebooks/14_nlp.ipynb))
* NLTK: tokenization, stemming, lemmatization, part of speech tagging, stopwords, Named Entity Recognition, LDA
* Alternative: TextBlob

**Resources:**
* [Natural Language Processing with Python](http://www.nltk.org/book/): free online book to go in-depth with NLTK
* [NLP online course](https://www.coursera.org/course/nlp): no sessions are available, but [video lectures](https://class.coursera.org/nlp/lecture) and [slides](http://web.stanford.edu/~jurafsky/NLPCourseraSlides.html) are still accessible
* [Brief slides](http://files.meetup.com/7616132/DC-NLP-2013-09%20Charlie%20Greenbacker.pdf) on the major task areas of NLP
* [Detailed slides](https://github.com/ga-students/DAT_SF_9/blob/master/16_Text_Mining/DAT9_lec16_Text_Mining.pdf) on a lot of NLP terminology
* [A visual survey of text visualization techniques](http://textvis.lnu.se/): for exploration and inspiration
* [DC Natural Language Processing](http://www.meetup.com/DC-NLP/): active Meetup group
* [Stanford CoreNLP](http://nlp.stanford.edu/software/corenlp.shtml): suite of tools if you want to get serious about NLP
* Getting started with regex: [Python introductory lesson](https://developers.google.com/edu/python/regular-expressions) and [reference guide](https://github.com/justmarkham/DAT3/blob/master/code/99_regex_reference.py), [real-time regex tester](https://regex101.com/#python), [in-depth tutorials](http://www.rexegg.com/)
* [A good explanation of LDA](http://www.quora.com/What-is-a-good-explanation-of-Latent-Dirichlet-Allocation)
* [Textblob documentation](http://textblob.readthedocs.org/en/dev/)
* [SpaCy](http://honnibal.github.io/spaCy/): a new NLP package


-----

### Class 15: Kaggle Stack Overflow
* Overview of how Kaggle works ([slides](slides/15_kaggle.pdf))
* Kaggle In-Class competition: [Predict whether a Stack Overflow question will be closed](https://inclass.kaggle.com/c/dat5-stack-overflow) ([code](code/15_kaggle.py))

**Optional:**
* Keep working on this competition! You can make up to 5 submissions per day, and the competition doesn't close until 6:30pm ET on Wednesday, May 27 (class 20).

**Resources:**
* For a great overview of the diversity of problems tackled by Kaggle competitions, watch [Kaggle Transforms Data Science Into Competitive Sport](https://www.youtube.com/watch?v=8w4UY66GKcM) (28 minutes) by Jeremy Howard (past president of Kaggle).
* [Getting in Shape for the Sport of Data Science](https://www.youtube.com/watch?v=kwt6XEh7U3g) (74 minutes), also by Jeremy Howard, contains a lot of tips for competitive machine learning.
* [Learning from the best](http://blog.kaggle.com/2014/08/01/learning-from-the-best/) is an excellent blog post covering top tips from Kaggle Masters on how to do well on Kaggle.
* [Feature Engineering Without Domain Expertise](https://www.youtube.com/watch?v=bL4b1sGnILU) (17 minutes), a talk by Kaggle Master Nick Kridler, provides some simple advice about how to iterate quickly and where to spend your time during a Kaggle competition.
* Kevin's [project presentation video](https://www.youtube.com/watch?v=HGr1yQV3Um0) (16 minutes) gives a nice tour of the end-to-end machine learning process for a Kaggle competition. (Or, just check out the [slides](https://speakerdeck.com/justmarkham/allstate-purchase-prediction-challenge-on-kaggle).)


-----

### Class 16: Decision Trees
* Decision trees ([notebook](notebooks/16_decision_trees.ipynb))

**Resources:**
* scikit-learn documentation: [Decision Trees](http://scikit-learn.org/stable/modules/tree.html)

**Installing Graphviz (optional):**
* Mac:
    * [Download and install PKG file](http://www.graphviz.org/Download_macos.php)
* Windows:
    * [Download and install MSI file](http://www.graphviz.org/Download_windows.php)
    * **Add it to your Path:** Go to Control Panel, System, Advanced System Settings, Environment Variables. Under system variables, edit "Path" to include the path to the "bin" folder, such as: `C:\Program Files (x86)\Graphviz2.38\bin`


-----

### Class 17: Ensembles
* Ensembles and random forests ([notebook](notebooks/17_ensembling.ipynb))

**Homework:**
* Your [project draft](other/project.md#may-18-first-draft-due) is due on Monday! Please submit a link to your project repository (with paper, code, and visualizations) before class using the homework submission form.
    * Your peers and your instructors will be giving you feedback on your project draft.
    * Here's an example of a great [final project paper](https://github.com/justmarkham/DAT-project-examples/blob/master/pdf/nba_paper.pdf) from a past student.
* Make at least one new submission to our [Kaggle competition](https://inclass.kaggle.com/c/dat5-stack-overflow)! We suggest trying Random Forests or building your own ensemble of models. For assistance, you could use this [framework code](code/17_ensembling_exercise.py), or refer to the [complete code](code/15_kaggle.py) from class 15. You can optionally submit your code to us if you want feedback.

**Resources:**
* scikit-learn documentation: [Ensembles](http://scikit-learn.org/stable/modules/ensemble.html)
* Quora: [How do random forests work in layman's terms?](http://www.quora.com/How-do-random-forests-work-in-laymans-terms/answer/Edwin-Chen-1)


-----

### Class 18: Clustering and Regularization
* Clustering ([slides](slides/18_clustering.pdf) and [code](code/18_clustering.py))
* Regularization ([notebook](notebooks/18_regularization.ipynb) and [code](code/18_regularization.py))

**Homework:**
* You will be assigned to review the project drafts of two of your peers. You have until next Monday to provide them with feedback, according to [these guidelines](other/peer_review.md).

**Resources:**
* [Introduction to Data Mining](http://www-users.cs.umn.edu/~kumar/dmbook/index.php) has a thorough [chapter on cluster analysis](http://www-users.cs.umn.edu/~kumar/dmbook/ch8.pdf).
* The scikit-learn user guide has a nice [section on clustering](http://scikit-learn.org/stable/modules/clustering.html).
* Wikipedia article on [determining the number of clusters](http://en.wikipedia.org/wiki/Determining_the_number_of_clusters_in_a_data_set).
* This [K-means clustering visualization](http://shiny.rstudio.com/gallery/kmeans-example.html) allows you to set different numbers of clusters for the iris data, and this [other visualization](http://asa.1gb.ru/kmeans/1.html) allows you to see the effects of different initial positions for the centroids.
* Fun examples of clustering: [A Statistical Analysis of the Work of Bob Ross](http://fivethirtyeight.com/features/a-statistical-analysis-of-the-work-of-bob-ross/) (with [data and Python code](https://github.com/fivethirtyeight/data/tree/master/bob-ross)), [How a Math Genius Hacked OkCupid to Find True Love](http://www.wired.com/2014/01/how-to-hack-okcupid/all/), and [characteristics of your zip code](http://www.esri.com/landing-pages/tapestry/).
* An Introduction to Statistical Learning has useful videos on [K-means clustering](https://www.youtube.com/watch?v=aIybuNt9ps4&list=PL5-da3qGB5IBC-MneTc9oBZz0C6kNJ-f2&index=3) (17 minutes), [ridge regression](https://www.youtube.com/watch?v=cSKzqb0EKS0&list=PL5-da3qGB5IB-Xdpj_uXJpLGiRfv9UVXI&index=6) (13 minutes), and [lasso regression](https://www.youtube.com/watch?v=A5I1G1MfUmA&index=7&list=PL5-da3qGB5IB-Xdpj_uXJpLGiRfv9UVXI) (15 minutes).
* Caltech's Learning From Data course has a great video introducing [regularization](http://work.caltech.edu/library/121.html) (8 minutes) that builds upon their video about the [bias-variance tradeoff](http://work.caltech.edu/library/081.html).
* Here is a longer example of [feature scaling](http://nbviewer.ipython.org/github/rasbt/pattern_classification/blob/master/preprocessing/about_standardization_normalization.ipynb) in scikit-learn, with additional discussion of the types of scaling you can use.
* [Clever Methods of Overfitting](http://hunch.net/?p=22) is a classic post by John Langford.


-----

### Class 19: Advanced scikit-learn and Regular Expressions
* Advanced scikit-learn ([code](code/19_advanced_sklearn.py))
    * Searching for optimal parameters: [GridSearchCV](http://scikit-learn.org/stable/modules/grid_search.html)
        * [Exercise](code/19_gridsearchcv_exercise.py)
    * Standardization of features: [StandardScaler](http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)
    * Chaining steps: [Pipeline](http://scikit-learn.org/stable/modules/pipeline.html)
* Regular expressions ("regex")
    * Motivating example: [data](data/homicides.txt), [code](code/19_regex_exercise.py)
    * Reference guide: [code](code/19_regex_reference.py)

**Optional:**
* Use regular expressions to create a list of causes from the homicide data. Your list should look like this: `['shooting', 'shooting', 'blunt force', ...]`. If the cause is not listed for a particular homicide, include it in the list as `'unknown'`.

**Resources:**
* scikit-learn has an incredibly active [mailing list](https://www.mail-archive.com/scikit-learn-general@lists.sourceforge.net/index.html) that is often much more useful than Stack Overflow for researching a particular function.
* The scikit-learn documentation includes a [machine learning map](http://scikit-learn.org/stable/tutorial/machine_learning_map/) that may help you to choose the "best" model for your task.
* In you want to build upon the regex material presented in today's class, Google's Python Class includes an excellent [lesson](https://developers.google.com/edu/python/regular-expressions) (with an associated [video](https://www.youtube.com/watch?v=kWyoYtvJpe4&index=4&list=PL5-da3qGB5IA5NwDxcEJ5dvt8F9OQP7q5)).
* [regex101](https://regex101.com/#python) is an online tool for testing your regular expressions in real time.
* If you want to go really deep with regular expressions, [RexEgg](http://www.rexegg.com/) includes endless articles and tutorials.
* [Exploring Expressions of Emotions in GitHub Commit Messages](http://geeksta.net/geeklog/exploring-expressions-emotions-github-commit-messages/) is a fun example of how regular expressions can be used for data analysis.


-----

### Class 20: Databases and SQL
* Databases and SQL ([slides](slides/20_sql.pdf) and [code](code/20_sql.py))

**Homework:**
* Read this classic paper, which may help you to connect many of the topics we have studied throughout the course: [A Few Useful Things to Know about Machine Learning](http://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf).
* Your [final project](other/project.md#june-3-project-presentation-2) is due next Wednesday!
    * Please submit a link to your project repository before Wednesday's class using the homework submission form.
    * Your presentation should start with a recap of the key information from the previous presentation, but you should spend most of your presentation discussing what has happened since then.
    * Don't forget to practice your presentation and time yourself!

**Resources:**
* [SQLZOO](http://sqlzoo.net/wiki/SQL_Tutorial), [Mode Analytics](http://sqlschool.modeanalytics.com/), and [Code School](http://campus.codeschool.com/courses/try-sql/contents) all have online SQL tutorials that look promising.
* [w3schools](http://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all) has a sample database that allows you to practice your SQL.
* [10 Easy Steps to a Complete Understanding of SQL](http://tech.pro/tutorial/1555/10-easy-steps-to-a-complete-understanding-of-sql) is a good article for those who have some SQL experience and want to understand it at a deeper level.
* [A Comparison Of Relational Database Management Systems](https://www.digitalocean.com/community/tutorials/sqlite-vs-mysql-vs-postgresql-a-comparison-of-relational-database-management-systems) gives the pros and cons of SQLite, MySQL, and PostgreSQL.
* If you want to go deeper into databases and SQL, Stanford has a well-respected series of [14 mini-courses](https://lagunita.stanford.edu/courses/DB/2014/SelfPaced/about).


-----

### Class 21: Course Review
* Pipelines ([code](code/19_advanced_sklearn.py))
* Class review
* Creating an ensemble ([code](code/21_ensembles_example.py))

**Resources:**
* [Data science review](https://docs.google.com/document/d/1XCdyrsQwU5OC5os7RHdVTEtS-tpHBbsoKKWLpYI6Svo/edit?usp=sharing): A summary of key concepts from the Data Science course.
* [Comparing supervised learning algorithms](https://docs.google.com/spreadsheets/d/15_QJXm6urctsbIXO-C_eXrsSffbHedio8z0E5ozxO-M/edit?usp=sharing): Kevin's table comparing the machine learning models we studied in the course.
* [Choosing a Machine Learning Classifier](http://blog.echen.me/2011/04/27/choosing-a-machine-learning-classifier/): Edwin Chen's short and highly readable guide.
* [Machine Learning Done Wrong](http://ml.posthaven.com/machine-learning-done-wrong) and [Common Pitfalls in Machine Learning](http://danielnee.com/?p=155): Thoughtful advice on common mistakes to avoid in machine learning.
* [Practical machine learning tricks from the KDD 2011 best industry paper](http://blog.david-andrzejewski.com/machine-learning/practical-machine-learning-tricks-from-the-kdd-2011-best-industry-paper/): More advanced advice than the resources above.
* [An Empirical Comparison of Supervised Learning Algorithms](http://www.cs.cornell.edu/~caruana/ctp/ct.papers/caruana.icml06.pdf): Research paper from 2006.
* [Many more resources for continued learning!](other/resources.md)


-----

### Class 22: Project Presentation #2
* Presentations!
 
**Class is over!  What should I do now?**
* Take a break!
* Go back through class notes/code/videos to make sure you feel comfortable with what we've learned.
* Take a look at the **Resources** for each class to get a deeper understanding of what we've learned.  Start with the **Resources** from Class 21 and move to topics you are most interested in.
* You might not realize it, but you are at a point where you can continue learning on your own.  You have all of the skills necessary to read papers, blogs, documentation, etc.
* GA Data Guild
 * [8/24/2015](https://generalassemb.ly/education/data-science-guild/washington-dc/13274)
 * [9/21/2015](https://generalassemb.ly/education/data-science-guild/washington-dc/13275)
 * [10/19/2015](https://generalassemb.ly/education/data-science-guild/washington-dc/13276)
 * [11/9/2015](https://generalassemb.ly/education/data-science-guild/washington-dc/13277)
* Follow data scientists on Twitter.  This will help you stay up on the latest news/models/applications/tools.
* Participate in [Data Community DC](http://www.datacommunitydc.org/) events.  They sponsor meetups, workshops, etc, notably the [Data Science DC Meetup](http://www.meetup.com/Data-Science-DC/).  Sign up for their [newsletter](http://www.datacommunitydc.org/newsletter/) also!
* Read blogs to keep learning.  I really like [District Data Labs](http://districtdatalabs.silvrback.com/).
* Do Kaggle competitions!  This is a good way to continue and hone your skillset.  Plus, you'll learn a ton along the way.

And finally, don't forget about [graduation](https://generalassemb.ly/education/graduation-april-may-june-courses/washington-dc/12892)!
