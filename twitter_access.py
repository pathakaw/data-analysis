from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener

consumer_key = 'vE5TYT1PJx1vqhkp5FAHV6rWd'
consumer_secret = 'MxcuTPnxTZCbz8sVL4XpCql4KgjM7ayILMp5xGFAqUjfluwZNP'

access_token= '152664718-XhksaRoQn8u9j0kkzjxylCwQo5DfUmbDBpXjizqs'
access_token_secret = 'rIuEoZ61Mggy1S49cIPFk091804IFBGFItmTYJxOHRuNp'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

class PrintListener(StreamListener):
	def on_status(self, status):
		print(status.text)
    	print(status.autthor.screen_name,)
		
	def on_error(self, status_code):
		print("Error code: {}".format(status_code))
		return True #Keep alive
	
	def on_timeout(self):
		print('Listern timed out')
		return True
    
def main():
	listener = PrintListener()
	stream = Stream(auth, listener)
	stream.sample()
	
if __name__ == '__main__':
	main()