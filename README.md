# EchoMood 🎵

EchoMood is a fun and interactive app that uses sentiment analysis to detect the mood from a user's recent X (formerly Twitter) posts or simulated tweets. Based on the analyzed mood, EchoMood generates a playlist from Bandcamp and embeds it for users to enjoy.

## Features
- Sentiment analysis of X (Twitter) posts using NLP
- Mood-based playlist generation using Bandcamp
- Interactive web interface built with Streamlit
- Visual representation of mood changes over time with Plotly

## Demo

Check out a video demo of simulated tweets and songs to see how the app works below:

[![EchoMood Demo](https://img.youtube.com/vi/0-QGBGpeGfE/0.jpg)]([https://www.youtube.com/watch?v=0-QGBGpeGfE])

Click the image above to watch the demo or [here](https://www.youtube.com/watch?v=0-QGBGpeGfE).

## Setup and Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/dunktra/pet-project-echomood.git
   cd pet-project-echomood
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:

   ```bash
   streamlit run echomood.py
   ```

## Usage

1. Enter a X (Twitter) handle (without `@`).
2. EchoMood will simulate tweets (or use real tweets if API keys are configured).
3. The app analyzes the sentiment of tweets and generates a playlist based on the mood.
4. The playlist will be embedded using Bandcamp, and mood changes will be visualized.

## Requirements

- Python 3.8+
- Streamlit
- Bandcamp API
- Tweepy (Twitter API)
- TextBlob (NLP for sentiment analysis)
- Plotly (Data visualization)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Other notes

To fetches the top 5 recent tweets from a real Twitter (X) account instead of using simulated tweets, you'll need to integrate the Twitter API using Tweepy. Ensure that you have proper access to the Twitter API by using your API keys and tokens. You may need to apply for Elevated access or switch to API v2 in order to generate tweets from other users.

Recommended fix below
 ```bash
   import tweepy #Twitter API

   # Twitter API credentials
   TWITTER_API_KEY = 'Your_API_Key'
   TWITTER_API_SECRET_KEY = 'Your_API_Secret_Key'
   TWITTER_ACCESS_TOKEN = 'Your_Access_Token'
   TWITTER_ACCESS_TOKEN_SECRET = 'Your_Access_Token_Secret'

   # Authenticate to Twitter
   auth = tweepy.OAuth1UserHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
   api = tweepy.API(auth)

   # Function to get the 5 most recent tweets from a user
   def get_recent_tweets(username, count=5):
      try:
        tweets = api.user_timeline(screen_name=username, count=count, tweet_mode='extended')
        recent_tweets = [tweet.full_text for tweet in tweets]
        return recent_tweets
      except Exception as e:
        st.error(f"Error fetching tweets: {e}")
        return []
 ```

To generate personalized playlist on Bandcamp, you may need Bandcamp API as described in https://bandcamp.com/developer. Recommended fix below:
 ```bash
   # Hypothetical Bandcamp API integration
   import bandcamp_api

   # Function to fetch Bandcamp songs by mood (hypothetical)
   def fetch_bandcamp_tracks_by_mood(mood, count=3):
      # Search tracks based on mood using a hypothetical Bandcamp API
      try:
        if mood == 'positive':
            query = 'happy upbeat'
        elif mood == 'negative':
            query = 'sad melancholic'
        else:
            query = 'relaxing'

   # Search Bandcamp tracks using the API
        results = bandcamp_api.search_tracks(query, limit=count)
        track_uris = [track['uri'] for track in results['tracks']]
        return track_uris
      except Exception as e:
        st.error(f"Error fetching tracks from Bandcamp: {e}")
        return []

   # Function to create a Bandcamp playlist (hypothetical)
   def create_bandcamp_playlist(track_uris):
      try:
        # Hypothetically creating a playlist on Bandcamp
        playlist = bandcamp_api.create_playlist(track_uris)
        return playlist['id']
      except Exception as e:
        st.error(f"Error creating playlist: {e}")
        return None
  ```

---
**Enjoy using EchoMood?** Give it a ⭐ on GitHub!
