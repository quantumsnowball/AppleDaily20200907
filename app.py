import argparse
import pandas as pd
from twitter import scrap
from sentiment import tweet_sentiment


def main(args):
    while True:
        try:
            query = input('\nKeyword to search Twitter: ')
            result = scrap(query, start=args.s, end=args.e, batch_size=args.n)
            sentiments = result.tweet.apply(tweet_sentiment).rename('sentiment')
            valids = sentiments[sentiments!=0]
            sts = valids.describe()
            if args.show:
                print(pd.concat((result, sentiments), axis=1)[sentiments!=0].reset_index(drop=True))
            print(' | '.join((
                f'Keyword: {"`"+query+"`": <8}',
                f'Tweets: total={sentiments.shape[0]}, valid={valids.shape[0]}',
                f'Sentiment: mean={sts["mean"]:+.3f}, std={sts["std"]:.3f}, min={sts["min"]:+.1f}, max={sts["max"]:+.1f}',
            )))
        except Exception as e:
            print(e)
        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    pars = argparse.ArgumentParser()
    pars.add_argument('-s', metavar='start', help='start date', default=None)
    pars.add_argument('-e', metavar='end', help='end date', default=None)
    pars.add_argument('-n', metavar='limit', help='number of tweets to scrap', default=250)
    pars.add_argument('--show', action='store_true', help='print out tweets as dataframe')
    args = pars.parse_args()
    main(args)