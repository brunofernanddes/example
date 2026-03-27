import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

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

# -------------------------------------------------
# Data for recommendation engine
# -------------------------------------------------
RECOMMENDATIONS = {
    "1": {
        "Low": {
            "Environmental": ("Microsoft (MSFT)", "Exelon (EXC)"),
            "Sustainability / Social": ("Microsoft (MSFT)", "Pinnacle West Capital (PNW)"),
            "Governance": ("Regency Centers (REG)", "Amazon (AMZN)"),
            "All Equal": ("Microsoft (MSFT)", "Exelon (EXC)"),
        },
        "Medium": {
            "Environmental": ("Microsoft (MSFT)", "Trane Technologies (TT)"),
            "Sustainability / Social": ("ConocoPhillips (COP)", "Microsoft (MSFT)"),
            "Governance": ("Amazon (AMZN)", "Microsoft (MSFT)"),
            "All Equal": ("Microsoft (MSFT)", "ConocoPhillips (COP)"),
        },
        "High": {
            "Environmental": ("Trane Technologies (TT)", "Amazon (AMZN)"),
            "Sustainability / Social": ("ConocoPhillips (COP)", "Trane Technologies (TT)"),
            "Governance": ("Amazon (AMZN)", "Raytheon Technologies (RTX)"),
            "All Equal": ("ConocoPhillips (COP)", "Amazon (AMZN)"),
        },
    },
    "2": {
        "Low": {
            "Environmental": ("Microsoft (MSFT)", "Exelon (EXC)"),
            "Sustainability / Social": ("Microsoft (MSFT)", "Exelon (EXC)"),
            "Governance": ("Regency Centers (REG)", "Amazon (AMZN)"),
            "All Equal": ("Microsoft (MSFT)", "Exelon (EXC)"),
        },
        "Medium": {
            "Environmental": ("Microsoft (MSFT)", "Trane Technologies (TT)"),
            "Sustainability / Social": ("Microsoft (MSFT)", "Trane Technologies (TT)"),
            "Governance": ("Amazon (AMZN)", "Microsoft (MSFT)"),
            "All Equal": ("Microsoft (MSFT)", "Trane Technologies (TT)"),
        },
        "High": {
            "Environmental": ("Trane Technologies (TT)", "Amazon (AMZN)"),
            "Sustainability / Social": ("Trane Technologies (TT)", "ConocoPhillips (COP)"),
            "Governance": ("Amazon (AMZN)", "Trane Technologies (TT)"),
            "All Equal": ("Trane Technologies (TT)", "Amazon (AMZN)"),
        },
    },
    "3": {
        "Low": {
            "Environmental": ("Microsoft (MSFT)", "PepsiCo (PEP)"),
            "Sustainability / Social": ("Microsoft (MSFT)", "Pinnacle West Capital (PNW)"),
            "Governance": ("Regency Centers (REG)", "Amazon (AMZN)"),
            "All Equal": ("Microsoft (MSFT)", "Exelon (EXC)"),
        },
        "Medium": {
            "Environmental": ("Microsoft (MSFT)", "Trane Technologies (TT)"),
            "Sustainability / Social": ("ConocoPhillips (COP)", "Microsoft (MSFT)"),
            "Governance": ("Amazon (AMZN)", "Microsoft (MSFT)"),
            "All Equal": ("Microsoft (MSFT)", "ConocoPhillips (COP)"),
        },
        "High": {
            "Environmental": ("Trane Technologies (TT)", "Amazon (AMZN)"),
            "Sustainability / Social": ("ConocoPhillips (COP)", "Airbnb (ABNB)"),
            "Governance": ("Amazon (AMZN)", "Raytheon Technologies (RTX)"),
            "All Equal": ("ConocoPhillips (COP)", "Edison International (EIX)"),
        },
    },
}

