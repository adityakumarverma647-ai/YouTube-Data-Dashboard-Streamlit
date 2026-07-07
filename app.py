import streamlit as st
import pandas as pd
import plotly.express as px

from utils.youtube_api import (
    search_channel,
    get_channel_summary,
    get_top_videos,
)

from utils.analytics import (
    calculate_engagement,
    dashboard_summary,
    chart_data,
    top_videos,
)

from utils.helper import (
    format_number,
    convert_date,
)

from utils.config import *

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT,
    initial_sidebar_state=INITIAL_SIDEBAR_STATE,
)

# ==========================================================
# Premium Dashboard Theme
# ==========================================================

st.markdown(
    """
<style>

.main {

    background-color:#F4F7FC;

}

/* Hide Streamlit Menu */

#MainMenu{

visibility:hidden;

}

footer{

visibility:hidden;

}

header{

visibility:hidden;

}

/* Section Title */

.section-title{

font-size:30px;

font-weight:700;

color:#F8FAFC;

margin-top:20px;

margin-bottom:18px;

letter-spacing:0.5px;

}

/* Premium Card */

.premium-card{

background:white;

padding:22px;

border-radius:18px;

box-shadow:0px 5px 18px rgba(0,0,0,.08);

border:1px solid #ECECEC;

margin-bottom:20px;

transition:.3s;

}

.premium-card:hover{

transform:translateY(-3px);

box-shadow:0px 8px 25px rgba(0,0,0,.12);

}

</style>
""",
    unsafe_allow_html=True,
)

# ==========================================================
# Premium Header
# ==========================================================

st.info(
    """
📌 **Project**

Professional YouTube Analytics Dashboard

✔ Search any public YouTube channel

✔ Analyze engagement

✔ Explore latest uploads

✔ Interactive Plotly charts

✔ Download analytics as CSV
"""
)

st.markdown(
    """
    <div style="
        background:linear-gradient(90deg,#FF0000,#C1121F);
        padding:30px;
        border-radius:18px;
        color:white;
        text-align:center;
        margin-bottom:25px;
    ">

    <h1 style="margin-bottom:8px;">
        📺 YouTube Analytics Dashboard
    </h1>

    <h4 style="margin-top:0;">
        Professional Streamlit Dashboard using
        YouTube Data API v3
    </h4>

    <p style="font-size:17px;">
        Analyze any public YouTube channel,
        visualize performance,
        explore engagement,
        and download analytics.
    </p>

    </div>
    """,
    unsafe_allow_html=True,
)

# ==========================================================
# Premium Sidebar
# ==========================================================

with st.sidebar:

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/b/b8/YouTube_Logo_2017.svg",
        use_container_width=True,
    )

    st.markdown("## 🔍 Channel Search")

    st.markdown(
        """
        Search any **public YouTube channel**
        and instantly view professional analytics.
        """
    )

    st.divider()

    channel_name = st.text_input(
        "Channel Name",
        placeholder=SEARCH_PLACEHOLDER,
    )

    search = st.button(
        "🚀 Analyze Channel",
        use_container_width=True,
    )

    st.divider()

    st.markdown("### 📊 Dashboard Features")

    st.markdown("""
- 📈 Interactive Charts
- 📊 KPI Cards
- 🎥 Latest Videos
- 🏆 Top Videos
- ❤️ Engagement Analytics
- 📥 CSV Export
""")

    st.divider()

    st.success("🟢 YouTube API Connected")

st.markdown("---")

st.markdown("### 💡 Quick Tips")

st.info(
    """
✔ Search any public YouTube channel

✔ Examples:
- MrBeast
- T-Series
- TED
- NASA
- Google
"""
)

st.markdown("---")

st.caption("🚀 Dashboard Version 4")
st.markdown("---")

st.caption(
    "Built for Internship Project"
)
# ==========================================================
# Welcome Screen
# ==========================================================

