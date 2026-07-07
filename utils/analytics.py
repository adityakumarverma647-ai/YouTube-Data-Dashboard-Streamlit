"""
==========================================================
YouTube Analytics Dashboard
analytics.py
Version 3

Features
--------
✓ Engagement Rate
✓ Average Statistics
✓ KPI Calculations
✓ Plotly Ready Analytics
✓ Data Validation
✓ Modular Functions
==========================================================
"""

from __future__ import annotations

from typing import Dict

import pandas as pd


# ==========================================================
# Safe Numeric Conversion
# ==========================================================

def _numeric(df: pd.DataFrame, column: str) -> pd.Series:

    if column not in df.columns:
        return pd.Series(dtype="float64")

    return pd.to_numeric(
        df[column],
        errors="coerce"
    ).fillna(0)


# ==========================================================
# Engagement Rate
# ==========================================================

def calculate_engagement(
    df: pd.DataFrame
) -> pd.DataFrame:

    if df.empty:
        return df.copy()

    result = df.copy()

    views = _numeric(result, "Views")
    likes = _numeric(result, "Likes")
    comments = _numeric(result, "Comments")

    result["Engagement Rate"] = (
        (likes + comments)
        .div(views.where(views != 0, 1))
        * 100
    ).round(2)

    return result


# ==========================================================
# Average Views
# ==========================================================

def average_views(
    df: pd.DataFrame
) -> int:

    if df.empty:
        return 0

    return int(_numeric(df, "Views").mean())


# ==========================================================
# Average Likes
# ==========================================================

def average_likes(
    df: pd.DataFrame
) -> int:

    if df.empty:
        return 0

    return int(_numeric(df, "Likes").mean())


# ==========================================================
# Average Comments
# ==========================================================

def average_comments(
    df: pd.DataFrame
) -> int:

    if df.empty:
        return 0

    return int(_numeric(df, "Comments").mean())

# ==========================================================
# Total Statistics
# ==========================================================

def total_views(
    df: pd.DataFrame
) -> int:

    if df.empty:
        return 0

    return int(_numeric(df, "Views").sum())


def total_likes(
    df: pd.DataFrame
) -> int:

    if df.empty:
        return 0

    return int(_numeric(df, "Likes").sum())


def total_comments(
    df: pd.DataFrame
) -> int:

    if df.empty:
        return 0

    return int(_numeric(df, "Comments").sum())


# ==========================================================
# Top Videos
# ==========================================================

def top_videos(
    df: pd.DataFrame,
    n: int = 5
) -> pd.DataFrame:

    if df.empty:
        return df.copy()

    result = df.copy()

    result["Views"] = _numeric(result, "Views")

    return (
        result.sort_values(
            by="Views",
            ascending=False
        )
        .head(n)
        .reset_index(drop=True)
    )


# ==========================================================
# KPI Summary
# ==========================================================

def dashboard_summary(
    df: pd.DataFrame
) -> Dict:

    if df.empty:

        return {

            "Total Views": 0,
            "Total Likes": 0,
            "Total Comments": 0,
            "Average Views": 0,
            "Average Likes": 0,
            "Average Comments": 0,
            "Average Engagement": 0.0,

        }

    working = calculate_engagement(df)

    return {

        "Total Views":
            total_views(working),

        "Total Likes":
            total_likes(working),

        "Total Comments":
            total_comments(working),

        "Average Views":
            average_views(working),

        "Average Likes":
            average_likes(working),

        "Average Comments":
            average_comments(working),

        "Average Engagement":
            round(
                working["Engagement Rate"].mean(),
                2
            ),

    }


# ==========================================================
# Plotly Ready Data
# ==========================================================

def chart_data(
    df: pd.DataFrame
) -> pd.DataFrame:

    if df.empty:
        return df.copy()

    result = calculate_engagement(df)

    numeric_columns = [

        "Views",
        "Likes",
        "Comments",
        "Engagement Rate",

    ]

    for column in numeric_columns:

        if column in result.columns:

            result[column] = pd.to_numeric(
                result[column],
                errors="coerce"
            ).fillna(0)

    return result


# ==========================================================
# Public Exports
# ==========================================================

__all__ = [

    "calculate_engagement",

    "average_views",

    "average_likes",

    "average_comments",

    "total_views",

    "total_likes",

    "total_comments",

    "top_videos",

    "dashboard_summary",

    "chart_data",

]
