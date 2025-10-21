import streamlit as st
import requests
from pages import dashboard, insights, settings

st.set_page_config(
    page_title="🍕 Restaurant Analytics",
    page_icon="🍕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Oldalválasztó menü
pages = {
    "📊 Dashboard": dashboard,
    "🧠 AI Insights": insights,
    "⚙️ Beállítások": settings,
}

st.sidebar.title("🍽️ Navigáció")
selection = st.sidebar.radio("Válaszd ki az oldalt:", tuple(pages.keys()))

page = pages[selection]
page.show()
