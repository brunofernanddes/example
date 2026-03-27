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
# Session state
# -------------------------------------------------
def init_session_state() -> None:
    defaults = {
        "show_splash": True,
        "current_view": "home",   # home | recommendation | builder
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
# Styling
# -------------------------------------------------
def inject_css() -> None:
    st.markdown(
        """
        <style>
            :root {
                --bg1: #f7fbfa;
                --bg2: #eef6f4;
                --card: rgba(255,255,255,0.92);
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
                background: linear-gradient(135deg, rgba(255,255,255,0.95), rgba(255,255,255,0.86));
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

            .builder-shell {
                background: rgba(255,255,255,0.96);
                border: 1px solid rgba(15,23,42,0.06);
                border-radius: 24px;
                padding: 1.45rem;
                box-shadow: var(--shadow-soft);
            }

            .builder-heading {
                color: #000000;
                font-size: 2rem;
                font-weight: 850;
                letter-spacing: -0.03em;
                margin-bottom: 0.2rem;
            }

            .builder-subheading {
                color: #000000;
                font-size: 1rem;
                margin-bottom: 1.2rem;
            }

            .builder-section-title {
                color: #000000;
                font-size: 1.08rem;
                font-weight: 800;
                margin-top: 0.5rem;
                margin-bottom: 0.75rem;
            }

            /* Make builder text clearly visible */
            .builder-shell p,
            .builder-shell h1,
            .builder-shell h2,
            .builder-shell h3,
            .builder-shell h4,
            .builder-shell h5,
            .builder-shell h6,
            .builder-shell label,
            .builder-shell span,
            .builder-shell div {
                color: #000000;
            }

            .builder-shell [data-testid="stWidgetLabel"] p,
            .builder-shell [data-testid="stMarkdownContainer"] p,
            .builder-shell .stCaption,
            .builder-shell .stRadio p,
            .builder-shell .stSlider p {
                color: #000000 !important;
            }

            .builder-shell input,
            .builder-shell textarea {
                color: #000000 !important;
            }

            .builder-shell .stNumberInput input,
            .builder-shell .stTextInput input {
                color: #000000 !important;
            }

            .minimal-divider {
                height: 1px;
                background: rgba(15,23,42,0.06);
                margin: 1rem 0 1.2rem 0;
                border-radius: 999px;
            }

            .metric-card {
                background: #ffffff;
                border: 1px solid rgba(15,23,42,0.06);
                border-radius: 16px;
                padding: 0.95rem 1rem;
            }

            .metric-card-title {
                color: #64748b;
                font-size: 0.85rem;
                margin-bottom: 0.3rem;
            }

            .metric-card-value {
                color: #000000;
                font-weight: 800;
                font-size: 1.2rem;
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


# -------------------------------------------------
# Shared UI blocks
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
# Recommendation placeholder
# -------------------------------------------------
def render_recommendation_screen() -> None:
    col_back, col_title = st.columns([0.16, 0.84])
    with col_back:
        st.button("← Back", on_click=open_home, use_container_width=True)

    st.markdown('<div class="builder-shell">', unsafe_allow_html=True)
    st.markdown('<div class="builder-heading">Portfolio Recommendation</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="builder-subheading">This area is ready for your recommended-public-companies workflow.</div>',
        unsafe_allow_html=True,
    )
    st.info("You can connect your recommendation engine here.")
    st.markdown('</div>', unsafe_allow_html=True)


# -------------------------------------------------
# Builder screen
# -------------------------------------------------
def render_builder_screen() -> None:
    col_back, col_title = st.columns([0.16, 0.84])
    with col_back:
        st.button("← Back", on_click=open_home, use_container_width=True)

    st.markdown('<div class="builder-shell">', unsafe_allow_html=True)

    st.markdown(
        '<div class="builder-heading">Build Your Portfolio Based on Your ESG Preferences</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="builder-subheading">Enter your inputs below to generate a clean ESG-aware portfolio recommendation.</div>',
        unsafe_allow_html=True,
    )

    with st.form("portfolio_builder_form", clear_on_submit=False):
        st.markdown('<div class="builder-section-title">Portfolio setup</div>', unsafe_allow_html=True)

        asset_choice = st.radio(
            "Asset selection method",
            ["Input my own assets", "Use recommended public companies"],
            horizontal=True,
        )

        investment_priority = st.radio(
            "Investment priority",
            [
                "Balanced return and sustainability",
                "Prioritise financial growth",
                "Prioritise sustainability",
            ],
            horizontal=True,
        )

        st.markdown('<div class="minimal-divider"></div>', unsafe_allow_html=True)

        if asset_choice == "Input my own assets":
            st.markdown('<div class="builder-section-title">Asset details</div>', unsafe_allow_html=True)

            col1, col2 = st.columns(2)

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

            st.markdown('<div class="minimal-divider"></div>', unsafe_allow_html=True)
            st.markdown('<div class="builder-section-title">Risk and ESG preferences</div>', unsafe_allow_html=True)

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

            run_optimiser = st.form_submit_button(
                "Generate portfolio recommendation",
                type="primary",
                use_container_width=True,
            )

        else:
            st.info("Recommended public companies mode can be connected to your curated ESG universe next.")
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
            gamma = 11 - risk_tolerance
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

            max_sharpe_idx = np.argmax(portfolio_sharpes)
            optimal_idx = np.argmax(portfolio_utility)

            st.markdown('<div class="minimal-divider"></div>', unsafe_allow_html=True)
            st.markdown('<div class="builder-section-title">Portfolio recommendation</div>', unsafe_allow_html=True)

            opt_w1 = weights[optimal_idx]
            opt_w2 = 1 - opt_w1

            m1, m2, m3 = st.columns(3)
            with m1:
                st.markdown(
                    f"""
                    <div class="metric-card">
                        <div class="metric-card-title">{asset1} weight</div>
                        <div class="metric-card-value">{opt_w1:.2%}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with m2:
                st.markdown(
                    f"""
                    <div class="metric-card">
                        <div class="metric-card-title">{asset2} weight</div>
                        <div class="metric-card-value">{opt_w2:.2%}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with m3:
                st.markdown(
                    f"""
                    <div class="metric-card">
                        <div class="metric-card-title">Sharpe ratio</div>
                        <div class="metric-card-value">{portfolio_sharpes[optimal_idx]:.2f}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

            m4, m5, m6 = st.columns(3)
            with m4:
                st.markdown(
                    f"""
                    <div class="metric-card">
                        <div class="metric-card-title">Expected return</div>
                        <div class="metric-card-value">{portfolio_returns[optimal_idx]:.2%}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with m5:
                st.markdown(
                    f"""
                    <div class="metric-card">
                        <div class="metric-card-title">Portfolio risk</div>
                        <div class="metric-card-value">{portfolio_risks[optimal_idx]:.2%}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with m6:
                st.markdown(
                    f"""
                    <div class="metric-card">
                        <div class="metric-card-title">Portfolio ESG score</div>
                        <div class="metric-card-value">{portfolio_esg[optimal_idx] * 100:.2f}/100</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            st.markdown('<div class="minimal-divider"></div>', unsafe_allow_html=True)
            st.markdown('<div class="builder-section-title">Efficient frontier</div>', unsafe_allow_html=True)

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

            st.markdown('<div class="builder-section-title">Sensitivity to ESG preference</div>', unsafe_allow_html=True)

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
# Router
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
