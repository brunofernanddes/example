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
# Recommendation engine data
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

# Built-in ESG lookup data so the app works with only streamlit/numpy/matplotlib
ESG_COMPANY_PROFILES = [
    {
        "display_name": "Airbnb (ABNB)",
        "grade": "B",
        "environment": "B",
        "social": "B",
        "governance": "B",
        "industry": "Consumer Services",
        "exchange": "NASDAQ",
    },
    {
        "display_name": "Amazon (AMZN)",
        "grade": "B",
        "environment": "B",
        "social": "B",
        "governance": "A",
        "industry": "Consumer Discretionary",
        "exchange": "NASDAQ",
    },
    {
        "display_name": "ConocoPhillips (COP)",
        "grade": "B",
        "environment": "B",
        "social": "B",
        "governance": "B",
        "industry": "Energy",
        "exchange": "NYSE",
    },
    {
        "display_name": "Consolidated Edison (ED)",
        "grade": "A",
        "environment": "A",
        "social": "B",
        "governance": "A",
        "industry": "Utilities",
        "exchange": "NYSE",
    },
    {
        "display_name": "Edison International (EIX)",
        "grade": "B",
        "environment": "B",
        "social": "B",
        "governance": "B",
        "industry": "Utilities",
        "exchange": "NYSE",
    },
    {
        "display_name": "Exelon (EXC)",
        "grade": "A",
        "environment": "A",
        "social": "B",
        "governance": "A",
        "industry": "Utilities",
        "exchange": "NASDAQ",
    },
    {
        "display_name": "General Mills (GIS)",
        "grade": "B",
        "environment": "B",
        "social": "B",
        "governance": "B",
        "industry": "Consumer Staples",
        "exchange": "NYSE",
    },
    {
        "display_name": "Microsoft (MSFT)",
        "grade": "A",
        "environment": "A",
        "social": "A",
        "governance": "A",
        "industry": "Technology",
        "exchange": "NASDAQ",
    },
    {
        "display_name": "PepsiCo (PEP)",
        "grade": "A",
        "environment": "B",
        "social": "A",
        "governance": "A",
        "industry": "Consumer Staples",
        "exchange": "NASDAQ",
    },
    {
        "display_name": "Pinnacle West Capital (PNW)",
        "grade": "A",
        "environment": "A",
        "social": "B",
        "governance": "A",
        "industry": "Utilities",
        "exchange": "NYSE",
    },
    {
        "display_name": "Procter & Gamble (PG)",
        "grade": "A",
        "environment": "B",
        "social": "A",
        "governance": "A",
        "industry": "Consumer Staples",
        "exchange": "NYSE",
    },
    {
        "display_name": "Raytheon Technologies (RTX)",
        "grade": "B",
        "environment": "B",
        "social": "B",
        "governance": "A",
        "industry": "Industrials",
        "exchange": "NYSE",
    },
    {
        "display_name": "Regency Centers (REG)",
        "grade": "A",
        "environment": "B",
        "social": "A",
        "governance": "A",
        "industry": "Real Estate",
        "exchange": "NASDAQ",
    },
    {
        "display_name": "Trane Technologies (TT)",
        "grade": "A",
        "environment": "A",
        "social": "B",
        "governance": "A",
        "industry": "Industrials",
        "exchange": "NYSE",
    },
]