if not search:

    st.markdown(
    """
    <div style="
        background:#F8F9FA;
        padding:35px;
        border-radius:15px;
        text-align:center;
        border:1px solid #E5E7EB;
    ">

    <h2>👋 Welcome</h2>

    <p style="font-size:18px;">
    Analyze any public YouTube channel with
interactive analytics, performance insights,
engagement metrics, latest uploads,
and downloadable reports.

    </p>

    </div>
    """,
    unsafe_allow_html=True,
)

    st.stop()

# ==========================================================
# Empty Search
# ==========================================================

if not channel_name.strip():

    st.warning(EMPTY_SEARCH)

    st.stop()

# ==========================================================
# Fetch Data
# ==========================================================

with st.spinner("🔍 Fetching channel data from YouTube..."):

    channel_id = search_channel(channel_name)

    if not channel_id:

        st.error(
    """
❌ Channel not found.

Please check the spelling and try again.
"""
)
        st.stop()

    channel, videos = get_channel_summary(channel_id)

    if channel is None:
        st.error("Unable to fetch channel information. Please try again.")
        st.stop()
# ==========================================================
# DataFrame
# ==========================================================

df = pd.DataFrame(videos)

df = calculate_engagement(df)

summary = dashboard_summary(df)

chart_df = chart_data(df)

top_video_df = top_videos(df)

# ==========================================================
# Banner
# ==========================================================

if channel.get("Banner"):

    st.image(
        channel["Banner"],
        use_container_width=True,
    )

# ==========================================================
# Channel Information
# ==========================================================

left, right = st.columns([1, 4])

with left:

    st.image(
        channel["Thumbnail"],
        width=180,
    )

with right:

    st.subheader(channel["Channel Name"])

    description = channel["Description"]

    if len(description) > MAX_DESCRIPTION_LENGTH:

        description = (
            description[:MAX_DESCRIPTION_LENGTH]
            + "..."
        )

    st.write(description)

# ==========================================================
# Premium KPI Cards
# ==========================================================

st.markdown(
    '<p class="section-title">📊 Channel Overview</p>',
    unsafe_allow_html=True,
)

c1, c2, c3, c4 = st.columns(4)

cards = [

    ("👥", "Subscribers", format_number(channel["Subscribers"])),

    ("👁️", "Total Views", format_number(channel["Views"])),

    ("🎥", "Videos", format_number(channel["Videos"])),

    ("🌍", "Country", channel["Country"]),

]

for col, (icon, title, value) in zip(
    [c1, c2, c3, c4],
    cards,
):

    with col:

        st.markdown(
            f"""
<div style="
background:#111827;
border-radius:18px;
padding:24px;
text-align:center;
box-shadow:0px 5px 15px rgba(0,0,0,.35);
border:1px solid #2E3A4E;
min-height:170px;
">

<div style="
font-size:34px;
margin-bottom:12px;
">
{icon}
</div>

<div style="
font-size:20px;
font-weight:600;
color:white;
margin-bottom:18px;
">
{title}
</div>

<div style="
font-size:42px;
font-weight:bold;
color:#38BDF8;
">
{value}
</div>

</div>
""",
            unsafe_allow_html=True,
        )

st.divider()
# ==========================================================
# Analytics Summary
# ==========================================================

st.markdown(
    '<p class="section-title">📈 Analytics Summary</p>',
    unsafe_allow_html=True,
)

k1, k2, k3, k4 = st.columns(4)

analytics_cards = [

    (
        "📊 Avg Views",
        format_number(summary["Average Views"])
    ),

    (
        "👍 Avg Likes",
        format_number(summary["Average Likes"])
    ),

    (
        "💬 Avg Comments",
        format_number(summary["Average Comments"])
    ),

    (
        "❤️ Engagement",
        f'{summary["Average Engagement"]:.2f}%'
    )

]

for col, (title, value) in zip(
    [k1, k2, k3, k4],
    analytics_cards,
):

    with col:

        st.markdown(
            f"""
            <div style="
                background:#111827;
                color:white;
                padding:22px;
                border-radius:18px;
                text-align:center;
                min-height:145px;
                box-shadow:0 4px 10px rgba(0,0,0,0.35);
            ">

            <h4>{title}</h4>

            <h2 style="color:#38BDF8;">
            {value}
            </h2>

            </div>
            """,
            unsafe_allow_html=True,
        )

