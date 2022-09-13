import streamlit as st
from Annotation_Explorer import get_data
#import pandas as pd


st.title('Image Annotation')

tag_choice = st.sidebar.selectbox("Tags", options=["Aaptos aaptos", "Corallis polyporum",
                                                   "Hypodytes carinatus", "Lichen ater",
                                                   "Lydia annulipes", "Poritella decidua",
                                                   "Verrucula maritimaria"])

df = get_data()

annotation_data = df[[isinstance(x, dict) and (tag_choice in x.keys()) for x in df['properties.metadata.tags']]]

images = annotation_data[annotation_data['properties.metadata.S3Key'].str.contains(".JPG")]

image_list = []
for i in images['properties.metadata.S3Key']:
    image_list.append("https://d9we9npuc9dc.cloudfront.net/{}".format(i))


st.image(image_list)