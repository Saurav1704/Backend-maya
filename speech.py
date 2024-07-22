import speech_recognition as sr
def recognize_speech(st):
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
# initialize the return variables
    text = error  = ''
    with microphone as source:
        # st.write("Listening...")
        audio = recognizer.listen(source)

    try:
        # st.write("Recognizing...")
        text = recognizer.recognize_google(audio)
        # st.write(f"Recognized text: {text}")
        return text
    except sr.UnknownValueError:
        error = "Sorry, I could not understand the audio."
    except sr.RequestError as e:
        # st.write(f"Could not request results; {e}")
        error=  f"Could not request results; {e}"
    return text,error
    