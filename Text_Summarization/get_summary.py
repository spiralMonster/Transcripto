from transformers import pipeline

def GetSummary(input_text):
    total_words=len(input_text.split(" "))
    min_length=int(0.4*total_words)
    max_length=int(0.6*total_words)

    summarizer=pipeline("summarization",model="t5-small")
    summary=summarizer(input_text,max_length=max_length,min_length=min_length,do_sample=True)
    print("Summary of text returned successfully.....")
    return summary[0]['summary_text']

