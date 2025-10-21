import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="🍕 Restaurant Analytics",
    page_icon="🍕",
    layout="wide",
    initial_sidebar_state="collapsed"  # Sidebar rejtve
)

# ============================================================================
# CUSTOM CSS - Szürke háttér + Bottom Navigation
# ============================================================================

st.markdown("""
<style>
    /* Szürke háttér mindenhol */
    .main {
        background-color: #f5f5f5 !important;
        padding-bottom: 80px !important; /* Hely a bottom nav-nak */
    }
    
    .block-container {
        padding: 1rem !important;
        background-color: #f5f5f5 !important;
    }
    
    /* Hero section */
    .hero {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 1rem;
        color: white;
        margin-bottom: 1rem;
        text-align: center;
    }
    
    /* Kártyák fehér háttérrel */
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
    }
    
    /* BOTTOM NAVIGATION BAR */
    .bottom-nav {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: white;
        box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
        display: flex;
        justify-content: space-around;
        padding: 0.75rem 0;
        z-index: 999;
    }
    
    .nav-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-decoration: none;
        color: #6b7280;
        font-size: 0.75rem;
        cursor: pointer;
        transition: all 0.3s;
    }
    
    .nav-item:hover {
        color: #667eea;
    }
    
    .nav-item.active {
        color: #667eea;
        font-weight: bold;
    }
    
    .nav-icon {
        font-size: 1.5rem;
        margin-bottom: 0.25rem;
    }
    
    /* Sidebar elrejtése */
    [data-testid="stSidebar"] {
        display: none;
    }
    
    /* Streamlit header elrejtése */
    header {
        visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# SESSION STATE - Oldal választás
# ============================================================================

if 'page' not in st.session_state:
    st.session_state.page = 'dashboard'

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
# PAGE CONTENT
# ============================================================================

if st.session_state.page == 'dashboard':
    # DASHBOARD PAGE
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
    
    # Chart
    st.subheader("📈 Napi bevétel trend")
    df = pd.DataFrame({
        'Dátum': pd.date_range('2025-10-14', periods=7),
        'Bevétel': [150000, 180000, 165000, 195000, 210000, 185000, 220000]
    })
    
    fig = px.area(df, x='Dátum', y='Bevétel', 
                  color_discrete_sequence=['#667eea'])
    fig.update_layout(height=300)
    st.plotly_chart(fig, use_container_width=True)

elif st.session_state.page == 'insights':
    # AI INSIGHTS PAGE
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

elif st.session_state.page == 'settings':
    # SETTINGS PAGE
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
# BOTTOM NAVIGATION BAR
# ============================================================================

st.markdown("""
<div class="bottom-nav">
    <div class="nav-item {}" onclick="window.parent.postMessage({{type: 'streamlit:setComponentValue', value: 'dashboard'}}, '*')">
        <div class="nav-icon">📊</div>
        <div>Dashboard</div>
    </div>
    <div class="nav-item {}" onclick="window.parent.postMessage({{type: 'streamlit:setComponentValue', value: 'insights'}}, '*')">
        <div class="nav-icon">🧠</div>
        <div>Insights</div>
    </div>
    <div class="nav-item {}" onclick="window.parent.postMessage({{type: 'streamlit:setComponentValue', value: 'settings'}}, '*')">
        <div class="nav-icon">⚙️</div>
        <div>Settings</div>
    </div>
</div>
""".format(
    'active' if st.session_state.page == 'dashboard' else '',
    'active' if st.session_state.page == 'insights' else '',
    'active' if st.session_state.page == 'settings' else ''
), unsafe_allow_html=True)

# Button navigation (mivel onclick nem működik Streamlit-ben)
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📊 Dashboard", use_container_width=True, type="primary" if st.session_state.page == 'dashboard' else "secondary"):
        st.session_state.page = 'dashboard'
        st.rerun()

with col2:
    if st.button("🧠 Insights", use_container_width=True, type="primary" if st.session_state.page == 'insights' else "secondary"):
        st.session_state.page = 'insights'
        st.rerun()

with col3:
    if st.button("⚙️ Settings", use_container_width=True, type="primary" if st.session_state.page == 'settings' else "secondary"):
        st.session_state.page = 'settings'
        st.rerun()
