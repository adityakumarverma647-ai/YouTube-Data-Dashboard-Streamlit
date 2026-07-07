"""
==========================================================
YouTube Analytics Dashboard
youtube_api.py
Version 3

Features
--------
✓ Channel Search
✓ Channel Statistics
✓ Latest Videos
✓ Top Videos
✓ Streamlit Caching
✓ Error Handling
✓ Optimized API Requests
✓ Plotly Ready Data
✓ Analytics Helpers
==========================================================
"""

from __future__ import annotations

import os
from typing import List, Dict, Optional

import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# ==========================================================
# Load Environment
# ==========================================================

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

if not API_KEY:
    raise ValueError(
        "YOUTUBE_API_KEY not found in .env file."
    )

# ==========================================================
# YouTube Client
# ==========================================================

youtube = build(
    "youtube",
    "v3",
    developerKey=API_KEY,
    cache_discovery=False
)

# ==========================================================
# Internal Safe Execute
# ==========================================================

def _execute(request):

    try:
        return request.execute()

    except HttpError as e:
        st.error(f"YouTube API Error: {e}")
        return None

    except Exception as e:
        st.error(f"Unexpected Error: {e}")
        return None


# ==========================================================
# Search Channel
# ==========================================================

@st.cache_data(show_spinner=False)

def search_channel(channel_name: str) -> Optional[str]:

    request = youtube.search().list(
        part="snippet",
        q=channel_name,
        type="channel",
        maxResults=1,
    )

    response = _execute(request)

    if not response:
        return None

    items = response.get("items", [])

    if not items:
        return None

    return items[0]["snippet"]["channelId"]


# ==========================================================
# Channel Statistics
# ==========================================================

@st.cache_data(show_spinner=False)

def get_channel_statistics(
    channel_id: str,
) -> Optional[Dict]:

    request = youtube.channels().list(
        part="snippet,statistics,brandingSettings,contentDetails",
        id=channel_id,
    )

    response = _execute(request)

    if not response:
        return None

    items = response.get("items", [])

    if not items:
        return None

    item = items[0]

    snippet = item.get("snippet", {})
    stats = item.get("statistics", {})
    branding = item.get("brandingSettings", {})
    content = item.get("contentDetails", {})

    return {

        "Channel Name":
            snippet.get("title", ""),

        "Description":
            snippet.get("description", ""),

        "Subscribers":
            int(stats.get("subscriberCount", 0)),

        "Views":
            int(stats.get("viewCount", 0)),

        "Videos":
            int(stats.get("videoCount", 0)),

        "Thumbnail":
            snippet.get(
                "thumbnails",
                {}
            ).get(
                "high",
                {}
            ).get(
                "url",
                "",
            ),

        "Country":
            snippet.get(
                "country",
                "Not Available",
            ),

        "Published":
            snippet.get(
                "publishedAt",
                "",
            ),

        "Banner":
            branding.get(
                "image",
                {}
            ).get(
                "bannerExternalUrl",
                "",
            ),

        "Uploads Playlist":
            content.get(
                "relatedPlaylists",
                {}
            ).get(
                "uploads",
                "",
            ),
    }


# ==========================================================
# Upload Playlist
# ==========================================================

@st.cache_data(show_spinner=False)

def get_upload_playlist(
    channel_id: str,
) -> Optional[str]:

    data = get_channel_statistics(channel_id)

    if not data:
        return None

    return data["Uploads Playlist"]

# ==========================================================
# Latest Video IDs
# ==========================================================

@st.cache_data(show_spinner=False)
def get_latest_video_ids(
    playlist_id: str,
    max_results: int = 10,
) -> List[str]:

    request = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlist_id,
        maxResults=max_results,
    )

    response = _execute(request)

    if not response:
        return []

    ids = []

    for item in response.get("items", []):

        resource = item.get("snippet", {}).get(
            "resourceId",
            {}
        )

        video_id = resource.get("videoId")

        if video_id:
            ids.append(video_id)

    return ids


# ==========================================================
# Video Statistics
# ==========================================================

