import streamlit as st
from lesson_material_generator import generate_and_save_lesson_materials
from config import STREAMLIT_HOST, STREAMLIT_PORT
from gpt_assistant import interact_with_assistant, run_chat, get_assistant, get_messages_in_chat, start_new_chat,get_chat, client, assistant_id_to_use, add_message

# Set the Streamlit configurations
st.set_page_config(page_title="AI Lesson Plan Generator", page_icon=":books:")

def main():
    st.title("AI Lesson Plan Generator")
    st.write("Welcome to the AI Lesson Plan Generator. Please provide the following details to generate a lesson plan.")

    # Input for the user's message
    user_message = st.text_input("Your Lesson Topic", "Enter the topic you'd like to teach here")

    # Button to send the message
    if st.button("Send Answer"):
        if user_message:
            # Start a new chat
            thread = start_new_chat(client)

            # Save the thread id in the session state
            st.session_state.thread_id = thread.id

             # Add the user's message to the thread
            new_message = add_message(client, thread, user_message)
            print(new_message)

            # Run the thread with the assistant with the new message
            run = run_chat(client, thread, get_assistant(client, assistant_id_to_use))
            print(f"Run created with ID: {run.id}")

            # Retrieve the chat history
            history = get_messages_in_chat(client, thread)
            messages = history.data[::-1]
            for i in messages:
                print(i.role.upper() + ": "+ i.content[0].text.value)
        else:
            st.error("Please enter a message.")

    # Button to get messages in chat
    if st.button("Generate lesson plan"):
        if 'thread_id' in st.session_state:
            # Retrieve existing thread
            thread = get_chat(client, st.session_state.thread_id)

            # Get messages in chat
            messages = get_messages_in_chat(client, thread)

            # Display the entire thread
            for message in messages.data[::-1]:
                role = message.role.upper()
                content = message.content[0].text.value
                st.write(f"{role}: {content}")
        else:
            st.error("No thread id found. Please send a message first.")

if __name__ == "__main__":
    main()