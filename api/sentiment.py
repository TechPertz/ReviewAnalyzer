from textblob import TextBlob


def getSubjectivity(review):
    return TextBlob(review).sentiment.subjectivity

#Create a function to get the polarity
def getPolarity(review):
    return TextBlob(review).sentiment.polarity

def getAnalysis(score):
    if score < 0:
        return "Negative"
    elif score == 0:
        return "Neutral"
    else:
        return "Positive"

def getSentiment(review):
    #Create two new columns ‘Subjectivity’ & ‘Polarity’
    # subjectivity =getSubjectivity(review)
    polarity = getPolarity(review)
    sentiment = getAnalysis(polarity)
    print("sentiment done")
    return sentiment