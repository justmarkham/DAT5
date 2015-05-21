## Class 11 Pre-work: ROC Curves and Area Under the Curve (AUC)

Before learning about ROC curves, it's important to be comfortable with the following terms: true positive, true negative, false positive, false negative, sensitivity, and specificity. If you aren't yet comfortable, Rahul Patwari has excellent videos on [Intuitive sensitivity and specificity](https://www.youtube.com/watch?v=U4_3fditnWg) (9 minutes) and [The tradeoff between sensitivity and specificity](https://www.youtube.com/watch?v=vtYDyGGeQyo) (13 minutes).

Then, watch Kevin's video on [ROC Curves and Area Under the Curve](https://www.youtube.com/watch?v=OAl6eAyP-yo) (14 minutes), and be prepared to **discuss it in class** on Wednesday. (There's a blog post containing the [video transcript and screenshots](http://www.dataschool.io/roc-curves-and-auc-explained/), which might serve as a useful reference.) You can also play with the [visualization](http://www.navan.name/roc/) shown in the video. Optionally, you could also watch Rahul Patwari's video on [ROC curves](https://www.youtube.com/watch?v=21Igj5Pr6u4) (12 minutes).

Here are some questions to think about:

- If you have a classification model that outputs predicted probabilities, how could you convert those probabilities to class predictions?
    - Set a threshold, and classify everything above the threshold as a 1 and everything below the threshold as a 0.
- What are the methods in scikit-learn that output predicted probabilities and class predictions?
    - predict_proba and predict.
- Why are predicted probabilities (rather than just class predictions) required to generate an ROC curve?
    - Because an ROC curve is measuring the performance of a classifier at all possible thresholds, and thresholds only make sense in the context of predicted probabilities.
- Could you use an ROC curve for a regression problem? Why or why not?
    - No, because ROC is a plot of TPR vs FPR, and those concepts have no meaning in a regression problem.
- What's another term for True Positive Rate?
    - Sensitivity or recall.
- If I wanted to increase specificity, how would I change the classification threshold?
    - Increase it.
- Is it possible to adjust your classification threshold such that both sensitivity and specificity increase simultaneously? Why or why not?
    - No, because increasing either of those requires moving the threshold in opposite directions.
- What are the primary benefits of ROC curves over classification accuracy?
    - Doesn't require setting a classification threshold, allows you to visualize the performance of your classifier, works well for unbalanced classes.
- What should you do if your AUC is 0.2?
    - Reverse your predictions so that your AUC is 0.8.
- What would the plot of reds and blues look like for a dataset in which each observation was a credit card transaction, and the response variable was whether or not the transaction was fraudulent? (0 = not fraudulent, 1 = fraudulent)
    - Blues would be significantly larger, lots of overlap between blues and reds.
- Let's say your classifier has a sensitivity of 0.95 and a specificity of 0.3, and the classes are balanced. Would it result in more false positives or false negatives?
    - False positives, meaning it falsely predicted positive (the true status is negative).
- What's a real-world scenario in which you would prefer a high specificity (rather than a high sensitivity) for your classifier?
    - Speed cameras issuing speeding tickets.
