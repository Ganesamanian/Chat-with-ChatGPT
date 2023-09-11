#!/usr/bin/env python
# coding: utf-8

# In[1]:


import openai

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
api_key = 'Your API KEY'

# Initialize the OpenAI API client
openai.api_key = api_key

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can use other engines like "text-davinci-001" or "davinci-codex"
        prompt=prompt,
        max_tokens=150,  # You can adjust this value to control the response length
    )
    return response.choices[0].text.strip()

# Main loop for chatting
user_input = input("You: ")
    
# if user_input.lower() == "quit":
#     break
    
# Chat with GPT-3
response = chat_with_gpt(user_input)
    
print("ChatGPT:", response)


# In[ ]:




