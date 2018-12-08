import markovify

class Blabberbot():
    def __init__(self,filepath):
        with open(filepath) as file:
            text = [line.strip() for line in file.readlines()]
        self.text_model = markovify.Text(text)

    def generate_tweet(self,n):
        return self.text_model.make_short_sentence(n)

celebs = {}
celebs["ElonMusk"] = "../Tweets/ElonMusk.txt"
celebs["Tesla"] = "../Tweets/Tesla.txt"