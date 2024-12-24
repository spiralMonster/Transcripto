from transformers import pipeline

def GetSummary(input_text):
    input_text=input_text.strip()
    total_words=len(input_text.split(" "))
    summarizer = pipeline("summarization", model="t5-small")
    print(total_words)
    if total_words>256:
        print("Chunking data....")
        data=[]
        text=input_text.split(" ")
        num_batch=total_words//256
        ind=0
        for _ in range(num_batch):
            inp=text[ind:ind+256]
            inp=" ".join(inp)
            summary=summarizer(inp,max_length=128,min_length=80,do_sample=False)[0]['summary_text']
            data.append(summary)
            ind+=256

        inp=text[ind:]
        length_words=len(inp)
        max_len=int(0.5*length_words)
        min_len=int(0.3*length_words)
        inp = " ".join(inp)
        summary =summarizer(inp, max_length=max_len, min_length=min_len, do_sample=False)[0]['summary_text']
        data.append(summary)
        summary=" ".join(data)
        print("Summary of text returned successfully.....")
        return summary

    else:
        min_length = int(0.3 * total_words)
        max_length = int(0.5 * total_words)
        summary = summarizer(input_text, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text']
        print("Summary of text returned successfully.....")
        return summary



if __name__=="__main__":
    with open('text.txt','r') as file:
        data=file.read()
    summary=GetSummary(data)
    print(summary)