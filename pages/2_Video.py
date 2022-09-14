import streamlit as st
from annotation_explorer import get_data
import pandas as pd

# Set page title
st.title("Video")

# Create dropdown for tags
# tag_choice = st.sidebar.selectbox("Tags", options=["Aaptos aaptos", "Corallis polyporum",
#                                                    "Hypodytes carinatus", "Lichen ater",
#                                                    "Lydia annulipes", "Poritella decidua",
#                                                    "Verrucula maritimaria"])

# Get data
df = get_data()

# Limit to proper dictionaries
annotation_data = df[[isinstance(x, dict) for x in df['properties.metadata.tags']]]

# Add keys for mp4 videos (just for testing)
annotation_data['properties.metadata.S3Key'].iloc[3] = "EX1708/EX1708_VID_20170921T220500Z_ROVHD_Low.mp4" # for testing
annotation_data['properties.metadata.S3Key'].iloc[11] = "EX1708/EX1708_VID_20170921T220500Z_ROVHD_Low.mp4" # for testing

# Limit to mp4 files
videos = annotation_data[annotation_data['properties.metadata.S3Key'].str.contains(".mp4")]
# videos = pd.concat([mp4, annotation_data[annotation_data['properties.metadata.S3Key'].str.contains(".mp4")]])

keys = pd.json_normalize(videos['properties.metadata.tags']).columns

tag_choice = st.sidebar.selectbox("Tags", options= keys)

# Create list of Cloudfront URLs
video_list = []
for i in videos['properties.metadata.S3Key']:
    video_list.append("https://d9we9npuc9dc.cloudfront.net/{}".format(i))

# Create video-selector dropdown
video_choice = st.sidebar.number_input("Which Video?", max_value=len(video_list))

# Plot Videos
try:
    st.video(video_list[video_choice])
except:
    st.text("Try Another Video")

# TESTING
# for i in video_list:
#     st.video(i)
