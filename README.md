# 🌟 Growth Mindset Challenge

A daily motivation dashboard built with Streamlit to help users maintain a growth mindset and track their progress.

## Overview

The Growth Mindset Challenge is a web application that provides daily motivation, tracks your consistency streak, and helps you visualize your growth over time. It's designed to encourage a positive mindset and personal development through daily engagement.

## Features

- 💡 **Daily Motivational Quotes**: Random inspirational quotes fetched from the ZenQuotes API
- 📌 **Category Selection**: Filter quotes by categories like Life, Happiness, Success, and Motivation
- 🔥 **Streak Tracker**: Automatically tracks and displays your daily login streak
- 🌈 **Positive Affirmations**: Daily positive affirmations to boost your mindset
- 📊 **Growth Visualization**: Visual representation of your progress over time

## Installation

1. Clone the repository:
```bash
git clone https://github.com/hamdanbhatti/growth-mindset-challenge.git
```

2. Navigate to the project directory:
```bash
cd growth-mindset-challenge
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit application:
```bash
streamlit run main.py
```

The application will open in your default web browser at `http://localhost:8501`.

## Requirements

- Python 3.6+
- Streamlit
- Pandas
- Requests

## How It Works

- The application fetches a random motivational quote each time you load the page
- Your streak is automatically updated when you visit the dashboard on a new day
- The progress visualization shows your growth over time based on your streak
- Positive affirmations change daily to provide fresh motivation

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open License

## Acknowledgments

- [ZenQuotes API](https://zenquotes.io/) for providing the motivational quotes
- [Streamlit](https://streamlit.io/) for the web application framework
```

You may also want to create a requirements.txt file for your project:

```text:requirements.txt
streamlit
pandas
requests
