import random
import streamlit as st
import plotly.graph_objects as go
from textblob import TextBlob

# Set Streamlit page configuration (move this to the very top)
st.set_page_config(
    page_title="EchoMood",
    page_icon=":notes:",
)

# Simulated Bandcamp track embed URLs (using iframe embeds as strings)
bandcamp_tracks = [
    '<iframe style="border: 0; width: 400px; height: 120px;" src="https://bandcamp.com/EmbeddedPlayer/album=3835799211/size=large/bgcol=ffffff/linkcol=333333/tracklist=false/artwork=small/track=3615324482/transparent=true/" seamless><a href="https://intlanthem.bandcamp.com/album/mighty-vertebrate">Mighty Vertebrate by Anna Butterss</a></iframe>',
    '<iframe style="border: 0; width: 400px; height: 120px;" src="https://bandcamp.com/EmbeddedPlayer/album=305672436/size=large/bgcol=ffffff/linkcol=333333/tracklist=false/artwork=small/track=2536662699/transparent=true/" seamless><a href="https://warmagency.bandcamp.com/album/everything-above-the-sky-astral-travelling-w-luke-una">Everything Above The Sky / Astral Travelling w/ Luke Una by Sylvain Kassap</a></iframe>',
    '<iframe style="border: 0; width: 400px; height: 120px;" src="https://bandcamp.com/EmbeddedPlayer/album=4129255005/size=large/bgcol=ffffff/linkcol=333333/tracklist=false/artwork=small/track=1266739538/transparent=true/" seamless><a href="https://niluferyanya.bandcamp.com/album/my-method-actor">My Method Actor by Nilufer Yanya</a></iframe>',
    '<iframe style="border: 0; width: 400px; height: 120px;" src="https://bandcamp.com/EmbeddedPlayer/album=160929952/size=large/bgcol=ffffff/linkcol=333333/tracklist=false/artwork=small/transparent=true/" seamless><a href="https://eddiechaconofficial.bandcamp.com/album/lay-low">Lay Low by EDDIE CHACON</a></iframe>',
    '<iframe style="border: 0; width: 400px; height: 120px;" src="https://bandcamp.com/EmbeddedPlayer/album=1523435891/size=large/bgcol=ffffff/linkcol=333333/tracklist=false/artwork=small/track=155118096/transparent=true/" seamless><a href="https://sharadashashidhar.bandcamp.com/album/soft-echoes">Soft Echoes by Sharada Shashidhar</a></iframe>'
]

# Function to simulate fetching Bandcamp songs
def fetch_bandcamp_tracks(count=3):
    return random.sample(bandcamp_tracks, count)

# Function to analyze sentiment of tweets (using simulated tweets)
def analyze_sentiment(tweets):
    sentiment_scores = []
    for tweet in tweets:
        analysis = TextBlob(tweet)
        sentiment_scores.append(analysis.sentiment.polarity)
    return sentiment_scores

# Function to plot mood changes using Plotly
def plot_mood_changes(sentiment_scores):
    fig = go.Figure()

    # Add line plot
    fig.add_trace(go.Scatter(
        x=list(range(len(sentiment_scores))),
        y=sentiment_scores,
        mode='lines+markers',
        marker=dict(size=10, color='blue'),
        line=dict(color='blue')
    ))

    # Customize layout
    fig.update_layout(
        title="Mood Changes Over Time",
        xaxis_title="Post Index",
        yaxis_title="Sentiment Score",
        showlegend=False
    )

    # Display plot in Streamlit
    st.plotly_chart(fig)

# Streamlit App Layout
# Adding Font Awesome Icon for Musical Notes 🎵
st.title("EchoMood")
st.write("Enter a X (Twitter) username, and we'll analyze their recent tweets and recommend Bandcamp songs based on their mood!")

# Input field for Twitter username
username = st.text_input("Enter X handle (without @)", "")

# Simulated tweets for demo purposes
simulated_tweets = [
    f"{username} loves exploring new cafes in the city.",
    f"{username} is having a wonderful day with friends!",
    f"{username} feels uncertain about the future, but staying hopeful.",
    f"{username} feels a bit overwhelmed today. Need a break.",
    f"{username} just finished a great book about personal growth."
]

if username:
    st.write(f"Simulating tweets for @{username}...")
    tweets = simulated_tweets
    
    if tweets:
        sentiment_scores = analyze_sentiment(tweets)
        avg_sentiment = sum(sentiment_scores) / len(sentiment_scores)
        mood = 'positive' if avg_sentiment >= 0 else 'negative'
        st.write(f"Detected mood: **{mood}**")
        
        # Plot mood changes using Plotly
        st.write("Mood changes over time:")
        plot_mood_changes(sentiment_scores)
        
        # Fetch and embed Bandcamp songs
        if st.button("Generate Playlist 🎵"):
            st.write("Fetching Bandcamp songs...")
            tracks = fetch_bandcamp_tracks()
            
            # Embed tracks in a "playlist-like" format
            for i, track in enumerate(tracks):
                st.write(f"Song {i + 1}:")
                st.markdown(track, unsafe_allow_html=True)
    else:
        st.error("Oops! No tweets found or an error occurred :(")
