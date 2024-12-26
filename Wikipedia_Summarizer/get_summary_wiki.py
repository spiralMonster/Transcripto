from Text_Summarization.get_summary import GetSummary
from Wikipedia_Summarizer.get_info_from_wiki import GetInfoFromWiki

def GetSummaryWiki(url):
    info=GetInfoFromWiki(url)
    summary={}
    for topic in info.keys():
        input_text=info[topic]
        summ=GetSummary(input_text)
        summary[topic]=summ

    print("Summary of Wikipedia Article is sent...")
    return summary
