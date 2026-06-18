import streamlit as st
import requests
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="AI Currency Agent",
    page_icon=" ",
    layout="centered"
)

st.title("AI Currency Conversion Agent")

st.write("Convert currencies using real-time exchange rates.")

base_currency = st.text_input(
    "Base Currency",
    value="INR"
).upper()

target_currency = st.text_input(
    "Target Currency",
    value="USD"
).upper()

amount = st.number_input(
    "Amount",
    min_value=0.0,
    value=10.0
)

if st.button("Convert"):

    try:
        url = f"https://v6.exchangerate-api.com/v6/c754eab14ffab33112e380ca/pair/{base_currency}/{target_currency}"

        response = requests.get(url)

        data = response.json()

        conversion_rate = data["conversion_rate"]

        converted_amount = amount * conversion_rate

        st.success(
            f"{amount} {base_currency} = {converted_amount:.4f} {target_currency}"
        )

        st.info(
            f"Conversion Rate: 1 {base_currency} = {conversion_rate} {target_currency}"
        )

    except Exception as e:
        st.error(f"Error: {e}")