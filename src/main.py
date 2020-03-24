from twitterscraper.query import query_single_page
from twitterscraper.tweet import Tweet
import json

class ScrappedTweet:
    def __init__(self, text, timestamp):
        self.text = text
        self.timestamp = str(timestamp)

def write_infile(text, timestamp):
    st = ScrappedTweet(text, timestamp)
    try:
        file_output = open("../results/result.json", "w+")
        file_output.write(json.dumps(st.__dict__))
    except OSError:
        print(e)
        return

if __name__ == "__main__":
    list_of_tweets = query_single_page("felipendsdev", "", None, from_user=True)
    for tweet in list_of_tweets:
        for t in tweet:
            if type(t) == Tweet:
                if t.text.startswith("TIL:"):
                    write_infile(t.text, t.timestamp.date())
