import streamlit as st

st.set_page_config(page_title="Digital Detox Genie", layout="centered")
if "messages" not in st.session_state:
    st.session_state.messages = []
def add_message(role, content):
    st.session_state.messages.append({"role": role, "content": content})
    if role == "assistant":
        try:
            with st.chat_message(role):
                # Add CSS to hide default avatar and overlay genie image
                st.markdown("""
                    <style>
                    [data-testid="stChatMessageAvatar"] {
                        width: 50px !important;
                        height: 50px !important;
                        margin-top: 0 !important;
                        position: relative;
                    }
                    [data-testid="stChatMessageAvatar"] img {
                        display: none !important; /* Hide default avatar */
                    }
                    [data-testid="stChatMessageAvatar"]:after {
                        content: url('D:\\OneDrive\\Desktop\\doc\\genie.png');
                        position: absolute;
                        top: 0;
                        left: 0;
                        width: 50px !important;
                        height: 50px !important;
                        object-fit: contain;
                    }
                    [data-testid="stChatMessage"] {
                        align-items: flex-start !important;
                        padding-top: 8px !important;
                    }
                    </style>
                """, unsafe_allow_html=True)
                st.markdown(content)
        except Exception:
            with st.chat_message(role):
                # Add CSS for fallback avatar
                st.markdown("""
                    <style>
                    [data-testid="stChatMessageAvatar"] {
                        width: 50px !important;
                        height: 50px !important;
                        margin-top: 0 !important;
                        position: relative;
                    }
                    [data-testid="stChatMessageAvatar"] img {
                        display: none !important; /* Hide default avatar */
                    }
                    [data-testid="stChatMessageAvatar"]:after {
                        content: '🤖';
                        position: absolute;
                        top: 0;
                        left: 0;
                        width: 50px !important;
                        height: 50px !important;
                        font-size: 2rem;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                    }
                    [data-testid="stChatMessage"] {
                        align-items: flex-start !important;
                        padding-top: 8px !important;
                    }
                    </style>
                """, unsafe_allow_html=True)
                st.markdown(content)
    else:
        with st.chat_message(role):
            st.markdown(content)

# Artistic & Luxurious Color Schemes
color_schemes = {
    "Pearl Light": {
        "primary": "#e5e7eb",  # light grey
        "background": "#f9f9fb",  # clean off-white
        "accent": "#bcd0ee",  # gentle blue
        "text": "#222831"  # strong dark grey
    },
    "Morning Mist": {
        "primary": "#F0F4F8",  # soft blue-grey
        "background": "#FAFCFF",  # crisp white
        "accent": "#93B5E1",  # sky blue
        "text": "#2C405E"  # deep blue-grey
    },
    "Vanilla Breeze": {
        "primary": "#F8F6F0",  # cream
        "background": "#FFFDF7",  # warm white
        "accent": "#E6C9A8",  # soft peach
        "text": "#4A3F35"  # warm brown
    },
    "Mint Fresh": {
        "primary": "#F0F7F4",  # mint white
        "background": "#FBFEFC",  # fresh white
        "accent": "#A8E1C8",  # soft mint
        "text": "#2C4A3E"  # deep green
    },
    "Lavender Dawn": {
        "primary": "#F6F0F8",  # light lavender
        "background": "#FCFAFF",  # lavender white
        "accent": "#D4B8E8",  # soft purple
        "text": "#483355"  # deep purple
    },
    "Rose Quartz": {
        "primary": "#F8F0F4",  # light pink
        "background": "#FFF7FA",  # pink white
        "accent": "#E8B8C8",  # soft pink
        "text": "#553344"  # deep rose
    },
    "Classic Gold": {
        "primary": "#BFA14A", "background": "#1A1A1A", "accent": "#FFD700", "text": "#F5F5DC"
    },
    "Royal Blue": {
        "primary": "#283593", "background": "#0D1335", "accent": "#8C9EFF", "text": "#E3EAFD"
    },
    "Emerald Dream": {
        "primary": "#2ecc71", "background": "#1B2B24", "accent": "#A3E635", "text": "#E6F9E6"
    },
    "Velvet Red": {
        "primary": "#B71C1C", "background": "#2C0A0A", "accent": "#FF5252", "text": "#FFE6E6"
    },
    "Onyx & Silver": {
        "primary": "#757575", "background": "#111111", "accent": "#C0C0C0", "text": "#F8F8F8"
    },
    "Ivory & Rose": {
        "primary": "#E6C7C2", "background": "#F8F4F0", "accent": "#D72660", "text": "#3A2C2A"
    },
    "Sapphire Night": {
        "primary": "#0F52BA", "background": "#0A192F", "accent": "#64B5F6", "text": "#E3F2FD"
    },
    "Amethyst": {
        "primary": "#9B59B6", "background": "#2C003E", "accent": "#E1BEE7", "text": "#F3E5F5"
    },
    "Champagne": {
        "primary": "#F7E7CE", "background": "#3B2F2F", "accent": "#FFDAB9", "text": "#FFF8E1"
    },
    "Obsidian": {
        "primary": "#232526", "background": "#0F2027", "accent": "#414345", "text": "#F5F7FA"
    }
}

font_options = [
    "Arial", "Helvetica", "Georgia", "Times New Roman", "Courier New", "Verdana", "Trebuchet MS", "Palatino", "Garamond", "Comic Sans MS"
]

# Always use session state for color/font
if "color_scheme" not in st.session_state:
    st.session_state.color_scheme = "Pearl Light"
if "font_choice" not in st.session_state:
    st.session_state.font_choice = "Arial"

# Get current color scheme and font from session state
color_choice = st.session_state.color_scheme
font_choice = st.session_state.font_choice
scheme = color_schemes[color_choice]

def normalize_hex(hex_color):
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 3:
        return '#' + ''.join([c*2 for c in hex_color])
    elif len(hex_color) == 6:
        return '#' + hex_color
    else:
        raise ValueError(f"Invalid hex color: {hex_color}")

