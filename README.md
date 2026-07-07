# 📺 YouTube Data Dashboard using Streamlit

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit)
![YouTube API](https://img.shields.io/badge/YouTube-Data%20API%20v3-red?logo=youtube)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-blue?logo=plotly)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black?logo=pandas)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Project Overview

The **YouTube Data Dashboard** is a professional analytics dashboard built with **Python** and **Streamlit** that allows users to search any public YouTube channel and explore its statistics through interactive visualizations.

Using the **YouTube Data API v3**, the dashboard retrieves channel information, recent videos, engagement metrics, and presents them with an intuitive and responsive interface.

This project was developed as part of my internship to demonstrate API integration, data analysis, dashboard development, and visualization skills.

---

# ✨ Features

- 🔍 Search any public YouTube channel
- 📺 Display channel banner and thumbnail
- 👥 View subscriber count
- 👁 View total channel views
- 🎥 Display total uploaded videos
- 🌍 Show channel country
- ❤️ Calculate engagement rate
- 📊 Interactive Plotly charts
- 🏆 Top performing videos
- 📄 Latest uploaded videos dataset
- 📥 Download analytics as CSV
- 🧠 Channel Insights
- ⚡ Streamlit caching
- 🛡 Error handling
- 📱 Responsive dashboard layout

---

# 🛠 Tech Stack

### Frontend

- Streamlit

### Backend

- Python

### APIs

- YouTube Data API v3

### Libraries

- Pandas
- Plotly
- google-api-python-client
- python-dotenv

---

# 📂 Project Structure

```text
YouTube_Data_Dashboard/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
├── assets/
│
├── screenshots/
│
└── utils/
    ├── youtube_api.py
    ├── analytics.py
    ├── helper.py
    └── config.py
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YouTube-Data-Dashboard-Streamlit.git
```

Go inside the project

```bash
cd YouTube-Data-Dashboard-Streamlit
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 API Setup

1. Open Google Cloud Console.
2. Create a project.
3. Enable **YouTube Data API v3**.
4. Generate an API Key.
5. Create a `.env` file in the project root.

Example:

```env
YOUTUBE_API_KEY=YOUR_API_KEY_HERE
```

---

# ▶ Running the Application

```bash
streamlit run app.py
```

The dashboard will open automatically in your browser.

---

# 📊 Dashboard Features

## Channel Overview

- Subscribers
- Total Views
- Total Videos
- Country

---

## Analytics Summary

- Average Views
- Average Likes
- Average Comments
- Engagement Rate

---

## Channel Insights

- Best Performing Video
- Most Liked Video
- Most Commented Video
- Highest Engagement Video
- Performance Score

---

## Interactive Charts

- Views Analysis
- Engagement Analysis

---

## Video Analytics

- Top Videos
- Latest Uploaded Videos
- Download CSV

---

# 📸 Screenshots

Add screenshots inside the **screenshots** folder.

Example:

```
screenshots/
│
├── dashboard-home.png
├── analytics-summary.png
├── charts.png
├── videos.png
└── insights.png
```

Then update them here:

```markdown
![Dashboard](screenshots/dashboard-home.png)

![Analytics](screenshots/analytics-summary.png)

![Charts](screenshots/charts.png)

![Videos](screenshots/videos.png)

![Insights](screenshots/insights.png)
```

---

# 🌐 Deployment

The project can be deployed on:

- Streamlit Community Cloud

Deployment steps:

1. Push project to GitHub
2. Login to Streamlit Community Cloud
3. Connect GitHub repository
4. Select **app.py**
5. Add the environment variable

```
YOUTUBE_API_KEY
```

6. Deploy

---

# 🔮 Future Improvements

- Compare multiple YouTube channels
- Historical analytics
- AI-powered insights
- Search history
- PDF report generation
- Advanced filtering
- Sentiment analysis
- Dark/Light theme toggle

---

# 👨‍💻 Developer

**Aditya Kumar Verma**

B.Tech CSE (AI)

Python Developer | Data Analytics Enthusiast

---

# 🙏 Acknowledgements

- Google Developers
- YouTube Data API v3
- Streamlit
- Plotly
- Pandas

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.