from promts import SYSTEM_CFG
from chat_functions import generate_response
from collections import deque
import openai
from api_key import api_key

openai.api_key = api_key
mindsets_queue = deque([[SYSTEM_CFG["initial_promt"], 4], 
                            [SYSTEM_CFG['building_relationships_promt'], 8],
                            [SYSTEM_CFG['in_relationship_promt'], None]
                       ]
                      )
history = [SYSTEM_CFG["initial_promt"]]
message_idx = 1
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    history.append({"role": "user", "content": str(message_idx) + ". " + user_input})
    chatbot_response = generate_response(message_idx, mindsets_queue, history)
    history.append({"role": "assistant", "content": chatbot_response}) 
    
    #print(f"You: {user_input}")
    print(f"Chatbot: {chatbot_response}")
    print("-"*50)
            
    message_idx+=1
    