def blend(hex1, hex2, ratio):
    hex1 = normalize_hex(hex1)
    hex2 = normalize_hex(hex2)
    h1 = hex1.lstrip('#'); h2 = hex2.lstrip('#')
    r1, g1, b1 = int(h1[0:2],16), int(h1[2:4],16), int(h1[4:6],16)
    r2, g2, b2 = int(h2[0:2],16), int(h2[2:4],16), int(h2[4:6],16)
    r = int(r1 * (1-ratio) + r2 * ratio)
    g = int(g1 * (1-ratio) + g2 * ratio)
    b = int(b1 * (1-ratio) + b2 * ratio)
    return f'#{r:02x}{g:02x}{b:02x}'

# Improved contrast logic for text
from colorsys import rgb_to_hls

def is_dark(hex_color):
    hex_color = normalize_hex(hex_color)
    r = int(hex_color[1:3], 16) / 255.0
    g = int(hex_color[3:5], 16) / 255.0
    b = int(hex_color[5:7], 16) / 255.0
    l = rgb_to_hls(r, g, b)[1]
    return l < 0.5

strong_text = '#fffbe6' if is_dark(scheme['background']) else '#111111'

# Subtle, multi-stop gradients for bg and widgets
bg_grad1 = blend(scheme['background'], scheme['primary'], 0.10)
bg_grad2 = blend(scheme['background'], scheme['primary'], 0.25)
bg_grad3 = blend(scheme['background'], scheme['primary'], 0.45)
bg_grad4 = blend(scheme['background'], scheme['primary'], 0.65)
input_bg = blend(scheme['accent'], scheme['background'], 0.10)
input_bg2 = blend(scheme['accent'], scheme['background'], 0.25)
input_bg_focus = blend(scheme['accent'], scheme['background'], 0.35)
input_bg_grad = f"linear-gradient(120deg, {input_bg} 0%, {input_bg2} 100%)"
input_text = strong_text
heading_color = scheme['accent']

# Subtle glow for title
if is_dark(scheme['background']):
    glow = f"0 0 12px {blend(heading_color, '#fff', 0.5)}, 0 0 2px {blend(heading_color, '#fff', 0.2)}"
else:
    glow = f"0 0 8px {blend(heading_color, '#000', 0.2)}, 0 0 2px {blend(heading_color, '#000', 0.1)}"

# --- Custom Styled Question Function ---
def styled_question(text, font=font_choice, color=heading_color, size="1.15rem", weight="600", margin="0.3em 0 0.2em 0"): 
    st.markdown(f"""
        <div style="font-family: '{font}', sans-serif; color: {color}; font-size: {size}; font-weight: {weight}; margin: {margin}; letter-spacing:0.5px;">
            {text}
        </div>
    """, unsafe_allow_html=True)

# --- Enhanced Header Area (only one title, less thick) ---
st.markdown(f"""
    <div style="
        width: 100vw;
        margin-left: -3vw;
        margin-top: -1.2em;
        margin-bottom: 1em;
        padding: 1.1em 0 0.7em 0;
        background: linear-gradient(90deg, {blend(heading_color, '#fff', 0.18)} 0%, {heading_color} 60%, {blend(heading_color, '#000', 0.18)} 100%);
        box-shadow: 0 6px 32px 0 {blend(heading_color, '#000', 0.18)};
        border-radius: 0 0 24px 24px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    ">
        <h1 style="
            font-size: 2.2rem;
            font-family: '{font_choice}', sans-serif;
            color: {strong_text};
            text-align: center;
            letter-spacing: 2px;
            margin-bottom: 0.1em;
            text-shadow: {glow};
            -webkit-text-stroke: 0.5px {blend(heading_color, '#000000', 0.3)};
        ">
        <span style="background: rgba(255,255,255,0.08); padding: 0.1em 0.7em; border-radius: 16px; box-shadow: 0 2px 16px {blend(heading_color, '#000', 0.10)};">Digital Detox Genie</span>
        </h1>
        <div style="font-size:1.05rem; color:{blend(heading_color, '#fff', 0.7)}; font-family:'{font_choice}',sans-serif; margin-top:0.1em; letter-spacing:0.5px;">
            Your luxury assistant for mindful digital living
        </div>
    </div>
""", unsafe_allow_html=True)

# --- Sidebar Section Customization (no duplicate, styled options) ---
section_labels = [
    "Add New Timetable",
    "Add Detox Activities",
    "Reduce time waste and scrolling",
    "View Timetable",
    "Settings"
]

# Only show the styled header ONCE
st.sidebar.markdown(f"""
    <div style="font-family: '{font_choice}', sans-serif; color: {heading_color}; font-size: 1.13rem; font-weight: 700; margin-bottom: 0.2em; letter-spacing:0.5px;">
        Select Section
    </div>
""", unsafe_allow_html=True)

# Hide the radio label, and style the options via CSS
section = st.sidebar.radio(
    " ",
    section_labels,
    key="sidebar_section_radio"
)

# Settings section logic - MOVED HERE after section is defined
if section == "Settings":
    styled_question("Customize Your Experience", size="1.15rem", weight="700")
    styled_question("Color Scheme", size="1.08rem", weight="600")
    styled_question("Choose a theme that matches your style:", size="1.01rem", weight="500")
    color_choice = st.selectbox(
        " ",
        list(color_schemes.keys()),
        index=list(color_schemes.keys()).index(st.session_state.color_scheme),
        key="global_color_scheme_selectbox"
    )
    
    styled_question("Typography", size="1.08rem", weight="600")
    styled_question("Select your preferred font:", size="1.01rem", weight="500")
    font_choice = st.selectbox(
        " ",
        font_options,
        index=font_options.index(st.session_state.font_choice),
        key="global_font_selectbox"
    )
    
    if st.session_state.color_scheme != color_choice:
        st.session_state.color_scheme = color_choice
    if st.session_state.font_choice != font_choice:
        st.session_state.font_choice = font_choice
        
    styled_question("Your settings have been updated. The changes will be applied when you navigate to a different section.", size="1.01rem", weight="500", color=blend(heading_color, '#000', 0.3))

