from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

import time
import threading

X = 5
time_started = time.time()
running = True # 线程的运行状态
pause_event = threading.Event() # 用于控制线程的暂停和继续

def timecheck():
    global time_started, running
    time_check = 0
    while running:
        pause_event.wait()
        if time.time() > time_started + X:
            print("time up")
            time_started = time.time()
            continue  # or raise TimeoutException()
        print (time_check) # do whatever you need to do
        time.sleep(1)
        time_check += 1

t1 = threading.Thread(target=timecheck)



template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="llama3.2")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    global time_started, running

    t1.start()

    context = ""
    print("Welcome to the AI ChatBot, Type 'exit' to quit.")
    while True:
        user_input = input("You:")
        print("reset time")
        pause_event.clear() # 清除事件，线程将会阻塞

        if user_input.lower() == "exit":
            print("Bye, have a nice day!")
            break
        result = chain.invoke({"context": context, "question": user_input})
        print("Bot: ", result)
        pause_event.set() # 设置事件，允许线程继续运行
        time_started = time.time()
        context += f"\nUser: {user_input}\nAI: {result}"

if __name__ =="__main__":
    handle_conversation()