ASSET_DATA = {
    "PepsiCo (PEP)": {"expected_return": 7.33, "std_dev": 5.19},
    "Consolidated Edison (ED)": {"expected_return": 7.53, "std_dev": 5.22},
    "Edison International (EIX)": {"expected_return": 4.26, "std_dev": 8.20},
    "Procter & Gamble (PG)": {"expected_return": 8.61, "std_dev": 6.92},
    "Microsoft (MSFT)": {"expected_return": 23.16, "std_dev": 6.81},
    "Air Products and Chemicals (APD)": {"expected_return": 10.06, "std_dev": 6.64},
    "Regency Centers (REG)": {"expected_return": 4.14, "std_dev": 4.09},
    "Trane Technologies (TT)": {"expected_return": 23.15, "std_dev": 8.35},
    "Airbnb (ABNB)": {"expected_return": -5.81, "std_dev": 10.67},
    "Amazon (AMZN)": {"expected_return": 21.84, "std_dev": 7.90},
    "General Mills (GIS)": {"expected_return": -1.33, "std_dev": 7.33},
    "ConocoPhillips (COP)": {"expected_return": 15.21, "std_dev": 8.08},
    "Exelon (EXC)": {"expected_return": 10.72, "std_dev": 5.84},
    "Pinnacle West Capital (PNW)": {"expected_return": 7.01, "std_dev": 4.96},
    "Raytheon Technologies (RTX)": {"expected_return": 16.65, "std_dev": 8.73},
}