# Apply CSS for full app, sidebar, widgets, and text
st.markdown(f"""
    <style>
    /* Style the chat message avatar background */
    .stChatMessage [data-testid="stChatMessageAvatar"] {{
        background: linear-gradient(135deg, {scheme['accent']}, {blend(scheme['accent'], '#fff', 0.3)}) !important;
    }}
    
    html, body, [class*="css"]  {{
        background: linear-gradient(135deg, {bg_grad1} 0%, {bg_grad2} 40%, {bg_grad3} 80%, {bg_grad4} 100%) !important;
        color: {strong_text} !important;
        font-family: '{font_choice}', 'Comic Sans MS', 'Arial', 'Helvetica', sans-serif !important;
    }}

    .stApp {{
        background: linear-gradient(135deg, {bg_grad1} 0%, {bg_grad2} 40%, {bg_grad3} 80%, {bg_grad4} 100%) !important;
        font-family: '{font_choice}', 'Comic Sans MS', 'Arial', 'Helvetica', sans-serif !important;
    }}

    .stSidebar, .stSidebarContent, section[data-testid="stSidebar"] {{
        background: linear-gradient(135deg, {bg_grad2} 0%, {bg_grad1} 100%) !important;
        color: {strong_text} !important;
        font-family: '{font_choice}', 'Comic Sans MS', 'Arial', 'Helvetica', sans-serif !important;
    }}

    .stButton>button, .stDownloadButton>button {{
        background: {input_bg_grad} !important;
        color: {strong_text} !important;
        border-radius: 8px;
        border: 1.5px solid {heading_color};
        font-family: '{font_choice}', 'Comic Sans MS', 'Arial', 'Helvetica', sans-serif !important;
    }}

    .stButton>button:focus, .stDownloadButton>button:focus {{
        background: {input_bg_focus} !important;
        border: 2px solid {heading_color} !important;
    }}

    .stTextInput>div>div>input, .stTextArea textarea, .stSelectbox>div>div>div>input, .stNumberInput>div>input {{
        background: {input_bg_grad} !important;
        color: {input_text} !important;
        border: 1.5px solid {heading_color};
        font-family: '{font_choice}', 'Comic Sans MS', 'Arial', 'Helvetica', sans-serif !important;
    }}

    .stTextInput>div>div>input:focus, .stTextArea textarea:focus, .stSelectbox>div>div>div>input:focus {{
        background: {input_bg_focus} !important;
        border: 2px solid {heading_color} !important;
    }}

    .stRadio>div>label, .stCheckbox>label, .stSelectbox>div>div>div>div, .stMarkdown, .stChatMessageContent, .stChatMessage, .stMarkdown p, .stAlert, .stDataFrame, .stTable, .stMetric, .stMetricLabel, .stMetricValue {{
        color: {strong_text} !important;
        font-family: '{font_choice}', 'Comic Sans MS', 'Arial', 'Helvetica', sans-serif !important;
    }}

    .stSelectbox>div>div>div>div, .stSelectbox>div>div>div>input {{
        background: {input_bg_grad} !important;
        color: {input_text} !important;
        font-family: '{font_choice}', 'Comic Sans MS', 'Arial', 'Helvetica', sans-serif !important;
    }}

    .stRadio>div>label>div[data-testid="stMarkdownContainer"]>p {{
        color: {strong_text} !important;
        font-family: '{font_choice}', 'Comic Sans MS', 'Arial', 'Helvetica', sans-serif !important;
    }}

    .stAlert {{
        background: {input_bg_focus} !important;
        color: {strong_text} !important;
        font-family: '{font_choice}', 'Comic Sans MS', 'Arial', 'Helvetica', sans-serif !important;
    }}

    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {{
        color: {heading_color} !important;
        font-family: '{font_choice}', 'Comic Sans MS', 'Arial', 'Helvetica', sans-serif !important;
    }}

    /* Sidebar radio/section selection */
    .stRadio>div>label, .stRadio>div>div>label, .stSidebar .stRadio label, .stSidebar .stRadio>div>label, .stSidebar .stRadio>div>div>label {{
        color: {strong_text} !important;
        font-family: '{font_choice}', 'Comic Sans MS', 'Arial', 'Helvetica', sans-serif !important;
        font-weight: 600 !important;
    }}

    /* Sidebar section headers */
    .stSidebar h1, .stSidebar h2, .stSidebar h3, .stSidebar h4, .stSidebar h5, .stSidebar h6 {{
        color: {heading_color} !important;
        font-family: '{font_choice}', 'Comic Sans MS', 'Arial', 'Helvetica', sans-serif !important;
        font-weight: 700 !important;
    }}

    /* Force input, textarea, and select text color and background */
    input, textarea, select {{
        color: {input_text} !important;
        background: {input_bg_grad} !important;
        font-family: '{font_choice}', 'Comic Sans MS', 'Arial', 'Helvetica', sans-serif !important;
    }}

    .stTextInput input, .stTextArea textarea, .stSelectbox input, .stNumberInput input {{
        color: {input_text} !important;
        background: {input_bg_grad} !important;
        font-family: '{font_choice}', 'Comic Sans MS', 'Arial', 'Helvetica', sans-serif !important;
    }}

    .stTextInput input:focus, .stTextArea textarea:focus, .stSelectbox input:focus, .stNumberInput input:focus {{
        background: {input_bg_focus} !important;
        color: {input_text} !important;
    }}
    
    input::placeholder, textarea::placeholder {{
        color: {input_text} !important;
        opacity: 0.7;
    }}

    /* Enhanced input and placeholder styling for Streamlit widgets */
    .stTextInput input, .stTextArea textarea, .stSelectbox input, .stNumberInput input {{
        color: {input_text} !important;
        background: {input_bg_grad} !important;
        font-family: '{font_choice}', 'Comic Sans MS', 'Arial', 'Helvetica', sans-serif !important;
    }}
    .stTextInput input::placeholder, .stTextArea textarea::placeholder {{
        color: {input_text} !important;
        opacity: 0.7;
    }}
    /* Target Streamlit's data-baseweb attributes for even deeper input styling */
    div[data-baseweb="input"] input {{
        color: {input_text} !important;
        background: {input_bg_grad} !important;
        font-family: '{font_choice}', 'Comic Sans MS', 'Arial', 'Helvetica', sans-serif !important;
    }}
    div[data-baseweb="textarea"] textarea {{
        color: {input_text} !important;
        background: {input_bg_grad} !important;
        font-family: '{font_choice}', 'Comic Sans MS', 'Arial', 'Helvetica', sans-serif !important;
    }}
    div[data-baseweb="input"] input::placeholder, div[data-baseweb="textarea"] textarea::placeholder {{
        color: {input_text} !important;
        opacity: 0.7;
    }}
    </style>
""", unsafe_allow_html=True)

