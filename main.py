import os
import time
from instagrapi import Client

# Set up the Instagram client
client = Client()

# Log in to your Instagram account
username = "Your username"
password = "your password"

print("Logging in...")
try:
    client.login(username, password)
    print("Login successful.")
except Exception as e:
    print(f"Failed to log in: {e}")
    exit(1)

# Path to the video file
video_file =r"Your video path.mp4"

# Ensure the video file exists
if not os.path.exists(video_file):
    try:
        print(f"Video file not found: {video_file}".encode('utf-8', 'replace').decode())
    except UnicodeEncodeError:
        print("Video file not found.")
    exit(1)

def upload_video():
    try:
        print(f"Uploading: {video_file}".encode('utf-8', 'replace').decode())
        client.video_upload(video_file, "coustom caption")
        print(f"Uploaded: {video_file}".encode('utf-8', 'replace').decode())
    except Exception as e:
        print(f"Failed to upload video: {e}".encode('utf-8', 'replace').decode())

# Upload the same video 5 times per minute
for i in range(5):
    upload_video()
    time.sleep(12)  # Wait for 12 seconds before uploading the next video to maintain 5 videos per minute

print("All videos uploaded. Logging out...")
client.logout()
print("Logged out.")
