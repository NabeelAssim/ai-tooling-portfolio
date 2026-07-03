import os
import requests
import re

# 1. Set your Supadata API key as an environment variable: SUPADATA_API_KEY
API_KEY = os.environ.get("SUPADATA_API_KEY")
if not API_KEY:
    raise ValueError("SUPADATA_API_KEY not set. Run: setx SUPADATA_API_KEY your_key")
BASE_DIR = "research/youtube-transcripts"

def sanitize_name(name):
    """Cleans up names so they are safe to use as folder and file names."""
    # Removes illegal characters and replaces spaces with underscores
    clean = re.sub(r'[\\/*?:"<>|]', "", name)
    return clean.strip().replace(" ", "_")

def fetch_transcript():
    print("\n---  Growth Marketing Transcript Fetcher ---")
    
    # 2. Ask the user for the details interactively
    video_url = input("Enter YouTube URL: ").strip()
    expert_name = input("Enter Expert's Name (e.g., Neil Patel): ").strip()
    video_title = input("Enter Video Title (e.g., B2B Cold Outreach): ").strip()

    if not video_url or not expert_name or not video_title:
        print("Error: All fields are required. Please run the script again.")
        return

    # 3. Build the new nested folder path
    safe_expert = sanitize_name(expert_name)
    safe_title = sanitize_name(video_title)
    
    expert_dir = os.path.join(BASE_DIR, safe_expert)
    os.makedirs(expert_dir, exist_ok=True)
    
    output_path = os.path.join(expert_dir, f"{safe_title}_transcript.txt")
    
    # 4. API Configuration
    endpoint = "https://api.supadata.ai/v1/transcript"
    headers = {"x-api-key": API_KEY}
    params = {
        "url": video_url,
        "text": "true" 
    }
    
    print(f"\n Requesting transcript for {video_title}...")
    
    # 5. Fetch and Save
    response = requests.get(endpoint, headers=headers, params=params)
    
    if response.status_code == 200:
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(response.text)
        print(f"Success! Transcript saved to: {output_path}\n")
    else:
        print(f"API Error (Status {response.status_code}): {response.text}\n")

if __name__ == "__main__":
    fetch_transcript()