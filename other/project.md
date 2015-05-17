# Course Project


## Overview

The final project should represent significant original work applying data science techniques to an interesting problem. Final projects are individual attainments, but you should be talking frequently with your instructors and classmates about them.

Address a data-related problem in your professional field or a field you're interested in. Pick a subject that you're passionate about; if you're strongly interested in the subject matter it'll be more fun for you and you'll produce a better project!

To stimulate your thinking, here is an excellent list of [public data sources](public_data.md). Using public data is the most common choice. If you have access to private data, that's also an option, though you'll have to be careful about what results you can release. You are also welcome to compete in a [Kaggle competition](http://www.kaggle.com/) as your project, in which case the data will be provided to you.

You should also take a look at [past projects](https://github.com/justmarkham/DAT-project-examples) from other GA Data Science students, to get a sense of the variety and scope of projects.


## Project Milestones


### March 30: Deadline for Discussing Project Ideas with an Instructor

By March 30, you should talk with one of your instructors about your project idea(s). They can help you to choose between different project ideas, advise you on the appropriate scope for your project, and ensure that your project question might reasonably be answerable using the data science tools and techniques taught in the course.


### April 6: Project Question and Dataset

Create a GitHub repository for your project. It should include a document that answers these questions:

What is the question you hope to answer? What data are you planning to use to answer that question? What do you know about the data so far? Why did you choose this topic?

Example:
* I'm planning to predict passenger survival on the Titanic.
* I have Kaggle's Titanic dataset with 10 passenger characteristics.
* I know that many of the fields have missing values, that some of the text fields are messy and will require cleaning, and that about 38% of the passengers in the training set survive.
* I chose this topic because I'm fascinated by the history of the Titanic.


### April 27: Project Presentation #1: Data Exploration and Analysis Plan

You'll be giving a presentation to the class about the work you have done so far, as well as your plans for the project going forward. Your presentation should use slides (or a similar format). Your slides, exploratory code, and visualizations should be included in your GitHub repository. Here are some questions that you should address in your presentation:

What data have you gathered, and how did you gather it? What steps have you taken to explore the data? Which areas of the data have you cleaned, and which areas still need cleaning? What insights have you gained from your exploration? Will you be able to answer your question with this data, or do you need to gather more data (or adjust your question)? How might you use modeling to answer your question?

Example:
* I've created visualizations and numeric summaries to explore how survivability differs by passenger characteristic, and it appears that gender and class have a large role in determining survivability.
* I estimated missing values for age using the titles provided in the Name column.
* I created features to represent "spouse on board" and "child on board" by further analyzing names.
* I think that the fare and ticket columns might be useful for predicting survival, but I still need to clean those columns.
* I analyzed the differences between the training and testing sets, and found that the average fare was slightly higher in the testing set.
* Since I'm predicting a binary outcome, I plan to use a classification method such as logistic regression to make my predictions.


### May 18: First Draft Due

**At a minimum**, your project repository on GitHub should contain:
* A draft of your project paper (in the format specified [below](#june-3-project-presentation-2))
* Code, with lots of comments
* Visualizations of your data

**Ideally**, you would also include:
* Draft slides for presentation #2
* Data and data dictionary

Your peers and instructors will provide feedback by May 25, according to [these guidelines](peer_review.md).

**Tips for success:**
* The work should stand "on its own", and should not depend upon the reader remembering your first project presentation.
* The better you explain your project, and the easier it is to follow, the more useful feedback you will receive!
* If your reviewers can actually run your code on the provided data, they will be able to give you more useful feedback on your code. (It can be very hard to make useful code suggestions on code that can't be run!)


### June 3: Project Presentation #2

Your **project paper** should be written with a technical audience in mind. Here are the components you should cover:

* Problem statement and hypothesis
* Description of your data set and how it was obtained
* Description of any pre-processing steps you took
* What you learned from exploring the data, including visualizations
* How you chose which features to use in your analysis
* Details of your modeling process, including how you selected your models and validated them
* Your challenges and successes
* Possible extensions or business applications of your project
* Conclusions and key learnings

Your **presentation** should cover these components with less breadth and depth. Focus on creating an engaging, clear, and informative presentation that tells the story of your project and is suitable for a non-technical audience.

Your project repository on GitHub should contain the following:

* **Project paper:** any format (PDF, Markdown, etc.)
* **Presentation slides:** any format (PDF, PowerPoint, Google Slides, etc.)
* **Code:** commented Python scripts, and any other code you used in the project
* **Visualizations:** integrated into your paper and/or slides
* **Data:** data files in "raw" or "processed" format
* **Data dictionary (aka "code book"):** description of each variable, including units

If it's not possible or practical to include your entire dataset, you should link to your data source and provide a sample of the data. (GitHub has a [size limit](https://help.github.com/articles/what-is-my-disk-quota/) of 100 MB per file and 1 GB per repository.) If your data is private, you can either include an "anonymized" version of your data or create a private GitHub repository.
