import torch
from transformers import AutoModelForSeq2SeqLM,AutoTokenizer
from IndicTransToolkit import IndicProcessor

def get_translation(text,tgt_lang):
    model_name = "ai4bharat/indictrans2-en-indic-1B"

    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name, trust_remote_code=True)
    ip=IndicProcessor(inference=True)

    device="cuda" if torch.cuda.is_available() else "cpu"
    model=model.to(device)

    input_text=[text]

    batch=ip.preprocess_batch(input_text,src_lang="eng_Latn",tgt_lang=tgt_lang)
    batch=tokenizer(batch,
                    return_tensors="pt",
                    truncation=True,
                    padding="longest",
                    max_length=256)

    with torch.inference_mode():
        outputs=model.generate(**batch,num_beams=5,num_return_sequences=1,max_length=256)

    with tokenizer.as_target_tokenizer():
        outputs=tokenizer.batch_decode(outputs,clean_up_tokenization_spaces=True,skip_special_tokens=True)

    translations=ip.postprocess_batch(outputs,lang=tgt_lang)
    print(f"Summary in {tgt_lang} returned...")
    return translations[0]




if __name__=="__main__":
    tgt_lng="hin_Deva"
    text="How are you?"
    translation=get_translation(text,tgt_lng)
    print(translation)