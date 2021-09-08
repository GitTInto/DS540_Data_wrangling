import json
import tweepy
import dataset
import logging
from datetime import datetime
import mail


API_KEY = '5Hqg6JTZ0cC89hUThySd5yZcL'
API_SECRET = 'Ncp1oi5tUPbZF19Vdp8Jp8pNHBBfPdXGFtXqoKd6Cqn87xRj0c'
TOKEN_KEY = '3272304896-ZTGUZZ6QsYKtZqXAVMLaJzR8qjrPW22iiu9ko4w'
TOKEN_SECRET = 'nsNY13aPGWdm2QcgOl0qwqs5bwLBZ1iUVS2OE34QsuR4C'



def start_logger():
    logging.basicConfig(filename='/tmp/daily_report_%s.log' %
                        datetime.strftime(datetime.now(), '%m%d%Y_%H%M%S'),
                        level=logging.DEBUG,
                        format='%(asctime)s %(message)s',
                        datefmt='%m-%d %H:%M:%S')


def main():
    start_logger()
    logging.debug("SCRIPT: I'm starting to do things!")

    try:
        def store_tweet(item):
            db = dataset.connect('sqlite:///data_wrangling.db')
            table = db['tweets']
            item_json = item._json.copy()
            for k, v in item_json.items():
                if isinstance(v, dict):
                    item_json[k] = str(v)
            table.insert(item_json)

        auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
        auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)

        api = tweepy.API(auth)

        query = '#childlabor'
        cursor = tweepy.Cursor(api.search, q=query, lang="en")

        for page in cursor.pages():
            for item in page:
                store_tweet(item)

        mail.mail("Completed Successfully")
                
    except Exception:
        logging.exception('SCRIPT: We had a problem!')
        logging.error('SCRIPT: Issue with division in the main() function')
        mail.mail("Program Failed !!!!")

    logging.debug('SCRIPT: About to wrap things up!')





if __name__ == '__main__':
    main()