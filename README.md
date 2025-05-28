# Mood-of-the-Queue

Tiny internal tool to track the vibe of the support queue. Built fast with Streamlit + Google Sheets.

## Features

- Log moods via emoji + optional notes
- Store entries in Google Sheets
- Visualize daily mood trends
- Filter moods by day
- Auto-refresh button for quick updates

## Setup

1. Clone this repo
2. Set up a Google Sheet named `MoodLog` with headers: `timestamp`, `mood`, `note`
3. Create a Google service account, download the JSON credentials
4. Rename your JSON file to `your-credentials.json` or update the filename in code
5. Run:

```bash
pip install -r requirements.txt
streamlit run app.py
