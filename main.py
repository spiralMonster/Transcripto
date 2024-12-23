import streamlit as st

from Extracting_text_from_video.get_text_from_video import GetTextFromVideo
from Text_Summarization.get_summary import GetSummary

st.title("Transcripto")
# st.header("Video Summarizer")
video_url=st.sidebar.text_input("Please enter the video url...")
button=st.sidebar.button("Enter")

if "data" not in st.session_state:
    st.session_state.data=None

if "summary" not in st.session_state:
    st.session_state.summary=None

if button:
    st.session_state.data=GetTextFromVideo(video_url)
    st.session_state.summary=GetSummary(st.session_state.data)

col1,col2=st.columns(2)
with col1:
    b1=st.button("Get actual text")

with col2:
    b2=st.button("Get summary of text")

if b1:
    if st.session_state.data:

        st.header("Actual Text:")
        with st.expander("Click to see the full text"):
            st.write(st.session_state.data)

    else:
        st.write("Error")





if b2:
    if st.session_state.summary:
        st.header("Summary:")
        st.write(st.session_state.summary)

    else:
        st.write("Error")






