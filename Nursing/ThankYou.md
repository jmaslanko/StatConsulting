Hello,

I hope you are having a good day.  Our team was very happy to analyze the results
from the study to see if providing a thank-you note was inflential on the rating that
the patients gave the students.  After our intial analysis, the providing of a thank-you
note did not have a significant effect on the rating that the students receieved from
the patients.

Our process that lead to this conclusion is as follows.

First, we started by splitting the dataset into two subgroups of data; one for those with 
a note, and one without.  After this, we were then able to look at how the two sets of 
data were distributed.  We can see in the histogram below that both sets of data appear
to have the same distribution of data.

![histogram]('images/output.png')

The blue bars reference where no note was given, where orange is where a note was given.

To test whether or not there is a difference, we want to see if the average total rating 
was different between the two datasets.  If the data were normally distributed (i.e. in the
shape of a bell curve), then it would be fair to use the mean as the test statistic.
However, from the image above, we can see that our data is skewed and thus using the median
will be a better statistic to use.

Since we are testing if the medians have a significant difference, we will use the Mann-Whitney
test.  We start by assuming our median values are the same, and if the results from the Mann-Whitney
test are significant, then we will reject this prior assumption that they are the same.  For 
our experiment, the results did not provide anything that shows there is a significant difference
between the medians.

As a result, we conclude that providing a thank-you note does not have a siginicant effect on 
how the patients rated the students.

Thank you,
Jeremy Maslanko