import streamlit as st
import pandas as pd
import plotly.express as px
import websocket
import threading
import json
from components import realtime

BACKEND_URL = "http://localhost:8000"
WS_URL = "ws://localhost:8000/ws"

def on_message(ws, message):
    data = json.loads(message)
    if data.get("type") == "new_transaction":
        st.session_state['revenue'] = data['updated_kpis']['total_revenue_today']
        st.session_state['count'] = data['updated_kpis']['transaction_count']
        st.session_state['avg'] = data['updated_kpis']['avg_transaction']

def connect_ws(restaurant_id):
    ws = websocket.WebSocketApp(f"{WS_URL}/{restaurant_id}", on_message=on_message)
    threading.Thread(target=ws.run_forever, daemon=True).start()
    st.session_state['ws'] = ws

def show():
    st.header("📊 Restaurant Dashboard – Valós idejű nézet")

    if 'restaurant_id' not in st.session_state:
        st.info("Add meg a Restaurant ID‑t a Beállítások oldalon.")
        return

    restaurant_id = st.session_state['restaurant_id']
    if 'ws' not in st.session_state:
        connect_ws(restaurant_id)

    if 'revenue' not in st.session_state:
        st.session_state['revenue'] = 0
        st.session_state['count'] = 0
        st.session_state['avg'] = 0

    col1, col2, col3 = st.columns(3)
    col1.metric("💰 Mai bevétel", f"{st.session_state['revenue']:,.0f} Ft")
    col2.metric("🔢 Tranzakciók", f"{st.session_state['count']}")
    col3.metric("📈 Átlag számla", f"{st.session_state['avg']:,.0f} Ft")

    realtime.realtime_component()
