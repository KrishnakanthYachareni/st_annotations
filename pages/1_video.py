import streamlit as st
from annotation_explorer import get_data
import pandas as pd

tag_choice = st.sidebar.selectbox("Tags", options=["Aaptos aaptos", "Corallis polyporum",
                                                   "Hypodytes carinatus", "Lichen ater",
                                                   "Lydia annulipes", "Poritella decidua",
                                                   "Verrucula maritimaria"])

df = get_data()

annotation_data = df[[isinstance(x, dict) and (tag_choice in x.keys()) for x in df['properties.metadata.tags']]]

annotation_data['properties.metadata.S3Key'].iloc[3] = "EX1708/EX1708_VID_20170921T220500Z_ROVHD_Low.mp4" # for testing
annotation_data['properties.metadata.S3Key'].iloc[4] = "EX1708/EX1708_VID_20170921T220500Z_ROVHD_Low.mp4" # for testing


mp4 = annotation_data[annotation_data['properties.metadata.S3Key'].str.contains(".mov")]
videos = pd.concat([mp4, annotation_data[annotation_data['properties.metadata.S3Key'].str.contains(".mp4")]])

video_list = []
for i in videos['properties.metadata.S3Key']:
    video_list.append("https://d9we9npuc9dc.cloudfront.net/{}".format(i))

video_choice = st.sidebar.number_input("Which Video?", 0)

st.video(video_list[video_choice])
