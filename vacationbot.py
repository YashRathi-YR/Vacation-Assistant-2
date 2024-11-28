import os
import streamlit as st
import pandas as pd
import re  # For extracting structured data
import ast  # Safer alternative to eval()
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variables
api_key = os.getenv("GSK_API_KEY")

if not api_key:
    st.error("API Key not found. Ensure you have set it in a .env file.")

# Initialize Groq client
try:
    client = Groq(api_key=api_key)
except Exception as e:
    st.error(f"Error initializing Groq client: {e}")

# Initialize session state for theme
if "theme" not in st.session_state:
    st.session_state.theme = "Light"

# Define themes (updated for sidebar and input labels)
def apply_theme(theme):
    if theme == "Dark":
        st.markdown(
            """
            <style>
                body, .stApp { 
                    background-color: #121212; 
                    color: #E0E0E0; 
                    font-family: 'Arial', sans-serif; 
                    font-size: 18px; 
                }
                .stSidebar { 
                    background-color: #1e1e1e; 
                    color: #E0E0E0; 
                }
                .sidebar .css-1d391kg { 
                    background-color: #1e1e1e; 
                }
                .css-1n76uvr.e1fqkh3o3 {  /* Sidebar text elements */
                    color: #E0E0E0; 
                }
                label { 
                    color: #E0E0E0 !important; 
                    font-size: 20px !important; 
                }
                .stButton > button { 
                    background-color: #BB86FC; 
                    color: white; 
                    border-radius: 8px; 
                    padding: 10px 15px; 
                }
                .stDataFrame { 
                    border-radius: 10px; 
                }
                h3, h4, h5, h6, .stMarkdown { 
                    color: #BB86FC; 
                    font-size: 20px; 
                }
            </style>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <style>
                body, .stApp { 
                    background-color: #f9f9f9; 
                    color: #333; 
                    font-family: 'Arial', sans-serif; 
                    font-size: 18px; 
                }
                .stSidebar { 
                    background-color: #f0f0f0; 
                    color: #333; 
                }
                .sidebar .css-1d391kg { 
                    background-color: #f0f0f0; 
                }
                .css-1n76uvr.e1fqkh3o3 {  /* Sidebar text elements */
                    color: #333; 
                }
                label { 
                    color: #333 !important; 
                    font-size: 20px !important; 
                }
                .stButton > button { 
                    background-color: #4CAF50; 
                    color: white; 
                    border-radius: 8px; 
                    padding: 10px 15px; 
                }
                .stDataFrame { 
                    border-radius: 10px; 
                }
                h3, h4, h5, h6, .stMarkdown { 
                    color: #4CAF50; 
                    font-size: 20px; 
                }
            </style>
            """,
            unsafe_allow_html=True,
        )

# Apply the current theme
apply_theme(st.session_state.theme)

# Theme toggle button in the sidebar
if st.sidebar.button("Switch Theme"):
    # Toggle the theme
    st.session_state.theme = "Dark" if st.session_state.theme == "Light" else "Light"

# Streamlit UI
st.title("🌴 Vacation Planning Assistant")
st.markdown("Plan your perfect vacation with ease and confidence.")

# Input Section
st.markdown("### 📝 Enter Your Preferences")
col1, col2 = st.columns(2)

with col1:
    destinations = st.text_input("📍 Preferred Destinations or Vacation Types", placeholder="e.g., Paris, Beaches")
    travel_preferences = st.selectbox(
        "🏕️ Travel Preferences", ["Adventure", "Relaxation", "Family-Friendly"]
    )
with col2:
    budget = st.number_input("💰 Budget Constraints ($)", min_value=0, step=100, format="%d")
    days_available = st.number_input("🗓️ Number of Days Available", min_value=1, step=1, format="%d")

# Generate Recommendations Button
if st.button("🔍 Generate Recommendations"):
    with st.spinner("Finding the best vacation plans for you..."):
        prompt = f"""
        You are a vacation planner. Based on:
        - Destinations: {destinations}
        - Budget: {budget}
        - Days Available: {days_available}
        - Preferences: {travel_preferences}
        Provide recommendations as a Python list of dictionaries. Each dictionary should include:
        - "destination" (string)
        - "cost" (integer)
        - "days_required" (integer)
        - "best_travel_time" (string)
        - "activities" (list of strings)
        """
        try:
            # Request chat completion from Groq API
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama3-8b-8192",
            )

            # Extract response text
            response_text = chat_completion.choices[0].message.content

            # Use regex to extract structured data
            match = re.search(r'\[.*\]', response_text, re.DOTALL)
            if match:
                valid_data = match.group(0)
                try:
                    recommendations = pd.DataFrame(ast.literal_eval(valid_data))
                    st.success("🌟 Recommended Destinations:")
                    st.dataframe(recommendations, use_container_width=True)
                except (SyntaxError, ValueError) as e:
                    st.error(f"Error parsing structured data: {e}")
            else:
                st.error("No structured data found in the response.")
        except Exception as e:
            st.error(f"Error generating recommendations: {e}")

# Sidebar options
st.sidebar.title("🔍 Explore More")
sidebar_option = st.sidebar.radio(
    "Navigate", ["Destination Details", "Travel Tips", "Budget Breakdown"]
)

if sidebar_option == "Destination Details":
    st.sidebar.info("Details for destinations will appear here.")
elif sidebar_option == "Travel Tips":
    st.sidebar.info("Find tips for your travel.")
elif sidebar_option == "Budget Breakdown":
    st.sidebar.info("Here's a sample budget breakdown:")
    st.sidebar.write(f"🏠 Accommodation: ${budget * 0.3:.2f}")
    st.sidebar.write(f"🍴 Food: ${budget * 0.2:.2f}")
    st.sidebar.write(f"🚗 Transport: ${budget * 0.1:.2f}")
    st.sidebar.write(f"🎢 Activities: ${budget * 0.4:.2f}")
