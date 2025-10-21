import streamlit as st

st.set_page_config(
    page_title="🍕 Restaurant Analytics",
    page_icon="🍕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CUSTOM CSS
# ============================================================================

st.markdown("""
<style>
    .main {padding: 0 !important;}
    .block-container {padding: 1rem !important;}
    .hero {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 1rem;
        color: white;
        margin-bottom: 2rem;
        text-align: center;
    }
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 1rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# HERO SECTION
# ============================================================================

st.markdown("""
<div class="hero">
    <h1>🍕 Restaurant Analytics</h1>
    <p>AI-alapú éttermi analitika platform</p>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# SIDEBAR
# ============================================================================

st.sidebar.title("🍽️ Navigáció")
page = st.sidebar.radio(
    "Válassz oldalt:",
    ["📊 Dashboard", "🧠 AI Insights", "⚙️ Beállítások"]
)

# ============================================================================
# DASHBOARD PAGE
# ============================================================================

if page == "📊 Dashboard":
    st.header("📊 Dashboard - Élő Statisztikák")
    
    # KPI metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("💰 Mai bevétel", "0 Ft", "+12%")
    with col2:
        st.metric("🔢 Tranzakciók", "0", "+8%")
    with col3:
        st.metric("📈 Átlag számla", "0 Ft", "+5%")
    with col4:
        st.metric("💵 Készpénz", "0%", "-3%")
    
    st.info("💡 **Demo mód** – Kapcsold be a valós idejű szinkronizálást a Beállítások oldalon!")
    
    # Placeholder chart
    st.subheader("📈 Napi bevétel trend")
    import pandas as pd
    import plotly.express as px
    
    # Demo data
    df = pd.DataFrame({
        'Dátum': pd.date_range('2025-10-14', periods=7),
        'Bevétel': [150000, 180000, 165000, 195000, 210000, 185000, 220000]
    })
    
    fig = px.area(df, x='Dátum', y='Bevétel', 
                  color_discrete_sequence=['#667eea'])
    fig.update_layout(height=300)
    st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# AI INSIGHTS PAGE
# ============================================================================

elif page == "🧠 AI Insights":
    st.header("🧠 AI Insights - Adatvezérelt javaslatok")
    
    st.success("✅ **Top Javaslat:** Vezess be Happy Hour-t kedden 17-19h között → +80,000 Ft/hó")
    
    with st.expander("💰 Bevételi optimalizálás - MAGAS HATÁS"):
        st.write("""
        **Megfigyelés:**
        - Kedden 30% kevesebb forgalom vs pénteken
        - Átlag számla: 3,200 Ft
        
        **Javaslat:**
        1. Happy Hour bevezetése kedden 17-19h (-20% akció)
        2. Email kampány inaktív vendégeknek
        
        **Várható eredmény:** +80,000 Ft/hó
        """)
    
    with st.expander("🏆 Termék portfolio optimalizálás"):
        st.write("""
        **Dog termékek (vedd le):**
        - Vegán Lasagne: -12,000 Ft profit/hó
        
        **Star termékek (promótáld):**
        - Pizza Margherita: +85,000 Ft/hó
        
        **Áremelés javaslat:**
        - Steak: 6,800 → 7,500 Ft (+10%)
        """)
    
    st.info("📊 További insights elérhető valós adatok feltöltése után!")

# ============================================================================
# SETTINGS PAGE
# ============================================================================

elif page == "⚙️ Beállítások":
    st.header("⚙️ Beállítások")
    
    st.subheader("🔄 Automatikus szinkronizálás")
    
    sync_method = st.selectbox(
        "Szinkronizálási módszer:",
        [
            "Google Sheets (Ajánlott - INGYEN)",
            "Email Import",
            "Direct POS API (Prémium)"
        ]
    )
    
    if "Google Sheets" in sync_method:
        st.info("""
        **Google Sheets integráció:**
        1. POS rendszered exportáljon CSV-t naponta
        2. Állíts be Zapier-t: Email → Google Sheets  
        3. Add meg a Sheets URL-t itt:
        """)
        
        sheet_url = st.text_input(
            "Google Sheets URL",
            placeholder="https://docs.google.com/spreadsheets/d/..."
        )
        
        if st.button("💾 Mentés"):
            st.success("✅ Beállítások mentve!")
    
    st.markdown("---")
    
    st.subheader("👤 Profil")
    st.text_input("Étterem neve", "Demo Étterem")
    st.text_input("Email", "demo@example.com")
    
    if st.button("🚪 Kijelentkezés"):
        st.info("Kijelentkezés...")

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #6b7280; padding: 2rem;'>
    <p>🍕 Restaurant Analytics © 2025 | Készítette: AI-powered Platform</p>
</div>
""", unsafe_allow_html=True)
