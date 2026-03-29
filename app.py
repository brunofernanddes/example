import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import base64
import zlib
import json

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

ESG_COMPANY_DATA_B64 = """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"""

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
        "current_view": "home",
        "recommendation_result": None,
        "builder_result": None,
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


def open_recommendation_result() -> None:
    st.session_state["current_view"] = "recommendation_result"


def open_builder_result() -> None:
    st.session_state["current_view"] = "builder_result"


# -------------------------------------------------
# CSS
# -------------------------------------------------
def inject_css() -> None:
    st.markdown(
        """
        <style>
            :root {
                --bg1: #f2fcf5;
                --bg2: #e6f7ec;
                --card: rgba(255,255,255,0.96);
                --card-strong: rgba(255,255,255,0.99);
                --text: #081b14;
                --muted: #36574a;
                --line: rgba(8,27,20,0.08);
                --primary: #14532d;
                --primary-2: #166534;
                --primary-3: #15803d;
                --primary-4: #22c55e;
                --soft-green: rgba(22,163,74,0.08);
                --shadow: 0 20px 50px rgba(22, 101, 52, 0.08);
                --shadow-soft: 0 10px 24px rgba(22, 101, 52, 0.05);
            }

            .stApp {
                background:
                    radial-gradient(circle at top left, rgba(34,197,94,0.12), transparent 28%),
                    radial-gradient(circle at top right, rgba(22,163,74,0.09), transparent 24%),
                    linear-gradient(180deg, var(--bg1) 0%, var(--bg2) 100%);
            }

            .block-container {
                max-width: 1140px;
                padding-top: 1.15rem;
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
                background: linear-gradient(135deg, var(--primary), var(--primary-4));
                color: white;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 1.05rem;
                font-weight: 900;
                box-shadow: 0 12px 28px rgba(22,163,74,0.24);
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
                background: linear-gradient(135deg, rgba(255,255,255,0.98), rgba(245,255,249,0.93));
                border: 1px solid rgba(22,101,52,0.08);
                border-radius: 26px;
                padding: 2.2rem 2rem;
                box-shadow: var(--shadow);
                backdrop-filter: blur(8px);
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
                color: var(--muted);
                font-size: 1.04rem;
                line-height: 1.7;
                max-width: 760px;
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
                border: 1px solid rgba(22,101,52,0.08);
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

            .stat {
                background: var(--card-strong);
                border: 1px solid rgba(22,101,52,0.08);
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

            .page-title {
                color: #081b14;
                font-size: 2.2rem;
                font-weight: 900;
                letter-spacing: -0.04em;
                margin: 0.7rem 0 0.25rem 0;
            }

            .page-subtitle {
                color: #36574a;
                font-size: 0.98rem;
                line-height: 1.6;
                margin: 0 0 1.25rem 0;
                max-width: 760px;
            }

            div.stButton > button,
            div[data-testid="stFormSubmitButton"] > button {
                min-height: 3.02rem !important;
                border-radius: 14px !important;
                font-weight: 800 !important;
                font-size: 0.96rem !important;
                border: 1px solid var(--primary) !important;
                background: linear-gradient(135deg, var(--primary), var(--primary-3)) !important;
                color: #ffffff !important;
                box-shadow: 0 8px 18px rgba(20,83,45,0.18) !important;
                transition: all 0.18s ease !important;
            }

            div.stButton > button:hover,
            div[data-testid="stFormSubmitButton"] > button:hover {
                background: linear-gradient(135deg, #0f3f22, var(--primary)) !important;
                color: #ffffff !important;
                box-shadow: 0 12px 24px rgba(20,83,45,0.24) !important;
                transform: translateY(-1px);
            }

            div.stButton > button:focus,
            div[data-testid="stFormSubmitButton"] > button:focus {
                color: #ffffff !important;
                outline: none !important;
                box-shadow: 0 0 0 0.2rem rgba(21, 128, 61, 0.18), 0 10px 20px rgba(20,83,45,0.18) !important;
            }

            div.stButton > button p,
            div.stButton > button span,
            div.stButton > button div,
            div[data-testid="stFormSubmitButton"] > button p,
            div[data-testid="stFormSubmitButton"] > button span,
            div[data-testid="stFormSubmitButton"] > button div {
                color: #ffffff !important;
                -webkit-text-fill-color: #ffffff !important;
            }

            .tool-shell {
                background: rgba(255,255,255,0.98);
                border: 1px solid rgba(22,101,52,0.08);
                border-radius: 24px;
                padding: 1.45rem;
                box-shadow: var(--shadow-soft);
            }

            .tool-section-label {
                color: var(--primary);
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
                background: rgba(22,101,52,0.10);
                margin: 1.1rem 0 1.2rem 0;
                border-radius: 999px;
            }

            .tool-note {
                color: #2f4f43;
                font-size: 0.88rem;
                line-height: 1.55;
                margin-top: 0.2rem;
                margin-bottom: 0.2rem;
            }

            .metric-tile {
                background: #ffffff;
                border: 1px solid rgba(22,101,52,0.08);
                border-radius: 16px;
                padding: 0.95rem 1rem;
                box-shadow: 0 8px 20px rgba(22,101,52,0.04);
            }

            .metric-tile.compact {
                padding: 0.55rem 0.7rem;
                min-height: 82px;
            }

            .metric-tile-label {
                color: #58756a;
                font-size: 0.84rem;
                margin-bottom: 0.3rem;
                display: flex;
                align-items: center;
                gap: 0.35rem;
                flex-wrap: wrap;
            }

            .metric-tile.compact .metric-tile-label {
                font-size: 0.73rem;
                margin-bottom: 0.14rem;
            }

            .metric-tile-value {
                color: #000000;
                font-size: 1.2rem;
                font-weight: 800;
                line-height: 1.2;
            }

            .metric-tile.compact .metric-tile-value {
                font-size: 0.94rem;
                line-height: 1.15;
            }

            .tooltip-icon {
                display: inline-flex;
                align-items: center;
                justify-content: center;
                width: 16px;
                height: 16px;
                border-radius: 999px;
                border: 1px solid rgba(22,101,52,0.18);
                font-size: 0.72rem;
                font-weight: 800;
                color: #166534;
                background: rgba(22,163,74,0.06);
                cursor: help;
                line-height: 1;
            }

            .field-label {
                font-weight: 800;
                color: #000000;
                margin-bottom: 0.2rem;
            }

            .asset-summary {
                background: #ffffff;
                border: 1px solid rgba(22,101,52,0.08);
                border-radius: 18px;
                padding: 1rem;
                box-shadow: 0 8px 20px rgba(22,101,52,0.04);
                height: 100%;
            }

            .asset-summary.tight {
                padding: 1rem 1rem 0.95rem 1rem;
            }

            .asset-summary-title {
                color: #000000;
                font-size: 1.06rem;
                font-weight: 850;
                margin-bottom: 0.25rem;
            }

            .asset-summary-copy {
                color: #2f4f43;
                font-size: 0.94rem;
                line-height: 1.55;
                margin: 0;
            }

            .profile-shell {
                background: linear-gradient(135deg, rgba(255,255,255,0.99), rgba(245,255,249,0.96));
                border: 1px solid rgba(22,101,52,0.08);
                border-radius: 20px;
                padding: 1rem;
                box-shadow: 0 8px 20px rgba(22,101,52,0.04);
            }

            .profile-title {
                color: #081b14;
                font-size: 1rem;
                font-weight: 850;
                margin: 0 0 0.25rem 0;
            }

            .profile-copy {
                color: #36574a;
                font-size: 0.92rem;
                line-height: 1.55;
                margin: 0;
            }

            .side-header {
                color: #0b1c15;
                font-size: 1rem;
                font-weight: 850;
                margin: 0 0 0.75rem 0;
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
                    radial-gradient(circle at top left, rgba(34,197,94,0.14), transparent 28%),
                    radial-gradient(circle at top right, rgba(22,163,74,0.10), transparent 24%),
                    linear-gradient(180deg, #f3fbf6 0%, #eaf8ef 100%);
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
                background: linear-gradient(135deg, var(--primary), var(--primary-4));
                color: white;
                margin: 0 auto 1.15rem auto;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 2rem;
                font-weight: 900;
                box-shadow: 0 18px 42px rgba(22,163,74,0.24);
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
                background: rgba(22,163,74,0.08);
                border: 1px solid rgba(22,163,74,0.14);
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
                background: #ffffff !important;
            }

            div[data-baseweb="input"] {
                background: #ffffff !important;
                border-radius: 12px !important;
                border: 1px solid rgba(22,101,52,0.12) !important;
            }

            div[data-testid="stForm"] {
                background: #ffffff;
                border: 1px solid rgba(22,101,52,0.10);
                border-radius: 22px;
                padding: 1.15rem 1.15rem 0.8rem 1.15rem;
                box-shadow: 0 10px 24px rgba(22,101,52,0.04);
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
        </style>
        """,
        unsafe_allow_html=True,
    )