# -------------------------------------------------
# Session state
# -------------------------------------------------
def init_session_state():
    defaults = {
        "show_splash": True,
        "current_view": "home",
        "recommendation_result": None,
        "builder_result": None,
        "builder_asset_choice": "Input my own assets",
        "selected_company_lookup": None,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def open_home():
    st.session_state["current_view"] = "home"


def open_builder():
    st.session_state["current_view"] = "builder"


def open_recommendation():
    st.session_state["current_view"] = "recommendation"


def open_recommendation_result():
    st.session_state["current_view"] = "recommendation_result"


def open_builder_result():
    st.session_state["current_view"] = "builder_result"


# -------------------------------------------------
# CSS
# -------------------------------------------------
def inject_css():
    st.markdown(
        """
        <style>
            .stApp {
                background:
                    radial-gradient(circle at top left, rgba(34,197,94,0.12), transparent 28%),
                    radial-gradient(circle at top right, rgba(22,163,74,0.09), transparent 24%),
                    linear-gradient(180deg, #f2fcf5 0%, #e6f7ec 100%);
            }

            .block-container {
                max-width: 1140px;
                padding-top: 1.15rem;
                padding-bottom: 2rem;
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
                background: linear-gradient(135deg, #14532d, #22c55e);
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
                color: #081b14;
                font-weight: 850;
                font-size: 1.02rem;
            }

            .brand-subtitle {
                margin: 0.1rem 0 0 0;
                color: #36574a;
                font-size: 0.91rem;
            }

            .hero {
                background: linear-gradient(135deg, rgba(255,255,255,0.98), rgba(245,255,249,0.93));
                border: 1px solid rgba(22,101,52,0.08);
                border-radius: 26px;
                padding: 2.2rem 2rem;
                box-shadow: 0 20px 50px rgba(22, 101, 52, 0.08);
            }

            .hero h1 {
                margin: 0 0 0.9rem 0;
                color: #081b14;
                font-size: 3rem;
                line-height: 1.03;
                font-weight: 900;
            }

            .hero p {
                margin: 0;
                color: #36574a;
                font-size: 1.04rem;
                line-height: 1.7;
            }

            .section-label {
                color: #14532d;
                font-size: 0.81rem;
                font-weight: 800;
                letter-spacing: 0.08em;
                text-transform: uppercase;
                margin-bottom: 0.3rem;
            }

            .section-title {
                color: #081b14;
                font-size: 1.8rem;
                font-weight: 850;
                margin-bottom: 0.35rem;
            }

            .section-copy {
                color: #36574a;
                margin-bottom: 1rem;
                line-height: 1.65;
            }

            .card, .stat, .tool-shell, .lookup-shell, .profile-card, .asset-summary, .metric-tile {
                background: rgba(255,255,255,0.98);
                border: 1px solid rgba(22,101,52,0.08);
                border-radius: 18px;
                box-shadow: 0 10px 24px rgba(22, 101, 52, 0.05);
            }

            .card {
                padding: 1.05rem;
                height: 100%;
            }

            .card h3, .stat-value, .asset-summary-title, .profile-title {
                color: #081b14;
                font-weight: 850;
            }

            .card p, .stat-label, .profile-copy, .asset-summary-copy {
                color: #36574a;
            }

            .stat {
                padding: 0.95rem 1rem;
            }

            .stat-value {
                font-size: 1.35rem;
                margin: 0;
            }

            .stat-label {
                font-size: 0.9rem;
                margin-top: 0.15rem;
            }

            .page-title {
                color: #081b14;
                font-size: 2.2rem;
                font-weight: 900;
                margin: 0.7rem 0 0.25rem 0;
            }

            .page-subtitle {
                color: #36574a;
                font-size: 0.98rem;
                line-height: 1.6;
                margin: 0 0 1.25rem 0;
            }

            .tool-shell, .lookup-shell, .profile-card, .asset-summary, .metric-tile {
                padding: 1rem;
            }

            .tool-section-label {
                color: #14532d;
                font-size: 0.78rem;
                font-weight: 800;
                text-transform: uppercase;
                letter-spacing: 0.08em;
                margin-bottom: 0.3rem;
            }

            .tool-section-title, .side-header {
                color: #081b14;
                font-size: 1.05rem;
                font-weight: 850;
                margin: 0.2rem 0 0.85rem 0;
            }

            .tool-divider {
                height: 1px;
                background: rgba(22,101,52,0.10);
                margin: 1.1rem 0 1.2rem 0;
                border-radius: 999px;
            }

            .tool-note, .lookup-subtitle {
                color: #36574a;
                font-size: 0.88rem;
                line-height: 1.55;
            }

            .field-label {
                font-weight: 800;
                color: #000000;
                margin-bottom: 0.2rem;
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

            .metric-tile-value {
                color: #000000;
                font-size: 1.2rem;
                font-weight: 800;
                line-height: 1.2;
            }

            .compact {
                padding: 0.55rem 0.7rem !important;
                min-height: 82px;
            }

            .compact .metric-tile-label {
                font-size: 0.73rem;
                margin-bottom: 0.14rem;
            }

            .compact .metric-tile-value {
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

            div.stButton > button,
            div[data-testid="stFormSubmitButton"] > button {
                min-height: 3.02rem !important;
                border-radius: 14px !important;
                font-weight: 800 !important;
                font-size: 0.96rem !important;
                border: 1px solid #14532d !important;
                background: linear-gradient(135deg, #14532d, #15803d) !important;
                color: #ffffff !important;
                box-shadow: 0 8px 18px rgba(20,83,45,0.18) !important;
            }

            div.stButton > button:hover,
            div[data-testid="stFormSubmitButton"] > button:hover {
                background: linear-gradient(135deg, #0f3f22, #14532d) !important;
                color: #ffffff !important;
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
                background: linear-gradient(135deg, #14532d, #22c55e);
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
                color: #081b14;
                font-size: 2.7rem;
                font-weight: 900;
                margin: 0;
                animation: brandFadeOut 0.8s ease 2s forwards;
            }

            .splash-copy {
                color: #36574a;
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
                color: #14532d;
                font-size: 0.82rem;
                font-weight: 800;
                animation: copyFadeOut 0.7s ease 2.1s forwards;
            }

            @keyframes brandFadeOut {
                0% { opacity: 1; transform: translateY(0) scale(1); }
                100% { opacity: 0; transform: translateY(-12px) scale(0.97); }
            }

            @keyframes copyFadeOut {
                0% { opacity: 1; transform: translateY(0); }
                100% { opacity: 0; transform: translateY(-8px); }
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


# -------------------------------------------------
# Helpers
# -------------------------------------------------
def result_tile(label, value, tooltip=None, compact=False):
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


def render_page_header(title, subtitle):
    st.markdown(f'<div class="page-title">{title}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="page-subtitle">{subtitle}</div>', unsafe_allow_html=True)


def render_custom_label(text):
    st.markdown(f'<div class="field-label">{text}</div>', unsafe_allow_html=True)


def render_label_with_tooltip(text, tooltip):
    st.markdown(
        f'<div class="field-label">{text} <span class="tooltip-icon" title="{tooltip}">i</span></div>',
        unsafe_allow_html=True,
    )


def render_risk_tolerance_helper():
    st.markdown(
        '<div class="tool-note">Low: 1-4, Medium: 5-7, High: 8-10</div>',
        unsafe_allow_html=True,
    )


def style_modern_axes(ax):
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


def render_splash_overlay():
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


def render_stat(value, label):
    st.markdown(
        f"""
        <div class="stat">
            <div class="stat-value">{value}</div>
            <div class="stat-label">{label}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_card(title, body):
    st.markdown(
        f"""
        <div class="card">
            <h3>{title}</h3>
            <p>{body}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_company_lookup_panel():
    profiles = ESG_COMPANY_PROFILES
    labels = [p["display_name"] for p in profiles]

    st.markdown('<div class="lookup-shell">', unsafe_allow_html=True)
    render_custom_label("Search Public Company ESG Profile")
    st.markdown(
        f'<div class="lookup-subtitle">Search across {len(labels)} built-in public companies. Results narrow automatically as you type.</div>',
        unsafe_allow_html=True,
    )

    selected_company = st.selectbox(
        "Search Public Company ESG Profile",
        options=labels,
        index=None,
        placeholder="Type a company name or ticker...",
        label_visibility="collapsed",
        key="selected_company_lookup",
    )

    if selected_company:
        company = None
        for profile in profiles:
            if profile["display_name"] == selected_company:
                company = profile
                break

        if company is not None:
            st.markdown(
                f"""
                <div class="profile-card">
                    <div class="profile-title">{company["display_name"]}</div>
                    <p class="profile-copy">
                        Industry: {company["industry"]}<br>
                        Exchange: {company["exchange"]}<br>
                        Overall ESG Grade: <strong>{company["grade"]}</strong>
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )

            c1, c2, c3 = st.columns(3, gap="small")
            with c1:
                st.markdown(result_tile("Environmental", company["environment"], compact=True), unsafe_allow_html=True)
            with c2:
                st.markdown(result_tile("Social", company["social"], compact=True), unsafe_allow_html=True)
            with c3:
                st.markdown(result_tile("Governance", company["governance"], compact=True), unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


# -------------------------------------------------
# Core calculations
# -------------------------------------------------
def compute_recommendation(priority_label, risk_tolerance, esg_aspect):
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
        "risk_tolerance": risk_tolerance,
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
    asset1,
    asset2,
    exp_return1,
    exp_return2,
    std_dev1,
    std_dev2,
    esg_score1,
    esg_score2,
    correlation,
    risk_free_rate,
    risk_tolerance,
    esg_slider,
):
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
# Screens
# -------------------------------------------------
def render_home():
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

    b1, b2 = st.columns(2, gap="large")
    with b1:
        st.button(
            "Give Me a Portfolio Recommendation",
            use_container_width=True,
            on_click=open_recommendation,
        )
    with b2:
        st.button(
            "Build Your Portfolio Based on ESG Preferences",
            use_container_width=True,
            on_click=open_builder,
        )


def render_recommendation_screen():
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


def render_recommendation_result_screen():
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

        a, b = st.columns(2, gap="small")
        with a:
            st.markdown(result_tile("Risk Level", result["risk_level"], compact=True), unsafe_allow_html=True)
        with b:
            st.markdown(result_tile("Preferred ESG Aspect", result["esg_aspect"], compact=True), unsafe_allow_html=True)

        st.markdown("<div style='height:0.45rem;'></div>", unsafe_allow_html=True)

        c, d = st.columns(2, gap="small")
        with c:
            st.markdown(result_tile("Expected Returns", f'{result["portfolio_return"]:.2f}%', compact=True), unsafe_allow_html=True)
        with d:
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
            <div class="asset-summary">
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
            <div class="asset-summary">
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


def render_builder_screen():
    st.button("← Back", on_click=open_home, use_container_width=False)
    render_page_header(
        "Portfolio Builder",
        "Enter your asset assumptions, use the standard 4.84% risk-free rate by default unless you change it, and search for a company ESG profile.",
    )

    st.markdown('<div class="tool-section-label">Step 1</div>', unsafe_allow_html=True)
    st.markdown('<div class="tool-section-title">Choose Your Setup</div>', unsafe_allow_html=True)

    setup_left, setup_right = st.columns([0.95, 1.05], gap="large")

    with setup_left:
        render_custom_label("Asset Selection Method")
        asset_choice = st.radio(
            "Asset Selection Method",
            ["Input my own assets", "Use recommended public companies"],
            horizontal=True,
            label_visibility="collapsed",
        )
        st.session_state["builder_asset_choice"] = asset_choice

    with setup_right:
        render_company_lookup_panel()

    st.markdown('<div class="tool-divider"></div>', unsafe_allow_html=True)

    with st.form("portfolio_builder_form", clear_on_submit=False):
        asset_choice = st.session_state["builder_asset_choice"]

        if asset_choice == "Input my own assets":
            st.markdown('<div class="tool-section-label">Step 2</div>', unsafe_allow_html=True)
            st.markdown('<div class="tool-section-title">Enter Asset Assumptions</div>', unsafe_allow_html=True)

            col1, col2 = st.columns(2, gap="large")

            with col1:
                asset1 = st.text_input("Asset 1 name", value="Asset 1")
                exp_return1 = st.number_input(f"{asset1} expected return (%)", 0.0, 100.0, 8.0, 0.1)
                std_dev1 = st.number_input(f"{asset1} standard deviation (%)", 0.0, 100.0, 15.0, 0.1)
                esg_score1 = st.number_input(f"{asset1} ESG score (0–100)", 0.0, 100.0, 70.0, 1.0)

            with col2:
                asset2 = st.text_input("Asset 2 name", value="Asset 2")
                exp_return2 = st.number_input(f"{asset2} expected return (%)", 0.0, 100.0, 12.0, 0.1)
                std_dev2 = st.number_input(f"{asset2} standard deviation (%)", 0.0, 100.0, 20.0, 0.1)
                esg_score2 = st.number_input(f"{asset2} ESG score (0–100)", 0.0, 100.0, 55.0, 1.0)

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

                use_default_rf = st.checkbox("Use standard Risk-Free Rate of 4.84%", value=True)

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
                    disabled=use_default_rf,
                    label_visibility="collapsed",
                )

                if use_default_rf:
                    risk_free_rate = 4.84

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

            submitted = st.form_submit_button("Continue", use_container_width=True)

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
            asset1,
            asset2,
            exp_return1,
            exp_return2,
            std_dev1,
            std_dev2,
            esg_score1,
            esg_score2,
            correlation,
            risk_free_rate,
            risk_tolerance,
            esg_slider,
        )
        open_builder_result()
        st.rerun()


def render_builder_result_screen():
    result = st.session_state.get("builder_result")

    if not result:
        open_builder()
        st.rerun()

    weights = np.array(result["weights"])
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

    st.pyplot(fig)
    plt.close(fig)


# -------------------------------------------------
# Router
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
