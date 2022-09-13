import streamlit as st
import requests
import pandas as pd
import json

st.title('Annotation Explorer')

tag_choice = st.sidebar.selectbox("Tags", options=["Aaptos aaptos", "Corallis polyporum",
                                                   "Hypodytes carinatus", "Lichen ater",
                                                   "Lydia annulipes", "Poritella decidua",
                                                   "Verrucula maritimaria"])



@st.cache
def get_data():
    init_ann_res = requests.get("http://18.232.136.117:5000/api/noaa/annotations")
    annotations_text = init_ann_res.text
    annotations_json = json.loads(annotations_text)
    annotations_flat = pd.json_normalize(annotations_json['features'], max_level=2)
    annotations_final = annotations_flat
    return annotations_final

df = get_data()

annotation_data = df[[isinstance(x, dict) and (tag_choice in x.keys()) for x in df['properties.metadata.tags']]]

images = annotation_data[annotation_data['properties.metadata.S3Key'].str.contains(".JPG")]

image_list = []
for i in images['properties.metadata.S3Key']:
    image_list.append("https://d9we9npuc9dc.cloudfront.net/{}".format(i))

st.image(image_list)