# -------------------------------------------------
# Helpers
# -------------------------------------------------
@st.cache_data
def load_esg_company_data() -> pd.DataFrame:
    raw = zlib.decompress(base64.b64decode(ESG_COMPANY_DATA_B64)).decode("utf-8")
    rows = json.loads(raw)
    df = pd.DataFrame(rows)
    df["ticker"] = df["ticker"].astype(str).str.upper()
    df["search_label"] = df["name"].astype(str) + " (" + df["ticker"] + ")"
    return df.sort_values("name").reset_index(drop=True)


def render_company_profile_card(company: pd.Series) -> None:
    st.markdown(
        f"""
        <div class="profile-shell">
            <div class="profile-title">ESG Profile</div>
            <p class="profile-copy">
                <strong>{company['name']}</strong> ({company['ticker']})<br>
                Industry: {company['industry']}<br>
                Overall grade: {company['total_grade']} · {company['total_level']}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("<div style='height:0.6rem;'></div>", unsafe_allow_html=True)
    a, b, c, d = st.columns(4, gap="small")
    with a:
        st.markdown(result_tile("Overall Grade", str(company["total_grade"]), compact=True), unsafe_allow_html=True)
    with b:
        st.markdown(result_tile("Environmental", str(company["environment_grade"]), compact=True), unsafe_allow_html=True)
    with c:
        st.markdown(result_tile("Social", str(company["social_grade"]), compact=True), unsafe_allow_html=True)
    with d:
        st.markdown(result_tile("Governance", str(company["governance_grade"]), compact=True), unsafe_allow_html=True)


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


def result_tile(label: str, value: str, tooltip: str | None = None, compact: bool = False) -> str:
    tooltip_html = ""
    compact_class = " compact" if compact else ""
    if tooltip:
        tooltip_html = f'<span class="tooltip-icon" title="{tooltip}">i</span>'
    return f"""
    <div class="metric-tile{compact_class}">
        <div class="metric-tile-label">{label} {tooltip_html}</div>
        <div class="metric-tile-value">{value}</div>
    </div>
    """


def risk_level_from_score(risk_tolerance: int) -> str:
    if 1 <= risk_tolerance <= 4:
        return "Low"
    if 5 <= risk_tolerance <= 7:
        return "Medium"
    return "High"


def render_risk_tolerance_helper() -> None:
    st.markdown(
        '<div class="tool-note">Low: 1-4, Medium: 5-7, High: 8-10</div>',
        unsafe_allow_html=True,
    )


def render_custom_label(text: str) -> None:
    st.markdown(f'<div class="field-label">{text}</div>', unsafe_allow_html=True)


def render_label_with_tooltip(text: str, tooltip: str) -> None:
    st.markdown(
        f'<div class="field-label">{text} <span class="tooltip-icon" title="{tooltip}">i</span></div>',
        unsafe_allow_html=True,
    )


def render_page_header(title: str, subtitle: str) -> None:
    st.markdown(f'<div class="page-title">{title}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="page-subtitle">{subtitle}</div>', unsafe_allow_html=True)


def style_modern_axes(ax) -> None:
    ax.set_facecolor("#ffffff")
    ax.grid(axis="y", linestyle="--", linewidth=0.8, alpha=0.22)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#d7e8dc")
    ax.spines["bottom"].set_color("#d7e8dc")
    ax.tick_params(colors="#234236", labelsize=10)
    ax.title.set_color("#0a1f17")
    ax.xaxis.label.set_color("#234236")
    ax.yaxis.label.set_color("#234236")


def compute_recommendation(priority_label: str, risk_tolerance: int, esg_aspect_ui: str) -> dict:
    investment_priority_map = {
        "Balanced return and sustainability": "1",
        "Prioritise financial growth": "2",
        "Prioritise sustainability": "3",
    }

    esg_internal_map = {
        "All Equal": "All Equal",
        "Governance": "Governance",
        "Environmental": "Environmental",
        "Social": "Sustainability / Social",
    }

    investment_priority_key = investment_priority_map[priority_label]
    risk_level = risk_level_from_score(risk_tolerance)
    esg_internal_key = esg_internal_map[esg_aspect_ui]

    asset1, asset2 = RECOMMENDATIONS[investment_priority_key][risk_level][esg_internal_key]
    exp_return1 = ASSET_DATA[asset1]["expected_return"]
    std_dev1 = ASSET_DATA[asset1]["std_dev"]
    exp_return2 = ASSET_DATA[asset2]["expected_return"]
    std_dev2 = ASSET_DATA[asset2]["std_dev"]

    rho = 0.30
    w1 = 0.5
    w2 = 0.5
    s1 = std_dev1 / 100
    s2 = std_dev2 / 100

    portfolio_return = w1 * exp_return1 + w2 * exp_return2
    portfolio_std_dev = (
        np.sqrt((w1 ** 2) * (s1 ** 2) + (w2 ** 2) * (s2 ** 2) + 2 * w1 * w2 * s1 * s2 * rho) * 100
    )

    return {
        "investment_priority_label": priority_label,
        "risk_tolerance": risk_tolerance,
        "risk_level": risk_level,
        "esg_aspect": esg_aspect_ui,
        "asset1": asset1,
        "asset2": asset2,
        "exp_return1": exp_return1,
        "std_dev1": std_dev1,
        "exp_return2": exp_return2,
        "std_dev2": std_dev2,
        "portfolio_return": portfolio_return,
        "portfolio_std_dev": portfolio_std_dev,
    }


def compute_builder_result(
    asset1: str,
    asset2: str,
    exp_return1: float,
    exp_return2: float,
    std_dev1: float,
    std_dev2: float,
    esg_score1: float,
    esg_score2: float,
    correlation: float,
    risk_free_rate: float,
    risk_tolerance: int,
    esg_slider: float,
) -> dict:
    r1 = exp_return1 / 100
    r2 = exp_return2 / 100
    s1 = std_dev1 / 100
    s2 = std_dev2 / 100
    rho = correlation
    rf = risk_free_rate / 100
    esg1 = esg_score1 / 100
    esg2 = esg_score2 / 100

    gamma = 11 - risk_tolerance
    weights = np.linspace(0, 1, 600)

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
        utility = port_return - 0.5 * gamma * port_variance + esg_slider * port_esg

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

    max_sharpe_idx = int(np.argmax(portfolio_sharpes))
    optimal_idx = int(np.argmax(portfolio_utility))

    opt_w1 = float(weights[optimal_idx])
    opt_w2 = float(1 - opt_w1)

    return {
        "asset1": asset1,
        "asset2": asset2,
        "weights": weights.tolist(),
        "portfolio_returns": portfolio_returns.tolist(),
        "portfolio_risks": portfolio_risks.tolist(),
        "portfolio_esg": portfolio_esg.tolist(),
        "portfolio_sharpes": portfolio_sharpes.tolist(),
        "max_sharpe_idx": max_sharpe_idx,
        "optimal_idx": optimal_idx,
        "opt_w1": opt_w1,
        "opt_w2": opt_w2,
        "opt_return": float(portfolio_returns[optimal_idx]),
        "opt_risk": float(portfolio_risks[optimal_idx]),
        "opt_esg": float(portfolio_esg[optimal_idx]),
        "opt_sharpe": float(portfolio_sharpes[optimal_idx]),
    }


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
                <h1>Build an investment portfolio that reflects both financial goals and ESG values.</h1>
                <p>
                    This app helps investors move from intention to action through a cleaner,
                    smarter portfolio experience. It places ESG preferences at the centre of the
                    decision-making process, so portfolio recommendations can better reflect both
                    financial goals and sustainability priorities.
                </p>
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

    st.markdown("<div style='height:1.5rem;'></div>", unsafe_allow_html=True)

    btn1, btn2 = st.columns(2, gap="large")
    with btn1:
        st.button(
            "Give Me a Portfolio Recommendation",
            type="primary",
            use_container_width=True,
            on_click=open_recommendation,
        )
    with btn2:
        st.button(
            "Build Your Portfolio Based on ESG Preferences",
            use_container_width=True,
            on_click=open_builder,
        )


# -------------------------------------------------
# Recommendation input screen
# -------------------------------------------------
def render_recommendation_screen() -> None:
    inject_tool_black_text_css()

    st.button("← Back", on_click=open_home, use_container_width=False)
    render_page_header(
        "Portfolio Recommendation",
        "Set your preferences to receive a recommended two-asset portfolio aligned with your investment priority, risk tolerance, and ESG focus.",
    )

    with st.form("recommendation_form", clear_on_submit=False):
        st.markdown('<div class="tool-section-label">Step 1</div>', unsafe_allow_html=True)
        st.markdown('<div class="tool-section-title">Set Your Preferences</div>', unsafe_allow_html=True)

        left, right = st.columns(2, gap="large")

        with left:
            render_custom_label("Investment Priority")
            investment_priority_label = st.radio(
                "Investment Priority",
                [
                    "Prioritise sustainability",
                    "Prioritise financial growth",
                    "Balanced return and sustainability",
                ],
                horizontal=False,
                label_visibility="collapsed",
            )

            render_custom_label("Risk Tolerance")
            risk_tolerance = st.slider(
                "Risk Tolerance",
                min_value=1,
                max_value=10,
                value=5,
                label_visibility="collapsed",
            )
            render_risk_tolerance_helper()

        with right:
            render_custom_label("Which ESG aspect matters most?")
            esg_aspect = st.radio(
                "Which ESG aspect matters most?",
                ["All Equal", "Governance", "Environmental", "Social"],
                horizontal=False,
                label_visibility="collapsed",
            )

        submitted = st.form_submit_button(
            "Generate Portfolio Recommendation",
            type="primary",
            use_container_width=True,
        )

    if submitted:
        st.session_state["recommendation_result"] = compute_recommendation(
            investment_priority_label,
            risk_tolerance,
            esg_aspect,
        )
        open_recommendation_result()
        st.rerun()


# -------------------------------------------------
# Recommendation result screen
# -------------------------------------------------
def render_recommendation_result_screen() -> None:
    inject_tool_black_text_css()
    result = st.session_state.get("recommendation_result")

    if not result:
        open_recommendation()
        st.rerun()

    st.button("← Back", on_click=open_recommendation, use_container_width=False)
    render_page_header(
        "Your Recommended Portfolio",
        "A recommended pair selected using your chosen investment priority, risk tolerance, and ESG focus.",
    )

    left, right = st.columns([0.82, 1.18], gap="large")

    with left:
        st.markdown(result_tile("Investment Priority", result["investment_priority_label"], compact=True), unsafe_allow_html=True)
        st.markdown("<div style='height:0.55rem;'></div>", unsafe_allow_html=True)

        grid1_col1, grid1_col2 = st.columns(2, gap="small")
        with grid1_col1:
            st.markdown(result_tile("Risk Level", result["risk_level"], compact=True), unsafe_allow_html=True)
        with grid1_col2:
            st.markdown(result_tile("Preferred ESG Aspect", result["esg_aspect"], compact=True), unsafe_allow_html=True)

        st.markdown("<div style='height:0.45rem;'></div>", unsafe_allow_html=True)

        grid2_col1, grid2_col2 = st.columns(2, gap="small")
        with grid2_col1:
            st.markdown(result_tile("Expected Returns", f'{result["portfolio_return"]:.2f}%', compact=True), unsafe_allow_html=True)
        with grid2_col2:
            st.markdown(
                result_tile(
                    "Portfolio Risk",
                    f'{result["portfolio_std_dev"]:.2f}%',
                    tooltip="Portfolio risk is characterised by standard deviation.",
                    compact=True,
                ),
                unsafe_allow_html=True,
            )

    with right:
        st.markdown('<div class="side-header">Recommended Assets</div>', unsafe_allow_html=True)
        st.markdown(
            f"""
            <div class="asset-summary tight">
                <div class="asset-summary-title">{result["asset1"]}</div>
                <p class="asset-summary-copy">
                    Expected return: {result["exp_return1"]:.2f}%<br>
                    Standard deviation: {result["std_dev1"]:.2f}%
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("<div style='height:0.7rem;'></div>", unsafe_allow_html=True)
        st.markdown(
            f"""
            <div class="asset-summary tight">
                <div class="asset-summary-title">{result["asset2"]}</div>
                <p class="asset-summary-copy">
                    Expected return: {result["exp_return2"]:.2f}%<br>
                    Standard deviation: {result["std_dev2"]:.2f}%
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown('<div class="tool-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">Asset Comparison</div>', unsafe_allow_html=True)

    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=180, constrained_layout=True)
    fig.patch.set_facecolor("white")
    labels = [result["asset1"], result["asset2"]]
    returns = [result["exp_return1"], result["exp_return2"]]
    risks = [result["std_dev1"], result["std_dev2"]]
    x = np.arange(len(labels))
    width = 0.34

    ax.bar(x - width / 2, returns, width, label="Expected Return (%)", color="#16a34a", edgecolor="#166534")
    ax.bar(x + width / 2, risks, width, label="Standard Deviation (%)", color="#86efac", edgecolor="#15803d")

    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("Percentage (%)")
    ax.set_title("Asset Metrics")
    style_modern_axes(ax)
    ax.legend(frameon=False)

    st.pyplot(fig)
    plt.close(fig)


# -------------------------------------------------
# Builder input screen
# -------------------------------------------------
def render_builder_screen() -> None:
    inject_tool_black_text_css()
    companies_df = load_esg_company_data()

    st.button("← Back", on_click=open_home, use_container_width=False)
    render_page_header(
        "Portfolio Builder",
        "Enter your asset assumptions and sustainability preferences to build a personalised ESG-aware portfolio.",
    )

    with st.form("portfolio_builder_form", clear_on_submit=False):
        st.markdown('<div class="tool-section-label">Step 1</div>', unsafe_allow_html=True)
        st.markdown('<div class="tool-section-title">Choose your setup</div>', unsafe_allow_html=True)

        step1_left, step1_right = st.columns([0.9, 1.1], gap="large")

        with step1_left:
            render_custom_label("Asset Selection Method")
            asset_choice = st.radio(
                "Asset Selection Method",
                ["Input my own assets", "Use recommended public companies"],
                horizontal=True,
                label_visibility="collapsed",
            )

        with step1_right:
            render_custom_label("Search Company ESG Profile")
            selected_company_label = st.selectbox(
                "Search Company ESG Profile",
                companies_df["search_label"].tolist(),
                index=None,
                placeholder="Start typing a company name...",
                label_visibility="collapsed",
            )

        if selected_company_label:
            selected_company = companies_df.loc[
                companies_df["search_label"] == selected_company_label
            ].iloc[0]
            st.markdown("<div style='height:0.75rem;'></div>", unsafe_allow_html=True)
            render_company_profile_card(selected_company)

        st.markdown('<div class="tool-divider"></div>', unsafe_allow_html=True)

        if asset_choice == "Input my own assets":
            st.markdown('<div class="tool-section-label">Step 2</div>', unsafe_allow_html=True)
            st.markdown('<div class="tool-section-title">Enter Asset Assumptions</div>', unsafe_allow_html=True)

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
            st.markdown('<div class="tool-section-title">Set Portfolio Preferences</div>', unsafe_allow_html=True)

            pref_left, pref_right = st.columns(2, gap="large")

            with pref_left:
                correlation = st.slider(
                    f"Correlation between {asset1} and {asset2}",
                    min_value=-1.0,
                    max_value=1.0,
                    value=0.30,
                    step=0.01,
                )

                render_label_with_tooltip(
                    "Risk-Free Rate",
                    "Standard rate of 4.84% as per the UK 10 year bond yield since it represents a safe, long-term investment alternative",
                )
                risk_free_rate = st.number_input(
                    "Risk-Free Rate",
                    min_value=0.0,
                    max_value=20.0,
                    value=4.84,
                    step=0.01,
                    label_visibility="collapsed",
                )
                st.caption("Defaulted to 4.84%. Change it only if you want to use a different assumption.")

                render_custom_label("Risk Tolerance")
                risk_tolerance = st.slider(
                    "Risk Tolerance",
                    min_value=1,
                    max_value=10,
                    value=5,
                    label_visibility="collapsed",
                )
                render_risk_tolerance_helper()

            with pref_right:
                render_custom_label("How important is ESG when choosing investments?")
                esg_preference_label = st.radio(
                    "How important is ESG when choosing investments?",
                    ["Not important", "Very important", "Somewhat important"],
                    horizontal=False,
                    label_visibility="collapsed",
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

            submitted = st.form_submit_button(
                "Generate Portfolio Recommendation",
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

            submitted = st.form_submit_button(
                "Continue",
                type="primary",
                use_container_width=True,
            )

            asset1 = asset2 = ""
            exp_return1 = exp_return2 = 0.0
            std_dev1 = std_dev2 = 0.0
            esg_score1 = esg_score2 = 0.0
            correlation = 0.0
            risk_free_rate = 4.84
            risk_tolerance = 5
            esg_slider = 0.0

    if asset_choice == "Input my own assets" and submitted:
        st.session_state["builder_result"] = compute_builder_result(
            asset1=asset1,
            asset2=asset2,
            exp_return1=exp_return1,
            exp_return2=exp_return2,
            std_dev1=std_dev1,
            std_dev2=std_dev2,
            esg_score1=esg_score1,
            esg_score2=esg_score2,
            correlation=correlation,
            risk_free_rate=risk_free_rate,
            risk_tolerance=risk_tolerance,
            esg_slider=esg_slider,
        )
        open_builder_result()
        st.rerun()


# -------------------------------------------------
# Builder result screen
# -------------------------------------------------
def render_builder_result_screen() -> None:
    inject_tool_black_text_css()
    result = st.session_state.get("builder_result")

    if not result:
        open_builder()
        st.rerun()

    portfolio_returns = np.array(result["portfolio_returns"])
    portfolio_risks = np.array(result["portfolio_risks"])
    portfolio_esg = np.array(result["portfolio_esg"])
    portfolio_sharpes = np.array(result["portfolio_sharpes"])
    max_sharpe_idx = result["max_sharpe_idx"]
    optimal_idx = result["optimal_idx"]

    st.button("← Back", on_click=open_builder, use_container_width=False)
    render_page_header(
        "Portfolio Builder",
        "Your ESG-aware portfolio outcome based on the assumptions and sustainability preferences you provided.",
    )

    row1_col1, row1_col2, row1_col3 = st.columns(3)
    with row1_col1:
        st.markdown(result_tile(f'{result["asset1"]} weight', f'{result["opt_w1"]:.2%}'), unsafe_allow_html=True)
    with row1_col2:
        st.markdown(result_tile(f'{result["asset2"]} weight', f'{result["opt_w2"]:.2%}'), unsafe_allow_html=True)
    with row1_col3:
        st.markdown(result_tile("Sharpe ratio", f'{result["opt_sharpe"]:.2f}'), unsafe_allow_html=True)

    st.markdown("<div style='height:0.7rem;'></div>", unsafe_allow_html=True)

    row2_col1, row2_col2, row2_col3 = st.columns(3)
    with row2_col1:
        st.markdown(result_tile("Expected return", f'{result["opt_return"]:.2%}'), unsafe_allow_html=True)
    with row2_col2:
        st.markdown(
            result_tile(
                "Portfolio risk",
                f'{result["opt_risk"]:.2%}',
                tooltip="Portfolio risk is characterised by standard deviation.",
            ),
            unsafe_allow_html=True,
        )
    with row2_col3:
        st.markdown(result_tile("Portfolio ESG score", f'{result["opt_esg"] * 100:.2f}/100'), unsafe_allow_html=True)

    st.markdown('<div class="tool-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">Efficient frontier</div>', unsafe_allow_html=True)

    fig, ax = plt.subplots(figsize=(10, 6), dpi=180, constrained_layout=True)
    fig.patch.set_facecolor("white")
    scatter = ax.scatter(
        portfolio_risks,
        portfolio_returns,
        c=portfolio_esg,
        cmap="Greens",
        s=28,
        alpha=0.92,
        edgecolors="none",
    )
    ax.scatter(
        portfolio_risks[max_sharpe_idx],
        portfolio_returns[max_sharpe_idx],
        marker="*",
        s=300,
        color="#166534",
        label="Max Sharpe",
        zorder=5,
    )
    ax.scatter(
        portfolio_risks[optimal_idx],
        portfolio_returns[optimal_idx],
        marker="X",
        s=240,
        color="#0f172a",
        label="Optimal ESG-aware",
        zorder=6,
    )

    ax.annotate(
        "Optimal ESG-aware",
        (portfolio_risks[optimal_idx], portfolio_returns[optimal_idx]),
        xytext=(10, 10),
        textcoords="offset points",
        fontsize=9,
        color="#0f172a",
        weight="bold",
    )

    ax.set_xlabel("Portfolio Risk")
    ax.set_ylabel("Expected Return")
    ax.set_title("Efficient Frontier")
    style_modern_axes(ax)
    ax.legend(frameon=False)

    cbar = plt.colorbar(scatter, ax=ax, pad=0.02)
    cbar.set_label("Portfolio ESG Score")
    cbar.outline.set_edgecolor("#d7e8dc")

    st.pyplot(fig)
    plt.close(fig)


# -------------------------------------------------
# App router
# -------------------------------------------------
init_session_state()
inject_css()

if st.session_state["current_view"] == "builder":
    render_builder_screen()
elif st.session_state["current_view"] == "builder_result":
    render_builder_result_screen()
elif st.session_state["current_view"] == "recommendation":
    render_recommendation_screen()
elif st.session_state["current_view"] == "recommendation_result":
    render_recommendation_result_screen()
else:
    render_home()

if st.session_state["show_splash"]:
    render_splash_overlay()
    st.session_state["show_splash"] = False
