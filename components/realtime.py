import streamlit.components.v1 as components

def realtime_component():
    components.html("""
    <div id="feed"></div>
    <script>
    const feed = document.getElementById('feed');
    let ws;

    function connect() {
        ws = new WebSocket("ws://localhost:8000/ws/demo_restaurant");
        ws.onopen = () => console.log("✅ WebSocket connected");
        ws.onmessage = e => {
            const m = JSON.parse(e.data);
            if (m.type === "new_transaction"){
                const div = document.createElement('div');
                div.style.padding='0.5rem';
                div.style.borderBottom='1px solid #e5e7eb';
                div.innerText = `${m.data.time} • ${m.data.item_name} • ${m.data.amount} Ft`;
                feed.prepend(div);
            }
        };
        ws.onclose = () => {
            console.log("🔄 reconnect in 3 s");
            setTimeout(connect, 3000);
        };
    }
    connect();
    </script>
    """, height=400)