# Style sidebar radio options
st.markdown(f"""
    <style>
    /* Style sidebar radio options */
    section[data-testid="stSidebar"] .stRadio label div[data-testid="stMarkdownContainer"] p {{
        color: {heading_color} !important;
        font-family: '{font_choice}', sans-serif !important;
        font-size: 1.05rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.5px;
    }}
    </style>
""", unsafe_allow_html=True)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    
st.session_state.tt_set=False
twdaskneeded=True
item_no=0
item_count=0
reminder_needed=""
twisthere=False
a=0
b=0
c=0
d=0
e=0
edit_needed=""
tw_items=0
total_tw=0
dda_item_group={
1: "Music therapy",
2: "Crystal ball activity",
3: "Exercise/ sports",
4: "Art",
5: "Spend time with nature"}
#starting the app
edit_needed_reinput=0
event_count_reinput=0
da_needed_reinput=0
starttimereinput=0
endtimereinput=0
choice_of_da_reinput=0
duration_dda_reinput=0
twd_needed_reinput=0

def start():
    global edit_needed,edit_needed_reinput
    edit_needed_reinput+=1
    if not st.session_state.tt_set:
        add_message("assistant","Enter your current timetable, in which you would want to fit in digital detox activities")
        create_tt()
    
#initiating the timetable creation
def create_tt():
    # Ensure choice_of_da is initialized
    if 'choice_of_da' not in st.session_state:
        st.session_state.choice_of_da = []
    # Initialize session state for sequential input handling
    if 'input_step' not in st.session_state:
        st.session_state.input_step = 'count'
        st.session_state.item_count = 0
        st.session_state.current_item = 1
        st.session_state.time_left = sorted(set(range(0,1441)))
        st.session_state.tw_items = 0
        st.session_state.total_tw = 0
        st.session_state.itemsss = {}
        st.session_state.groups = []
        st.session_state.twdaskneeded = True
        st.session_state.tt_set = False
        st.session_state.twisthere = False
    
    # Update global variables from session state
    item_count = st.session_state.item_count
    item_no = st.session_state.current_item
    
    # Before rendering the widgets, check for reset flags and clear values if needed
    if st.session_state.get("reset_start_time", False):
        st.session_state[f"start_time_{st.session_state.current_item}"] = ""
        st.session_state["reset_start_time"] = False
    if st.session_state.get("reset_end_time", False):
        st.session_state[f"end_time_{st.session_state.current_item}"] = ""
        st.session_state["reset_end_time"] = False
    
    # Step 1: Get event count
    if st.session_state.input_step == 'count':
        styled_question("Step 1: Number of Events", size="1.18rem", weight="700")
        styled_question("How many events are present in your timetable? <br><span style='font-size:0.98em;font-weight:400;'>If something occurs twice in your timetable, count it as two different things.<br>The end time of one event can also be the start time of the next one.</span>", size="1.08rem", weight="500")
        count_input = st.text_input(" ", key="event_count")
        
        if st.button('Submit Count'):
            try:
                count = int(count_input)
                if count >= 3:
                    st.session_state.item_count = count
                    st.session_state.input_step = 'event_details'
                    st.rerun()
                else:
                    st.error("At least 3 items/events are required.")
            except ValueError:
                st.error("Please enter a valid number")
    
    # Step 2: Get event details one by one
    elif st.session_state.input_step == 'event_details':
        styled_question(f"Step 2: Event {st.session_state.current_item} of {st.session_state.item_count}", size="1.15rem", weight="700")
        styled_question("To decrease any activity like timewaste, name it '<b>timewaste</b>' or '<b>scrolling</b>'.", size="1.01rem", weight="500")
        # Get event name
        styled_question(f"Name of event {st.session_state.current_item}:", size="1.08rem", weight="600")
        event_name = st.text_input(" ", key=f"event_name_{st.session_state.current_item}")
        
        # Get start time
        styled_question(f"Start time in 24 hour format as HH:MM or HH.MM for event {st.session_state.current_item}", size="1.08rem", weight="600")
        start_time = st.text_input(" ", key=f"start_time_{st.session_state.current_item}")
        
        # Get end time
        styled_question(f"End time in 24 hour format as HH:MM or HH.MM for event {st.session_state.current_item}", size="1.08rem", weight="600")
        end_time = st.text_input(" ", key=f"end_time_{st.session_state.current_item}")
        
        # Real-time validation
        error_message = None
        start_float = end_float = st_mins = et_mins = None  # Only set if valid
        try:
            if start_time:
                # Check format and convert to float
                if ':' in start_time:
                    hours, minutes = start_time.split(':')
                    if not (hours.isdigit() and minutes.isdigit() and len(minutes) <= 2):
                        error_message = "Invalid time format. Use HH:MM"
                        raise ValueError
                    start_float = float(hours + "." + minutes.zfill(2))
                elif '.' in start_time:
                    hours, minutes = start_time.split('.')
                    if not (hours.isdigit() and minutes.isdigit() and len(minutes) <= 2):
                        error_message = "Invalid time format. Use HH.MM"
                        raise ValueError
                    start_float = float(hours + "." + minutes.zfill(2))
                else:
                    # Handle whole numbers
                    if not start_time.isdigit():
                        error_message = "Time must be a number"
                        raise ValueError
                    start_float = float(start_time)
                
                minutes_part = start_float % 1
                if minutes_part >= 0.60:
                    error_message = "The minutes value must be less than 60"
                    raise ValueError
                st_mins = int(60*((start_float//1)) + 100*((start_float)%1))
                if st_mins < 0 or st_mins >= 1440:  # Check if time is within 24 hours
                    error_message = "Start time must be between 00:00 and 23:59"
                    raise ValueError
                    
            if end_time and not error_message:
                # Check format and convert to float
                if ':' in end_time:
                    hours, minutes = end_time.split(':')
                    if not (hours.isdigit() and minutes.isdigit() and len(minutes) <= 2):
                        error_message = "Invalid time format. Use HH:MM"
                        raise ValueError
                    end_float = float(hours + "." + minutes.zfill(2))
                elif '.' in end_time:
                    hours, minutes = end_time.split('.')
                    if not (hours.isdigit() and minutes.isdigit() and len(minutes) <= 2):
                        error_message = "Invalid time format. Use HH.MM"
                        raise ValueError
                    end_float = float(hours + "." + minutes.zfill(2))
                else:
                    # Handle whole numbers
                    if not end_time.isdigit():
                        error_message = "Time must be a number"
                        raise ValueError
                    end_float = float(end_time)
                
                minutes_part = end_float % 1
                if minutes_part >= 0.60:
                    error_message = "The minutes value must be less than 60"
                    raise ValueError
                et_mins = int(60*((end_float//1)) + 100*((end_float)%1))
                if et_mins < 0 or et_mins >= 1440:  # Check if time is within 24 hours
                    error_message = "End time must be between 00:00 and 23:59"
                    raise ValueError
                elif et_mins <= st_mins:
                    error_message = "End time must be after start time"
                    raise ValueError
        except ValueError:
            if not error_message:
                error_message = "Please enter time as HH:MM, HH.MM, or just HH (for whole hours)"

        # Show error if present
        if error_message:
            st.error(error_message)
        
        if st.button('Submit Event'):
            if not event_name or not start_time or not end_time:
                st.error("Please fill in all fields")
                return
            
            if error_message:
                st.error("Please fix the errors before submitting")
                return
                
            # Additional validation for time slot availability
            time_range = list(range(st_mins, et_mins))
            
            # Check if any minute in the time range is already taken
            unavailable_times = [t for t in time_range if t not in st.session_state.time_left]
            if unavailable_times:
                # Convert first unavailable time to HH:MM format for user-friendly message
                conflict_hour = unavailable_times[0] // 60
                conflict_minute = unavailable_times[0] % 60
                st.error(f"Time slot conflict at {conflict_hour:02d}:{conflict_minute:02d}. Please choose a different time.")
                return
                
            # Check if enough time is left for remaining events
            remaining_events = st.session_state.item_count - st.session_state.current_item
            remaining_time_slots = len(st.session_state.time_left) - len(time_range)
            if remaining_events > 0 and remaining_time_slots < remaining_events * 15:  # Assuming minimum 15 minutes per event
                st.error("Not enough time left for remaining events. Please adjust the duration.")
                return
            
            # If all validation passes, store the event
            st.session_state.itemsss[st.session_state.current_item] = {
                'name': event_name,
                'start_float': start_float,
                'end_float': end_float,
                'st_mins': st_mins,
                'et_mins': et_mins,
                'time_range': time_range
            }
            
            # Update time_left
            for i in time_range:
                st.session_state.time_left.remove(i)
            st.session_state.time_left = sorted(st.session_state.time_left)
            
            # Move to next event or finish
            if st.session_state.current_item < st.session_state.item_count:
                st.session_state.current_item += 1
                st.rerun()
            else:
                # Check for timewaste events first
                has_timewaste = any(
                    item.get('name', '').lower() in ["timewaste", "scrolling"]
                    for item in st.session_state.itemsss.values()
                )
                if has_timewaste:
                    st.session_state.input_step = 'check_timewaste'
                else:
                    st.session_state.input_step = 'detox_activities'
                st.rerun()

    # Step 3: Time Waste Management
    elif st.session_state.input_step == 'check_timewaste':
        styled_question("Step 3: Time Waste Management", size="1.15rem", weight="700")
        styled_question("Do you want to decrease time waste?", size="1.08rem", weight="600")
        twd_needed = st.radio(
            " ",
            options=["Yes", "No"],
            key="twd_choice"
        )
        
        if st.button('Continue'):
            if twd_needed == "Yes":
                twd()
            st.session_state.input_step = 'detox_activities'
            st.rerun()

    # Step 4: Digital Detox Activities
    elif st.session_state.input_step == 'detox_activities':
        styled_question("Step 4: Digital Detox Activities", size="1.15rem", weight="700")
        styled_question("Do you want to add digital detox activities?", size="1.08rem", weight="600")
        da_needed = st.radio(
            " ",
            options=["Yes", "No"],
            key="detox_choice"
        )
        
        if st.button('Continue'):
            if da_needed == "Yes":
                st.session_state.input_step = 'add_detox'
                st.rerun()
            else:
                # Check if there are any timewaste/scrolling events
                has_timewaste = any(
                    item.get('name', '').lower() in ["timewaste", "scrolling"]
                    for item in st.session_state.itemsss.values()
                )
                if has_timewaste:
                    st.session_state.input_step = 'check_timewaste'
                else:
                    st.session_state.input_step = 'show_timetable'
                st.rerun()

    # Step 3a: Add Detox Activities
    elif st.session_state.input_step == 'add_detox':
        add_message("assistant","""Digital detox activities include:
1) Music therapy
2) Crystal ball activity
3) Exercise/ sports
4) Art
5) Spend time with nature""")
        styled_question("Give the list of detox activities you want to include (numbers 1-5). For multiple activities, separate with commas (e.g., 1,2,4)", size="1.08rem", weight="600")
        activity_input = st.text_input(
            " ",
            key="choice_of_da_input"
        )
        
        if st.button('Submit Activities'):
            try:
                activities = [int(x.strip()) for x in activity_input.split(",")]
                if all(1 <= x <= 5 for x in activities):
                    st.session_state.choice_of_da = activities
                    st.session_state.input_step = 'duration_selection'
                    st.rerun()
                else:
                    st.error("Please enter valid activity numbers (1-5)")
            except ValueError:
                st.error("Please enter numbers separated by commas (e.g., 1,2,4)")

    # Step 4b: Duration Selection
    elif st.session_state.input_step == 'duration_selection':
        styled_question("How many minutes of digital detox do you want?", size="1.08rem", weight="600")
        duration_input = st.text_input(
            " ",
            key="duration_dda_input"
        )
        
        if st.button('Submit Duration'):
            try:
                duration = int(duration_input.strip())
                
            except ValueError as e:
                st.error(f"Please enter a valid number for duration. Error: {str(e)}")
            else:
                if duration > 0:
                    st.session_state.duration_dda = duration
                    duration_per_activity = duration//len(st.session_state.choice_of_da)
                    
                    # Find all available time slots of sufficient length
                    st.session_state.groups = find_consecutive_groups(duration_per_activity)
                    
                    # Check if we have enough slots for all activities
                    if not st.session_state.groups:
                        st.error("No time slots available that are long enough for the activities. Try a shorter duration.")
                        return
                    
                    if len(st.session_state.groups) < len(st.session_state.choice_of_da):
                        st.error(f"Not enough time slots available. Found {len(st.session_state.groups)} time slots but need {len(st.session_state.choice_of_da)}. Try a shorter duration.")
                        return

                    # Schedule activities in available time slots
                    for i in range(len(st.session_state.choice_of_da)):
                        activity_idx = st.session_state.choice_of_da[i]
                        start_time = st.session_state.groups[i][0]
                        end_time = start_time + duration_per_activity
                        
                        st.session_state.itemsss[st.session_state.item_count + i + 1] = {
                            'name': dda_item_group[activity_idx],
                            'st_mins': start_time,
                            'et_mins': end_time,
                            'time_range': list(range(start_time, end_time))
                        }
                        
                        # Update time_left
                        for i in range(start_time, end_time):
                            st.session_state.time_left.remove(i)
                        st.session_state.time_left = sorted(st.session_state.time_left)
                    
                    st.session_state.input_step = 'show_timetable'
                    st.rerun()
                else:
                    st.error("Please enter a positive duration")


    # Final Step: Show Timetable
    elif st.session_state.input_step == 'show_timetable':
        # Display final timetable
        final_items = []
        final_starts = []
        final_ends = []
        
        for i in range(1, st.session_state.item_count + len(st.session_state.choice_of_da) + 1):
            if i in st.session_state.itemsss:
                final_items.append(st.session_state.itemsss[i]['name'])
                final_starts.append(st.session_state.itemsss[i]['st_mins'])
                final_ends.append(st.session_state.itemsss[i]['et_mins'])
        
        if final_items:
            add_message("assistant", "Here is your updated timetable.")
            combined = sorted(zip(final_starts, final_ends, final_items))
            final_starts, final_ends, final_items = zip(*combined)
            
            for stt, et, name in zip(final_starts, final_ends, final_items):
                st_hr, st_min = stt // 60, str(stt % 60).zfill(2)
                et_hr, et_min = et // 60, str(et % 60).zfill(2)
                add_message("assistant", f"{st_hr}:{st_min} to {et_hr}:{et_min}    {name}")
        
        styled_question("Would you like reminders for all events in your timetable?", size="1.08rem", weight="600")
        reminder_choice = st.radio(
            " ",
            options=["Yes", "No"],
            key="reminder_choice"
        )
        if st.button('Finish'):
            add_message("user", "Yes" if reminder_choice == "Yes" else "No")
            st.session_state.tt_set = True
            st.session_state.making_tt = False
            # Reset session state for next time
            st.session_state.input_step = 'count'
            st.rerun()

def start_time_input():
    global a,item_no,starttimereinput
    while True:
        starttimereinput+=1
        try:
            globals()[f"start_{item_no}"]=st.text_input(f"Start time in 24 hour format as HH:MM or HH.MM of event {item_no}",key=f"starttimereinput{starttimereinput}")##add event no.
            add_message("user",globals()[f"start_{item_no}"])
            globals()[f"start_{item_no}"]=float(globals()[f"start_{item_no}"].replace(":","."))
        except ValueError:
            st.error("Give valid values in 'HH.MM' 24 hour format")
        else:
            if globals()[f"start_{item_no}"]%1 >=0.60 :
                st.error("The minutes value must be less than 60")
            else:
                try :
                    a=int(100*((globals()[f"start_{item_no}"])%1))
                except ValueError:
                    st.error("the minutes value should be an integer")
                else:
                    break
   
def end_time_input():
    global a,item_no,endtimereinput
    while True:
        endtimereinput+=1
        try:
            globals()[f"end_{item_no}"]=st.text_input("End time in 24 hour format as HH:MM or HH.MM for event {item_no}",key=f"endtimereinput{endtimereinput}")
            add_message("user",globals()[f"end_{item_no}"])
            globals()[f"end_{item_no}"]=float(globals()[f"end_{item_no}"].replace(":","."))
        except ValueError:
            st.error("Give valid values in 'HH.MM' 24 hour format")
        else:
            if globals()[f"end_{item_no}"]%1 >=0.60 :
                st.error("The minutes value must be less than 60")
            else:
                try:
                    a=int(100*((globals()[f"end_{item_no}"])%1))
                except ValueError:
                    st.error("the minutes value should be an integer")
                else:
                    break
def et_validinputcheck():
    globals()[f"et_mins{item_no}"]= int(60*((globals()[f"end_{item_no}"])//1) + 100*((globals()[f"end_{item_no}"])%1))
    if not (globals()[f"et_mins{item_no}"]-1) in st.session_state.time_left :
        st.error("Give a valid input The value you entered is either already set in the timetable or out of the range of 24 hours (00.00 to 24.00)")
    elif globals()[f"et_mins{item_no}"] > 1440:  # 24 hours in minutes
        st.error("End time cannot be after 24.00")
        end_time_input()
        end_time_input()
    elif globals()[f"et_mins{item_no}"]<globals()[f"st_mins{item_no}"]:
        st.error("End time cannot be before the start time")
        end_time_input()
    elif (item_count-item_no)>len(set(st.session_state.time_left) - set(range(globals()[f"st_mins{item_no}"],globals()[f"et_mins{item_no}"]))):
        st.error("Leave enough time to accommodate other events in your timetable. Enter a smaller end time")
    else:
        globals()[f"time_range_item_{item_no}"]=list(range(globals()[f"st_mins{item_no}"],globals()[f"et_mins{item_no}"]))
        st.session_state.time_left = sorted(set(st.session_state.time_left) - set(globals()[f"time_range_item_{item_no}"]))
def st_validinputcheck():
    
    #calculating the start time value in minutes
    globals()[f"st_mins{item_no}"]= int(60*((globals()[f"start_{item_no}"]//1)) + 100*((globals()[f"start_{item_no}"])%1))
    if not (globals()[f"st_mins{item_no}"]) in st.session_state.time_left :
        st.error("Give a valid input. The value you entered is either already set in the timetable or out of the range of 24 hours")
        start_time_input()
    end_time_input()
    #calculating the end time value in minutes
    et_validinputcheck()
def detox_activities():
    # Initialize session state for detox activities if needed
    if 'detox_step' not in st.session_state:
        st.session_state.detox_step = 'activity_selection'
        st.session_state.choice_of_da = None
        st.session_state.duration_dda = None
        st.session_state.groups = []
        st.session_state.da_mins = 0
    add_message("assistant","""Digital detox activities include:
1) Music therapy
2) Crystal ball activity
3) Exercise/ sports
4) Art
5) Spend time with nature""")
    # Step 1: Activity Selection
    if st.session_state.detox_step == 'activity_selection':
        styled_question("Give the list of detox activities you want to include (numbers 1-5). For multiple activities, separate with commas (e.g., 1,2,4)", size="1.08rem", weight="600")
        activity_input = st.text_input(
            " ",
            key="choice_of_da_input"
        )
        if st.button('Submit Activities'):
            try:
                activities = [int(x.strip()) for x in activity_input.split(",")]
                if all(1 <= x <= 5 for x in activities):
                    st.session_state.choice_of_da = activities
                    st.session_state.detox_step = 'duration_selection'
                    st.rerun()
                else:
                    st.error("Please enter valid activity numbers (1-5)")
            except ValueError:
                st.error("Please enter numbers separated by commas (e.g., 1,2,4)")
    # Step 2: Duration Selection
    elif st.session_state.detox_step == 'duration_selection':
        styled_question("How many minutes of digital detox do you want?", size="1.08rem", weight="600")
        duration_input = st.text_input(
            " ",
            key="duration_dda_input"
        )
        if st.button('Submit Duration'):
            try:
                duration = int(duration_input.strip())
            except ValueError:
                st.error("Please enter a valid number for duration")
            else:
                if duration > 0:
                    st.session_state.duration_dda = duration
                    duration_per_activity = duration//len(st.session_state.choice_of_da)
                    # Find all available time slots of sufficient length
                    st.session_state.groups = find_consecutive_groups(duration_per_activity)
                    # Check if we have enough slots for all activities
                    if not st.session_state.groups:
                        st.error("No time slots available that are long enough for the activities. Try a shorter duration.")
                        return
                    if len(st.session_state.groups) < len(st.session_state.choice_of_da):
                        st.error(f"Not enough time slots available. Found {len(st.session_state.groups)} time slots but need {len(st.session_state.choice_of_da)}. Try a shorter duration.")
                        return
                    # Schedule activities in available time slots
                    for i in range(len(st.session_state.choice_of_da)):
                        activity_idx = st.session_state.choice_of_da[i]
                        start_time = st.session_state.groups[i][0]
                        end_time = start_time + duration_per_activity
                        st.session_state.itemsss[st.session_state.item_count + i + 1] = {
                            'name': dda_item_group[activity_idx],
                            'st_mins': start_time,
                            'et_mins': end_time,
                            'time_range': list(range(start_time, end_time))
                        }
                        # Update time_left
                        for i in range(start_time, end_time):
                            st.session_state.time_left.remove(i)
                        st.session_state.time_left = sorted(st.session_state.time_left)
                    st.session_state.input_step = 'show_timetable'
                    st.rerun()
                else:
                    st.error("Please enter a positive duration")
    elif st.session_state.detox_step == 'complete':
        # Display final timetable
        final_items = []
        final_starts = []
        final_ends = []
        for i in range(1, st.session_state.item_count + len(st.session_state.choice_of_da) + 1):
            if i in st.session_state.itemsss:
                final_items.append(st.session_state.itemsss[i]['name'])
                final_starts.append(st.session_state.itemsss[i]['st_mins'])
                final_ends.append(st.session_state.itemsss[i]['et_mins'])
        if final_items:
            add_message("assistant", "Here is your updated timetable.")
            combined = sorted(zip(final_starts, final_ends, final_items))
            final_starts, final_ends, final_items = zip(*combined)
            for stt, et, name in zip(final_starts, final_ends, final_items):
                st_hr, st_min = stt // 60, str(stt % 60).zfill(2)
                et_hr, et_min = et // 60, str(et % 60).zfill(2)
                add_message("assistant", f"{st_hr}:{st_min} to {et_hr}:{et_min}    {name}")
        styled_question("Would you like reminders for all events in your timetable?", size="1.08rem", weight="600")
        reminder_choice = st.radio(
            " ",
            options=["Yes", "No"],
            key="reminder_choice"
        )
        add_message("user", "Yes" if reminder_choice == "Yes" else "No")
        st.session_state.detox_step = 'activity_selection'  # Reset for next time

def is_twd_needed(): #Does the user want to decrease time waste?
    global twd_needed,twd_needed_reinput
    twd_needed_reinput+=1
    styled_question("Do you want to decrease time waste?", size="1.08rem", weight="600")
    twd_needed=st.text_input(" ",key=f"twd_needed_reinput{twd_needed_reinput}")
    if twd_needed:
        add_message("user",twd_needed)
        if twd_needed.lower() in ["y", "yes", "yup", "yeah", "yea", "i do", "yep", "of course"]:
            twd() #Decreasing the time wasted
            return
        elif twd_needed.lower() in ["n","no","nope", "i don't", "i do not"]:
            return
        else:
            add_message("assistant","Give a valid answer")
            is_twd_needed() #Recursively ask for valid input

def twd():
    global total_tw, tw_items
    tw_items = 0
    total_tw = 0
    
    # Find all timewaste events and calculate total time waste
    for i in range(1, st.session_state.item_count + 1):
        if st.session_state.itemsss[i]['name'].lower() in ["timewaste", "scrolling"]:
            tw_items += 1
            tw_duration = st.session_state.itemsss[i]['et_mins'] - st.session_state.itemsss[i]['st_mins']
            total_tw += tw_duration
            globals()[f"tw_item{tw_items}"] = i
    
    # Apply reduction based on total time waste
    if total_tw >= 120:
        total_tw = total_tw // 3
        reduction = 3
    elif total_tw >= 60:
        total_tw = total_tw // 2
        reduction = 2
    elif total_tw > 20:
        total_tw = 2 * total_tw // 3
        reduction = 1.5
    else:
        return
    
    # Update each timewaste event
    for i in range(1, tw_items + 1):
        item_id = globals()[f"tw_item{i}"]
        item = st.session_state.itemsss[item_id]
        old_et_mins = item['et_mins']  # Save the old end time
        new_duration = int((item['et_mins'] - item['st_mins']) / reduction)
        new_et_mins = item['st_mins'] + new_duration
        
        # Update the event end time
        st.session_state.itemsss[item_id]['et_mins'] = new_et_mins
        st.session_state.itemsss[item_id]['time_range'] = list(range(item['st_mins'], new_et_mins))
        
        # Add freed up time back to time_left
        st.session_state.time_left.extend(range(new_et_mins, old_et_mins))
        st.session_state.time_left = sorted(set(st.session_state.time_left))

def find_consecutive_groups(min_length):
    # First find basic consecutive groups
    st.session_state.time_left = sorted(st.session_state.time_left)  # Get a sorted copy
    slices = [i for i in range(len(st.session_state.time_left)) if i == 0 or st.session_state.time_left[i] - st.session_state.time_left[i - 1] != 1]
    ends = slices[1:] + [len(st.session_state.time_left)]
    
    # Find groups where ALL minutes in the range are available
    result = []
    for s, e in zip(slices, ends):
        group = st.session_state.time_left[s:e]
        if len(group) >= min_length:
            # Verify that all minutes in the range are available
            start, end = group[0], group[-1]
            if all(x in st.session_state.time_left for x in range(start, end + 1)):
                result.append(group)
    
    # Split large time slots
    final_groups = []
    for group in result:
        if len(group) >= (2 * min_length):
            # Split the group into chunks of min_length
            num_chunks = len(group) // min_length
            for i in range(num_chunks):
                start_idx = i * min_length
                end_idx = start_idx + min_length
                if end_idx <= len(group):
                    chunk = group[start_idx:end_idx]
                    # Verify that all minutes in the chunk are available
                    if all(x in st.session_state.time_left for x in chunk):
                        final_groups.append(chunk)
        else:
            # Verify that all minutes in the group are available
            if all(x in st.session_state.time_left for x in group):
                final_groups.append(group)
    
    # Separate into preferred and non-preferred time slots
    preferred_groups = []
    second_preferred_groups = []
    not_preferred_groups = []
    preferred_groups_final = []
    
    for group in final_groups:
        # Check if slot is in preferred time (5:30-10:00 or 17:30-22:30)
        if all(330 <= x <= 600 for x in group):
            preferred_groups.append(group)
        elif all(1050 <= x <= 1350 for x in group):
            second_preferred_groups.append(group)
        elif all(601 <= x <= 1049 for x in group):
            preferred_groups_final.append(group)
        else:
            not_preferred_groups.append(group)
    
    return (preferred_groups + second_preferred_groups + preferred_groups_final + not_preferred_groups)  # Preferred groups come first

def printtimetable():
    for i in range(1,item_count+1+len(choice_of_da)):
        if f"st_mins{i}" in globals() and f"et_mins{i}" in globals():
            globals()[f"st_display_hrs{i}"]=globals()[f"st_mins{i}"]//60 
            globals()[f"st_display_mins{i}"]=str(globals()[f"st_mins{i}"]%60).zfill(2)
            globals()[f"et_display_hrs{i}"]=globals()[f"et_mins{i}"]//60 
            globals()[f"et_display_mins{i}"]=str(globals()[f"et_mins{i}"]%60).zfill(2)   
            add_message("assistant",f'{globals()[f"st_display_hrs{i}"]}:{globals()[f"st_display_mins{i}"]} to {globals()[f"et_display_hrs{i}"]}:{globals()[f"et_display_mins{i}"]}    {globals()[f"item_{i}"]}')

if section == "Add New Timetable":
    if not st.session_state.get("making_tt", False):
        styled_question("Do you want to make a new timetable? This will delete any previously made timetables.", size="1.08rem", weight="600")
        make_new_tt = st.radio(
            " ",
            ["No", "Yes"],
            key="make_new_tt_radio"
        )
        st.markdown(f"""
            <style>
            section[data-testid="stSidebar"] .stRadio label div[data-testid="stMarkdownContainer"] p,
            div[data-testid="stRadio"] label div[data-testid="stMarkdownContainer"] p {{
                color: {heading_color} !important;
                font-family: '{font_choice}', sans-serif !important;
                font-size: 1.05rem !important;
                font-weight: 600 !important;
                letter-spacing: 0.5px;
            }}
            </style>
        """, unsafe_allow_html=True)
        if st.button("Start New Timetable", key="start_new_tt_btn"):
            if make_new_tt == "Yes":
                # Reset all per-timetable state
                st.session_state.itemsss = {}
                st.session_state.time_left = sorted(set(range(0,1441)))
                st.session_state.tw_items = 0
                st.session_state.total_tw = 0
                st.session_state.groups = []
                st.session_state.twdaskneeded = True
                st.session_state.tt_set = False
                st.session_state.twisthere = False
                st.session_state.choice_of_da = []
                st.session_state.duration_dda = 0
                st.session_state.input_step = 'count'
                st.session_state.item_count = 0
                st.session_state.current_item = 1
                st.session_state.da_mins = 0
                st.session_state.detox_step = 'activity_selection'
                st.session_state.making_tt = True
                st.success("Timetable reset. You can now create a new one.")
                create_tt()
            else:
                st.info("You can view or edit your existing timetable in the other sections.")
    else:
        create_tt()
elif section == "Add Detox Activities":
    if st.session_state.tt_set==True:
        twdaskneeded=False
        detox_activities()
        printtimetable()
    else:
        add_message("assistant","First create your timetable in order to add detox activities")
elif section == "Reduce time waste and scrolling":
    if st.session_state.tt_set==True:
        twd()
        printtimetable()
    else:
        add_message("assistant","First create your timetable in order to decrease time waste and scrolling")
elif section == "View Timetable":
    if st.session_state.tt_set==True:
        printtimetable()
    else:
        add_message("assistant","First create your timetable in order to view it")

for sender, msg in st.session_state.chat_history:
    add_message("assistant",f"**{sender}:** {msg}")