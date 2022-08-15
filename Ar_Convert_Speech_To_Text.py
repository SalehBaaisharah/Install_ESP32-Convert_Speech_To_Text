from gtts import gTTS
from playsound import playsound
import speech_recognition as SR
r=SR.Recognizer()
with SR.Microphone() as source:
    print('تحدث...')
    audio=r.listen(source)
try:
    t=r.recognize_google(audio,language='ar-AR')
    print(t)
    f=open('text.txt','a',encoding='utf-8')
    f.writelines(t+'\n')
    f.close()
    obj=gTTS(text=t,lang='ar',slow=False)
    obj.save('text.mp3')
    playsound('text.mp3')
except SR.UnknownValueError as U:
    print(U)
except SR.RequestError as R:
    print(R)