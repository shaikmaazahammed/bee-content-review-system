import streamlit as st

st.set_page_config(page_title="Bee Content Review", layout="wide")

# 🌸 Aesthetic Background (Cherry Blossom feel)
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to bottom, #f8f5f7, #e4cddc);
}
h1, h2, h3 {
    color: #3a2a6d;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("🐝 Bee Content Review System")
st.markdown("### 🌸 Create. Submit. Perfect your content")

st.divider()

# Upload Section
uploaded_file = st.file_uploader("📤 Upload Image or Video", type=["png", "jpg", "jpeg", "mp4"])
caption = st.text_area("✍️ Write your caption")

st.divider()

# 🎯 BRAND CHECKLIST
st.subheader("✅ Brand Compliance Checklist")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🎨 Design")
    color_check = st.checkbox("Used only brand colors (#fad51b, #3a2a6d, etc.)")
    contrast_check = st.checkbox("Good contrast & readability")

    st.markdown("### 🔤 Typography")
    title_font = st.checkbox("Futura Bold used for title")
    body_font = st.checkbox("Avenir used for body")

    st.markdown("### 🐝 Logo")
    logo_place = st.checkbox("Logo correctly placed")
    logo_space = st.checkbox("Clear space maintained")
    logo_distort = st.checkbox("Logo NOT distorted")

with col2:
    st.markdown("### 🎬 Reel Safety")
    safe_zone = st.checkbox("Text inside safe zone (no top/bottom cut)")

    st.markdown("### 🎭 Graphics")
    graphics = st.checkbox("Used approved graphic sets only")

    st.markdown("### 🧠 Caption Tone")
    tone = st.checkbox("Caption is warm, human, inclusive (not robotic)")

st.divider()

# 🚀 Submission Logic
if st.button("🚀 Submit for Review"):

    if not uploaded_file or not caption:
        st.error("❌ Please upload content and write a caption.")
    else:
        checks = [
            color_check, contrast_check,
            title_font, body_font,
            logo_place, logo_space, logo_distort,
            safe_zone,
            graphics,
            tone
        ]

        score = sum(checks)
        total = len(checks)

        st.subheader("📊 Result")

        if score == total:
            st.success(f"✅ Perfect! ({score}/{total}) - Ready to post 🚀")
        elif score >= total * 0.7:
            st.warning(f"⚠️ Good ({score}/{total}) - Minor fixes needed")
        else:
            st.error(f"❌ Not approved ({score}/{total}) - Fix before posting")
