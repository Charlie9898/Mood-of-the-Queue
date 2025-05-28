import streamlit as st
import pandas as pd
import datetime
from google.oauth2.service_account import Credentials
import gspread
import plotly.express as px

# Define the scope and authenticate
scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file("mood-461203-302085ab3340.json", scopes=scope)

# Authorize and open the sheet
client = gspread.authorize(creds)
sheet = client.open("MoodLog").sheet1

# start the UI creation
st.title("Mood Tracker")
mood=st.selectbox("How are you feeling today?", ["😊", "😠", "😕", "🎉"])
note=st.text_input("Any notes for today?")

# button to submit mood with note
if st.button("Submit"):
    timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([timestamp, mood, note])
    st.success("Mood logged!")

# fetch data from GS
dat=sheet.get_all_records()
df=pd.DataFrame(dat)


if not df.empty:
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["date"] = df["timestamp"].dt.date

    # Date filter
    unique_dates = sorted(df["date"].unique(), reverse=True)
    selected_date = st.selectbox("Select a date to view moods", unique_dates)
    df_filtered = df[df["date"] == selected_date]

    if not df_filtered.empty:
        mood_counts = df_filtered["mood"].value_counts().reset_index()
        mood_counts.columns = ["mood", "count"]

        fig = px.bar(mood_counts, x="mood", y="count", title=f"Mood Trends on {selected_date}")
        st.plotly_chart(fig)
    else:
        st.info("No moods logged on the selected date.")
else:
    st.info("No mood data available.")


st.rerun() if st.button("Refresh Chart") else None