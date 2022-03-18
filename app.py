import os
import installer
import speech_recognition as sr
import pyttsx3 as tts
import datetime

def speak(audio):
    engine = tts.init()
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')

        if "minikube start" in query:
            # speak('What driver do you want to use? (ex: hyperv, virtualbox)')
            # driver = query.split(' ')[-1]
            # print(driver)
            os.system('minikube start')
            speak("Minikube Started Successfully")
        elif "minikube stop" in query:
            os.system('minikube stop')
            speak("Minikube Stopped Successfully")
        elif "minikube status" in query:
            os.system('minikube status')
            speak("Minikube Status")
        elif "minikube delete" in query:
            os.system('minikube delete')
            speak("Minikube deleted Successfully")
        elif "get pods" in query:
            os.system('kubectl get pods')
            speak("Pods")
        elif "get services" in query:
            os.system('kubectl get svc')
            speak("Services ")
        elif "get nodes" in query:
            os.system('kubectl get nodes')
            speak("Nodes")
        elif "get deploy" in query:
            os.system('kubectl get deployments')
            speak("Deployments")
        elif "create deployment" in query:
            current_dir = os.getcwd()
            os.system('kubectl apply -f ' + current_dir + '\\deployment.yaml')
            speak("Deployment Created Successfully")
        elif "delete deployment" in query:
            speak("Which deployment do you want to delete?")
            deploy_name = query.split()[-1]
            os.system('kubectl delete deployment ' + deploy_name)
            speak("Deployment Deleted Successfully")
        elif "create service" in query:
            current_dir = os.getcwd()
            os.system('kubectl apply -f ' + current_dir + '\\service.yaml')
            speak("Service Created Successfully")
        elif "delete service" in query:
            speak("Which service do you want to delete?")
            svc_name = query.split()[-1]
            os.system('kubectl delete service ' + svc_name)
            # os.system('kubectl delete service --all')
            speak("Service Deleted Successfully")
        elif "close" in query:
            exit()
        else:
            print("I didn't get that")
            speak("I didn't get that")
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def main():
    command = takeCommand()
    speak(command)


if __name__ == "__main__":
    while True:
        main()

