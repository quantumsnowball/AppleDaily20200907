from textblob import TextBlob


def tweet_sentiment(text, verbose=False):
    """
    The sentiment function of textblob returns two properties, polarity, and subjectivity.

    Polarity is float which lies in the range of [-1,1] where 1 means positive statement
    and -1 means a negative statement.

    Subjective sentences generally refer to personal opinion, emotion or judgment whereas
    objective refers to factual information. Subjectivity is also a float which lies in
    the range of [0,1].
    """
    # parse the tweet into textblob object
    blob = TextBlob(text)
    # we define the sentiment of sentence to be the product of its polarity and subjectivity
    # tweet sentiment is the sum of sentiment for all sentences in a tweet
    sentiment = sum(s.polarity * s.subjectivity for s in blob.sentences)
    # print if verbose
    if verbose:
        polarity = sum(s.polarity for s in blob.sentences)
        subjectivity = sum(s.subjectivity for s in blob.sentences)
        num_sentence = len(blob.sentences)
        return text, num_sentence, polarity, subjectivity, sentiment
    else:
        return sentiment


def test():
    sentences = [
        '$AAPL so is this the price that gets split? If so, looks like it’ll be $125.50 a share on Monday. Nice.',
        'Stocks head into September in high gear as Apple and Tesla split, and markets await the August jobs report',
        'S&P 500 SETS FRESH RECORD CLOSING HIGH OF 3,508.01',
        'Massive $tsla dump be careful out there short term oversold tho $spy $amzn',
        '$SPX is overbought but momentum is very very strong. My bet is unless we correct quickly this week, we are looking for a blow off top. ',
        '$SPY reached 350 2 points from our target of 352.. RSI is overbought - sell and wait ti buy for later. Short $SHOP and $NVAX.',
        'Slight setback, nothing to worry about. Outlook dismal. 28 trade session left - Target $SPX 2394.25',
        'Russell looks bad. Big bearish RSI divergence and ejected from the channel after riding up the bottom rail.',
    ]
    print(' | '.join(['',' #','Sentence'+' '*92,'# sentence','polarity','subjectivity','sentiment','']))
    print('-'*162)
    for i,sentence in enumerate(sentences):
        text, num_sentence, polarity, subjectivity, sentiment = tweet_sentiment(sentence, verbose=True)
        print(f' | {i+1:2d} | {text[:100]: <100} | {num_sentence: >10} | {polarity:+8.2f} | {subjectivity:+12.2f} | {sentiment:+9.2f} |')


if __name__ == '__main__':
    test()