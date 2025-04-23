import streamlit as st

st.title("Municipal Complaint Classifier")

# streamlit_grievance_app.py
import streamlit as st
import pandas as pd
from textblob import TextBlob
from datetime import datetime

# Sample complaints (now extended and in English)
complaints = [
    "There is a lot of garbage outside the hospital, and it smells terrible.",
    "The road near my house is full of potholes.",
    "No electricity for two days in our area.",
    "Overflowing sewage near the school.",
    "Street lights are not working in the garden.",
    "Power cut in the colony since morning.",
    "Drainage is clogged near the bus stop.",
    "Garbage collection has not been done for a week.",
    "Street light pole is broken and dangerous.",
    "Water is not coming in our area."
]

# Define keywords for rule-based classification
categories_keywords = {
    "garbage": ["garbage", "trash", "smell"],
    "road": ["road", "pothole", "crack"],
    "electricity": ["electricity", "power", "light gone"],
    "sewage": ["sewage", "drainage", "overflow", "clogged"],
    "light": ["light", "street light", "lamp"],
    "water": ["water", "no water"]
}

priority_rules = {
    "HIGH": ["hospital", "school", "sewage", "dangerous", "overflow"],
    "MEDIUM": ["pothole", "electricity", "garbage", "drainage"],
    "LOW": []
}

def classify_complaint(text):
    text_lower = text.lower()
    category = "other"
    priority = "LOW"
    sentiment = "Neutral"

    for cat, keywords in categories_keywords.items():
        if any(word in text_lower for word in keywords):
            category = cat
            break

    for p, keywords in priority_rules.items():
        if any(word in text_lower for word in keywords):
            priority = p
            break

    if "not" in text_lower or "no" in text_lower or "bad" in text_lower or "smell" in text_lower:
        sentiment = "Negative"
    elif "good" in text_lower or "nice" in text_lower:
        sentiment = "Positive"

    return category, priority, sentiment

st.subheader("Sample Complaints Classification")

for comp in complaints:
    category, priority, sentiment = classify_complaint(comp)
    st.markdown(f"**Complaint:** {comp}")
    st.write(f"➡️ Category: `{category}`")
    st.write(f"🚨 Priority: `{priority}`")
    st.write(f"🧠 Sentiment: `{sentiment}`")
    st.markdown("---")
