# James' Emotional Breakdown
[![Project Purpose](https://img.shields.io/badge/Hackathon%2001-Complete-green)](https://bitbucket.org/h2ecommerce/james-hack-01/)
[![Project Version](https://img.shields.io/badge/Version-0.0.1-yellow)](https://bitbucket.org/h2ecommerce/james-hack-01/)
[![Vocabulary Status](https://img.shields.io/badge/Vocabulary-Incomplete-yellow)](https://bitbucket.org/h2ecommerce/james-hack-01/src/master/vocabulary.json)

## Scope
This application analyses the sentiment of text that is submitted to it by checking for a number of strongly emotive words (and collections of words) to break it down and determine a suitable strength of feeling score for the overall piece, with the intention to being to provide as level a playing field as possible, regardless of length.

The result is distilled down into a score of negative words (or word casing) versus a score of positive words. The positive and negative values are then added together to provide a score, and with the --divide argument, this can score is divided by the total number of words submitted.

**Sentiment = ( ( Total positive word [score or +1] + Total negative word [score or -1] ) [/ Submission length] )**

Strongly positive and strongly negative scores are intended to be deemed as most in need of attention, with values approaching ever closer to zero being unlikely to need attention as quickly.

The functionality could be imported into another Python project, an API developed for it, or it could be used via the CLI as is possible now.

## Limitations
Humans can struggle to understand emotion in text, as it isn't accompanied by body language, which led the growth in acceptance and use of emojis over time.

Another example of something even humans struggle to understand is sarcasm, even when transmitted through speech along with facial expressions and general body language.

So, simply put, some context is lacking from this application (e.g. punctuation is ignored, as is uppercase 'SHOUTING'), and so expressions such as "THANKS FOR NOTHING!" may be read as neutral, since "Thanks" is generally deemed positive and "nothing" is most likely negative.

**One could factor in the above by adding a modest multiplier to the value of the words being 'shouted', or to the contents of a sentence ending in an exclamation mark, or those with, for example, three or more question marks '???' at the end of a sentence.**

Another issue is that of *typing errors* - if someone has made a **typo** or **misspelt** a word, then it won't be matched. Some fuzzy logic would need to be added to determine what word they most likely meant based on derived context from a sentence and the letters available. One would also need to make allowances for American English spellings, for example, replacing 's' with 'z' for words such as "realise".

## Testing
To aid with the original set up and test this application, a number of comments were randomly selected from a range of rating levels at [Cartridge People's Reviews.co.uk pages](https://www.reviews.co.uk/company-reviews/store/cartridge-people). To view a selection of the tests, run the script with the "--tests" flag.

## Proper solution recommendations
Machine Learning would be a better route to go down, given a large enough dataset,  but I wanted to make something original, so I didn't simply follow the guide found here: [Tensor Flow Text Classification](https://www.tensorflow.org/tutorials/keras/text_classification).

It would, however, more than likely provide a more solid basis for a solution to the problem posed in the brief, in part due to the much greater vocabulary fed in.

## Future development opportunities

### Create an API
This could be put into Docker on an Azure server and an API set up to receive POST requests.

### Entering the vocabulary into a database
As the vocabulary grows, it is unfeasible to keep it in a flat file, so, it should be put into a database.

### Auto-updating vocabulary
The application could update the vocabulary dictionary with new words it encounters by entering the new word into the vocabulary.json file and searching for the word via an online thesaurus, e.g. [https://words.bighugelabs.com/site/api](https://words.bighugelabs.com/site/api) and looking for synonyms in the returned data which are already found within the file, then, taking the synonyms scores and averaging them to provide the new word with a score of its own, with a flag of "unverified" included, so that it could be checked by an administrator.

### Implementing tests using PyTest or similar
The testing that I have built in is somewhat manual and would benefit from being standardised into assertions.

### User defined weightings
A future version could accept a single piece of text submitted by a user as the first parameter, and a weighting multiplier for positive sentiment on a scale from 0-10, plus a weighting multiplier for negative sentiment on a scale from 0-10 (where 0 gives no consideration and 10 gives maximum weighting) as a second parameter **OR** a pre-set word to denote the type of submission (i.e. "Review", "Email", "Question", or "Answer").

The type of submission would then be used to determine how to weight the positive versus negative words included, since for a review, we might want to respond to a bad one asap, but perhaps also to showcase an especially positive one too, leaving the middle of the road ones as less important. Whereas in the case of an email, unfortunately, we are most likely to need to prioritising a response to submissions that are loaded negatively over those which are less negative.

**Sentiment = ( ( Positive word score * Positive weighting + Negative word score * Negative weighting ) / Submission length )**

e.g.
```python
# The weightings could be passed in as (positive, negative) with each as a score from 0-10,
# with the below pre-sets available:
#
# "Review" provides a default weighting of (3,5)
# "Email" provides a default weighting of (1,2)
# "Question" provides a default weighting of (1,1)
# "Answer" provides a default weighting of (1,1)
```

#### Providing extra weighting to the length of submissions
Building on the above, the longer a submission, the more detailed and worthy of a response one may assume it to be, so perhaps the formula should simply be:

**Sentiment = ( Positive word score * Positive weighting + Negative word score * Negative weighting )**

### Checking for incorrect review score submissions
The application could also accept a third argument for "Review" type submissions, to include the score out of 5 given by the submitter, and use that to check whether or not someone has made a mistake and needed a response, or if they were trying to bypass a minimum score filter of sorts to appear front and centre.

### Taking multiple submissions
The application could take a list of submissions and return a list of scores to reduce future API call numbers.

## Project Brief

### The problem
The company receives "written" correspondence from customers on a  daily basis, via reviews, questions and answers as well as customer service emails.  Sometimes the volume of emails makes it hard to prioritise them.

### The solution
Sentiment analysis (also known as opinion mining or emotion AI) is a means of using natural language processing to systematically identify and study affective states and subjective info.  One such application of this analysis is our problem above and so we wish to use sentiment analysis to achieve this goal

### Brief
1. Develop a service using sentiment analysis that will take in a customer input and quantify their emotions on a scalable level to aid prioritising correspondence
2. Use any solution you deem suitable to achieve this goal
3. Entries will be scored on a variety of areas such as (but not limited to)
    1. Creativeness
    2. Innovation
    3. Usefulness
    4. Technical (Code structure, tests, architecture etc)
    5. Polish

Submissions
Entries should be submitted by the end of your working day to the preconfigured repository provided to you.  We appreciate people work different hours.

## Installation

TBC

## Usage

```bash
python3 emotionalbreakdown/main.py -h
# usage: main.py [-h] [-c CONTENT] [-t] [-v] [-b] [-l] [-d]

# optional arguments:
#   -h, --help            show this help message and exit
#   -c CONTENT, --content CONTENT
#                         Enter the content to be processed here
#   -t, --tests           Include this argument to show the tests performed
#                         originally
#   -v, --verbose         Increase output verbosity/show working
#   -b, --binary          Include this argument to score with +1 or -1 for
#                         positive or negative lexicon items respectively
#                         (without this argument, defaults to using the prepared
#                         lexicon grading set)
#   -l, --lexicon         Include this argument to print out the lexicon
#   -d, --divide          Include this argument to divide the overall score by
#                         the total number of words

# Examples:
python3 emotionalbreakdown/main.py --lexicon
python3 emotionalbreakdown/main.py --tests
python3 emotionalbreakdown/main.py --content='I love Cartridge People'
python3 emotionalbreakdown/main.py --binary --content='I love Cartridge People'
python3 emotionalbreakdown/main.py --divide --content='I love Cartridge People'
python3 emotionalbreakdown/main.py --binary --divide --content='I love Cartridge People'
python3 emotionalbreakdown/main.py -b -d -l -v -t -c 'I love Cartridge People'
```

## Contributing
This is a private repo :)

## License
[MIT](https://choosealicense.com/licenses/mit/)

## References
*Bo Pang and Lillian Lee "Opinion mining and sentiment analysis"* [http://www.cs.cornell.edu/home/llee/omsa/omsa.pdf](http://www.cs.cornell.edu/home/llee/omsa/omsa.pdf)