st.divider()

# ==========================================================
# Channel Insights
# ==========================================================

st.markdown(
    '<p class="section-title">🧠 Channel Insights</p>',
    unsafe_allow_html=True,
)

if not chart_df.empty:

    highest_views = chart_df.loc[
        chart_df["Views"].idxmax()
    ]

    highest_likes = chart_df.loc[
        chart_df["Likes"].idxmax()
    ]

    highest_comments = chart_df.loc[
        chart_df["Comments"].idxmax()
    ]

    highest_engagement = chart_df.loc[
        chart_df["Engagement Rate"].idxmax()
    ]

    col1, col2 = st.columns(2)

    with col1:

        st.success(
            f"""
🏆 **Best Performing Video**

**{highest_views['Title']}**

👁 Views :
{format_number(highest_views['Views'])}
"""
        )

        st.info(
            f"""
👍 **Most Liked Video**

**{highest_likes['Title']}**

Likes :
{format_number(highest_likes['Likes'])}
"""
        )

    with col2:

        st.warning(
            f"""
💬 **Most Commented Video**

**{highest_comments['Title']}**

Comments :
{format_number(highest_comments['Comments'])}
"""
        )

        st.error(
            f"""
❤️ **Highest Engagement**

**{highest_engagement['Title']}**

Engagement :
{highest_engagement['Engagement Rate']:.2f}%
"""
        )

    st.divider()
    st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# Performance Summary
# ==========================================================

performance_score = 0

if summary["Average Engagement"] >= 10:
    performance_score = 95

elif summary["Average Engagement"] >= 7:
    performance_score = 88

elif summary["Average Engagement"] >= 5:
    performance_score = 80

elif summary["Average Engagement"] >= 3:
    performance_score = 72

else:
    performance_score = 60


left, right = st.columns([1, 2])

with left:

    st.metric(
        "⭐ Performance Score",
        f"{performance_score}/100"
    )

with right:

    if performance_score >= 90:

        st.success(
            "Excellent channel performance with outstanding audience engagement."
        )

    elif performance_score >= 80:

        st.info(
            "Strong overall channel performance with healthy audience interaction."
        )

    elif performance_score >= 70:

        st.warning(
            "Good performance, but engagement can be improved."
        )

    else:

        st.error(
            "Channel engagement is relatively low compared to recent uploads."
        )

st.divider()

# ==========================================================
# Dashboard Tabs
# ==========================================================

overview_tab, analytics_tab, videos_tab = st.tabs(
    [
        "📊 Overview",
        "📈 Analytics",
        "🎥 Videos",
    ]
)

# ==========================================================
# Professional Views Chart
# ==========================================================
with overview_tab:
    st.markdown(
    '<p class="section-title">📊 Video Views Analysis</p>',
    unsafe_allow_html=True,
)

if not chart_df.empty:

    fig = px.bar(
        chart_df,
        x="Title",
        y="Views",
        color="Views",
        text="Views",
        color_continuous_scale="Reds",
    )

    fig.update_traces(
        texttemplate="%{text:,}",
        textposition="outside",
        hovertemplate="<b>%{x}</b><br>Views: %{y:,}<extra></extra>",
    )

    fig.update_layout(

        height=520,

        plot_bgcolor="white",

        paper_bgcolor="white",

        title=dict(
            text="Latest Video Performance",
            x=0.5,
            font=dict(size=24)
        ),

        xaxis=dict(
            tickangle=-35,
            showgrid=False,
            title=""
        ),

        yaxis=dict(
            title="Views",
            gridcolor="#ECECEC"
        ),

        coloraxis_showscale=False,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )
    st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# Professional Engagement Chart
# ==========================================================

