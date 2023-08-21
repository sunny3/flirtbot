# GPT-based Flirty Bot

Welcome to the GPT-based Flirty Bot repository! The main idea behind my approach is to dynamically adjust the system message (the first message in the history of a conversation, for example `{"role": "system", "content": "you are a helpful assistant"}` is a system message) based on specific stages defined in the project's requirements.

## Approach

The chatbot's system message undergoes dynamic changes throughout the conversation, aligned with three distinct stages specified in the project guidelines. These variations are triggered by message numbers assigned to each customer interaction (each message from a user are put into the history 
with serial number). Depending on these numbers, the chatbot may adapt its behavior or modify the system message to enhance the user experience. I use a gpt-4 from openai via API and do all my customization of a gpt with promts.

## Promts
The main idea: drop the default GPT behavior with 1) adopted personality 2) instructions like "your main goal is to communicate, not to provide help". Set human-like behavior. And take into account the serial number of the user message. 

The chatbot embodies a fictional 24-year-old woman living in vibrant San Francisco. As the conversation progresses (typically after the 28th message), the chatbot skillfully engages the user by inquiring about their desired relationship format, be it romantic or a deep and meaningful friendship.

## Evaluation

To assess the bot's performance, an evaluation process is detailed in the accompanying Jupyter Notebook (`evaluation.ipynb`). The evaluation methodology is built upon a test bot that interacts with the primary bot, and an adjudicator bot that evaluates the conversation and provides insightful reasoning. Test bot with specific promt interact with FlirtBot and make a conversation, which then is judged by judgment bot, who rank a conversation between 1 and 10 and give an explonation of it's decision. This evaluation methodology draws inspiration from the GPT-4-based technique featured in the Qlora article. While human evaluation stays also the best way to mesuare the perfomance before going to production, automatic evaluation can be good in imporving promts.

## Getting Started
To begin experimenting with the bot's behavior, paste api_key openai and execute the `run_flirtbot.py` script. You can also opt to run the bot within a Docker container using the following steps:

1. Build the Docker image: `docker build -t flirty_bot .`
2. Launch the Docker container: `docker run -d --name flirty_bot flirty_bot`
3. Gain access to the container's shell: `docker exec -it flirty_bot bash`

For a more user-friendly interaction, it is advisable to communicate with the bot directly from the console. 

## Usage

The bot boasts a user-friendly command-line interface, enabling you to engage in lifelike conversations. To initiate a conversation, simply execute the `run_flirtbot.py` script and follow the prompts. Start by introducing yourself and sharing a bit about your background, and then proceed to exchange warm and meaningful messages.

![Example_conversation](example_conversation.png)
