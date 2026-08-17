import streamlit as st
import pandas as pd

st.title("📚 Book Popularity Prediction")

st.write(
    "Enter the book details below to predict whether "
    "the book is Popular or Not Popular."
)

st.header("Enter Book Details")

pages = st.number_input(
    "Number of Pages",
    min_value=1,
    max_value=2000,
    value=250
)

rating = st.number_input(
    "Rating",
    min_value=0.0,
    max_value=5.0,
    value=3.5,
    step=0.1
)

reviews = st.number_input(
    "Number of Reviews",
    min_value=0,
    max_value=100000,
    value=100
)

price = st.number_input(
    "Price (₹)",
    min_value=0,
    max_value=10000,
    value=300
)

if st.button("🔮 Predict Popularity"):

    score = 0

    # Rule 1: Rating
    if rating >= 4.0:
        score += 1

    # Rule 2: Reviews
    if reviews >= 500:
        score += 1

    # Rule 3: Price
    if price <= 500:
        score += 1

    st.header("Prediction")

    if score >= 2:
        st.success("📚 POPULAR")
    else:
        st.warning("📖 NOT POPULAR")

    st.subheader("Prediction Details")

    st.write("Popularity Score:", score, "/ 3")

    if rating >= 4.0:
        st.write("✅ Rating is 4.0 or above")
    else:
        st.write("❌ Rating is below 4.0")

    if reviews >= 500:
        st.write("✅ Reviews are 500 or above")
    else:
        st.write("❌ Reviews are below 500")

    if price <= 500:
        st.write("✅ Price is ₹500 or below")
    else:
        st.write("❌ Price is above ₹500")