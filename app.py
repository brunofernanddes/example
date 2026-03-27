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

# Update these to match your actual Streamlit page filenames
RECOMMENDATION_PAGE = "pages/1_Portfolio_Recommendation.py"
BUILDER_PAGE = "pages/2_Build_Your_Portfolio.py"


# -------------------------------------------------
# Session state
# -------------------------------------------------
def init_session_state() -> None:
    defaults = {
        "show_splash": True,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


# -------------------------------------------------
# Navigation
# -------------------------------------------------
def go_to_recommendation() -> None:
    try:
        st.switch_page(RECOMMENDATION_PAGE)
    except Exception:
        st.warning(
            f"Create a page at '{RECOMMENDATION_PAGE}' so this button can open your recommendation screen."
        )


def go_to_builder() -> None:
    try:
        st.switch_page(BUILDER_PAGE)
    except Exception:
        st.warning(
            f"Create a page at '{BUILDER_PAGE}' so this button can open your portfolio builder."
        )


# -------------------------------------------------
# Styling
# -------------------------------------------------
def inject_css() -> None:
    st.markdown(
        """
        <style>
            :root {
                --bg1: #f7fbfa;
                --bg2: #eef6f4;
                --card: rgba(255,255,255,0.86);
                --card-strong: rgba(255,255,255,0.96);
                --text: #0f172a;
                --muted: #475569;
                --line: rgba(15,23,42,0.08);
                --primary: #0f766e;
                --primary-2: #14b8a6;
                --shadow: 0 18px 50px rgba(15, 23, 42, 0.08);
                --shadow-soft: 0 10px 28px rgba(15, 23, 42, 0.05);
            }

            .stApp {
                background:
                    radial-gradient(circle at top left, rgba(20,184,166,0.10), transparent 28%),
                    radial-gradient(circle at top right, rgba(15,118,110,0.07), transparent 24%),
                    linear-gradient(180deg, var(--bg1) 0%, #f3f7fb 100%);
            }

            .block-container {
                max-width: 1180px;
                padding-top: 1.3rem;
                padding-bottom: 2rem;
            }

            [data-testid="stSidebarNav"] {
                display: none;
            }

            .brand-row {
                display: flex;
                align-items: center;
                gap: 0.85rem;
                margin-bottom: 1.2rem;
            }

            .logo-box {
                width: 52px;
                height: 52px;
                border-radius: 16px;
                background: linear-gradient(135deg, var(--primary), var(--primary-2));
                color: white;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 1.1rem;
                font-weight: 900;
                box-shadow: 0 14px 34px rgba(15,118,110,0.22);
            }

            .brand-title {
                margin: 0;
                color: var(--text);
                font-weight: 850;
                font-size: 1.04rem;
                letter-spacing: -0.02em;
            }

            .brand-subtitle {
                margin: 0.12rem 0 0 0;
                color: var(--muted);
                font-size: 0.92rem;
            }

            .hero {
                background: linear-gradient(135deg, rgba(255,255,255,0.92), rgba(255,255,255,0.78));
                border: 1px solid rgba(255,255,255,0.68);
                border-radius: 28px;
                padding: 2.35rem 2.2rem;
                box-shadow: var(--shadow);
                backdrop-filter: blur(8px);
            }

            .badge {
                display: inline-block;
                padding: 0.42rem 0.78rem;
                border-radius: 999px;
                background: rgba(15,118,110,0.09);
                color: var(--primary);
                border: 1px solid rgba(15,118,110,0.13);
                font-size: 0.82rem;
                font-weight: 800;
                margin-bottom: 0.95rem;
            }

            .hero h1 {
                margin: 0 0 0.95rem 0;
                color: var(--text);
                font-size: 3.1rem;
                line-height: 1.02;
                letter-spacing: -0.05em;
                font-weight: 900;
                max-width: 760px;
            }

            .hero p {
                margin: 0;
                color: #334155;
                font-size: 1.08rem;
                line-height: 1.65;
                max-width: 760px;
            }

            .pill-row {
                display: flex;
                flex-wrap: wrap;
                gap: 0.55rem;
                margin-top: 1.1rem;
            }

            .pill {
                padding: 0.45rem 0.8rem;
                border-radius: 999px;
                background: rgba(255,255,255,0.90);
                border: 1px solid var(--line);
                color: var(--text);
                font-size: 0.88rem;
                font-weight: 700;
            }

            .section-label {
                color: var(--primary);
                font-size: 0.82rem;
                font-weight: 800;
                letter-spacing: 0.08em;
                text-transform: uppercase;
                margin-bottom: 0.35rem;
            }

            .section-title {
                color: var(--text);
                font-size: 1.85rem;
                font-weight: 850;
                letter-spacing: -0.03em;
                margin-bottom: 0.35rem;
            }

            .section-copy {
                color: var(--muted);
                margin-bottom: 1rem;
                line-height: 1.6;
            }

            .card {
                background: var(--card);
                border: 1px solid rgba(255,255,255,0.7);
                border-radius: 22px;
                padding: 1.15rem;
                box-shadow: var(--shadow-soft);
                backdrop-filter: blur(8px);
                height: 100%;
            }

            .card h3 {
                margin: 0 0 0.35rem 0;
                color: var(--text);
                font-size: 1.05rem;
                font-weight: 800;
            }

            .card p {
                margin: 0;
                color: var(--muted);
                font-size: 0.96rem;
                line-height: 1.55;
            }

            .cta-panel {
                background: linear-gradient(135deg, rgba(15,118,110,0.12), rgba(20,184,166,0.07));
                border: 1px solid rgba(15,118,110,0.13);
                border-radius: 28px;
                padding: 1.5rem;
                box-shadow: var(--shadow);
            }

            .cta-title {
                color: var(--text);
                font-size: 1.65rem;
                font-weight: 850;
                letter-spacing: -0.03em;
                margin: 0 0 0.35rem 0;
            }

            .cta-copy {
                color: var(--muted);
                font-size: 1rem;
                line-height: 1.6;
                margin: 0;
            }

            .stat {
                background: var(--card-strong);
                border: 1px solid var(--line);
                border-radius: 18px;
                padding: 0.95rem 1rem;
                box-shadow: var(--shadow-soft);
            }

            .stat-value {
                color: var(--text);
                font-size: 1.45rem;
                font-weight: 850;
                margin: 0;
            }

            .stat-label {
                color: var(--muted);
                font-size: 0.9rem;
                margin-top: 0.15rem;
            }

            .spacer {
                height: 0.65rem;
            }

            div.stButton > button {
                min-height: 3.2rem;
                border-radius: 14px;
                font-weight: 800;
                font-size: 0.98rem;
                border: none;
            }

            .splash-overlay {
                position: fixed;
                inset: 0;
                z-index: 9999;
                display: flex;
                align-items: center;
                justify-content: center;
                background:
                    radial-gradient(circle at top left, rgba(20,184,166,0.14), transparent 28%),
                    radial-gradient(circle at top right, rgba(15,118,110,0.10), transparent 24%),
                    linear-gradient(180deg, #f7fbfa 0%, #f3f7fb 100%);
                animation: overlayFadeOut 0.9s ease 2s forwards;
            }

            .splash-card {
                text-align: center;
                padding: 2.5rem 2rem;
                width: min(720px, 92vw);
            }

            .splash-logo {
                width: 100px;
                height: 100px;
                border-radius: 28px;
                background: linear-gradient(135deg, var(--primary), var(--primary-2));
                color: white;
                margin: 0 auto 1.15rem auto;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 2rem;
                font-weight: 900;
                box-shadow: 0 18px 42px rgba(15,118,110,0.25);
                animation: brandFadeOut 0.8s ease 2s forwards;
            }

            .splash-title {
                color: var(--text);
                font-size: 2.7rem;
                font-weight: 900;
                letter-spacing: -0.05em;
                margin: 0;
                animation: brandFadeOut 0.8s ease 2s forwards;
            }

            .splash-copy {
                color: var(--muted);
                font-size: 1.03rem;
                line-height: 1.65;
                margin: 0.7rem auto 0 auto;
                max-width: 540px;
                animation: copyFadeOut 0.7s ease 2.05s forwards;
            }

            .splash-tag {
                display: inline-block;
                margin-top: 1rem;
                padding: 0.4rem 0.75rem;
                border-radius: 999px;
                background: rgba(15,118,110,0.08);
                border: 1px solid rgba(15,118,110,0.12);
                color: var(--primary);
                font-size: 0.82rem;
                font-weight: 800;
                animation: copyFadeOut 0.7s ease 2.1s forwards;
            }

            @keyframes brandFadeOut {
                0% {
                    opacity: 1;
                    transform: translateY(0) scale(1);
                    filter: blur(0px);
                }
                100% {
                    opacity: 0;
                    transform: translateY(-12px) scale(0.97);
                    filter: blur(3px);
                }
            }

            @keyframes copyFadeOut {
                0% {
                    opacity: 1;
                    transform: translateY(0);
                    filter: blur(0px);
                }
                100% {
                    opacity: 0;
                    transform: translateY(-8px);
                    filter: blur(2px);
                }
            }

            @keyframes overlayFadeOut {
                0% {
                    opacity: 1;
                    visibility: visible;
                }
                99% {
                    opacity: 0;
                    visibility: visible;
                }
                100% {
                    opacity: 0;
                    visibility: hidden;
                }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


# -------------------------------------------------
# Reusable sections
# -------------------------------------------------
def render_stat(value: str, label: str) -> None:
    st.markdown(
        f"""
        <div class="stat">
            <div class="stat-value">{value}</div>
            <div class="stat-label">{label}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_card(title: str, body: str) -> None:
    st.markdown(
        f"""
        <div class="card">
            <h3>{title}</h3>
            <p>{body}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_splash_overlay() -> None:
    st.markdown(
        f"""
        <div class="splash-overlay">
            <div class="splash-card">
                <div class="splash-logo">VW</div>
                <div class="splash-title">{APP_NAME}</div>
                <div class="splash-copy">
                    {APP_TAGLINE}<br>
                    A streamlined sustainable finance experience built around
                    financial risk and ESG priorities.
                </div>
                <div class="splash-tag">Professional • Personalised • ESG-aware</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# -------------------------------------------------
# Homepage
# -------------------------------------------------
def render_home() -> None:
    st.markdown(
        f"""
        <div class="brand-row">
            <div class="logo-box">VW</div>
            <div>
                <p class="brand-title">{APP_NAME}</p>
                <p class="brand-subtitle">{APP_TAGLINE}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    left, right = st.columns([1.35, 0.65], gap="large")

    with left:
        st.markdown(
            """
            <div class="hero">
                <div class="badge">Personalised sustainable investing</div>
                <h1>Build an investment portfolio that reflects both financial goals and ESG values.</h1>
                <p>
                    This app helps investors move from intention to action through a cleaner,
                    smarter portfolio experience. It places ESG preferences at the centre of the
                    decision-making process, so portfolio recommendations can better reflect both
                    financial goals and sustainability priorities.
                </p>
                <div class="pill-row">
                    <span class="pill">Risk-aware design</span>
                    <span class="pill">ESG-first thinking</span>
                    <span class="pill">Portfolio optimisation</span>
                    <span class="pill">Professional user journey</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        render_stat("Environmental", "Climate, energy, and ecological impact")
        st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
        render_stat("Social", "People, communities, and workplace outcomes")
        st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
        render_stat("Governance", "Leadership, ethics, and accountability")

    st.markdown("<div style='height:1.2rem;'></div>", unsafe_allow_html=True)

    st.markdown('<div class="section-label">Why this app?</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-title">An investment app that prioritises ESG preferences</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="section-copy">
            This app is designed for investors who want their portfolios to reflect more than financial return alone.
            It prioritises ESG preferences by allowing sustainability considerations to play a central role in portfolio
            construction, helping users align their investments with environmental values, social impact priorities,
            and expectations around strong governance.
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3, gap="large")
    with c1:
        render_card(
            "Environmental (E)",
            "Environmental factors consider how investments interact with climate risk, carbon emissions, resource use, pollution, and wider ecological sustainability."
        )
    with c2:
        render_card(
            "Social (S)",
            "Social factors focus on how organisations treat people, including labour standards, diversity and inclusion, community impact, health, safety, and human rights."
        )
    with c3:
        render_card(
            "Governance (G)",
            "Governance factors examine how organisations are led, including board quality, executive accountability, shareholder rights, transparency, and ethical decision-making."
        )

    st.markdown("<div style='height:1.4rem;'></div>", unsafe_allow_html=True)

    cta_left, cta_right = st.columns([1.15, 0.85], gap="large")

    with cta_left:
        st.markdown(
            """
            <div class="cta-panel">
                <div class="section-label">Choose your next step</div>
                <h2 class="cta-title">Explore portfolio outcomes or build your own</h2>
                <p class="cta-copy">
                    You can move straight to a portfolio recommendation or continue to a dedicated
                    journey that builds a portfolio around your ESG priorities and investment preferences.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with cta_right:
        if st.button("Give me a portfolio recommendation", type="primary", use_container_width=True):
            go_to_recommendation()

        st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

        if st.button("Build your portfolio based on your ESG preferences", use_container_width=True):
            go_to_builder()


# -------------------------------------------------
# Run app
# -------------------------------------------------
init_session_state()
inject_css()
render_home()

if st.session_state["show_splash"]:
    render_splash_overlay()
    st.session_state["show_splash"] = False
