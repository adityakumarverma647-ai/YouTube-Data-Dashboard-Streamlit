"""
==========================================================
YouTube Analytics Dashboard
helper.py
Version 3

Features
--------
✓ Number Formatting
✓ Date Formatting
✓ Duration Formatting
✓ Percentage Formatting
✓ Data Validation
✓ Utility Functions
==========================================================
"""

from __future__ import annotations

from datetime import datetime


# ==========================================================
# Number Formatting
# ==========================================================

def format_number(number):

    try:
        number = float(number)
    except (TypeError, ValueError):
        return "0"

    if number >= 1_000_000_000:
        return f"{number/1_000_000_000:.1f}B"

    if number >= 1_000_000:
        return f"{number/1_000_000:.1f}M"

    if number >= 1_000:
        return f"{number/1_000:.1f}K"

    return f"{int(number)}"


# ==========================================================
# Date Formatting
# ==========================================================

def convert_date(date_string):

    if not date_string:
        return ""

    try:
        date = datetime.strptime(
            date_string,
            "%Y-%m-%dT%H:%M:%SZ"
        )

        return date.strftime("%d %b %Y")

    except Exception:
        return date_string


# ==========================================================
# Percentage Formatting
# ==========================================================

def format_percentage(value):

    try:
        return f"{float(value):.2f}%"

    except (TypeError, ValueError):
        return "0.00%"


# ==========================================================
# ISO 8601 Duration Formatting
# ==========================================================

def format_duration(duration):

    if not duration:
        return "N/A"

    duration = duration.replace("PT", "")

    hours = 0
    minutes = 0
    seconds = 0

    temp = ""

    for char in duration:

        if char.isdigit():

            temp += char

        else:

            if char == "H":
                hours = int(temp)

            elif char == "M":
                minutes = int(temp)

            elif char == "S":
                seconds = int(temp)

            temp = ""

    if hours > 0:
        return f"{hours}h {minutes}m {seconds}s"

    if minutes > 0:
        return f"{minutes}m {seconds}s"

    return f"{seconds}s"


# ==========================================================
# Safe Integer Conversion
# ==========================================================

def safe_int(value):

    try:
        return int(value)

    except (TypeError, ValueError):
        return 0


# ==========================================================
# Safe Float Conversion
# ==========================================================

def safe_float(value):

    try:
        return float(value)

    except (TypeError, ValueError):
        return 0.0


# ==========================================================
# Empty Text Handling
# ==========================================================

def clean_text(text):

    if not text:
        return "Not Available"

    return str(text).strip()


# ==========================================================
# Public Exports
# ==========================================================

__all__ = [

    "format_number",

    "convert_date",

    "format_percentage",

    "format_duration",

    "safe_int",

    "safe_float",

    "clean_text",

]