@st.cache_data(show_spinner=False)
def get_video_statistics(
    video_ids: List[str],
) -> List[Dict]:

    if not video_ids:
        return []

    request = youtube.videos().list(
        part="snippet,statistics,contentDetails",
        id=",".join(video_ids),
    )

    response = _execute(request)

    if not response:
        return []

    videos = []

    for item in response.get("items", []):

        snippet = item.get("snippet", {})
        statistics = item.get("statistics", {})
        thumbnails = snippet.get("thumbnails", {})

        videos.append({

            "Title":
                snippet.get("title", ""),

            "Published":
                snippet.get("publishedAt", ""),

            "Views":
                int(statistics.get("viewCount", 0)),

            "Likes":
                int(statistics.get("likeCount", 0)),

            "Comments":
                int(statistics.get("commentCount", 0)),

            "Thumbnail":
                thumbnails.get(
                    "high",
                    {}
                ).get(
                    "url",
                    "",
                ),

            "Video ID":
                item.get("id", ""),

            "Video URL":
                f"https://www.youtube.com/watch?v={item.get('id','')}",

            "Duration":
                item.get(
                    "contentDetails",
                    {}
                ).get(
                    "duration",
                    "",
                ),
        })

    return videos


# ==========================================================
# Video DataFrame
# ==========================================================

def videos_to_dataframe(
    videos: List[Dict],
) -> pd.DataFrame:

    if not videos:
        return pd.DataFrame()

    return pd.DataFrame(videos)


# ==========================================================
# Average Statistics
# ==========================================================

def average_statistics(
    videos: List[Dict],
) -> Dict:

    df = videos_to_dataframe(videos)

    if df.empty:

        return {

            "Average Views": 0,
            "Average Likes": 0,
            "Average Comments": 0,
        }

    return {

        "Average Views":
            int(df["Views"].mean()),

        "Average Likes":
            int(df["Likes"].mean()),

        "Average Comments":
            int(df["Comments"].mean()),
    }


# ==========================================================
# Plotly Ready Data
# ==========================================================

def chart_dataframe(
    videos: List[Dict],
) -> pd.DataFrame:

    df = videos_to_dataframe(videos)

    if df.empty:
        return df

    numeric = [
        "Views",
        "Likes",
        "Comments",
    ]

    for col in numeric:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce",
        ).fillna(0)

    return df

# ==========================================================
# Top Videos
# ==========================================================

@st.cache_data(show_spinner=False)
def get_top_videos(
    channel_id: str,
    limit: int = 20,
) -> List[Dict]:

    playlist = get_upload_playlist(channel_id)

    if not playlist:
        return []

    ids = get_latest_video_ids(
        playlist,
        max_results=limit,
    )

    videos = get_video_statistics(ids)

    videos.sort(
        key=lambda video: video.get("Views", 0),
        reverse=True,
    )

    return videos


# ==========================================================
# Engagement Rate
# ==========================================================

def add_engagement_rate(
    videos: List[Dict],
) -> List[Dict]:

    updated = []

    for video in videos:

        views = int(video.get("Views", 0))
        likes = int(video.get("Likes", 0))
        comments = int(video.get("Comments", 0))

        if views > 0:
            engagement = ((likes + comments) / views) * 100
        else:
            engagement = 0

        item = dict(video)
        item["Engagement Rate"] = round(engagement, 2)

        updated.append(item)

    return updated


# ==========================================================
# Channel Summary
# ==========================================================

@st.cache_data(show_spinner=False)
def get_channel_summary(
    channel_id: str,
):

    channel = get_channel_statistics(channel_id)

    if not channel:
        return None, []

    playlist = channel.get("Uploads Playlist")

    if not playlist:
        return channel, []

    ids = get_latest_video_ids(
        playlist,
        max_results=10,
    )

    videos = get_video_statistics(ids)

    videos = add_engagement_rate(videos)

    return channel, videos


# ==========================================================
# Dashboard Analytics
# ==========================================================

def get_dashboard_analytics(
    channel_id: str,
) -> Dict:

    channel, videos = get_channel_summary(channel_id)

    stats = average_statistics(videos)

    top_videos = sorted(
        videos,
        key=lambda x: x["Views"],
        reverse=True,
    )[:5]

    return {

        "channel": channel,

        "videos": videos,

        "top_videos": top_videos,

        "chart_data": chart_dataframe(videos),

        "average_statistics": stats,
    }


# ==========================================================
# Public API
# ==========================================================

__all__ = [

    "search_channel",

    "get_channel_statistics",

    "get_upload_playlist",

    "get_latest_video_ids",

    "get_video_statistics",

    "videos_to_dataframe",

    "average_statistics",

    "chart_dataframe",

    "add_engagement_rate",

    "get_top_videos",

    "get_channel_summary",

    "get_dashboard_analytics",
]