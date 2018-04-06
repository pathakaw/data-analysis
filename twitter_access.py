import json
from tweepy import OAuthHandler, Stream, API
from tweepy.streaming import StreamListener

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

class PrintListener(StreamListener):
	
	def on_status(self, status):	    
		if not status.text[:3] == 'RT':
			print(status.text)
			print(status.autthor.screen_name,)
		
	def on_error(self, status_code):
		print("Error code: {}".format(status_code))
		return True #Keep alive
	
	def on_timeout(self):
		print('Listern timed out')
		return True
    
def print_to_console():
	listener = PrintListener()
	stream = Stream(auth, listener)
	languages = ('en',)
	stream.sample()

def get_tweets(screen_name):
	api = API(auth)
	tweets = api.user_timeline(screen_name=screen_name, count=200)
	
	for tweet in tweets:
		print(json.dumps(tweet._json, indent=4))
	
def main():
	#print_to_console()
	get_tweets(auth.username)

if __name__ == '__main__':
	main()
