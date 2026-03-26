import time
import streamlit as st

# -------------------------------------------------
# Page config
# -------------------------------------------------
st.set_page_config(
    page_title="Verdant Wealth",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

APP_NAME = "Verdant Wealth"
APP_TAGLINE = "Sustainable investing, built around you."
TARGET_PAGE = "pages/1_Build_Your_Portfolio.py"  # update if your page name differs


# -------------------------------------------------
# Helpers
# -------------------------------------------------
def init_session_state() -> None:
    defaults = {
        "launch_screen_shown": False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def inject_css() -> None:
    st.markdown(
        """
        <style>
            :root {
                --bg: #f5f9f8;
                --bg-2: #eef5f3;
                --card: rgba(255, 255, 255, 0.88);
                --card-strong: rgba(255, 255, 255, 0.96);
                --text: #0f172a;
                --muted: #475569;
                --line: rgba(15, 23, 42, 0.08);
                --primary: #0f766e;
                --primary-2: #14b8a6;
                --shadow: 0 18px 50px rgba(15, 23, 42, 0.08);
            }

            .stApp {
                background:
                    radial-gradient(circle at top left, rgba(20,184,166,0.08), transparent 28%),
                    radial-gradient(circle at top right, rgba(15,118,110,0.06), transparent 22%),
                    linear-gradient(180deg, #f8fcfb 0%, #f3f7fb 100%);
            }

            .block-container {
                max-width: 1180px;
                padding-top: 1.4rem;
                padding-bottom: 2.2rem;
            }

            .brand-bar {
                display: flex;
                align-items: center;
                gap: 0.9rem;
                margin-bottom: 1.25rem;
            }

            .brand-mark {
                width: 52px;
                height: 52px;
                border-radius: 16px;
                background: linear-gradient(135deg, var(--primary), var(--primary-2));
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                font-weight: 800;
                font-size: 1.1rem;
                box-shadow: 0 12px 30px rgba(15,118,110,0.22);
            }

            .brand-name {
                font-size: 1.05rem;
                font-weight: 800;
                color: var(--text);
                margin: 0;
                letter-spacing: -0.02em;
            }

            .brand-sub {
                margin: 0.1rem 0 0 0;
                color: var(--muted);
                font-size: 0.92rem;
            }

            .hero {
                background: linear-gradient(135deg, rgba(255,255,255,0.92), rgba(255,255,255,0.78));
                border: 1px solid rgba(255,255,255,0.65);
                border-radius: 28px;
                padding: 2.4rem 2.2rem;
                box-shadow: var(--shadow);
                backdrop-filter: blur(8px);
            }

            .hero-badge {
                display: inline-block;
                background: rgba(15,118,110,0.09);
                color: var(--primary);
                border: 1px solid rgba(15,118,110,0.12);
                border-radius: 999px;
                padding: 0.4rem 0.8rem;
                font-size: 0.82rem;
                font-weight: 800;
                letter-spacing: 0.02em;
                margin-bottom: 0.95rem;
            }

            .hero h1 {
                color: var(--text);
                font-size: 3.15rem;
                line-height: 1.02;
                letter-spacing: -0.05em;
                font-weight: 850;
                margin: 0 0 0.95rem 0;
                max-width: 720px;
            }

            .hero p {
                color: #334155;
                font-size: 1.08rem;
                line-height: 1.65;
                max-width: 760px;
                margin: 0;
            }

            .hero-pills {
                display: flex;
                flex-wrap: wrap;
                gap: 0.6rem;
                margin-top: 1.15rem;
            }

            .pill {
                padding: 0.45rem 0.82rem;
                border-radius: 999px;
                background: rgba(255,255,255,0.82);
                border: 1px solid var(--line);
                color: var(--text);
                font-size: 0.88rem;
                font-weight: 700;
            }

            .glass-card {
                background: var(--card);
                border: 1px solid rgba(255,255,255,0.7);
                border-radius: 22px;
                padding: 1.15rem;
                box-shadow: var(--shadow);
                backdrop-filter: blur(8px);
                height: 100%;
            }

            .glass-card h3 {
                color: var(--text);
                font-size: 1.05rem;
                font-weight: 800;
                margin: 0 0 0.35rem 0;
            }

            .glass-card p {
                color: var(--muted);
                font-size: 0.96rem;
                line-height: 1.55;
                margin: 0;
            }

            .section-label {
                font-size: 0.82rem;
                font-weight: 800;
                letter-spacing: 0.08em;
                text-transform: uppercase;
                color: var(--primary);
                margin-bottom: 0.35rem;
            }

            .section-title {
                color: var(--text);
                font-size: 1.85rem;
                letter-spacing: -0.03em;
                font-weight: 850;
                margin-bottom: 0.35rem;
            }

            .section-subtitle {
                color: var(--muted);
                margin-bottom: 1rem;
            }

            .cta-panel {
                background: linear-gradient(135deg, rgba(15,118,110,0.12), rgba(20,184,166,0.07));
                border: 1px solid rgba(15,118,110,0.12);
                border-radius: 28px;
                padding: 1.5rem;
                box-shadow: var(--shadow);
            }

            .cta-title {
                color: var(--text);
                font-size: 1.65rem;
                font-weight: 850;
                letter-spacing: -0.03em;
                margin: 0 0 0.4rem 0;
            }

            .cta-copy {
                color: var(--muted);
                font-size: 1rem;
                line-height: 1.6;
                margin: 0;
            }

            .mini-stat {
                background: var(--card-strong);
                border: 1px solid var(--line);
                border-radius: 18px;
                padding: 0.95rem 1rem;
                box-shadow: var(--shadow);
            }

            .mini-stat-value {
                color: var(--text);
                font-size: 1.45rem;
                font-weight: 850;
                margin: 0;
            }

            .mini-stat-label {
                color: var(--muted);
                font-size: 0.9rem;
                margin-top: 0.15rem;
            }

            div.stButton > button {
                min-height: 3.15rem;
                border-radius: 14px;
                font-weight: 800;
                font-size: 0.98rem;
                border: none;
            }

            .splash-wrap {
                min-height: 88vh;
                display: flex;
                align-items: center;
                justify-content: center;
            }

            .splash-card {
                width: min(700px, 100%);
                text-align: center;
                background: linear-gradient(135deg, rgba(255,255,255,0.92), rgba(255,255,255,0.78));
                border: 1px solid rgba(255,255,255,0.72);
                border-radius: 30px;
                padding: 3rem 2rem;
                box-shadow: var(--shadow);
                backdrop-filter: blur(10px);
            }

            .splash-logo {
                width: 92px;
                height: 92px;
                border-radius: 26px;
                background: linear-gradient(135deg, var(--primary), var(--primary-2));
                color: white;
                margin: 0 auto 1.1rem auto;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 2rem;
                font-weight: 900;
                box-shadow: 0 18px 40px rgba(15,118,110,0.24);
            }

            .splash-title {
                color: var(--text);
                font-size: 2.4rem;
                font-weight: 900;
                letter-spacing: -0.04em;
                margin: 0;
            }

            .splash-copy {
                color: var(--muted);
                font-size: 1.02rem;
                margin-top: 0.55rem;
                line-height: 1.6;
            }

            .divider-space {
                height: 0.65rem;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def show_splash_screen() -> None:
    splash = st.empty()
    with splash.container():
        st.markdown(
            f"""
            <div class="splash-wrap">
                <div class="splash-card">
                    <div class="splash-logo">VW</div>
                    <div class="splash-title">{APP_NAME}</div>
                    <div class="splash-copy">{APP_TAGLINE}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    time.sleep(1.6)
    st.session_state["launch_screen_shown"] = True
    st.rerun()


def navigate_to_builder() -> None:
    try:
        st.switch_page(TARGET_PAGE)
    except Exception:
        st.info(
            f"Create a separate Streamlit page at `{TARGET_PAGE}` to enable direct navigation "
            "from this homepage."
        )


def info_card(title: str, body: str) -> str:
    return f"""
    <div class="glass-card">
        <h3>{title}</h3>
        <p>{body}</p>
    </div>
    """


def mini_stat(value: str, label: str) -> str:
    return f"""
    <div class="mini-stat">
        <div class="mini-stat-value">{value}</div>
        <div class="mini-stat-label">{label}</div>
    </div>
    """


# -------------------------------------------------
# App
# -------------------------------------------------
init_session_state()
inject_css()

if not st.session_state["launch_screen_shown"]:
    show_splash_screen()

# Top brand bar
st.markdown(
    f"""
    <div class="brand-bar">
        <div class="brand-mark">VW</div>
        <div>
            <p class="brand-name">{APP_NAME}</p>
            <p class="brand-sub">{APP_TAGLINE}</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Hero section
left, right = st.columns([1.35, 0.65], gap="large")

with left:
    st.markdown(
        """
        <div class="hero">
            <div class="hero-badge">Personalised sustainable investing</div>
            <h1>Build an investment portfolio that reflects both financial goals and ESG priorities.</h1>
            <p>
                A modern portfolio experience that helps users move from intention to action.
                The app combines risk-aware portfolio construction with sustainability preferences,
                delivering a more personal and transparent investment journey.
            </p>
            <div class="hero-pills">
                <span class="pill">Risk-aware allocation</span>
                <span class="pill">ESG-integrated design</span>
                <span class="pill">Professional user flow</span>
                <span class="pill">Optimiser-ready architecture</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with right:
    st.markdown(mini_stat("Risk", "Tailored to user profile"), unsafe_allow_html=True)
    st.markdown('<div class="divider-space"></div>', unsafe_allow_html=True)
    st.markdown(mini_stat("ESG", "Aligned with user values"), unsafe_allow_html=True)
    st.markdown('<div class="divider-space"></div>', unsafe_allow_html=True)
    st.markdown(mini_stat("Flow", "Clear handoff to portfolio builder"), unsafe_allow_html=True)

st.markdown("<div style='height: 1.2rem;'></div>", unsafe_allow_html=True)

# Feature section
st.markdown('<div class="section-label">Why this app</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">A homepage built for clarity, trust, and momentum</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">The landing experience stays focused: explain the product, establish credibility, and move the user directly into the portfolio-building journey.</div>',
    unsafe_allow_html=True,
)

c1, c2, c3 = st.columns(3, gap="large")
with c1:
    st.markdown(
        info_card(
            "Professional first impression",
            "A polished, brand-led interface that feels like a real fintech product rather than a classroom prototype."
        ),
        unsafe_allow_html=True,
    )
with c2:
    st.markdown(
        info_card(
            "Streamlined user journey",
            "The homepage avoids clutter and keeps data entry off the landing screen, improving focus and usability."
        ),
        unsafe_allow_html=True,
    )
with c3:
    st.markdown(
        info_card(
            "Clear transition to action",
            "Users are guided into a dedicated portfolio builder screen where preferences and risk inputs can be collected cleanly."
        ),
        unsafe_allow_html=True,
    )

st.markdown("<div style='height: 1.4rem;'></div>", unsafe_allow_html=True)

# Build your portfolio CTA
cta_left, cta_right = st.columns([1.15, 0.85], gap="large")

with cta_left:
    st.markdown(
        """
        <div class="cta-panel">
            <div class="section-label">Build your portfolio</div>
            <h2 class="cta-title">Start the guided portfolio creation journey</h2>
            <p class="cta-copy">
                Continue to the next screen to define investment objectives, risk appetite,
                and sustainability preferences. This keeps the homepage clean while preserving
                a premium user experience.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with cta_right:
    st.write("")
    st.write("")
    if st.button("Build Your Portfolio", type="primary", use_container_width=True):
        navigate_to_builder()

    st.caption("This button should open your separate portfolio-builder page.")

# Optional subtle page link if supported by your Streamlit version
try:
    st.page_link(TARGET_PAGE, label="Open portfolio builder page", icon="→")
except Exception:
    pass
