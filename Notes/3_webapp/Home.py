import streamlit as st 

st.set_page_config(page_title="Home",
                   layout='wide',
                   page_icon='./images/home.png')

st.title("YOLO V5 Object Detection App")
st.caption('This web application demostrate Object Detection')

# Content
st.markdown("""
### This App detects objects from Images
- Automatically detects 20 objects from image
- [Click here for App](/YOLO_for_image/)  

Below give are the object the our model will detect
1. With Seatbelt
2. Without Seatbelt""")