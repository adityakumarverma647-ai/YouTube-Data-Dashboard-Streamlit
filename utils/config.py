"""
==========================================================
YouTube Analytics Dashboard
config.py
Version 3

Central configuration file
==========================================================
"""

from __future__ import annotations

import os
from dotenv import load_dotenv

# ==========================================================
# Load Environment Variables
# ==========================================================

load_dotenv()

# ==========================================================
# API Configuration
# ==========================================================

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY", "")

if not YOUTUBE_API_KEY:
    raise ValueError(
        "YOUTUBE_API_KEY not found. Please check your .env file."
    )

# ==========================================================
# YouTube API Parts
# ==========================================================

CHANNEL_PART = (
    "snippet,"
    "statistics,"
    "brandingSettings,"
    "contentDetails"
)

VIDEO_PART = (
    "snippet,"
    "statistics,"
    "contentDetails"
)

PLAYLIST_PART = "snippet"

SEARCH_PART = "snippet"

# ==========================================================
# Dashboard Configuration
# ==========================================================

DEFAULT_MAX_RESULTS = 10

TOP_VIDEO_LIMIT = 20

MAX_DESCRIPTION_LENGTH = 500

CSV_FILENAME = "youtube_channel_data.csv"

CACHE_TTL = 600

# ==========================================================
# Streamlit Configuration
# ==========================================================

PAGE_TITLE = "YouTube Analytics Dashboard"

PAGE_ICON = "📺"

LAYOUT = "wide"

INITIAL_SIDEBAR_STATE = "expanded"

# ==========================================================
# Chart Configuration
# ==========================================================

CHART_HEIGHT = 450

BAR_CHART_TITLE = "Views by Latest Videos"

SCATTER_CHART_TITLE = "Likes vs Comments"

LINE_CHART_TITLE = "Video Performance"

# ==========================================================
# KPI Labels
# ==========================================================

KPI_SUBSCRIBERS = "Subscribers"

KPI_VIEWS = "Views"

KPI_VIDEOS = "Videos"

KPI_COUNTRY = "Country"

KPI_AVG_VIEWS = "Average Views"

KPI_AVG_LIKES = "Average Likes"

KPI_AVG_COMMENTS = "Average Comments"

KPI_ENGAGEMENT = "Engagement Rate"

# ==========================================================
# Messages
# ==========================================================

SEARCH_PLACEHOLDER = "e.g. MrBeast"

LOADING_MESSAGE = "Fetching data from YouTube..."

CHANNEL_NOT_FOUND = "Channel not found."

EMPTY_SEARCH = "Please enter a channel name."

WELCOME_MESSAGE = (
    "👈 Enter a YouTube channel name "
    "in the sidebar and click Search."
)

# ==========================================================
# Public Exports
# ==========================================================

__all__ = [

    "YOUTUBE_API_KEY",

    "CHANNEL_PART",

    "VIDEO_PART",

    "PLAYLIST_PART",

    "SEARCH_PART",

    "DEFAULT_MAX_RESULTS",

    "TOP_VIDEO_LIMIT",

    "MAX_DESCRIPTION_LENGTH",

    "CSV_FILENAME",

    "CACHE_TTL",

    "PAGE_TITLE",

    "PAGE_ICON",

    "LAYOUT",

    "INITIAL_SIDEBAR_STATE",

    "CHART_HEIGHT",

    "BAR_CHART_TITLE",

    "SCATTER_CHART_TITLE",

    "LINE_CHART_TITLE",

    "KPI_SUBSCRIBERS",

    "KPI_VIEWS",

    "KPI_VIDEOS",

    "KPI_COUNTRY",

    "KPI_AVG_VIEWS",

    "KPI_AVG_LIKES",

    "KPI_AVG_COMMENTS",

    "KPI_ENGAGEMENT",

    "SEARCH_PLACEHOLDER",

    "LOADING_MESSAGE",

    "CHANNEL_NOT_FOUND",

    "EMPTY_SEARCH",

    "WELCOME_MESSAGE",

]