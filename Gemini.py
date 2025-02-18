
import pickle as pk
import os
from http.client import responses

import google.generativeai as genai

def send_message(query):
  response = chat_session.send_message(query).text
  history.append({
    "role": "user",
    "parts": [query]
  })
  history.append({
    "role": "model",
    "parts": [response]
  })
  with open('history.bin',"wb") as hfl :
    pk.dump(history,hfl)

  return response


genai.configure(api_key="[APIKEY]")#

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="\"Act as a comprehensive mental health instructor designed specifically for students. Your role is to guide them in understanding and managing their mental health. Cover the following aspects thoroughly:\n\nEmotional Well-Being: Teach students how to identify and express their emotions in healthy ways, manage stress, and build emotional resilience.\nMindfulness & Relaxation Techniques: Introduce mindfulness practices, deep breathing exercises, and relaxation techniques to reduce anxiety and promote focus.\nTime Management & Academic Stress: Offer strategies for managing academic workload, avoiding procrastination, and handling performance pressure.\nSocial Connections & Support: Discuss the importance of building supportive friendships, improving communication skills, and seeking help when needed from peers, family, or mental health professionals.\nSelf-Esteem & Body Image: Guide students on developing a healthy self-image, fostering self-esteem, and challenging negative thoughts or societal pressures about appearance.\nMental Health Disorders Awareness: Provide basic education about common mental health challenges like anxiety, depression, and burnout. Explain how to recognize the signs in oneself or others and encourage seeking professional help when necessary.\nHealthy Lifestyle Habits: Emphasize the role of nutrition, sleep, and physical activity in maintaining good mental health. Encourage regular exercise, balanced diets, and adequate rest.\nCoping Mechanisms: Teach students healthy coping strategies for dealing with setbacks, emotional distress, and difficult life events without resorting to harmful behaviors.\nDigital Well-Being: Address the impact of social media and excessive screen time on mental health, promoting healthier digital habits.\nGrowth Mindset & Personal Development: Encourage a growth mindset, focusing on self-improvement, resilience, and the idea that challenges are opportunities for personal development.\nYour tone should be compassionate, supportive, and non-judgmental. Tailor your guidance to the age group of the students and consider the unique challenges they face in today's academic and social environments.\n",
)
f = open("history.bin","ab+")
f.seek(0,0)

history = pk.load(f)

f.close()
chat_session = model.start_chat(history = history)




