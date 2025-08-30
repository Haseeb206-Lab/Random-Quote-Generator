import streamlit as st
import random

# Title
st.title("📜 Random Quote Generator")

# List of sample quotes
quotes = [
    "The best way to predict the future is to create it. – Peter Drucker",
    "In the middle of every difficulty lies opportunity. – Albert Einstein",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "Do what you can, with what you have, where you are. – Theodore Roosevelt",
    "Happiness depends upon ourselves. – Aristotle",
    "Act as if what you do makes a difference. It does. – William James",
    "Turn your wounds into wisdom. – Oprah Winfrey",
]

# Button to generate random quote
if st.button("✨ Generate Quote"):
    quote = random.choice(quotes)
    st.success(quote)
else:
    st.info("Click the button to get a random quote!")

