import streamlit as st

def show():
    st.header("⚙️ Beállítások")
    restaurant_id = st.text_input("Étterm azonosító (restaurant_id)", 
                                  st.session_state.get('restaurant_id', 'demo_restaurant'))
    if st.button("Mentés"):
        st.session_state['restaurant_id'] = restaurant_id
        st.success("Elmentve!")
