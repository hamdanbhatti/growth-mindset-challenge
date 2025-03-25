import streamlit as st
import requests
import pandas as pd
import datetime
import random
import os


st.set_page_config(page_title="Motivation Dashboard", page_icon=":sunglasses:", layout="wide")
st.title("🌟 Daily Motivation Dashboard")

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden !important;}
        header {visibility: hidden !important;}
        #stDecoration {display: none !important;}
        
        /* Hide GitHub corner logo */
        .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob, .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137, .viewerBadge_text__1JaDK {
            display: none !important;
        }
        
        /* Hide any "View source" links */
        a[data-testid="stDecoration"] {display: none !important;}
        
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

def random_color():
    colors = ["#FF5733", "#33FF57", "#3399FF", "#FF33A8", "#FFC300", "#8E44AD", "#2ECC71"]
    return random.choice(colors)


def fetch_quote(category=None):
    url = "https://zenquotes.io/api/random"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            quote = data[0]['q']
            author = data[0]['a']
            return f'<p style="color:{random_color()}; font-size:24px; font-weight:bold;">💡 "{quote}"</p><p style="color:gray; font-size:18px;">— {author}</p>'
        else:
            return '<p style="color:red;">⚠️ Could not fetch quote, please try again later.</p>'
    except:
        return '<p style="color:red;">⚠️ Network error, check your connection.</p>'


categories = ["All", "Life", "Happiness", "Success", "Motivation"]
selected_category = st.selectbox("📌 Select a Category", categories)


quote_text = fetch_quote(selected_category if selected_category != "All" else None)
st.markdown(quote_text, unsafe_allow_html=True)

# Streak Tracker
st.subheader("🔥 Your Motivation Streak")
streak_file = "streak.txt"

# Load Streak Data
if os.path.exists(streak_file):
    with open(streak_file, "r") as f:
        last_date, streak = f.read().split(",")
        last_date = datetime.datetime.strptime(last_date, "%Y-%m-%d").date()
        streak = int(streak)
else:
    last_date, streak = datetime.date.today(), 0

# Update Streak
today = datetime.date.today()
if today > last_date:
    streak += 1
    with open(streak_file, "w") as f:
        f.write(f"{today},{streak}")

st.metric("Current Streak", f"{streak} Days", delta=1)

# Affirmation Generator
st.subheader("🌈 Positive Affirmation")
affirmations = [
    "You are enough! 💖",
    "Believe in yourself! 🚀",
    "Today is a fresh start! 🌅",
    "You are stronger than you think! 💪",
    "Your hard work will pay off! 💎"
]
st.markdown(f'<p style="color:{random_color()}; font-size:20px;">✨ {affirmations[today.day % len(affirmations)]}</p>', unsafe_allow_html=True)

# Progress Visualization
st.subheader("📊 Growth Over Time")
data = {"Days": list(range(1, streak + 1)), "Progress": [i * 10 for i in range(1, streak + 1)]}
df = pd.DataFrame(data)

st.line_chart(df)

