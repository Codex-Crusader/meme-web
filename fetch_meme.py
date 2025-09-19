import requests
import datetime
import os
import json

# Number of memes to fetch each day
MEME_COUNT = 5
SAVE_PATH = "memes"


def fetch_memes():
    meme_list = []
    unique_urls = set()
    max_attempts = MEME_COUNT * 3  # Limit attempts to avoid infinite loops
    attempts = 0

    while len(meme_list) < MEME_COUNT and attempts < max_attempts:
        try:
            attempts += 1
            response = requests.get("https://meme-api.com/gimme", timeout=10)
            response.raise_for_status()
            data = response.json()

            # Check if this URL is already in our collection
            url = data.get("url")
            if url and url not in unique_urls:
                unique_urls.add(url)
                meme_list.append({
                    "title": data.get("title"),
                    "url": url,
                    "postLink": data.get("postLink"),
                    "subreddit": data.get("subreddit"),
                    "timestamp": datetime.datetime.now(datetime.UTC).isoformat()
                })
                print(f"Fetched unique meme {len(meme_list)}/{MEME_COUNT}")
            else:
                print("Skipped duplicate meme")
        except requests.RequestException as e:
            print(f"Error fetching meme: {e}")

    return meme_list

def save_memes(meme_list):
    os.makedirs(SAVE_PATH, exist_ok=True)
    today = datetime.date.today().isoformat()
    with open(os.path.join(SAVE_PATH, f"{today}.json"), "w", encoding="utf-8") as f:
        json.dump(meme_list, f, indent=2)

if __name__ == "__main__":
    todays_memes = fetch_memes()
    if todays_memes:
        save_memes(todays_memes)
        print(f"Saved {len(todays_memes)} memes for today.")
    else:
        print("No memes fetched today.")