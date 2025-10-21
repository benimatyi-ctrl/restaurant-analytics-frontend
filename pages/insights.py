import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000"

def show():
    st.header("🧠 AI Insights")
    rid = st.session_state.get('restaurant_id')
    if not rid:
        st.info("Állíts be Restaurant ID‑t a Beállítások oldalon.")
        return
    res = requests.get(f"{BACKEND_URL}/api/restaurants/{rid}/transactions")
    if res.status_code == 200:
        data = res.json()
        st.write("📄 Utolsó 5 tranzakció:")
        st.dataframe(data[:5])
    else:
        st.error("Nem sikerült lekérni az adatokat.")
