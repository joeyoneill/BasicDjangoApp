from django.shortcuts import render

# Create your views here.
resultSearch = ''

tweets = [

	{
		'username' : '@kanyewest',
		'content' : 'Have you ever thought you were in love with someone but then realized you were just staring in a mirror for 20 minutes?',
		'likes' : 36484,
		'retweets' : 50981,
		'date_posted' : '10 February 2014'
	},
	{
		'username' : '@elonmusk',
		'content' : 'Am considering taking Tesla private at $420. Funding secured.',
		'likes' : 85733,
		'retweets' : 15370,
		'date_posted' : '7 August 2018'
	},
	{
		'username' : '@JohnCena',
		'content' : 'These are test tweets to show I can read in data!',
		'likes' : 15,
		'retweets' : 4,
		'date_posted' : '8 October 2019'
	},
	{
		'username' : '@itsyourdustiny',
		'content' : 'Look it is working!',
		'likes' : 3,
		'retweets' : 0,
		'date_posted' : '9 October 2019'
	},
	{
		'username' : '@realDonaldTrump',
		'content' : 
		"Sorry losers and haters, but my I.Q. is one of the highest -and you all know it! Please don't feel so stupid or insecure,it's not your fault",
		'likes' : 54503,
		'retweets' : 60207,
		'date_posted' : '8 May 2013'
	},
	{
		'username' : '@itsyourdustiny',
		'content' : 'search and see',
		'likes' : 3,
		'retweets' : 5,
		'date_posted' : '11 October 2019'
	},
]

resultTweets = []



def home(request):
	'''
	if search:
		resultSearch = search
		resultTweets = []
		for tweet in tweets:
			if resultSearch.upper() in tweet['content'].upper():
				resultTweets.append(tweet)
	'''
	context = {

		'tweets' : tweets,
		#'resultTweets' : resultTweets,
		#'resultSearch' : resultSearch,
		#'search' : search
	}

	return render(request, 'home/home.html', context)

def aboutUs(request):
	context = {
		'title' : 'About Us'
	}
	return render(request, 'home/aboutUs.html', context)

def results(request):
	context = {
		'title' : resultSearch,
		'resultTweets' : resultTweets
	}
	return render(request, 'home/results.html', context)