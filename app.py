import streamlit as st
import language_tool_python

st.set_page_config(page_title="Bee Content Review", layout="wide")

# 🖤 Minimal Black Theme
st.markdown("""
<style>
.stApp {
    background-color: #0e0e0e;
    color: white;
}

h1, h2, h3 {
    color: white;
}

div.stButton > button {
    background-color: #fad51b;
    color: black;
    border-radius: 8px;
    font-weight: bold;
}

.stTextArea textarea {
    background-color: #1a1a1a;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("🐝 Bee Content Review")
st.markdown("Minimal. Clean. On-brand.")

st.divider()

# Upload
uploaded_file = st.file_uploader("Upload Content", type=["png", "jpg", "jpeg", "mp4"])
caption = st.text_area("Caption")

# 🧠 Grammar Tool
tool = language_tool_python.LanguageTool('en-US')

if caption:
    matches = tool.check(caption)

    st.subheader("🧠 Caption Check")

    if len(matches) == 0:
        st.success("✅ No spelling or grammar issues found")
        grammar_ok = True
    else:
        grammar_ok = False
        st.warning(f"⚠️ Found {len(matches)} issue(s):")

        for match in matches[:5]:  # show top 5 issues
            st.write(f"• {match.message}")

st.divider()

# Checklist
st.subheader("Checklist")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Design**")
    color_check = st.checkbox("Brand colors used")
    contrast_check = st.checkbox("Good contrast")

    st.markdown("**Typography**")
    title_font = st.checkbox("Futura (title)")
    body_font = st.checkbox("Avenir (body)")

    st.markdown("**Logo**")
    logo_place = st.checkbox("Correct placement")
    logo_space = st.checkbox("Clear spacing")
    logo_distort = st.checkbox("Not distorted")

with col2:
    st.markdown("**Reel Safety**")
    safe_zone = st.checkbox("Inside safe zone")

    st.markdown("**Graphics**")
    graphics = st.checkbox("Approved graphics")

    st.markdown("**Tone**")
    tone = st.checkbox("Human & warm caption")

st.divider()

# Submit
if st.button("Submit"):

    if not uploaded_file or not caption:
        st.error("Upload content and add caption")
    else:
        checks = [
            color_check, contrast_check,
            title_font, body_font,
            logo_place, logo_space, logo_distort,
            safe_zone,
            graphics,
            tone,
            grammar_ok
        ]

        score = sum(checks)
        total = len(checks)

        st.subheader("Result")

        if score == total:
            st.success(f"Perfect ({score}/{total})")
        elif score >= total * 0.7:
            st.warning(f"Needs minor fixes ({score}/{total})")
        else:
            st.error(f"Not approved ({score}/{total})")
