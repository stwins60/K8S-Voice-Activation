import speech_recognition as sr
import subprocess
import pyttsx3 as tts


def speak(text):
    engine = tts.init()
    engine.say(text)
    engine.runAndWait()

def listen_command(recognizer, mic):
    with mic as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"Command: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Could not understand the audio.")
        return ""
    except sr.RequestError as e:
        print(f"Error: {e}")
        return ""

def execute_command(command):
    NAMESPACE = "What is the name of the namespace?"
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    if "start minikube" in command or "start mini cube" in command or "start mini-cube" in command or "start cluster" in command or "start kubernetes" in command or "start cube" in command:
        subprocess.run(["minikube", "start"])
    elif "stop minikube" in command:
        subprocess.run(["minikube", "stop"])
    elif "delete minikube" in command:
        subprocess.run(["minikube", "delete"])
    elif "start docker" in command:
        subprocess.run(["systemctl", "start", "docker"])
    elif "stop docker" in command:
        subprocess.run(["systemctl", "stop", "docker"])
    elif "delete docker" in command:
        subprocess.run(["systemctl", "delete", "docker"])
    elif "create deployment" in command:
        speak("Which namespace should the deployment be created in?")
        namespace = listen_command(recognizer, mic)
        if namespace:
            subprocess.run(["kubectl", "create", "namespace", namespace])
        speak("What is the name of the deployment?")
        deployment_name = listen_command(recognizer, mic)
        speak("What is the name of the image?")
        image_name = listen_command(recognizer, mic)
        subprocess.run(["kubectl", "create", "deployment", deployment_name, "--image", image_name , "--namespace", namespace])
    elif "get deployments" in command:
        subprocess.run(["kubectl", "get", "deployments"])
    elif "get pods" in command:
        speak(NAMESPACE)
        namespace = listen_command(recognizer, mic)
        subprocess.run(["kubectl", "get", "pods", "--namespace", namespace])
    elif "get services" in command:
        speak(NAMESPACE)
        namespace = listen_command(recognizer, mic)
        subprocess.run(["kubectl", "get", "services", "--namespace", namespace])
    elif "get nodes" in command:
        subprocess.run(["kubectl", "get", "nodes"])
    elif "get all" in command:
        subprocess.run(["kubectl", "get", "all"])
    elif "create service" in command:
        speak("What is the name of the service?")
        service_name = listen_command(recognizer, mic)
        speak("What is the name of the port?")
        port_name = listen_command(recognizer, mic)
        speak("What is the port number?")
        port_number = listen_command(recognizer, mic)
        speak("What is the target port?")
        target_port = listen_command(recognizer, mic)
        subprocess.run(["kubectl", "expose", "deployment", service_name, "--type=NodePort", "--port", port_number, "--name", port_name, "--target-port", target_port, "--namespace", namespace])
    elif "delete deployment" in command:
        speak(NAMESPACE)
        namespace = listen_command(recognizer, mic)
        speak("What is the name of the deployment?")
        deployment_name = listen_command(recognizer, mic)
        subprocess.run(["kubectl", "delete", "deployment", deployment_name, "--namespace", namespace])
    elif "delete service" in command:
        speak("What is the name of the service?")
        service_name = listen_command(recognizer, mic)
        speak(NAMESPACE)
        namespace = listen_command(recognizer, mic)
        subprocess.run(["kubectl", "delete", "service", service_name, "--namespace", namespace])
    elif "delete pod" in command:
        speak("What is the name of the pod?")
        pod_name = listen_command(recognizer, mic)
        speak(NAMESPACE)
        namespace = listen_command(recognizer, mic)
        subprocess.run(["kubectl", "delete", "pod", pod_name, "--namespace", namespace])
    elif "delete node" in command:
        speak("What is the name of the node?")
        node_name = listen_command(recognizer, mic)
        subprocess.run(["kubectl", "delete", "node", node_name])
    elif "delete all" in command:
        speak(NAMESPACE)
        namespace = listen_command(recognizer, mic)
        subprocess.run(["kubectl", "delete", "all", "--all", "--namespace", namespace])
    elif "hello" in command:
        speak("Hello, how are you?")
    elif "exit" in command:
        exit()
    # Add more commands here if needed

def clear_previous_audio(recognizer):
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 4000

def main():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    while True:
        clear_previous_audio(recognizer)
        user_command = listen_command(recognizer, mic)
        if user_command:
            execute_command(user_command)

if __name__ == "__main__":
    main()