with analytics_tab:

    st.markdown(
    '<p class="section-title">❤️ Engagement Analysis</p>',
    unsafe_allow_html=True,
)
if not chart_df.empty:

    fig2 = px.scatter(

        chart_df,

        x="Likes",

        y="Comments",

        size="Views",

        color="Engagement Rate",

        hover_name="Title",

        color_continuous_scale="Turbo",

    )

    fig2.update_layout(

        height=520,

        plot_bgcolor="white",

        paper_bgcolor="white",

        title=dict(
            text="Likes vs Comments",
            x=0.5,
            font=dict(size=24)
        ),

        xaxis_title="Likes",

        yaxis_title="Comments",

    )

    fig2.update_traces(
        marker=dict(
            line=dict(width=1, color="black")
        )
    )

    st.plotly_chart(
        fig2,
        use_container_width=True,
    )
    st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# Top Videos
# ==========================================================
with videos_tab:

    st.markdown(
    '<p class="section-title">🏆 Top Videos</p>',
    unsafe_allow_html=True,
)

if not top_video_df.empty:

    top_display = top_video_df[
        [
            "Title",
            "Views",
            "Likes",
            "Comments",
            "Engagement Rate",
        ]
    ].copy()

    st.dataframe(
        top_display,
        use_container_width=True,
    )
    st.markdown("<br>", unsafe_allow_html=True)

st.divider()

# ==========================================================
# Latest Videos Data
# ==========================================================

st.markdown(
    '<p class="section-title">📄 Latest Videos Dataset</p>',
    unsafe_allow_html=True,
)

display_df = chart_df.copy()

if not display_df.empty:

    display_df["Published"] = display_df[
        "Published"
    ].apply(convert_date)

    st.dataframe(
        display_df,
        use_container_width=True,
    )

    csv = display_df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        "⬇ Download CSV",
        csv,
        file_name=CSV_FILENAME,
        mime="text/csv",
        use_container_width=True,
    )
    st.markdown("<br>", unsafe_allow_html=True)

st.divider()

# ==========================================================
# Premium Video Gallery
# ==========================================================

st.markdown(
    '<p class="section-title">🎥 Latest Uploaded Videos</p>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    Browse the latest uploads with detailed performance metrics.
    """
)

for index, video in display_df.iterrows():

    st.markdown(
        f"""
        <div style="
            background:white;
            border-radius:18px;
            padding:18px;
            margin-bottom:20px;
            box-shadow:0px 3px 12px rgba(0,0,0,0.10);
            border:1px solid #ECECEC;
        ">
        </div>
        """,
        unsafe_allow_html=True,
    )

    image_col, info_col = st.columns([1, 2.6])

    with image_col:

        st.image(
            video["Thumbnail"],
            use_container_width=True,
        )

    with info_col:

        st.markdown(
            f"### {video['Title']}"
        )

        st.caption(
            f"📅 Published : {video['Published']}"
        )

        a, b, c, d = st.columns(4)

        a.metric(
            "👁 Views",
            format_number(video["Views"])
        )

        b.metric(
            "👍 Likes",
            format_number(video["Likes"])
        )

        c.metric(
            "💬 Comments",
            format_number(video["Comments"])
        )

        d.metric(
            "❤️ Engagement",
            f"{video['Engagement Rate']:.2f}%"
        )

        st.link_button(
            "▶ Watch on YouTube",
            video["Video URL"],
            use_container_width=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# Premium Footer
# ==========================================================

st.markdown("---")

st.markdown(
    """
<div style="
text-align:center;
padding:25px;
border-radius:15px;
background:linear-gradient(90deg,#202124,#3C4043);
color:white;
">

<h3 style="margin-bottom:10px;">
🚀 YouTube Analytics Dashboard
</h3>

<p>
Developed by <b>Aditya Kumar Verma</b>
</p>

<p>
Python • Streamlit • Plotly • Pandas •
YouTube Data API v3
</p>

<p style="font-size:13px;color:#DADCE0;">
Internship Project 2026
</p>

</div>
""",
    unsafe_allow_html=True,
)
