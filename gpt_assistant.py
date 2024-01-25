from openai import OpenAI
import openai
import time
from dotenv import load_dotenv
load_dotenv() # Load .env file
from openai import OpenAI
client = OpenAI() # Initialize OpenAI Client
from config import OPENAI_API_KEY
# Set the OpenAI API key
openai.api_key = OPENAI_API_KEY
client = OpenAI()

# List assistant ID
assistant_id_to_use = "asst_UEKShOokXRXVdGOSmB8gRc24"
# List thread ID / Determine if existing thread should be used
get_previous_thread = False

def get_assistant(client, assistant_id):
    assistant = client.beta.assistants.retrieve(assistant_id)
    return assistant

# Description: "Start a new chat with a user"

def start_new_chat(client):
    empty_thread = client.beta.threads.create()
    return empty_thread

# Description: Retrieve previous chat/Thread

def get_chat(client, thread_id):
    thread = client.beta.threads.retrieve(thread_id)
    return thread

# Description: "Add a message to a chat/Thread" 

def add_message(client, thread, content):
    thread_message = client.beta.threads.messages.create(
    thread_id = thread.id,
    role="user",
    content=content,
    )
    return thread_message

# Description: "Get the previous messages in a chat/Thread"
def get_messages_in_chat(client, thread):
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    return messages

# Description: "Run the thread with the assistant"
def run_chat(client, thread, assistant):
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id,
    )

    # Poll the run status
    while True:
        run = client.beta.threads.runs.retrieve(run.id, thread_id=thread.id)
        if run.status == 'completed':
            break
        time.sleep(1)  # Wait for a second before polling again

    return run



# Call existing assistant
assistant = get_assistant(client, assistant_id_to_use) # Retrieve Assistant
print(assistant.name + " is ready to go!")

    # Retrieve existing thread
'''if get_previous_thread:
    thread = get_chat(client, thread_id_to_use)
    print("Chat retrieved with ID: " + thread.id)
    print(thread)
else:'''
thread = start_new_chat(client)
print("New chat created with ID: " + thread.id)
    # Determine new message content
    

    # Add the message into the thread
content = "What is 3x3?"
new_message = add_message(client, thread, content)
print(new_message)


# Retrieve the chat history
history = get_messages_in_chat(client, thread)
messages = history.data[::-1]
for i in messages:
        print(i.role.upper() + ": "+ i.content[0].text.value)



def chat_with_assistant(client, assistant, thread, content):
    # Add the message into the thread
    new_message = add_message(client, thread, content)

    # Run the thread with the assistant with the new message
    run = run_chat(client, thread, assistant)

    # Retrieve the chat history
    history = get_messages_in_chat(client, thread)
    messages = history.data[::-1]
    return messages


# Instead of hardcoding the content, we'll use a function to chat with the assistant
def interact_with_assistant(content, thread):
    # Call existing assistant
    assistant = get_assistant(client, assistant_id_to_use) # Retrieve Assistant

    # Get the chat messages
    messages = chat_with_assistant(client, assistant, thread, content)
    return messages