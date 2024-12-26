import streamlit as st
from Youtube_Summarizer.get_text_from_video import GetTextFromVideo
from Text_Summarization.get_summary import GetSummary
from Wikipedia_Summarizer.get_summary_wiki import GetSummaryWiki



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
    url=st.text_input("Enter the url of wikipedia page")
    c1, c2, c3, c4, c5 = st.columns([1, 2, 2, 1, 1])
    with c3:
        button = st.button("Enter")

    b3 = st.sidebar.button("Go to Home page")
    if b3:
        navigate_page("Home")

    if "wiki_summary" not in st.session_state:
        st.session_state.wiki_summary=None

    if button:
        st.session_state.wiki_summary=GetSummaryWiki(url)
        for topic in st.session_state.wiki_summary.keys():
            with st.expander(topic):
                st.write(st.session_state.wiki_summary[topic])






