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
# Data
# -------------------------------------------------
RECOMMENDATIONS = {
    "1": {
        "Low": {
            "Environmental": ("Microsoft (MSFT)", "Exelon (EXC)"),
            "Social": ("Microsoft (MSFT)", "Pinnacle West Capital (PNW)"),
            "Governance": ("Regency Centers (REG)", "Amazon (AMZN)"),
            "All Equal": ("Microsoft (MSFT)", "Exelon (EXC)"),
        },
        "Medium": {
            "Environmental": ("Microsoft (MSFT)", "Trane Technologies (TT)"),
            "Social": ("ConocoPhillips (COP)", "Microsoft (MSFT)"),
            "Governance": ("Amazon (AMZN)", "Microsoft (MSFT)"),
            "All Equal": ("Microsoft (MSFT)", "ConocoPhillips (COP)"),
        },
        "High": {
            "Environmental": ("Trane Technologies (TT)", "Amazon (AMZN)"),
            "Social": ("ConocoPhillips (COP)", "Trane Technologies (TT)"),
            "Governance": ("Amazon (AMZN)", "Raytheon Technologies (RTX)"),
            "All Equal": ("ConocoPhillips (COP)", "Amazon (AMZN)"),
        },
    },
    "2": {
        "Low": {
            "Environmental": ("Microsoft (MSFT)", "Exelon (EXC)"),
            "Social": ("Microsoft (MSFT)", "Exelon (EXC)"),
            "Governance": ("Regency Centers (REG)", "Amazon (AMZN)"),
            "All Equal": ("Microsoft (MSFT)", "Exelon (EXC)"),
        },
        "Medium": {
            "Environmental": ("Microsoft (MSFT)", "Trane Technologies (TT)"),
            "Social": ("Microsoft (MSFT)", "Trane Technologies (TT)"),
            "Governance": ("Amazon (AMZN)", "Microsoft (MSFT)"),
            "All Equal": ("Microsoft (MSFT)", "Trane Technologies (TT)"),
        },
        "High": {
            "Environmental": ("Trane Technologies (TT)", "Amazon (AMZN)"),
            "Social": ("Trane Technologies (TT)", "ConocoPhillips (COP)"),
            "Governance": ("Amazon (AMZN)", "Trane Technologies (TT)"),
            "All Equal": ("Trane Technologies (TT)", "Amazon (AMZN)"),
        },
    },
    "3": {
        "Low": {
            "Environmental": ("Microsoft (MSFT)", "PepsiCo (PEP)"),
            "Social": ("Microsoft (MSFT)", "Pinnacle West Capital (PNW)"),
            "Governance": ("Regency Centers (REG)", "Amazon (AMZN)"),
            "All Equal": ("Microsoft (MSFT)", "Exelon (EXC)"),
        },
        "Medium": {
            "Environmental": ("Microsoft (MSFT)", "Trane Technologies (TT)"),
            "Social": ("ConocoPhillips (COP)", "Microsoft (MSFT)"),
            "Governance": ("Amazon (AMZN)", "Microsoft (MSFT)"),
            "All Equal": ("Microsoft (MSFT)", "ConocoPhillips (COP)"),
        },
        "High": {
            "Environmental": ("Trane Technologies (TT)", "Amazon (AMZN)"),
            "Social": ("ConocoPhillips (COP)", "Airbnb (ABNB)"),
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
        "current_view": "home",
        "show_splash": True,
        "show_recommendation_popup": False,
        "show_builder_popup": False,
        # Recommendation widgets
        "rec_investment_priority": "Prioritise sustainability",
        "rec_risk_tolerance": 5,
        "rec_esg_aspect": "All Equal",
        # Builder widgets
        "builder_asset_choice": "Input my own assets",
        "builder_asset1": "Asset 1",
        "builder_asset2": "Asset 2",
        "builder_exp_return1": 8.0,
        "builder_exp_return2": 12.0,
        "builder_std_dev1": 15.0,
        "builder_std_dev2": 20.0,
        "builder_esg_score1": 70.0,
        "builder_esg_score2": 55.0,
        "builder_correlation": 0.30,
        "builder_risk_free_rate": 4.84,
        "builder_risk_tolerance": 5,
        "builder_esg_importance": "Somewhat important",
        "builder_esg_slider": 0.05,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


# -------------------------------------------------
# Navigation and popup state
# -------------------------------------------------
def open_home() -> None:
    st.session_state.current_view = "home"
    st.session_state.show_recommendation_popup = False
    st.session_state.show_builder_popup = False


def open_recommendation() -> None:
    st.session_state.current_view = "recommendation"
    st.session_state.show_builder_popup = False


def open_builder() -> None:
    st.session_state.current_view = "builder"
    st.session_state.show_recommendation_popup = False


def show_recommendation_popup() -> None:
    st.session_state.show_recommendation_popup = True


def hide_recommendation_popup() -> None:
    st.session_state.show_recommendation_popup = False


def show_builder_popup() -> None:
    st.session_state.show_builder_popup = True


def hide_builder_popup() -> None:
    st.session_state.show_builder_popup = False


# -------------------------------------------------
# Styling
# -------------------------------------------------
def inject_css() -> None:
    st.markdown(
        """
        <style>
            :root {
                --bg1: #f2fcf5;
                --bg2: #e6f7ec;
                --text: #081b14;
                --muted: #36574a;
                --line: rgba(8,27,20,0.08);
                --primary: #14532d;
                --primary2: #166534;
                --primary3: #15803d;
                --primary4: #22c55e;
                --soft: rgba(22,163,74,0.08);
                --shadow: 0 18px 50px rgba(20, 83, 45, 0.08);
                --shadow-soft: 0 10px 24px rgba(20, 83, 45, 0.05);
            }

            .stApp {
                background:
                    radial-gradient(circle at top left, rgba(34,197,94,0.12), transparent 28%),
                    radial-gradient(circle at top right, rgba(22,163,74,0.09), transparent 24%),
                    linear-gradient(180deg, var(--bg1) 0%, var(--bg2) 100%);
            }

            .block-container {
                max-width: 1160px;
                padding-top: 1.15rem;
                padding-bottom: 2rem;
            }

            [data-testid="stSidebarNav"] { display: none; }

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
                background: linear-gradient(135deg, var(--primary), var(--primary4));
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
                padding: 2.25rem 2rem;
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
                background: rgba(255,255,255,0.97);
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
                background: rgba(255,255,255,0.99);
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

            .page-title {
                color: var(--text);
                font-size: 2.2rem;
                font-weight: 900;
                letter-spacing: -0.04em;
                margin: 0.7rem 0 0.25rem 0;
            }

            .page-subtitle {
                color: var(--muted);
                font-size: 0.98rem;
                line-height: 1.6;
                margin: 0 0 1.25rem 0;
                max-width: 760px;
            }

            .field-label {
                font-weight: 800;
                color: #000000;
                margin-bottom: 0.2rem;
            }

            .tool-note {
                color: #2f4f43;
                font-size: 0.88rem;
                line-height: 1.55;
                margin-top: 0.2rem;
                margin-bottom: 0.2rem;
            }

            .section-divider {
                height: 1px;
                background: rgba(22,101,52,0.10);
                margin: 1.1rem 0 1.2rem 0;
                border-radius: 999px;
            }

            .popup-title {
                color: #081b14;
                font-size: 1.45rem;
                font-weight: 900;
                letter-spacing: -0.03em;
                margin: 0;
            }

            .popup-subtitle {
                color: #36574a;
                font-size: 0.92rem;
                line-height: 1.55;
                margin: 0.25rem 0 0 0;
            }

            .metric-tile {
                background: #ffffff;
                border: 1px solid rgba(22,101,52,0.08);
                border-radius: 16px;
                padding: 0.78rem 0.82rem;
                box-shadow: 0 8px 18px rgba(22,101,52,0.04);
                height: 100%;
            }

            .metric-tile-label {
                color: #58756a;
                font-size: 0.74rem;
                margin-bottom: 0.18rem;
                display: flex;
                align-items: center;
                gap: 0.35rem;
                flex-wrap: wrap;
            }

            .metric-tile-value {
                color: #000000;
                font-size: 0.95rem;
                font-weight: 800;
                line-height: 1.15;
            }

            .asset-card {
                background: #ffffff;
                border: 1px solid rgba(22,101,52,0.08);
                border-radius: 18px;
                padding: 1rem;
                box-shadow: 0 8px 20px rgba(22,101,52,0.04);
            }

            .asset-card-title {
                color: #000000;
                font-size: 1.04rem;
                font-weight: 850;
                margin-bottom: 0.25rem;
            }

            .asset-card-copy {
                color: #2f4f43;
                font-size: 0.94rem;
                line-height: 1.55;
                margin: 0;
            }

            .mini-header {
                color: #0b1c15;
                font-size: 0.98rem;
                font-weight: 850;
                margin: 0 0 0.65rem 0;
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

            div[data-testid="stVerticalBlockBorderWrapper"] {
                border-radius: 24px !important;
                border: 1px solid rgba(22,101,52,0.10) !important;
                background: rgba(255,255,255,0.98) !important;
                box-shadow: 0 18px 40px rgba(20,83,45,0.08) !important;
                padding: 0.2rem !important;
            }

            div.stButton > button,
            div[data-testid="stFormSubmitButton"] > button {
                min-height: 3.02rem !important;
                border-radius: 14px !important;
                font-weight: 800 !important;
                font-size: 0.96rem !important;
                border: 1px solid var(--primary) !important;
                background: linear-gradient(135deg, var(--primary), var(--primary3)) !important;
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

            div.stButton > button p,
            div.stButton > button span,
            div.stButton > button div,
            div[data-testid="stFormSubmitButton"] > button p,
            div[data-testid="stFormSubmitButton"] > button span,
            div[data-testid="stFormSubmitButton"] > button div {
                color: #ffffff !important;
                -webkit-text-fill-color: #ffffff !important;
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
                background: linear-gradient(135deg, var(--primary), var(--primary4));
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


def inject_tool_text_css() -> None:
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
            .stApp h6 {
                color: #000000;
            }

            [data-testid="stWidgetLabel"] p,
            [data-testid="stWidgetLabel"] label,
            .stRadio label,
            .stSlider label,
            .stTextInput label,
            .stNumberInput label,
            .stSelectbox label,
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
        </style>
        """,
        unsafe_allow_html=True,
    )


# -------------------------------------------------
# UI helpers
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


def render_page_header(title: str, subtitle: str) -> None:
    st.markdown(f'<div class="page-title">{title}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="page-subtitle">{subtitle}</div>', unsafe_allow_html=True)


def render_custom_label(text: str) -> None:
    st.markdown(f'<div class="field-label">{text}</div>', unsafe_allow_html=True)


def render_label_with_tooltip(text: str, tooltip: str) -> None:
    st.markdown(
        f'<div class="field-label">{text} <span class="tooltip-icon" title="{tooltip}">i</span></div>',
        unsafe_allow_html=True,
    )


def render_risk_tolerance_helper() -> None:
    st.markdown(
        '<div class="tool-note">Low: 1-4, Medium: 5-7, High: 8-10</div>',
        unsafe_allow_html=True,
    )


def result_tile(label: str, value: str, tooltip: str | None = None) -> str:
    tooltip_html = ""
    if tooltip:
        tooltip_html = f'<span class="tooltip-icon" title="{tooltip}">i</span>'
    return f"""
    <div class="metric-tile">
        <div class="metric-tile-label">{label} {tooltip_html}</div>
        <div class="metric-tile-value">{value}</div>
    </div>
    """


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


# -------------------------------------------------
# Computation helpers
# -------------------------------------------------
def risk_level_from_score(risk_tolerance: int) -> str:
    if 1 <= risk_tolerance <= 4:
        return "Low"
    if 5 <= risk_tolerance <= 7:
        return "Medium"
    return "High"


def compute_recommendation(priority_label: str, risk_tolerance: int, esg_aspect: str) -> dict:
    investment_priority_map = {
        "Balanced return and sustainability": "1",
        "Prioritise financial growth": "2",
        "Prioritise sustainability": "3",
    }

    investment_priority_key = investment_priority_map[priority_label]
    risk_level = risk_level_from_score(risk_tolerance)

    asset1, asset2 = RECOMMENDATIONS[investment_priority_key][risk_level][esg_aspect]
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
        "risk_level": risk_level,
        "esg_aspect": esg_aspect,
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
        "weights": weights,
        "portfolio_returns": portfolio_returns,
        "portfolio_risks": portfolio_risks,
        "portfolio_esg": portfolio_esg,
        "portfolio_sharpes": portfolio_sharpes,
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
# Popup renderers
# -------------------------------------------------
def render_recommendation_popup() -> None:
    result = compute_recommendation(
        st.session_state.rec_investment_priority,
        int(st.session_state.rec_risk_tolerance),
        st.session_state.rec_esg_aspect,
    )

    outer_left, outer_mid, outer_right = st.columns([0.08, 0.84, 0.08])
    with outer_mid:
        popup = st.container(border=True)
        with popup:
            header_left, header_right = st.columns([0.82, 0.18], gap="small")
            with header_left:
                st.markdown('<div class="popup-title">Live Portfolio Recommendation</div>', unsafe_allow_html=True)
                st.markdown(
                    '<div class="popup-subtitle">This recommendation updates live as you change the inputs below.</div>',
                    unsafe_allow_html=True,
                )
            with header_right:
                st.button("Close", key="close_rec_popup_btn", use_container_width=True, on_click=hide_recommendation_popup)

            st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

            left, right = st.columns([0.9, 1.1], gap="large")

            with left:
                st.markdown(result_tile("Investment Priority", result["investment_priority_label"]), unsafe_allow_html=True)
                st.markdown("<div style='height:0.45rem;'></div>", unsafe_allow_html=True)

                g1c1, g1c2 = st.columns(2, gap="small")
                with g1c1:
                    st.markdown(result_tile("Risk Level", result["risk_level"]), unsafe_allow_html=True)
                with g1c2:
                    st.markdown(result_tile("Preferred ESG Aspect", result["esg_aspect"]), unsafe_allow_html=True)

                st.markdown("<div style='height:0.45rem;'></div>", unsafe_allow_html=True)

                g2c1, g2c2 = st.columns(2, gap="small")
                with g2c1:
                    st.markdown(result_tile("Expected Returns", f'{result["portfolio_return"]:.2f}%'), unsafe_allow_html=True)
                with g2c2:
                    st.markdown(
                        result_tile(
                            "Portfolio Risk",
                            f'{result["portfolio_std_dev"]:.2f}%',
                            tooltip="Portfolio risk is characterised by standard deviation.",
                        ),
                        unsafe_allow_html=True,
                    )

            with right:
                st.markdown('<div class="mini-header">Recommended Assets</div>', unsafe_allow_html=True)

                st.markdown(
                    f"""
                    <div class="asset-card">
                        <div class="asset-card-title">{result["asset1"]}</div>
                        <p class="asset-card-copy">
                            Expected return: {result["exp_return1"]:.2f}%<br>
                            Standard deviation: {result["std_dev1"]:.2f}%
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                st.markdown("<div style='height:0.65rem;'></div>", unsafe_allow_html=True)
                st.markdown(
                    f"""
                    <div class="asset-card">
                        <div class="asset-card-title">{result["asset2"]}</div>
                        <p class="asset-card-copy">
                            Expected return: {result["exp_return2"]:.2f}%<br>
                            Standard deviation: {result["std_dev2"]:.2f}%
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
            st.markdown('<div class="mini-header">Asset Comparison</div>', unsafe_allow_html=True)

            fig, ax = plt.subplots(figsize=(9, 4.2), dpi=180, constrained_layout=True)
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


def render_builder_popup() -> None:
    if st.session_state.builder_asset_choice != "Input my own assets":
        outer_left, outer_mid, outer_right = st.columns([0.08, 0.84, 0.08])
        with outer_mid:
            popup = st.container(border=True)
            with popup:
                header_left, header_right = st.columns([0.82, 0.18], gap="small")
                with header_left:
                    st.markdown('<div class="popup-title">Live Portfolio Recommendation</div>', unsafe_allow_html=True)
                    st.markdown(
                        '<div class="popup-subtitle">This panel stays open while you refine your settings.</div>',
                        unsafe_allow_html=True,
                    )
                with header_right:
                    st.button("Close", key="close_builder_popup_btn_info", use_container_width=True, on_click=hide_builder_popup)

                st.info("Recommended public companies mode is ready for your curated ESG universe integration.")
        return

    try:
        result = compute_builder_result(
            asset1=st.session_state.builder_asset1,
            asset2=st.session_state.builder_asset2,
            exp_return1=float(st.session_state.builder_exp_return1),
            exp_return2=float(st.session_state.builder_exp_return2),
            std_dev1=float(st.session_state.builder_std_dev1),
            std_dev2=float(st.session_state.builder_std_dev2),
            esg_score1=float(st.session_state.builder_esg_score1),
            esg_score2=float(st.session_state.builder_esg_score2),
            correlation=float(st.session_state.builder_correlation),
            risk_free_rate=float(st.session_state.builder_risk_free_rate),
            risk_tolerance=int(st.session_state.builder_risk_tolerance),
            esg_slider=float(st.session_state.builder_esg_slider),
        )
    except Exception:
        outer_left, outer_mid, outer_right = st.columns([0.08, 0.84, 0.08])
        with outer_mid:
            popup = st.container(border=True)
            with popup:
                header_left, header_right = st.columns([0.82, 0.18], gap="small")
                with header_left:
                    st.markdown('<div class="popup-title">Live Portfolio Recommendation</div>', unsafe_allow_html=True)
                with header_right:
                    st.button("Close", key="close_builder_popup_btn_error", use_container_width=True, on_click=hide_builder_popup)
                st.error("Please check your inputs and try again.")
        return

    outer_left, outer_mid, outer_right = st.columns([0.05, 0.90, 0.05])
    with outer_mid:
        popup = st.container(border=True)
        with popup:
            header_left, header_right = st.columns([0.82, 0.18], gap="small")
            with header_left:
                st.markdown('<div class="popup-title">Live Portfolio Recommendation</div>', unsafe_allow_html=True)
                st.markdown(
                    '<div class="popup-subtitle">Your portfolio updates live as you adjust assumptions, ESG scores, risk tolerance, and ESG weight.</div>',
                    unsafe_allow_html=True,
                )
            with header_right:
                st.button("Close", key="close_builder_popup_btn", use_container_width=True, on_click=hide_builder_popup)

            st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

            row1c1, row1c2, row1c3 = st.columns(3, gap="small")
            with row1c1:
                st.markdown(result_tile(f'{result["asset1"]} weight', f'{result["opt_w1"]:.2%}'), unsafe_allow_html=True)
            with row1c2:
                st.markdown(result_tile(f'{result["asset2"]} weight', f'{result["opt_w2"]:.2%}'), unsafe_allow_html=True)
            with row1c3:
                st.markdown(result_tile("Sharpe Ratio", f'{result["opt_sharpe"]:.2f}'), unsafe_allow_html=True)

            st.markdown("<div style='height:0.45rem;'></div>", unsafe_allow_html=True)

            row2c1, row2c2, row2c3 = st.columns(3, gap="small")
            with row2c1:
                st.markdown(result_tile("Expected Return", f'{result["opt_return"]:.2%}'), unsafe_allow_html=True)
            with row2c2:
                st.markdown(
                    result_tile(
                        "Portfolio Risk",
                        f'{result["opt_risk"]:.2%}',
                        tooltip="Portfolio risk is characterised by standard deviation.",
                    ),
                    unsafe_allow_html=True,
                )
            with row2c3:
                st.markdown(result_tile("Portfolio ESG Score", f'{result["opt_esg"] * 100:.2f}/100'), unsafe_allow_html=True)

            st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
            st.markdown('<div class="mini-header">Efficient Frontier</div>', unsafe_allow_html=True)

            fig, ax = plt.subplots(figsize=(9.2, 5.1), dpi=180, constrained_layout=True)
            fig.patch.set_facecolor("white")
            scatter = ax.scatter(
                result["portfolio_risks"],
                result["portfolio_returns"],
                c=result["portfolio_esg"],
                cmap="Greens",
                s=26,
                alpha=0.92,
                edgecolors="none",
            )
            ax.scatter(
                result["portfolio_risks"][result["max_sharpe_idx"]],
                result["portfolio_returns"][result["max_sharpe_idx"]],
                marker="*",
                s=300,
                color="#166534",
                label="Max Sharpe",
                zorder=5,
            )
            ax.scatter(
                result["portfolio_risks"][result["optimal_idx"]],
                result["portfolio_returns"][result["optimal_idx"]],
                marker="X",
                s=240,
                color="#0f172a",
                label="Optimal ESG-aware",
                zorder=6,
            )

            ax.annotate(
                "Optimal ESG-aware",
                (
                    result["portfolio_risks"][result["optimal_idx"]],
                    result["portfolio_returns"][result["optimal_idx"]],
                ),
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
# Screens
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
        st.markdown("<div style='height:0.65rem;'></div>", unsafe_allow_html=True)
        render_stat("Social", "People, communities, and workplace outcomes")
        st.markdown("<div style='height:0.65rem;'></div>", unsafe_allow_html=True)
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
            "Environmental factors consider climate risk, carbon emissions, resource use, pollution, and broader ecological sustainability.",
        )
    with c2:
        render_card(
            "Social (S)",
            "Social factors focus on how organisations treat people, including labour standards, diversity, community impact, health, safety, and human rights.",
        )
    with c3:
        render_card(
            "Governance (G)",
            "Governance factors examine how organisations are led, including board quality, executive accountability, transparency, ethics, and shareholder rights.",
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


def render_recommendation_screen() -> None:
    inject_tool_text_css()

    st.button("← Back", on_click=open_home, use_container_width=False)
    render_page_header(
        "Portfolio Recommendation",
        "Set your preferences below. When you generate a recommendation, a live popup-style panel appears on the same screen and updates as you refine the inputs.",
    )

    if st.session_state.show_recommendation_popup:
        render_recommendation_popup()
        st.markdown("<div style='height:1.05rem;'></div>", unsafe_allow_html=True)

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-label">Step 1</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Set Your Preferences</div>', unsafe_allow_html=True)

    left, right = st.columns(2, gap="large")

    with left:
        render_custom_label("Investment Priority")
        st.radio(
            "Investment Priority",
            [
                "Prioritise sustainability",
                "Prioritise financial growth",
                "Balanced return and sustainability",
            ],
            key="rec_investment_priority",
            horizontal=False,
            label_visibility="collapsed",
        )

        render_custom_label("Risk Tolerance")
        st.slider(
            "Risk Tolerance",
            min_value=1,
            max_value=10,
            key="rec_risk_tolerance",
            label_visibility="collapsed",
        )
        render_risk_tolerance_helper()

    with right:
        render_custom_label("Which ESG aspect matters most?")
        st.radio(
            "Which ESG aspect matters most?",
            ["All Equal", "Governance", "Environmental", "Social"],
            key="rec_esg_aspect",
            horizontal=False,
            label_visibility="collapsed",
        )

    st.markdown("<div style='height:1rem;'></div>", unsafe_allow_html=True)
    st.button(
        "Generate Portfolio Recommendation",
        type="primary",
        use_container_width=True,
        on_click=show_recommendation_popup,
    )


def render_builder_screen() -> None:
    inject_tool_text_css()

    st.button("← Back", on_click=open_home, use_container_width=False)
    render_page_header(
        "Portfolio Builder",
        "Build a personalised ESG-aware portfolio. The recommendation opens in a live popup-style panel on this same screen and updates as you change the inputs.",
    )

    if st.session_state.show_builder_popup:
        render_builder_popup()
        st.markdown("<div style='height:1.05rem;'></div>", unsafe_allow_html=True)

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-label">Step 1</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Choose Your Setup</div>', unsafe_allow_html=True)

    render_custom_label("Asset Selection Method")
    st.radio(
        "Asset Selection Method",
        ["Input my own assets", "Use recommended public companies"],
        key="builder_asset_choice",
        horizontal=True,
        label_visibility="collapsed",
    )

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-label">Step 2</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Enter Asset Assumptions</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")
    with col1:
        asset1_value = st.text_input("Asset 1 name", key="builder_asset1")
        st.number_input(
            f"{asset1_value} expected return (%)",
            min_value=0.0,
            max_value=100.0,
            step=0.1,
            key="builder_exp_return1",
        )
        st.number_input(
            f"{asset1_value} standard deviation (%)",
            min_value=0.0,
            max_value=100.0,
            step=0.1,
            key="builder_std_dev1",
        )
        st.number_input(
            f"{asset1_value} ESG score (0–100)",
            min_value=0.0,
            max_value=100.0,
            step=1.0,
            key="builder_esg_score1",
        )

    with col2:
        asset2_value = st.text_input("Asset 2 name", key="builder_asset2")
        st.number_input(
            f"{asset2_value} expected return (%)",
            min_value=0.0,
            max_value=100.0,
            step=0.1,
            key="builder_exp_return2",
        )
        st.number_input(
            f"{asset2_value} standard deviation (%)",
            min_value=0.0,
            max_value=100.0,
            step=0.1,
            key="builder_std_dev2",
        )
        st.number_input(
            f"{asset2_value} ESG score (0–100)",
            min_value=0.0,
            max_value=100.0,
            step=1.0,
            key="builder_esg_score2",
        )

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-label">Step 3</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Set Portfolio Preferences</div>', unsafe_allow_html=True)

    pref_left, pref_right = st.columns(2, gap="large")

    with pref_left:
        st.slider(
            f"Correlation between {st.session_state.builder_asset1} and {st.session_state.builder_asset2}",
            min_value=-1.0,
            max_value=1.0,
            step=0.01,
            key="builder_correlation",
        )

        render_label_with_tooltip(
            "Risk-Free Rate",
            "Standard rate of 4.84% as per the UK 10 year bond yield since it represents a safe, long-term investment alternative",
        )
        st.number_input(
            "Risk-Free Rate",
            min_value=0.0,
            max_value=20.0,
            step=0.01,
            key="builder_risk_free_rate",
            label_visibility="collapsed",
        )

        render_custom_label("Risk Tolerance")
        st.slider(
            "Risk Tolerance",
            min_value=1,
            max_value=10,
            key="builder_risk_tolerance",
            label_visibility="collapsed",
        )
        render_risk_tolerance_helper()

    with pref_right:
        render_custom_label("How important is ESG when choosing investments?")
        st.radio(
            "How important is ESG when choosing investments?",
            ["Not important", "Very important", "Somewhat important"],
            key="builder_esg_importance",
            horizontal=False,
            label_visibility="collapsed",
        )

        lambda_map = {
            "Not important": 0.00,
            "Somewhat important": 0.05,
            "Very important": 0.10,
        }

        preferred_lambda = lambda_map[st.session_state.builder_esg_importance]
        if abs(st.session_state.builder_esg_slider - preferred_lambda) > 1e-9 and not st.session_state.show_builder_popup:
            st.session_state.builder_esg_slider = preferred_lambda

        st.slider(
            "ESG preference weight",
            min_value=0.00,
            max_value=0.10,
            step=0.01,
            key="builder_esg_slider",
        )
        st.markdown(
            """
            <div class="tool-note">
                Higher ESG weight increases the influence of sustainability scores in the portfolio recommendation.
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<div style='height:1rem;'></div>", unsafe_allow_html=True)
    st.button(
        "Generate Portfolio Recommendation",
        type="primary",
        use_container_width=True,
        on_click=show_builder_popup,
    )


# -------------------------------------------------
# App router
# -------------------------------------------------
init_session_state()
inject_css()

if st.session_state.current_view == "recommendation":
    render_recommendation_screen()
elif st.session_state.current_view == "builder":
    render_builder_screen()
else:
    render_home()

if st.session_state.show_splash:
    render_splash_overlay()
    st.session_state.show_splash = False
