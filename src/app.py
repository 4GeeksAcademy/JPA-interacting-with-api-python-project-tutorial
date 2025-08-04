import os
import spotipy
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

# Get credential values
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
redirect_uri = os.environ.get("REDIRECT_URI")

# Authenticate using Client Credentials Flow

from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(auth_manager=auth_manager)


# Artist ID for Michael Bibi

artist_id = '4cvdQRyHmkSQSakUrW2oxv'

# Get top tracks 
top_tracks = spotify.artist_top_tracks(artist_id, country="US")

# Print track info
print("\nTop 10 Songs:\n")

for i, track in enumerate(top_tracks["tracks"][:10], start=1):
    name = track["name"]
    popularity = track["popularity"]
    duration_min = round(track["duration_ms"] / (1000 * 60), 2)
    print(f"{i}. {name}")
    print(f"  Popularity: {popularity}")
    print(f"  Duration: {duration_min} min\n")

# # Extract name, popularity, and duration (in minutes)
# track_data = []

# # Get the top 10 songs
# for track in top_tracks["tracks"][:10]:  # Limit to top 10
#     name = track["name"]
#     popularity = track["popularity"]
#     duration_min = round(track["duration_ms"] / (1000 * 60), 2)
#     track_data.append({
#         "Name": name,
#         "Popularity": popularity,
#         "Duration (min)": duration_min
#     })
    

# # # Convert to DataFrame
# # df = pd.DataFrame(track_data)

# # # Show the table
# # df


# Convert to DataFrame
df = pd.DataFrame(track_data)

# Sort by increasing popularity
df_sorted = df.sort_values(by="Popularity", ascending=True)

# Show the bottom 3 songs (least popular)
print("\nTop 3 Songs by increasing Popularity:\n")
print(df_sorted.tail(3).to_string(index=False))



# Create the scatter plot
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Duration (min)", y="Popularity", s=80, color="teal")

plt.title("🎧 Song Duration vs Popularity")
plt.xlabel("Duration (minutes)")
plt.ylabel("Popularity")
plt.grid(True)
plt.tight_layout()
plt.show()


# According to the scatter plot, shorter lenght songs seem to be more popular for this artist then longer songs.

