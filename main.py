# import streamlit as st
#
# from Extracting_text_from_video.get_text_from_video import GetTextFromVideo
# from Text_Summarization.get_summary import GetSummary
#
# st.title("Transcripto")
# # st.header("Video Summarizer")
# video_url=st.sidebar.text_input("Please enter the video url...")
# button=st.sidebar.button("Enter")
#
# if "data" not in st.session_state:
#     st.session_state.data=None
#
# if "summary" not in st.session_state:
#     st.session_state.summary=None
#
# if button:
#     st.session_state.data=GetTextFromVideo(video_url)
#     st.session_state.summary=GetSummary(st.session_state.data)
#
# col1,col2=st.columns(2)
# with col1:
#     b1=st.button("Get actual text")
#
# with col2:
#     b2=st.button("Get summary of text")
#
# if b1:
#     if st.session_state.data:
#
#         st.header("Actual Text:")
#         with st.expander("Click to see the full text"):
#             st.write(st.session_state.data)
#
#     else:
#         st.write("Error")
#
#
#
#
#
# if b2:
#     if st.session_state.summary:
#         st.header("Summary:")
#         st.write(st.session_state.summary)
#
#     else:
#         st.write("Error")
#
#
#
#
#
#


import streamlit as st
from git.remote import flagKeyLiteral

from Extracting_text_from_video.get_text_from_video import GetTextFromVideo
from Text_Summarization.get_summary import GetSummary






def navigate_page(page_name):
    st.session_state.page=page_name

if "page" not in st.session_state:
    st.session_state.page="Home"

if st.session_state.page=="Home":
    st.title("Transcripto")
    col1,col2=st.columns(2)

    with col1:
        b1=st.button("Summarize Wikipedia Article")

    with col2:
        b2=st.button("Summarize You-Tube Video")


    if b1:
        navigate_page("Wikipedia")

    if b2:
        navigate_page("You-Tube")


elif st.session_state.page=="You-Tube":
    st.title("Summarize You-tube Video")
    video_url = st.text_input("Please enter the video url...")
    c1,c2,c3,c4,c5 = st.columns([1, 2, 2,1,1])
    with c3:
        button=st.button("Enter")

    if "data" not in st.session_state:
        st.session_state.data=None

    if "summary" not in st.session_state:
        st.session_state.summary=None

    if button:
        st.session_state.data=GetTextFromVideo(video_url)
        st.session_state.summary=GetSummary(st.session_state.data)

    for _ in range(10):
        st.empty()
    col1, col2,col3= st.columns([10,10,10])

    with col1:
        b1=st.button("Get actual text")

    with col3:
        b2=st.button("Get summary of text")

    for _ in range(10):
        st.empty()

    b3=st.sidebar.button("Go to Home page")
    if b3:
        navigate_page("Home")
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





elif st.session_state.page=="Wikipedia":
    st.title("Wikipedia Summarizer")
    keyword=st.text_input("Enter the topic to search")
    button=st.button("Enter")

    b3 = st.sidebar.button("Go to Home page")
    if b3:
        navigate_page("Home")

    if button:
        st.write("In development")






