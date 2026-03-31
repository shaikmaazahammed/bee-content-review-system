"""
Bee Content Review System
=========================
A Streamlit web app for the Bee Mentorship marketing team.

Features
--------
- Upload images or videos for review
- Write and review post captions
- Check content against brand guidelines
- Receive an automatic compliance score and feedback
"""

import streamlit as st
from PIL import Image

# ---------------------------------------------------------------------------
# Page configuration
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Bee Content Review System",
    page_icon="🐝",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------------------------
# Custom CSS – soft pastel palette, clean card-based layout
# ---------------------------------------------------------------------------
st.markdown(
    """
    <style>
    /* ── Global body ──────────────────────────────────────────────────── */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #FFF9F0;          /* warm cream */
        font-family: 'Segoe UI', sans-serif;
    }

    /* ── Main content block ───────────────────────────────────────────── */
    [data-testid="block-container"] {
        padding-top: 2rem;
    }

    /* ── Header banner ────────────────────────────────────────────────── */
    .header-banner {
        background: linear-gradient(135deg, #FFE0A3 0%, #FFD6E0 100%);
        border-radius: 16px;
        padding: 2rem 2.5rem;
        text-align: center;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 14px rgba(0,0,0,0.07);
    }
    .header-banner h1 {
        color: #5C3D2E;
        font-size: 2.2rem;
        font-weight: 700;
        margin: 0;
    }
    .header-banner p {
        color: #7A5C4A;
        font-size: 1rem;
        margin-top: 0.4rem;
    }

    /* ── Section card ─────────────────────────────────────────────────── */
    .card {
        background: #FFFFFF;
        border-radius: 14px;
        padding: 1.6rem 2rem;
        margin-bottom: 1.4rem;
        box-shadow: 0 3px 10px rgba(0,0,0,0.06);
        border-left: 5px solid #FFB347;
    }
    .card h3 {
        color: #5C3D2E;
        margin-top: 0;
        font-size: 1.15rem;
    }

    /* ── Score display ────────────────────────────────────────────────── */
    .score-box {
        background: linear-gradient(135deg, #D4F1C0 0%, #B5E8D0 100%);
        border-radius: 14px;
        padding: 1.6rem 2rem;
        text-align: center;
        margin-bottom: 1.4rem;
        box-shadow: 0 3px 10px rgba(0,0,0,0.07);
    }
    .score-box h2 {
        color: #2E7D52;
        font-size: 2.8rem;
        margin: 0;
    }
    .score-box p {
        color: #3A6B4F;
        margin-top: 0.3rem;
        font-size: 1rem;
    }

    /* ── Feedback pills ───────────────────────────────────────────────── */
    .feedback-perfect {
        background: #D4EDDA;
        color: #155724;
        border-radius: 30px;
        padding: 0.5rem 1.4rem;
        font-weight: 600;
        font-size: 1.1rem;
        display: inline-block;
    }
    .feedback-improve {
        background: #FFF3CD;
        color: #856404;
        border-radius: 30px;
        padding: 0.5rem 1.4rem;
        font-weight: 600;
        font-size: 1.1rem;
        display: inline-block;
    }

    /* ── Submit button ────────────────────────────────────────────────── */
    div[data-testid="stButton"] > button {
        background: linear-gradient(135deg, #FFB347 0%, #FF8C00 100%);
        color: white;
        border: none;
        border-radius: 30px;
        padding: 0.65rem 2.4rem;
        font-size: 1rem;
        font-weight: 600;
        cursor: pointer;
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    div[data-testid="stButton"] > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 18px rgba(255,140,0,0.35);
    }

    /* ── Divider ──────────────────────────────────────────────────────── */
    hr {
        border: none;
        border-top: 1.5px solid #FFE4B5;
        margin: 1.5rem 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
st.markdown(
    """
    <div class="header-banner">
        <h1>🐝 Bee Content Review System</h1>
        <p>Submit your Instagram content for brand compliance review</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Section 1 – Media upload
# ---------------------------------------------------------------------------
st.markdown('<div class="card"><h3>📂 Upload Your Content</h3>', unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Choose an image or video file",
    type=["jpg", "jpeg", "png", "gif", "mp4", "mov", "avi"],
    help="Supported formats: JPG, PNG, GIF, MP4, MOV, AVI",
)

if uploaded_file is not None:
    file_type = uploaded_file.type

    if file_type.startswith("image"):
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Preview", use_container_width=True)
    elif file_type.startswith("video"):
        # Display uploaded video
        st.video(uploaded_file)
    else:
        st.info(f"File uploaded: **{uploaded_file.name}** ({uploaded_file.size / 1024:.1f} KB)")

    st.success(f"✅ **{uploaded_file.name}** uploaded successfully!")
else:
    st.info("No file uploaded yet. Please upload an image or video.")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Section 2 – Caption
# ---------------------------------------------------------------------------
st.markdown('<div class="card"><h3>✍️ Write Your Caption</h3>', unsafe_allow_html=True)

caption = st.text_area(
    "Post caption",
    placeholder="Type your Instagram caption here…",
    height=130,
    help="Write a warm, human caption that reflects the Bee Mentorship tone of voice.",
)

# Show live character count
char_count = len(caption)
caption_color = "#888" if char_count < 2200 else "#C0392B"
st.markdown(
    f"<small style='color:{caption_color};'>{char_count} / 2200 characters</small>",
    unsafe_allow_html=True,
)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Section 3 – Brand guidelines checklist
# ---------------------------------------------------------------------------
st.markdown('<div class="card"><h3>✅ Brand Guidelines Checklist</h3>', unsafe_allow_html=True)
st.caption(
    "Tick every item that applies to this piece of content. "
    "Your score is calculated from these selections."
)

st.markdown("<hr>", unsafe_allow_html=True)

# Each checklist item: (label, key, helper text)
CHECKLIST_ITEMS = [
    (
        "🎨 Brand colors used",
        "brand_colors",
        "Honey yellow (#FFB347), warm white (#FFF9F0), deep brown (#5C3D2E) and accent coral.",
    ),
    (
        "🔤 Correct fonts used (Futura / Avenir)",
        "correct_fonts",
        "Headlines in Futura Bold, body copy in Avenir Book or equivalent web-safe fallbacks.",
    ),
    (
        "🖼️ Logo placement and spacing respected",
        "logo_placement",
        "Logo appears in the approved corner with a clear-space margin of at least 16px.",
    ),
    (
        "📐 Reel safe zone respected",
        "reel_safe_zone",
        "All key text and graphics sit within the central 1080 × 1350 px safe zone for Reels.",
    ),
    (
        "✨ Approved graphics / assets used",
        "approved_graphics",
        "Only graphics from the official Bee Mentorship asset library are used.",
    ),
    (
        "💬 Caption tone is warm and human",
        "caption_tone",
        "The caption reads as friendly, encouraging and relatable – not corporate or robotic.",
    ),
]

checks = {key: st.checkbox(label, key=key, help=helper) for label, key, helper in CHECKLIST_ITEMS}

st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Submit button
# ---------------------------------------------------------------------------
st.markdown("<div style='text-align:center; margin: 1rem 0 1.5rem;'>", unsafe_allow_html=True)
submitted = st.button("🐝 Submit for Review", use_container_width=False)
st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Section 4 – Score and feedback (shown only after submit)
# ---------------------------------------------------------------------------
if submitted:
    # Validate that at minimum a file OR a caption was provided
    has_content = uploaded_file is not None or caption.strip() != ""

    if not has_content:
        st.warning("⚠️ Please upload a file or write a caption before submitting.")
    else:
        total_items = len(CHECKLIST_ITEMS)
        checked_count = sum(checks.values())
        score_pct = int((checked_count / total_items) * 100)

        # ── Score display ──────────────────────────────────────────────
        st.markdown('<div class="score-box">', unsafe_allow_html=True)
        st.markdown(
            f"<h2>{score_pct}%</h2>"
            f"<p>{checked_count} out of {total_items} brand guidelines met</p>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

        # Progress bar (Streamlit native)
        st.progress(score_pct / 100)

        # ── Feedback pill ──────────────────────────────────────────────
        st.markdown("<div style='text-align:center; margin:1rem 0;'>", unsafe_allow_html=True)
        if score_pct == 100:
            st.markdown(
                '<span class="feedback-perfect">🌟 Perfect – Ready to publish!</span>',
                unsafe_allow_html=True,
            )
        elif score_pct >= 67:
            st.markdown(
                '<span class="feedback-improve">👍 Almost there – minor tweaks needed</span>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                '<span class="feedback-improve">🔧 Needs improvement – please review the checklist</span>',
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)

        # ── Unchecked item suggestions ─────────────────────────────────
        unchecked = [label for (label, key, _) in CHECKLIST_ITEMS if not checks[key]]
        if unchecked:
            st.markdown("<hr>", unsafe_allow_html=True)
            st.markdown("#### 📋 Items to address before publishing:")
            for item in unchecked:
                st.markdown(f"- {item}")

        # ── Caption feedback ───────────────────────────────────────────
        if caption.strip():
            st.markdown("<hr>", unsafe_allow_html=True)
            st.markdown("#### 📝 Caption review")
            if checks["caption_tone"]:
                st.success("Caption tone is marked as warm and human. ✅")
            else:
                st.warning(
                    "Caption tone has not been verified. Re-read your caption and ensure "
                    "it feels friendly and encouraging before publishing."
                )

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; color:#B0926A; font-size:0.85rem;'>"
    "🐝 Bee Mentorship · Content Review System · Built with Streamlit"
    "</p>",
    unsafe_allow_html=True,
)
