import streamlit as st
from Youtube_Summarizer.get_text_from_video import GetTextFromVideo
from Text_Summarization.get_summary import GetSummary
from Wikipedia_Summarizer.get_summary_wiki import GetSummaryWiki
from Text_Translation.translate_text import get_translation



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

    if "lang" not in st.session_state:
        st.session_state.lang=None

    if "hin_summary" not in st.session_state:
        st.session_state.hin_summary=None

    if "mar_summary" not in st.session_state:
        st.session_state.mar_summary=None

    if "tamil_summary" not in st.session_state:
        st.session_state.tamil_summary=None

    if "telgu_summary" not in st.session_state:
        st.session_state.telgu_summary=None


    tab1,tab2,tab3=st.tabs(['Get Actual Text','Get Summary','Get Related Videos'])

    for _ in range(10):
        st.empty()
    if button:
        st.session_state.data=GetTextFromVideo(video_url)
        st.session_state.summary=GetSummary(st.session_state.data)

        st.session_state.hin_summary = get_translation(st.session_state.summary, "hin_Deva")
        st.session_state.mar_summary = get_translation(st.session_state.summary, "mar_Deva")
        st.session_state.tamil_summary = get_translation(st.session_state.summary,"tam_Taml" )
        st.session_state.telgu_summary = get_translation(st.session_state.summary, "tel_Telu")



    for _ in range(10):
        st.empty()


    with tab1:
        b1=st.button("Get actual text")

    with tab2:
        option = ["English", "Hindi", "Marathi", "Tamil","Telugu"]
        st.session_state.lang= st.selectbox("Choose the language for summary generation", option)
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

            if st.session_state.lang=="English":
                st.write(st.session_state.summary)

            elif st.session_state.lang=="Hindi":
                st.write(st.session_state.hin_summary)

            elif st.session_state.lang=="Marathi":
                st.write(st.session_state.mar_summary)

            elif st.session_state.lang=="Tamil":
                st.write(st.session_state.tamil_summary)

            elif st.session_state.lang=="Telugu":
                st.write(st.session_state.telgu_summary)


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






