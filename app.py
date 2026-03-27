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
TARGET_PAGE = "pages/1_Build_Your_Portfolio.py"  # Change if your file name differs


# -------------------------------------------------
# State
# -------------------------------------------------
def init_session_state() -> None:
    defaults = {
        "splash_complete": False,
        "splash_cycle_started": False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def go_to_builder() -> None:
    try:
        st.switch_page(TARGET_PAGE)
    except Exception:
        st.warning(
            f"Create a page at '{TARGET_PAGE}' so this button can open your portfolio builder."
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

            .splash-shell {
                min-height: 88vh;
                display: flex;
                align-items: center;
                justify-content: center;
            }

            .splash-card {
                width: min(720px, 100%);
                text-align: center;
                background: linear-gradient(135deg, rgba(255,255,255,0.93), rgba(255,255,255,0.80));
                border: 1px solid rgba(255,255,255,0.72);
                border-radius: 32px;
                padding: 3rem 2rem 2.3rem 2rem;
                box-shadow: var(--shadow);
                backdrop-filter: blur(10px);
                animation: fadeUp 0.55s ease;
            }

            .splash-logo {
                width: 96px;
                height: 96px;
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
            }

            .splash-title {
                color: var(--text);
                font-size: 2.6rem;
                font-weight: 900;
                letter-spacing: -0.05em;
                margin: 0;
            }

            .splash-copy {
                color: var(--muted);
                font-size: 1.02rem;
                line-height: 1.65;
                margin: 0.6rem auto 0 auto;
                max-width: 520px;
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
            }

            @keyframes fadeUp {
                from {
                    opacity: 0;
                    transform: translateY(12px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


# -------------------------------------------------
# Reusable HTML blocks
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


# -------------------------------------------------
# Splash screen
# -------------------------------------------------
def splash_markup() -> None:
    st.markdown(
        f"""
        <div class="splash-shell">
            <div class="splash-card">
                <div class="splash-logo">VW</div>
                <div class="splash-title">{APP_NAME}</div>
                <div class="splash-copy">
                    {APP_TAGLINE}<br>
                    A streamlined sustainable finance experience for building portfolios
                    around both financial risk and ESG priorities.
                </div>
                <div class="splash-tag">Professional • Personalised • ESG-aware</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


if hasattr(st, "fragment"):
    @st.fragment(run_every=2)
    def auto_splash_fragment() -> None:
        if not st.session_state["splash_cycle_started"]:
            st.session_state["splash_cycle_started"] = True
            splash_markup()
        else:
            st.session_state["splash_complete"] = True
            st.rerun()
else:
    def auto_splash_fragment() -> None:
        # Fallback for older Streamlit versions:
        # skip the timed splash rather than breaking the app
        st.session_state["splash_complete"] = True
        st.rerun()


def render_splash() -> None:
    auto_splash_fragment()
    st.stop()


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
                    smarter portfolio experience. It combines personalised risk profiling with
                    sustainability preferences to support better-informed portfolio construction.
                </p>
                <div class="pill-row">
                    <span class="pill">Risk-aware design</span>
                    <span class="pill">ESG-integrated approach</span>
                    <span class="pill">Portfolio optimisation</span>
                    <span class="pill">Professional user journey</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        render_stat("Trust", "Transparent investment approach")
        st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
        render_stat("Clarity", "Guided and intuitive experience")
        st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
        render_stat("Optimisation", "Built for tailored portfolio outcomes")

    st.markdown("<div style='height:1.2rem;'></div>", unsafe_allow_html=True)

    st.markdown('<div class="section-label">Why this app</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-title">An investment app designed for trust, clarity, and optimisation</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="section-copy">
            This app is designed to help users make confident investment decisions through a process
            that feels both transparent and personalised. Trust comes from a clear sustainability-led
            framework, clarity comes from a focused and intuitive journey, and optimisation comes from
            transforming user preferences into a portfolio that better aligns with their financial and ESG objectives.
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3, gap="large")
    with c1:
        render_card(
            "Trust through transparency",
            "The app makes it easier for users to understand how risk and sustainability preferences shape portfolio decisions."
        )
    with c2:
        render_card(
            "Clarity through guided design",
            "A structured flow keeps the experience simple and readable, reducing friction while improving decision quality."
        )
    with c3:
        render_card(
            "Optimisation through personalisation",
            "The portfolio-building process is designed to convert user-specific inputs into more relevant and targeted outcomes."
        )

    st.markdown("<div style='height:1.4rem;'></div>", unsafe_allow_html=True)

    cta_left, cta_right = st.columns([1.15, 0.85], gap="large")

    with cta_left:
        st.markdown(
            """
            <div class="cta-panel">
                <div class="section-label">Build your portfolio</div>
                <h2 class="cta-title">Start the guided portfolio creation journey</h2>
                <p class="cta-copy">
                    Continue to the next screen to enter investment goals, risk appetite,
                    and ESG preferences in a dedicated workflow built for portfolio optimisation.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with cta_right:
        st.write("")
        st.write("")
        if st.button("Build Your Portfolio", type="primary", use_container_width=True):
            go_to_builder()

        try:
            st.page_link(
                TARGET_PAGE,
                label="Open portfolio builder",
                icon="→",
                use_container_width=True,
            )
        except Exception:
            pass


# -------------------------------------------------
# Run app
# -------------------------------------------------
init_session_state()
inject_css()

if not st.session_state["splash_complete"]:
    render_splash()

render_home()
if not st.session_state.entered_home:
    render_splash()

render_home()
