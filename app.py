# Import Libraries
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
import base64
from typing import List, Dict, Any

# load environment variables
load_dotenv()

# App configurations
st.set_page_config(
    page_title="Software Career RAG ChatBot",
    page_icon=":clipboard",
    layout="wide",
)

# Add a title to the app
st.title("🤖 AI Career Assistant")

# Add a description to the app
st.markdown(
    """
Your AI Career Software Advisor powered by GPT-5 and RAG technology. 
Get personalized guidance for your software development career path, technical skills, and industry insights.
"""
)

# About this webapp expander
with st.expander("About this webapp"):
    st.markdown(
        """
    ### 🤖 Model
    - **GPT-5**: Latest OpenAI language model for advanced reasoning and responses
    
    ### ⚙️ Configuration
    - Uses your **OPENAI_API_KEY** for secure API access
    - Connected to **VECTOR_STORE_ID** for intelligent document retrieval
    
    ### 🌟 Features
    - **Multi-turn conversations**: Maintains context across multiple exchanges
    - **Image input support**: Upload and analyze images alongside text
    - **Clear conversation history**: Reset chat when needed
    - **Intelligent document retrieval**: RAG-powered knowledge base access
    
    ### 🔧 How it works
    1. **Input Processing**: Your queries are processed using GPT-5
    2. **RAG Enhancement**: Relevant documents are retrieved from the vector store
    3. **Context Integration**: Retrieved information is combined with your question
    4. **Smart Response**: AI generates contextually aware, expert-level advice
    5. **Conversation Memory**: Chat history is maintained for seamless interaction
    """
    )

st.divider()

# Retrieve the credentials
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or st.secrets["OPENAI_API_KEY"]
VECTOR_STORE_ID = os.getenv("VECTOR_STORE_ID") or st.secrets["VECTOR_STORE_ID"]

# Set OpenAI API key in environment
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Initialize the OpenAI client
client = OpenAI()


# Warn if OpenAI API Key or the vector store id are not set:
if not OPENAI_API_KEY:
    st.error(
        "⚠️ OpenAI API Key is not set! Please add your OPENAI_API_KEY to the .env file or Streamlit secrets."
    )
    # st.stop()

if not VECTOR_STORE_ID:
    st.error(
        "⚠️ Vector Store ID is not set! Please add your VECTOR_STORE_ID to the .env file or Streamlit secrets."
    )
    # st.stop()

# Configuration of the system prompt
SYSTEM_PROMPT = """
You are an expert AI Career Software Advisor specializing in helping software developers advance their careers. 
You have access to a comprehensive knowledge base through RAG technology and should provide:

- Personalized career guidance for software developers
- Technical skill recommendations and learning paths
- Industry insights and market trends
- Code review and best practices advice
- Interview preparation and tips
- Resume and portfolio optimization suggestions
- Salary negotiation strategies
- Technology stack recommendations

Always provide actionable, specific advice tailored to the user's experience level and career goals. 
Use the retrieved documents to support your recommendations with current industry data and best practices.
Be encouraging, professional, and focus on practical steps the user can take to advance their career.
"""

# Store the previous response id
if "previous_response_id" not in st.session_state:
    st.session_state.previous_response_id = None

# Initialize the chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

if "thread_id" not in st.session_state:
    st.session_state.thread_id = None


# Create a sidebar with user controls
with st.sidebar:
    st.header("User Controls")
    st.divider()
    # Clear the conversation history - reset chat history and context
    if st.button("Clear Conversation History", use_container_width=True):
        st.session_state.messages = []
        st.session_state.previous_response_id = None
        # reset the page
        st.rerun()


# Helper functions
def build_input_parts(text: str, images: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Build input parts array for the OpenAI from text and images.

    Args:
        text (str): The text to be sent to OpenAI.
        images (List[Dict[str, Any]]): A list of images with their mime types and data URLs.

    Returns:
        List[Dict[str, Any]]: A list of input parts compatible with the OpenAI responses API.
    """
    content = []
    if text and text.strip():
        content.append(
            {
                "type": "input_text",
                "text": text.strip(),
            }
        )
    for image in images:
        content.append(
            {
                "type": "input_image",
                "image_url": image["data_url"],
            }
        )
    return [{"type": "message", "role": "user", "content": content}] if content else []


# Function to generate a response from OpenAI responses API
def call_responses_api(
    parts: List[Dict[str, Any]],
    previous_response_id: str | None = None,
) -> Any:
    """
    Call the OpenAI responses API to generate a response based on the provided messages and system prompt.

    Args:
        parts (List[Dict[str, Any]]): The input parts for the response.
        previous_response_id (str, optional): The ID of the previous response for context. Defaults to None.

    Returns:
        Dict[str, Any]: The response from the OpenAI API.
    """
    response = client.responses.create(
        model="gpt-5-nano",
        input=parts,
        tools=[
            {
                "type": "file_search",
                "vector_store_ids": [VECTOR_STORE_ID],
            }
        ],
        instructions=SYSTEM_PROMPT,
        previous_response_id=previous_response_id,
    )
    return response


# Function to get the text output from the response
def get_text_output(response: Any) -> str:
    """
    Extract the text content from the OpenAI response.
    """
    return response.output_text


# Initialize uploader key for resetting
if "uploader_key" not in st.session_state:
    st.session_state.uploader_key = 0

# User interface - upload images
uploaded = st.file_uploader(
    "Upload images",
    type=["jpg", "jpeg", "png", "webp"],
    accept_multiple_files=True,
    key=f"uploader_{st.session_state.uploader_key}",
)

# Display the chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] == "user":
            # Display user message text only
            st.markdown(message["content"]["text"])
            # Display images if they were part of this message
            if "images" in message["content"] and message["content"]["images"]:
                for img_url in message["content"]["images"]:
                    st.image(img_url, width=300)
        else:
            # Display assistant response
            st.markdown(message["content"])

# Add a chat input widget
chat_input = st.chat_input("Ask me anything about getting a Software Engineering job!")

if chat_input is not None:
    # Process the images into an API-compatible format
    images = [
        {
            "mime_type": f"image/{f.type.split('/')[-1]}" if f.type else "image/png",
            "data_url": f"data:{f.type};base64,{base64.b64encode(f.read()).decode('utf-8')}",
        }
        for f in (uploaded or [])
    ]

    # Build the input parts for the responses API
    parts = build_input_parts(chat_input, images)

    # Store image URLs for display in chat history
    image_urls = [img["data_url"] for img in images] if images else []

    # Store the user message with text and images
    st.session_state.messages.append(
        {"role": "user", "content": {"text": chat_input, "images": image_urls}}
    )

    # Display the user's message
    with st.chat_message("user"):
        st.markdown(chat_input)
        # Display uploaded images if any
        for image in images:
            st.image(image["data_url"], width=300)

    # Generate the AI response
    with st.chat_message("assistant"):
        with st.spinner("...thinking..."):
            try:
                response = call_responses_api(
                    parts,
                    st.session_state.previous_response_id,
                )
                ai_response_text = get_text_output(response)

                # Display the AI response
                st.markdown(ai_response_text)

                # Retrieve ID if available
                st.session_state.previous_response_id = (
                    response.id if response.id else None
                )
                # Store the AI response in the chat history
                st.session_state.messages.append(
                    {"role": "assistant", "content": ai_response_text}
                )

                # Clear the file uploader by incrementing the key
                st.session_state.uploader_key += 1
                st.rerun()

            except Exception as e:
                st.error(f"An error occurred: {e}")