# -------------------------------------------------
# Session state
# -------------------------------------------------
def init_session_state() -> None:
    defaults = {
        "show_splash": True,
        "current_view": "home",  # home | recommendation | builder
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def open_home() -> None:
    st.session_state["current_view"] = "home"


def open_builder() -> None:
    st.session_state["current_view"] = "builder"


def open_recommendation() -> None:
    st.session_state["current_view"] = "recommendation"


# -------------------------------------------------
# CSS
# -------------------------------------------------
def inject_css() -> None:
    st.markdown(
        """
        <style>
            :root {
                --bg1: #f7fbfa;
                --bg2: #eef6f4;
                --card: rgba(255,255,255,0.94);
                --card-strong: rgba(255,255,255,0.98);
                --text: #0f172a;
                --muted: #475569;
                --line: rgba(15,23,42,0.08);
                --primary: #0f766e;
                --primary-2: #14b8a6;
                --shadow: 0 18px 50px rgba(15, 23, 42, 0.08);
                --shadow-soft: 0 10px 24px rgba(15, 23, 42, 0.05);
            }

            .stApp {
                background:
                    radial-gradient(circle at top left, rgba(20,184,166,0.08), transparent 28%),
                    radial-gradient(circle at top right, rgba(15,118,110,0.05), transparent 24%),
                    linear-gradient(180deg, var(--bg1) 0%, #f4f7fb 100%);
            }

            .block-container {
                max-width: 1140px;
                padding-top: 1.2rem;
                padding-bottom: 2rem;
            }

            [data-testid="stSidebarNav"] {
                display: none;
            }

            .brand-row {
                display: flex;
                align-items: center;
                gap: 0.85rem;
                margin-bottom: 1.1rem;
            }

            .logo-box {
                width: 50px;
                height: 50px;
                border-radius: 16px;
                background: linear-gradient(135deg, var(--primary), var(--primary-2));
                color: white;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 1.05rem;
                font-weight: 900;
                box-shadow: 0 12px 28px rgba(15,118,110,0.22);
            }

            .brand-title {
                margin: 0;
                color: var(--text);
                font-weight: 850;
                font-size: 1.02rem;
                letter-spacing: -0.02em;
            }

            .brand-subtitle {
                margin: 0.1rem 0 0 0;
                color: var(--muted);
                font-size: 0.91rem;
            }

            .hero {
                background: linear-gradient(135deg, rgba(255,255,255,0.96), rgba(255,255,255,0.88));
                border: 1px solid rgba(255,255,255,0.7);
                border-radius: 26px;
                padding: 2.2rem 2rem;
                box-shadow: var(--shadow);
                backdrop-filter: blur(8px);
            }

            .badge {
                display: inline-block;
                padding: 0.4rem 0.76rem;
                border-radius: 999px;
                background: rgba(15,118,110,0.09);
                color: var(--primary);
                border: 1px solid rgba(15,118,110,0.13);
                font-size: 0.82rem;
                font-weight: 800;
                margin-bottom: 0.95rem;
            }

            .hero h1 {
                margin: 0 0 0.9rem 0;
                color: var(--text);
                font-size: 3rem;
                line-height: 1.03;
                letter-spacing: -0.05em;
                font-weight: 900;
                max-width: 760px;
            }

            .hero p {
                margin: 0;
                color: #334155;
                font-size: 1.04rem;
                line-height: 1.7;
                max-width: 760px;
            }

            .pill-row {
                display: flex;
                flex-wrap: wrap;
                gap: 0.55rem;
                margin-top: 1.05rem;
            }

            .pill {
                padding: 0.42rem 0.78rem;
                border-radius: 999px;
                background: rgba(255,255,255,0.92);
                border: 1px solid var(--line);
                color: var(--text);
                font-size: 0.87rem;
                font-weight: 700;
            }

            .section-label {
                color: var(--primary);
                font-size: 0.81rem;
                font-weight: 800;
                letter-spacing: 0.08em;
                text-transform: uppercase;
                margin-bottom: 0.3rem;
            }

            .section-title {
                color: var(--text);
                font-size: 1.8rem;
                font-weight: 850;
                letter-spacing: -0.03em;
                margin-bottom: 0.35rem;
            }

            .section-copy {
                color: var(--muted);
                margin-bottom: 1rem;
                line-height: 1.65;
            }

            .card {
                background: var(--card);
                border: 1px solid rgba(255,255,255,0.72);
                border-radius: 20px;
                padding: 1.05rem;
                box-shadow: var(--shadow-soft);
                height: 100%;
            }

            .card h3 {
                margin: 0 0 0.35rem 0;
                color: var(--text);
                font-size: 1.02rem;
                font-weight: 800;
            }

            .card p {
                margin: 0;
                color: var(--muted);
                font-size: 0.95rem;
                line-height: 1.55;
            }

            .cta-panel {
                background: linear-gradient(135deg, rgba(15,118,110,0.10), rgba(20,184,166,0.05));
                border: 1px solid rgba(15,118,110,0.10);
                border-radius: 24px;
                padding: 1.35rem;
                box-shadow: var(--shadow-soft);
            }

            .cta-title {
                color: var(--text);
                font-size: 1.55rem;
                font-weight: 850;
                letter-spacing: -0.03em;
                margin: 0 0 0.35rem 0;
            }

            .cta-copy {
                color: var(--muted);
                font-size: 0.98rem;
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
                font-size: 1.35rem;
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
                min-height: 3.05rem;
                border-radius: 14px;
                font-weight: 800;
                font-size: 0.96rem;
                border: none;
            }

            .tool-shell {
                background: rgba(255,255,255,0.98);
                border: 1px solid rgba(15,23,42,0.06);
                border-radius: 24px;
                padding: 1.45rem;
                box-shadow: var(--shadow-soft);
            }

            .tool-title {
                color: #000000;
                font-size: 2rem;
                font-weight: 850;
                letter-spacing: -0.03em;
                margin: 0 0 0.2rem 0;
            }

            .tool-subtitle {
                color: #000000;
                font-size: 1rem;
                line-height: 1.6;
                margin: 0 0 1.2rem 0;
            }

            .tool-section-label {
                color: #0f766e;
                font-size: 0.78rem;
                font-weight: 800;
                text-transform: uppercase;
                letter-spacing: 0.08em;
                margin-bottom: 0.3rem;
            }

            .tool-section-title {
                color: #000000;
                font-size: 1.05rem;
                font-weight: 800;
                margin: 0.2rem 0 0.85rem 0;
            }

            .tool-divider {
                height: 1px;
                background: rgba(15, 23, 42, 0.08);
                margin: 1.1rem 0 1.2rem 0;
                border-radius: 999px;
            }

            .tool-note {
                color: #334155;
                font-size: 0.93rem;
                line-height: 1.55;
                margin-top: 0.25rem;
                margin-bottom: 0.25rem;
            }

            .metric-tile {
                background: #ffffff;
                border: 1px solid rgba(15, 23, 42, 0.07);
                border-radius: 16px;
                padding: 0.95rem 1rem;
                box-shadow: 0 8px 20px rgba(15, 23, 42, 0.04);
            }

            .metric-tile-label {
                color: #64748b;
                font-size: 0.84rem;
                margin-bottom: 0.3rem;
            }

            .metric-tile-value {
                color: #000000;
                font-size: 1.2rem;
                font-weight: 800;
                line-height: 1.2;
            }

            .asset-summary {
                background: #ffffff;
                border: 1px solid rgba(15, 23, 42, 0.07);
                border-radius: 18px;
                padding: 1rem;
                box-shadow: 0 8px 20px rgba(15, 23, 42, 0.04);
            }

            .asset-summary-title {
                color: #000000;
                font-size: 1rem;
                font-weight: 800;
                margin-bottom: 0.25rem;
            }

            .asset-summary-copy {
                color: #334155;
                font-size: 0.94rem;
                line-height: 1.55;
                margin: 0;
            }

            .chart-title {
                color: #000000;
                font-size: 1rem;
                font-weight: 800;
                margin: 0.5rem 0 0.85rem 0;
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
                pointer-events: none;
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
                0% { opacity: 1; transform: translateY(0) scale(1); filter: blur(0px); }
                100% { opacity: 0; transform: translateY(-12px) scale(0.97); filter: blur(3px); }
            }

            @keyframes copyFadeOut {
                0% { opacity: 1; transform: translateY(0); filter: blur(0px); }
                100% { opacity: 0; transform: translateY(-8px); filter: blur(2px); }
            }

            @keyframes overlayFadeOut {
                0% { opacity: 1; visibility: visible; }
                99% { opacity: 0; visibility: visible; }
                100% { opacity: 0; visibility: hidden; }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def inject_tool_black_text_css() -> None:
    st.markdown(
        """
        <style>
            .stApp,
            .stApp p,
            .stApp span,
            .stApp label,
            .stApp div,
            .stApp h1,
            .stApp h2,
            .stApp h3,
            .stApp h4,
            .stApp h5,
            .stApp h6,
            .stApp li {
                color: #000000;
            }

            [data-testid="stWidgetLabel"] p,
            [data-testid="stWidgetLabel"] label,
            .stRadio label,
            .stSlider label,
            .stTextInput label,
            .stNumberInput label,
            .stSelectbox label,
            .stMultiSelect label,
            .stCheckbox label,
            .stMarkdown p,
            .stCaption,
            small {
                color: #000000 !important;
            }

            .stRadio p,
            .stSlider p,
            .stRadio span,
            .stSlider span {
                color: #000000 !important;
            }

            input,
            textarea,
            [data-baseweb="input"] input,
            [data-baseweb="textarea"] textarea {
                color: #000000 !important;
                -webkit-text-fill-color: #000000 !important;
            }

            .stNumberInput input,
            .stTextInput input {
                color: #000000 !important;
                -webkit-text-fill-color: #000000 !important;
            }

            div[data-testid="stForm"] {
                background: #ffffff;
                border: 1px solid rgba(15, 23, 42, 0.08);
                border-radius: 22px;
                padding: 1.15rem 1.15rem 0.8rem 1.15rem;
                box-shadow: 0 10px 24px rgba(15, 23, 42, 0.04);
            }

            div[data-testid="stForm"] p,
            div[data-testid="stForm"] span,
            div[data-testid="stForm"] label,
            div[data-testid="stForm"] div,
            div[data-testid="stForm"] h1,
            div[data-testid="stForm"] h2,
            div[data-testid="stForm"] h3 {
                color: #000000 !important;
            }

            [data-testid="stAlert"] *,
            [data-testid="metric-container"] *,
            [data-testid="stMarkdownContainer"] * {
                color: #000000 !important;
            }

            div.stButton > button {
                color: #000000 !important;
                border: 1px solid rgba(15, 23, 42, 0.10) !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


# -------------------------------------------------
# Helpers
# -------------------------------------------------
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


def result_tile(label: str, value: str) -> str:
    return f"""
    <div class="metric-tile">
        <div class="metric-tile-label">{label}</div>
        <div class="metric-tile-value">{value}</div>
    </div>
    """


def risk_level_from_score(risk_tolerance: int) -> str:
    if 1 <= risk_tolerance <= 4:
        return "Low"
    if 5 <= risk_tolerance <= 7:
        return "Medium"
    return "High"


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
            "Environmental factors consider climate risk, carbon emissions, resource use, pollution, and broader ecological sustainability."
        )
    with c2:
        render_card(
            "Social (S)",
            "Social factors focus on how organisations treat people, including labour standards, diversity, community impact, health, safety, and human rights."
        )
    with c3:
        render_card(
            "Governance (G)",
            "Governance factors examine how organisations are led, including board quality, executive accountability, transparency, ethics, and shareholder rights."
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
        st.button(
            "Give me a portfolio recommendation",
            type="primary",
            use_container_width=True,
            on_click=open_recommendation,
        )
        st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
        st.button(
            "Build your portfolio based on your ESG preferences",
            use_container_width=True,
            on_click=open_builder,
        )


# -------------------------------------------------
# Recommendation screen
# -------------------------------------------------
def render_recommendation_screen() -> None:
    inject_tool_black_text_css()

    col_back, col_main = st.columns([0.14, 0.86])
    with col_back:
        st.button("← Back", on_click=open_home, use_container_width=True)

    st.markdown('<div class="tool-shell">', unsafe_allow_html=True)
    st.markdown('<div class="tool-section-label">Portfolio recommendation</div>', unsafe_allow_html=True)
    st.markdown('<div class="tool-title">Give me a portfolio recommendation</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="tool-subtitle">
            Receive a recommended two-asset portfolio based on your investment priority,
            risk tolerance, and preferred ESG focus.
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("recommendation_form", clear_on_submit=False):
        st.markdown('<div class="tool-section-label">Step 1</div>', unsafe_allow_html=True)
        st.markdown('<div class="tool-section-title">Set your preferences</div>', unsafe_allow_html=True)

        left, right = st.columns(2, gap="large")

        with left:
            investment_priority_label = st.radio(
                "Investment priority",
                [
                    "Balanced return and sustainability",
                    "Prioritise financial growth",
                    "Prioritise sustainability",
                ],
                horizontal=True,
            )

            risk_tolerance = st.slider(
                "Risk tolerance",
                min_value=1,
                max_value=10,
                value=5,
            )

        with right:
            esg_aspect = st.radio(
                "Which ESG aspect matters most?",
                ["Environmental", "Sustainability / Social", "Governance", "All Equal"],
                horizontal=True,
            )

            correlation_assumption = st.slider(
                "Portfolio correlation assumption",
                min_value=-1.0,
                max_value=1.0,
                value=0.30,
                step=0.01,
                help="Used to estimate 50/50 portfolio standard deviation for the recommended pair.",
            )

        run_recommendation = st.form_submit_button(
            "Generate portfolio recommendation",
            type="primary",
            use_container_width=True,
        )

    if run_recommendation:
        investment_priority_map = {
            "Balanced return and sustainability": "1",
            "Prioritise financial growth": "2",
            "Prioritise sustainability": "3",
        }

        investment_priority_key = investment_priority_map[investment_priority_label]
        risk_level = risk_level_from_score(risk_tolerance)

        asset1, asset2 = RECOMMENDATIONS[investment_priority_key][risk_level][esg_aspect]

        if asset1 in ASSET_DATA and asset2 in ASSET_DATA:
            exp_return1 = ASSET_DATA[asset1]["expected_return"]
            std_dev1 = ASSET_DATA[asset1]["std_dev"]
            exp_return2 = ASSET_DATA[asset2]["expected_return"]
            std_dev2 = ASSET_DATA[asset2]["std_dev"]

            w1 = 0.5
            w2 = 0.5
            s1 = std_dev1 / 100
            s2 = std_dev2 / 100
            rho = correlation_assumption

            portfolio_return = w1 * exp_return1 + w2 * exp_return2
            portfolio_std_dev = (
                np.sqrt((w1 ** 2) * (s1 ** 2) + (w2 ** 2) * (s2 ** 2) + 2 * w1 * w2 * s1 * s2 * rho) * 100
            )

            st.markdown('<div class="tool-divider"></div>', unsafe_allow_html=True)
            st.markdown('<div class="tool-section-label">Recommendation</div>', unsafe_allow_html=True)
            st.markdown('<div class="tool-section-title">Your recommended portfolio</div>', unsafe_allow_html=True)

            a1, a2 = st.columns(2, gap="large")
            with a1:
                st.markdown(
                    f"""
                    <div class="asset-summary">
                        <div class="asset-summary-title">{asset1}</div>
                        <p class="asset-summary-copy">
                            Expected return: {exp_return1:.2f}%<br>
                            Standard deviation: {std_dev1:.2f}%
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with a2:
                st.markdown(
                    f"""
                    <div class="asset-summary">
                        <div class="asset-summary-title">{asset2}</div>
                        <p class="asset-summary-copy">
                            Expected return: {exp_return2:.2f}%<br>
                            Standard deviation: {std_dev2:.2f}%
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            st.markdown("<div style='height:0.8rem;'></div>", unsafe_allow_html=True)

            r1, r2, r3 = st.columns(3)
            with r1:
                st.markdown(result_tile("Investment priority", investment_priority_label), unsafe_allow_html=True)
            with r2:
                st.markdown(result_tile("Risk level", risk_level), unsafe_allow_html=True)
            with r3:
                st.markdown(result_tile("Preferred ESG aspect", esg_aspect), unsafe_allow_html=True)

            st.markdown("<div style='height:0.7rem;'></div>", unsafe_allow_html=True)

            m1, m2 = st.columns(2)
            with m1:
                st.markdown(result_tile("50/50 expected return", f"{portfolio_return:.2f}%"), unsafe_allow_html=True)
            with m2:
                st.markdown(result_tile("50/50 portfolio risk", f"{portfolio_std_dev:.2f}%"), unsafe_allow_html=True)

            st.markdown(
                f"""
                <div class="tool-note">
                    Portfolio risk is estimated using equal weights and a correlation assumption of {correlation_assumption:.2f}.
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown('<div class="tool-divider"></div>', unsafe_allow_html=True)
            st.markdown('<div class="chart-title">Recommended asset comparison</div>', unsafe_allow_html=True)

            fig, ax = plt.subplots(figsize=(10, 5))
            labels = [asset1, asset2]
            returns = [exp_return1, exp_return2]
            risks = [std_dev1, std_dev2]
            x = np.arange(len(labels))
            width = 0.34

            ax.bar(x - width / 2, returns, width, label="Expected Return (%)")
            ax.bar(x + width / 2, risks, width, label="Standard Deviation (%)")
            ax.set_xticks(x)
            ax.set_xticklabels(labels, rotation=0)
            ax.set_ylabel("Percentage")
            ax.set_title("Recommended Asset Metrics")
            ax.legend()

            st.pyplot(fig)
            plt.close(fig)

    st.markdown('</div>', unsafe_allow_html=True)


# -------------------------------------------------
# Builder screen
# -------------------------------------------------
def render_builder_screen() -> None:
    inject_tool_black_text_css()

    col_back, col_main = st.columns([0.14, 0.86])
    with col_back:
        st.button("← Back", on_click=open_home, use_container_width=True)

    st.markdown('<div class="tool-shell">', unsafe_allow_html=True)
    st.markdown('<div class="tool-section-label">Portfolio builder</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="tool-title">Build your portfolio based on your ESG preferences</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="tool-subtitle">
            Create a simple ESG-aware portfolio recommendation using your asset assumptions,
            risk tolerance, and sustainability preferences.
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("portfolio_builder_form", clear_on_submit=False):
        st.markdown('<div class="tool-section-label">Step 1</div>', unsafe_allow_html=True)
        st.markdown('<div class="tool-section-title">Choose your setup</div>', unsafe_allow_html=True)

        top_left, top_right = st.columns(2)

        with top_left:
            asset_choice = st.radio(
                "Asset selection method",
                ["Input my own assets", "Use recommended public companies"],
                horizontal=True,
            )

        with top_right:
            investment_priority = st.radio(
                "Investment priority",
                [
                    "Balanced return and sustainability",
                    "Prioritise financial growth",
                    "Prioritise sustainability",
                ],
                horizontal=True,
            )

        st.markdown('<div class="tool-divider"></div>', unsafe_allow_html=True)

        if asset_choice == "Input my own assets":
            st.markdown('<div class="tool-section-label">Step 2</div>', unsafe_allow_html=True)
            st.markdown('<div class="tool-section-title">Enter asset assumptions</div>', unsafe_allow_html=True)

            col1, col2 = st.columns(2, gap="large")

            with col1:
                asset1 = st.text_input("Asset 1 name", value="Asset 1")
                exp_return1 = st.number_input(
                    f"{asset1} expected return (%)",
                    min_value=0.0,
                    max_value=100.0,
                    value=8.0,
                    step=0.1,
                )
                std_dev1 = st.number_input(
                    f"{asset1} standard deviation (%)",
                    min_value=0.0,
                    max_value=100.0,
                    value=15.0,
                    step=0.1,
                )
                esg_score1 = st.number_input(
                    f"{asset1} ESG score (0–100)",
                    min_value=0.0,
                    max_value=100.0,
                    value=70.0,
                    step=1.0,
                )

            with col2:
                asset2 = st.text_input("Asset 2 name", value="Asset 2")
                exp_return2 = st.number_input(
                    f"{asset2} expected return (%)",
                    min_value=0.0,
                    max_value=100.0,
                    value=12.0,
                    step=0.1,
                )
                std_dev2 = st.number_input(
                    f"{asset2} standard deviation (%)",
                    min_value=0.0,
                    max_value=100.0,
                    value=20.0,
                    step=0.1,
                )
                esg_score2 = st.number_input(
                    f"{asset2} ESG score (0–100)",
                    min_value=0.0,
                    max_value=100.0,
                    value=55.0,
                    step=1.0,
                )

            st.markdown('<div class="tool-divider"></div>', unsafe_allow_html=True)
            st.markdown('<div class="tool-section-label">Step 3</div>', unsafe_allow_html=True)
            st.markdown('<div class="tool-section-title">Set portfolio preferences</div>', unsafe_allow_html=True)

            pref_left, pref_right = st.columns(2, gap="large")

            with pref_left:
                correlation = st.slider(
                    f"Correlation between {asset1} and {asset2}",
                    min_value=-1.0,
                    max_value=1.0,
                    value=0.30,
                    step=0.01,
                )

                risk_free_rate = st.number_input(
                    "Risk-free rate (%)",
                    min_value=0.0,
                    max_value=20.0,
                    value=4.84,
                    step=0.01,
                )

                risk_tolerance = st.slider(
                    "Risk tolerance",
                    min_value=1,
                    max_value=10,
                    value=5,
                )

            with pref_right:
                esg_preference_label = st.radio(
                    "How important is ESG when choosing investments?",
                    ["Not important", "Somewhat important", "Very important"],
                    horizontal=True,
                )

                lambda_map = {
                    "Not important": 0.00,
                    "Somewhat important": 0.05,
                    "Very important": 0.10,
                }

                default_lambda = lambda_map[esg_preference_label]

                esg_slider = st.slider(
                    "ESG preference weight",
                    min_value=0.00,
                    max_value=0.10,
                    value=float(default_lambda),
                    step=0.01,
                )

                st.markdown(
                    """
                    <div class="tool-note">
                        Higher ESG weight increases the influence of sustainability scores
                        in the portfolio recommendation.
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            run_optimiser = st.form_submit_button(
                "Generate portfolio recommendation",
                type="primary",
                use_container_width=True,
            )

        else:
            st.markdown(
                """
                <div class="tool-note">
                    Recommended public companies mode can be connected next to a curated ESG-screened universe.
                </div>
                """,
                unsafe_allow_html=True,
            )

            run_optimiser = st.form_submit_button(
                "Continue",
                type="primary",
                use_container_width=True,
            )

            asset1 = asset2 = ""
            exp_return1 = exp_return2 = 0.0
            std_dev1 = std_dev2 = 0.0
            esg_score1 = esg_score2 = 0.0
            correlation = 0.0
            risk_free_rate = 0.0
            risk_tolerance = 5
            esg_slider = 0.0

    if asset_choice == "Input my own assets" and run_optimiser:
        r1 = exp_return1 / 100
        r2 = exp_return2 / 100
        s1 = std_dev1 / 100
        s2 = std_dev2 / 100
        rho = correlation
        rf = risk_free_rate / 100
        esg1 = esg_score1 / 100
        esg2 = esg_score2 / 100

        if s1 < 0 or s2 < 0:
            st.error("Standard deviations must be non-negative.")
        else:
            base_gamma = 11 - risk_tolerance

            priority_gamma_adjustment = {
                "Balanced return and sustainability": 0,
                "Prioritise financial growth": -2,
                "Prioritise sustainability": 1,
            }

            priority_esg_adjustment = {
                "Balanced return and sustainability": 0.00,
                "Prioritise financial growth": 0.00,
                "Prioritise sustainability": 0.03,
            }

            gamma = max(1, base_gamma + priority_gamma_adjustment[investment_priority])
            effective_esg_weight = min(0.15, esg_slider + priority_esg_adjustment[investment_priority])

            weights = np.linspace(0, 1, 500)

            portfolio_returns = []
            portfolio_risks = []
            portfolio_esg = []
            portfolio_sharpes = []
            portfolio_utility = []

            for w1 in weights:
                w2 = 1 - w1

                port_return = w1 * r1 + w2 * r2
                port_variance = (
                    (w1 ** 2) * (s1 ** 2)
                    + (w2 ** 2) * (s2 ** 2)
                    + 2 * w1 * w2 * s1 * s2 * rho
                )
                port_risk = np.sqrt(max(port_variance, 0))
                port_esg = w1 * esg1 + w2 * esg2
                sharpe = (port_return - rf) / port_risk if port_risk > 0 else 0.0
                utility = port_return - 0.5 * gamma * port_variance + effective_esg_weight * port_esg

                portfolio_returns.append(port_return)
                portfolio_risks.append(port_risk)
                portfolio_esg.append(port_esg)
                portfolio_sharpes.append(sharpe)
                portfolio_utility.append(utility)

            portfolio_returns = np.array(portfolio_returns)
            portfolio_risks = np.array(portfolio_risks)
            portfolio_esg = np.array(portfolio_esg)
            portfolio_sharpes = np.array(portfolio_sharpes)
            portfolio_utility = np.array(portfolio_utility)

            max_sharpe_idx = np.argmax(portfolio_sharpes)
            optimal_idx = np.argmax(portfolio_utility)

            opt_w1 = weights[optimal_idx]
            opt_w2 = 1 - opt_w1

            st.markdown('<div class="tool-divider"></div>', unsafe_allow_html=True)
            st.markdown('<div class="tool-section-label">Recommendation</div>', unsafe_allow_html=True)
            st.markdown('<div class="tool-section-title">Your ESG-aware portfolio outcome</div>', unsafe_allow_html=True)

            row1_col1, row1_col2, row1_col3 = st.columns(3)
            with row1_col1:
                st.markdown(result_tile(f"{asset1} weight", f"{opt_w1:.2%}"), unsafe_allow_html=True)
            with row1_col2:
                st.markdown(result_tile(f"{asset2} weight", f"{opt_w2:.2%}"), unsafe_allow_html=True)
            with row1_col3:
                st.markdown(result_tile("Sharpe ratio", f"{portfolio_sharpes[optimal_idx]:.2f}"), unsafe_allow_html=True)

            st.markdown("<div style='height:0.7rem;'></div>", unsafe_allow_html=True)

            row2_col1, row2_col2, row2_col3 = st.columns(3)
            with row2_col1:
                st.markdown(result_tile("Expected return", f"{portfolio_returns[optimal_idx]:.2%}"), unsafe_allow_html=True)
            with row2_col2:
                st.markdown(result_tile("Portfolio risk", f"{portfolio_risks[optimal_idx]:.2%}"), unsafe_allow_html=True)
            with row2_col3:
                st.markdown(result_tile("Portfolio ESG score", f"{portfolio_esg[optimal_idx] * 100:.2f}/100"), unsafe_allow_html=True)

            st.markdown('<div class="tool-divider"></div>', unsafe_allow_html=True)
            st.markdown('<div class="chart-title">Efficient frontier</div>', unsafe_allow_html=True)

            fig, ax = plt.subplots(figsize=(10, 6))
            scatter = ax.scatter(
                portfolio_risks,
                portfolio_returns,
                c=portfolio_esg,
                cmap="viridis",
                s=18,
            )
            ax.scatter(
                portfolio_risks[max_sharpe_idx],
                portfolio_returns[max_sharpe_idx],
                marker="*",
                s=250,
                label="Max Sharpe",
            )
            ax.scatter(
                portfolio_risks[optimal_idx],
                portfolio_returns[optimal_idx],
                marker="X",
                s=220,
                label="Optimal ESG-aware",
            )
            ax.set_xlabel("Portfolio Risk")
            ax.set_ylabel("Expected Return")
            ax.set_title("Efficient Frontier")
            ax.legend()

            cbar = plt.colorbar(scatter, ax=ax)
            cbar.set_label("Portfolio ESG Score")
            st.pyplot(fig)
            plt.close(fig)

            st.markdown('<div class="chart-title">Sensitivity to ESG preference</div>', unsafe_allow_html=True)

            lambdas = np.linspace(0.00, 0.10, 50)
            optimal_w1_list = []
            optimal_w2_list = []

            for lam in lambdas:
                utilities = []
                for i, w1 in enumerate(weights):
                    port_variance = portfolio_risks[i] ** 2
                    utility = portfolio_returns[i] - 0.5 * gamma * port_variance + lam * portfolio_esg[i]
                    utilities.append(utility)

                best_idx = np.argmax(utilities)
                optimal_w1_list.append(weights[best_idx])
                optimal_w2_list.append(1 - weights[best_idx])

            fig2, ax2 = plt.subplots(figsize=(10, 6))
            ax2.plot(lambdas, optimal_w1_list, label=f"{asset1} Weight")
            ax2.plot(lambdas, optimal_w2_list, label=f"{asset2} Weight")
            ax2.set_xlabel("ESG Preference Weight")
            ax2.set_ylabel("Optimal Portfolio Weight")
            ax2.set_title("Optimal Weights as ESG Preference Changes")
            ax2.legend()

            st.pyplot(fig2)
            plt.close(fig2)

    st.markdown('</div>', unsafe_allow_html=True)


# -------------------------------------------------
# App router
# -------------------------------------------------
init_session_state()
inject_css()

if st.session_state["current_view"] == "builder":
    render_builder_screen()
elif st.session_state["current_view"] == "recommendation":
    render_recommendation_screen()
else:
    render_home()

if st.session_state["show_splash"]:
    render_splash_overlay()
    st.session_state["show_splash"] = False
