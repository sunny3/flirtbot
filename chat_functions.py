import openai
from promts import JUDGE_PROMT
from copy import deepcopy
import json
        
def generate_response(message_idx, mindsets_queue, history=[]):
    '''Main FlirtBot function'''
    if mindsets_queue[0][1] == message_idx:
        # trigger message number, change FlirtyBot instructions
        history.pop(0)
        mindsets_queue.popleft()
        history.insert(0, mindsets_queue[0][0])
    resp = openai.ChatCompletion.create(
        model="gpt-4",  # Use the appropriate engine
        messages=history,  # Pass the entire history as messages
        temperature=0.2,
        top_p=0.1
    )
    return resp['choices'][0]['message']['content']

def generate_test_message(history):
    '''Main TestBot (which communicate with FlirtBot) function'''
    resp = openai.ChatCompletion.create(
        model="gpt-4",  
        messages=history,  
        temperature=0.7,
        top_p=0.8 # for creative writing
    )
    return resp['choices'][0]['message']['content']

def generate_judgment(history_flirty_bot):
    conv_to_judge = deepcopy(history_flirty_bot)
    conv_to_judge.pop(0)
    conv_to_judge.insert(0, JUDGE_PROMT)
    resp = openai.ChatCompletion.create(
            model="gpt-4", 
            messages=conv_to_judge,  
            temperature=0.2,
            top_p=0.1
        )
    judgment = json.loads(resp['choices'][0]['message']['content'])
    return judgment