import streamlit as st
import openai

# Set up OpenAI API credentials
openai.api_key = "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"

# Define the conversation history
conversation = []

# Main Streamlit app code
def main():
    st.title("ChatGPT Streamlit App")
    st.write("Enter a message and ChatGPT will respond!")

    # User input
    user_input = st.text_input("User input")

    # Conversation history display
    st.subheader("Conversation History")
    for message in conversation:
        if message["role"] == "system":
            st.write(f"**{message['content']}**")
        elif message["role"] == "user":
            st.write(f"User: {message['content']}")
        elif message["role"] == "assistant":
            st.write(f"ChatGPT: {message['content']}")

    # Handle user input
    if st.button("Send"):
        if user_input:
            # Add user message to conversation
            conversation.append({"role": "user", "content": user_input})

            # Call the OpenAI API to generate assistant response
            response = openai.Completion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ],
                max_tokens=50
            )

            # Add assistant message to conversation
            assistant_response = response.choices[0].text.strip()
            conversation.append({"role": "assistant", "content": assistant_response})

            # Clear the user input
            user_input = ""

    # Display assistant response input
    if len(conversation) > 0:
        st.subheader("Assistant's Response")
        st.write(f"ChatGPT: {conversation[-1]['content']}")

if __name__ == "__main__":
    main()
