from gtts import gTTS
import os
import datetime

def synthesize(text: str, output_dir="data/samples", filename=None):
    os.makedirs(output_dir, exist_ok=True)
    
    if filename is None:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"response_{timestamp}.mp3"
    
    output_path = os.path.join(output_dir, filename)
    
    tts = gTTS(text=text, lang='ar') 
    tts.save(output_path)
    # print(f"TTS saved to {output_path}")
    return output_path

samples = {
    "أحيانًا أحس إنّي ما لي قيمة، حتى وأنا بين أهلي. ما أعرف كيف أتخلص من هذا الشعور، ممكن تساعدني أفهم ليش أحس كذا؟":
        "Sometimes I feel worthless, even around my family. I don’t know how to get rid of this feeling. Can you help me understand why I feel this way?",

    "ما أقدر أنام الليل، الأفكار تلاحقني. أحس أني أعيش في دوامة، ومحتاج وسيلة تهديني وتريحني شوي.":
        "I can’t sleep at night; thoughts keep chasing me. I feel like I’m stuck in a loop, and I need something that helps me calm down and breathe.",

    "أكتم كل شي في قلبي، وما أعرف أتكلم. ساعدني أشرح اللي بداخلي بدون ما أتشتت.":
        "I bottle everything inside and don’t know how to talk. Help me express what’s inside me without getting overwhelmed.",

    "كل يوم أصحى بدون طاقة، حتى الأشياء اللي أحبها صارت مملة. وش تفسيرك لهالشي؟ هل هذا طبيعي؟":
        "Every day I wake up without energy, even things I used to enjoy feel dull. What’s your interpretation of this? Is this normal?",

    "أخاف أطلب مساعدة ويظنون إني ضعيف. بس قررت أتكلم معك لأني تعبت. ممكن تساعدني أبدأ من وين؟":
        "I’m afraid to ask for help because people might think I’m weak. But I decided to talk to you because I’m tired. Can you help me figure out where to start?",
}

if __name__ == "__main__":
    for ind, text in enumerate(samples.keys()):
        synthesize(text, output_dir="../data/samples", filename=f"sample{ind}.mp3")
