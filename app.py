# app.py
import streamlit as st
import streamlit.components.v1 as components
import markdown as md_lib
from Agents import agent

# =========================
# Page config
# =========================
st.set_page_config(page_title="City Assistant", page_icon="🏙️", layout="wide")

# =========================
# Custom CSS (Streamlit elements only)
# =========================
st.markdown("""
<style>
    .stApp { background-color: #0f0f1a; }
    .stTextInput > div > div > input {
        background-color: #1e1e35 !important;
        color: #ffffff !important;
        border: 1px solid #3a3a60 !important;
        border-radius: 12px !important;
        padding: 12px 16px !important;
        font-size: 1rem !important;
    }
    .stTextInput > div > div > input:focus {
        border-color: #6c63ff !important;
        box-shadow: 0 0 0 2px rgba(108,99,255,0.25) !important;
    }
    .stButton > button {
        background: linear-gradient(135deg, #6c63ff, #4f46e5) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 12px 28px !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        width: 100%;
    }
    .stButton > button:hover { opacity: 0.88 !important; }
    label { color: #a0a0c0 !important; }
</style>
""", unsafe_allow_html=True)

# =========================
# Header
# =========================
st.markdown("""
<div style="font-size:2.2rem;font-weight:800;color:#ffffff;margin-bottom:4px;">🏙️ City Assistant</div>
<div style="color:#a0a0c0;font-size:0.95rem;margin-bottom:20px;">
    Ask about the <strong style="color:#6c63ff">weather</strong> 🌡️ or 
    <strong style="color:#f97316">latest news</strong> 📰 of any Indian city.
</div>
""", unsafe_allow_html=True)

# =========================
# Session state
# =========================
if "history" not in st.session_state:
    st.session_state.history = []

# =========================
# Build chat HTML (rendered via components.html)
# =========================
def build_chat_html(history, typing=False):
    bubbles = ""

    if not history and not typing:
        bubbles = """
        <div style="text-align:center;color:#4a4a70;padding:50px 20px;">
            <div style="font-size:2.5rem;margin-bottom:10px;">🌆</div>
            <div>Ask me about weather or news in any Indian city!</div>
            <div style="margin-top:6px;font-size:0.82rem;color:#3a3a60">
                e.g. "What's the weather in Mumbai?" or "Top headlines in Delhi today"
            </div>
        </div>"""
    else:
        for sender, message in history:
            # Convert markdown to HTML (handles **bold**, bullet lists, etc.)
            message_html = md_lib.markdown(message)

            if sender == "You":
                bubbles += f"""
                <div style="display:flex;justify-content:flex-end;margin:10px 0;">
                    <div style="background:linear-gradient(135deg,#6c63ff,#4f46e5);color:white;
                                padding:12px 16px;border-radius:18px 18px 4px 18px;
                                max-width:70%;font-size:0.95rem;line-height:1.5;
                                box-shadow:0 2px 8px rgba(99,91,255,0.3);">
                        {message_html}
                    </div>
                </div>"""
            else:
                bubbles += f"""
                <div style="display:flex;justify-content:flex-start;margin:10px 0;gap:10px;align-items:flex-start;">
                    <div style="width:36px;height:36px;background:linear-gradient(135deg,#f97316,#ec4899);
                                border-radius:50%;display:flex;align-items:center;justify-content:center;
                                font-size:1.1rem;flex-shrink:0;">🤖</div>
                    <div style="background:#252540;color:#e0e0f0;padding:12px 16px;
                                border-radius:4px 18px 18px 18px;max-width:72%;
                                font-size:0.95rem;line-height:1.6;border:1px solid #2e2e50;">
                        {message_html}
                    </div>
                </div>"""

        if typing:
            bubbles += """
            <div style="color:#a0a0c0;font-style:italic;font-size:0.9rem;padding:6px 0 6px 46px;">
                🤖 Bot is thinking...
            </div>"""

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            background: #1a1a2e;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            padding: 16px;
            border-radius: 16px;
            border: 1px solid #2a2a4a;
        }}
        body::-webkit-scrollbar {{ width: 5px; }}
        body::-webkit-scrollbar-track {{ background: transparent; }}
        body::-webkit-scrollbar-thumb {{ background: #3a3a60; border-radius: 10px; }}
        p {{ margin: 4px 0; }}
        ul, ol {{ margin: 6px 0 6px 18px; }}
        li {{ margin: 3px 0; }}
        strong {{ font-weight: 700; }}
        a {{ color: #818cf8; }}
    </style>
    </head>
    <body>
        {bubbles}
        <script>window.scrollTo(0, document.body.scrollHeight);</script>
    </body>
    </html>
    """

# =========================
# Render chat
# =========================
chat_slot = st.empty()

def render_chat(typing=False):
    with chat_slot:
        components.html(
            build_chat_html(st.session_state.history, typing=typing),
            height=460,
            scrolling=True
        )

render_chat()

# =========================
# Input row
# =========================
col1, col2 = st.columns([5, 1])
with col1:
    user_input = st.text_input(
        "query", 
        placeholder="e.g. Weather in Jaipur, News in Kolkata...", 
        key="input",
        label_visibility="collapsed"
    )
with col2:
    send_clicked = st.button("Send 🚀")

# =========================
# Agent invocation
# =========================
if send_clicked and user_input.strip():
    st.session_state.history.append(("You", user_input.strip()))
    render_chat(typing=True)

    result = agent.invoke({"messages": [{"role": "user", "content": user_input.strip()}]})
    bot_response = result['messages'][-1].content

    st.session_state.history.append(("Bot", bot_response))
    render_chat()