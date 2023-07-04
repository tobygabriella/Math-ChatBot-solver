import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You will help answer math questions and give a step by step solution"}]

def Mathgpt(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    answer = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": answer})
    return answer

demo = gradio.Interface(fn=Mathgpt, inputs= "text", outputs="text", title = "Math Solver")

demo.launch(share=True)


