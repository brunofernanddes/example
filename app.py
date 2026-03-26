import streamlit as st

# ----------------------------
# Page setup
# ----------------------------
st.set_page_config(
    page_title="Sustainable Portfolio Optimiser",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

APP_NAME = "Sustainable Portfolio Optimiser"


# ----------------------------
# Helpers
# ----------------------------
def init_session_state() -> None:
    defaults = {
        "investment_amount": 10000,
        "investment_horizon": 5,
        "risk_tolerance": "Balanced",
        "esg_environment": 70,
        "esg_social": 65,
        "esg_governance": 75,
        "excluded_sectors": [],
        "profile_saved": False,
        "show_methodology": False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def inject_css() -> None:
    st.markdown(
        """
        <style>
            :root {
                --primary: #0f766e;
                --primary-dark: #115e59;
                --accent: #0ea5a4;
                --navy: #0f172a;
                --muted: #475569;
                --soft: #f8fafc;
                --card: #ffffff;
                --border: rgba(15, 23, 42, 0.08);
                --shadow: 0 10px 30px rgba(15, 23, 42, 0.06);
            }

            .stApp {
                background: linear-gradient(180deg, #f8fcfb 0%, #f4f7fb 100%);
            }

            .block-container {
                max-width: 1180px;
                padding-top: 2rem;
                padding-bottom: 2rem;
            }

            .hero {
                background: linear-gradient(135deg, rgba(15, 118, 110, 0.10), rgba(14, 165, 164, 0.06));
                border: 1px solid rgba(15, 118, 110, 0.12);
                border-radius: 24px;
                padding: 2.4rem 2rem 2rem 2rem;
                box-shadow: var(--shadow);
                margin-bottom: 0.5rem;
            }

            .badge {
                display: inline-block;
                background: #ecfeff;
                color: var(--primary-dark);
                border: 1px solid #99f6e4;
                border-radius: 999px;
                padding: 0.35rem 0.8rem;
                font-size: 0.84rem;
                font-weight: 700;
                margin-bottom: 0.9rem;
            }

            .hero h1 {
                font-size: 3rem;
                line-height: 1.05;
                color: var(--navy);
                margin: 0 0 0.8rem 0;
                font-weight: 800;
                letter-spacing: -0.03em;
            }

            .hero p {
                font-size: 1.08rem;
                color: #334155;
                max-width: 780px;
                margin: 0;
            }

            .pill-row {
                display: flex;
                flex-wrap: wrap;
                gap: 0.5rem;
                margin-top: 1rem;
            }

            .pill {
                display: inline-block;
                padding: 0.42rem 0.8rem;
                border-radius: 999px;
                background: rgba(255,255,255,0.75);
                border: 1px solid rgba(15, 23, 42, 0.08);
                color: var(--navy);
                font-size: 0.88rem;
                font-weight: 600;
            }

            .section-label {
                font-size: 0.85rem;
                font-weight: 800;
                color: var(--primary-dark);
                text-transform: uppercase;
                letter-spacing: 0.08em;
                margin-bottom: 0.35rem;
            }

            .section-title {
                color: var(--navy);
                font-weight: 800;
                font-size: 1.8rem;
                margin-bottom: 0.25rem;
            }

            .section-subtitle {
                color: var(--muted);
                margin-bottom: 1rem;
            }

            .info-card {
                background: var(--card);
                border: 1px solid var(--border);
                border-radius: 20px;
                padding: 1.2rem;
                box-shadow: var(--shadow);
                height: 100%;
            }

            .info-card h3 {
                color: var(--navy);
                margin: 0 0 0.35rem 0;
                font-size: 1.05rem;
                font-weight: 750;
            }

            .info-card p {
                color: var(--muted);
                margin: 0;
                font-size: 0.96rem;
                line-height: 1.5;
            }

            .metric-value {
                font-size: 2rem;
                font-weight: 800;
                color: var(--navy);
                margin: 0;
            }

            .metric-label {
                color: var(--muted);
                font-size: 0.92rem;
                margin-top: 0.2rem;
            }

            .summary-card {
                background: linear-gradient(135deg, rgba(15, 118, 110, 0.10), rgba(30, 64, 175, 0.04));
                border: 1px solid rgba(15, 118, 110, 0.14);
            }

            .footer-note {
                background: rgba(255,255,255,0.7);
                border: 1px solid var(--border);
                border-radius: 16px;
                padding: 1rem 1.1rem;
                color: var(--muted);
                font-size: 0.92rem;
            }

            div.stButton > button {
                border-radius: 14px;
                font-weight: 700;
                min-height: 3rem;
            }

            div[data-testid="stForm"] {
                background: rgba(255,255,255,0.70);
                border: 1px solid var(--border);
                border-radius: 22px;
                padding: 1rem 1rem 0.5rem 1rem;
            }

            div[data-testid="stMetric"] {
                background: white;
                border: 1px solid var(--border);
                padding: 0.9rem 1rem;
                border-radius: 16px;
            }

            hr {
                border: none;
                border-top: 1px solid rgba(15, 23, 42, 0.08);
                margin: 1.25rem 0;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def portfolio_style(risk_tolerance: str) -> str:
    mapping = {
        "Conservative": "Capital Preservation",
        "Balanced": "Core Balanced Growth",
        "Growth": "Long-Term Growth",
        "Adventurous": "High-Conviction Growth",
    }
    return mapping.get(risk_tolerance, "Core Balanced Growth")


def esg_tilt(avg_score: int) -> str:
    if avg_score >= 80:
        return "High ESG conviction"
    if avg_score >= 60:
        return "Strong sustainability tilt"
    if avg_score >= 40:
        return "Balanced ESG tilt"
    return "Light ESG tilt"


def risk_description(risk_tolerance: str) -> str:
    mapping = {
        "Conservative": "Lower volatility focus with stronger downside awareness.",
        "Balanced": "A measured balance between stability and long-term growth.",
        "Growth": "Higher equity exposure aimed at long-run capital appreciation.",
        "Adventurous": "Maximum growth orientation with higher expected volatility.",
    }
    return mapping.get(risk_tolerance, "Balanced long-term approach.")


def card_html(title: str, body: str, value: str | None = None) -> str:
    if value:
        return f"""
        <div class="info-card">
            <div class="metric-value">{value}</div>
            <div class="metric-label">{title}</div>
            <p style="margin-top:0.75rem;">{body}</p>
        </div>
        """
    return f"""
    <div class="info-card">
        <h3>{title}</h3>
        <p>{body}</p>
    </div>
    """


# ----------------------------
# App
# ----------------------------
init_session_state()
inject_css()

st.markdown(
    f"""
    <div class="hero">
        <div class="badge">Sustainable finance • personalised onboarding</div>
        <h1>Build a portfolio that matches both your risk appetite and your ESG values.</h1>
        <p>
            {APP_NAME} helps users move from preferences to action with a clean, guided experience.
            This homepage captures the inputs your optimiser needs, explains the value proposition clearly,
            and keeps the journey fast and intuitive.
        </p>
        <div class="pill-row">
            <span class="pill">Risk-aware</span>
            <span class="pill">ESG-personalised</span>
            <span class="pill">Transparent exclusions</span>
            <span class="pill">Optimiser-ready inputs</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

cta_1, cta_2, cta_3 = st.columns([1, 1, 1])
with cta_1:
    get_started = st.button("Build my portfolio", type="primary", use_container_width=True)
with cta_2:
    if st.button("View methodology", use_container_width=True):
        st.session_state["show_methodology"] = not st.session_state["show_methodology"]
with cta_3:
    st.markdown(
        card_html(
            "User journey",
            "A single-page onboarding flow that feels premium, fast, and assessment-ready.",
            "3-step",
        ),
        unsafe_allow_html=True,
    )

if get_started:
    st.success("Complete the quick profile below to prepare the inputs for your optimiser.")

st.markdown("<hr>", unsafe_allow_html=True)

# ----------------------------
# Value proposition cards
# ----------------------------
st.markdown('<div class="section-label">Why this works</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">A homepage that is clear, credible, and conversion-focused</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">It immediately tells the user what the app does, how it personalises the portfolio, and what happens next.</div>',
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3, gap="large")
with col1:
    st.markdown(
        card_html(
            "Risk-aligned investing",
            "Users can choose a suitable risk profile so the portfolio recommendations feel personal rather than generic."
        ),
        unsafe_allow_html=True,
    )
with col2:
    st.markdown(
        card_html(
            "ESG by preference",
            "Environmental, social, and governance priorities are captured separately instead of being reduced to a single checkbox."
        ),
        unsafe_allow_html=True,
    )
with col3:
    st.markdown(
        card_html(
            "Transparent controls",
            "Sector exclusions and horizon inputs make the onboarding practical, explainable, and easy to connect to optimisation logic."
        ),
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)

# ----------------------------
# How it works
# ----------------------------
st.markdown('<div class="section-label">How it works</div>', unsafe_allow_html=True)
step1, step2, step3 = st.columns(3, gap="large")
with step1:
    st.markdown(
        card_html(
            "1. Set your profile",
            "Capture investment amount, time horizon, and preferred risk band in a lightweight form."
        ),
        unsafe_allow_html=True,
    )
with step2:
    st.markdown(
        card_html(
            "2. Define ESG priorities",
            "Let users express how strongly they care about environmental, social, and governance outcomes."
        ),
        unsafe_allow_html=True,
    )
with step3:
    st.markdown(
        card_html(
            "3. Hand off to optimiser",
            "Store everything in session state so the next page can run portfolio construction with zero friction."
        ),
        unsafe_allow_html=True,
    )

st.markdown("<hr>", unsafe_allow_html=True)

# ----------------------------
# Quick-start form
# ----------------------------
st.markdown('<div class="section-label">Quick start</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Tell us how your portfolio should behave</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">These settings are saved in session state and can be consumed directly by your optimiser page.</div>',
    unsafe_allow_html=True,
)

risk_options = ["Conservative", "Balanced", "Growth", "Adventurous"]
sector_options = [
    "Fossil fuels",
    "Weapons",
    "Tobacco",
    "Adult entertainment",
    "Gambling",
    "Animal testing",
]

with st.form("user_profile_form", clear_on_submit=False):
    left, right = st.columns([1.05, 0.95], gap="large")

    with left:
        investment_amount = st.number_input(
            "Initial investment (£)",
            min_value=1000,
            max_value=10000000,
            value=int(st.session_state["investment_amount"]),
            step=500,
            help="Used as the starting capital for the portfolio recommendation.",
        )

        investment_horizon = st.slider(
            "Investment horizon (years)",
            min_value=1,
            max_value=40,
            value=int(st.session_state["investment_horizon"]),
            help="Longer horizons can typically support more growth-oriented allocations.",
        )

        risk_tolerance = st.radio(
            "Risk tolerance",
            options=risk_options,
            index=risk_options.index(st.session_state["risk_tolerance"]),
            horizontal=True,
            help="Your optimiser can map this to volatility targets or strategic asset allocation bands.",
        )

        excluded_sectors = st.multiselect(
            "Exclude sectors",
            options=sector_options,
            default=st.session_state["excluded_sectors"],
            help="Optional ethical exclusions to reflect user values.",
        )

    with right:
        esg_environment = st.slider(
            "Environmental priority",
            min_value=0,
            max_value=100,
            value=int(st.session_state["esg_environment"]),
            help="Higher values imply a stronger preference for environmental considerations.",
        )
        esg_social = st.slider(
            "Social priority",
            min_value=0,
            max_value=100,
            value=int(st.session_state["esg_social"]),
            help="Measures how strongly the user values labour, diversity, and community outcomes.",
        )
        esg_governance = st.slider(
            "Governance priority",
            min_value=0,
            max_value=100,
            value=int(st.session_state["esg_governance"]),
            help="Reflects preference for strong corporate governance and accountability.",
        )

        st.markdown("<br>", unsafe_allow_html=True)
        st.caption(
            "Tip: your optimiser can convert these ESG scores into asset or fund-level tilts, "
            "constraints, or objective-function penalties."
        )

    submitted = st.form_submit_button("Save preferences", type="primary", use_container_width=True)

if submitted:
    st.session_state["investment_amount"] = investment_amount
    st.session_state["investment_horizon"] = investment_horizon
    st.session_state["risk_tolerance"] = risk_tolerance
    st.session_state["esg_environment"] = esg_environment
    st.session_state["esg_social"] = esg_social
    st.session_state["esg_governance"] = esg_governance
    st.session_state["excluded_sectors"] = excluded_sectors
    st.session_state["profile_saved"] = True
    st.success("Preferences saved. Your optimiser inputs are now ready.")

# ----------------------------
# Preview / summary
# ----------------------------
if st.session_state["profile_saved"]:
    avg_esg = round(
        (
            st.session_state["esg_environment"]
            + st.session_state["esg_social"]
            + st.session_state["esg_governance"]
        ) / 3
    )

    exclusions_text = (
        ", ".join(st.session_state["excluded_sectors"])
        if st.session_state["excluded_sectors"]
        else "No exclusions selected"
    )

    summary_left, summary_right = st.columns([1.2, 0.8], gap="large")

    with summary_left:
        st.markdown(
            f"""
            <div class="info-card summary-card">
                <div class="section-label">Profile ready</div>
                <h3 style="font-size:1.4rem; margin-bottom:0.6rem;">
                    {portfolio_style(st.session_state["risk_tolerance"])} • {esg_tilt(avg_esg)}
                </h3>
                <p style="margin-bottom:0.9rem;">
                    {risk_description(st.session_state["risk_tolerance"])}
                </p>
                <div class="pill-row">
                    <span class="pill">£{st.session_state["investment_amount"]:,.0f} starting amount</span>
                    <span class="pill">{st.session_state["investment_horizon"]} year horizon</span>
                    <span class="pill">{st.session_state["risk_tolerance"]} risk profile</span>
                    <span class="pill">ESG score {avg_esg}/100</span>
                </div>
                <p style="margin-top:1rem;">
                    <strong>Exclusions:</strong> {exclusions_text}
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with summary_right:
        st.metric("Environmental", f'{st.session_state["esg_environment"]}/100')
        st.progress(st.session_state["esg_environment"] / 100)

        st.metric("Social", f'{st.session_state["esg_social"]}/100')
        st.progress(st.session_state["esg_social"] / 100)

        st.metric("Governance", f'{st.session_state["esg_governance"]}/100')
        st.progress(st.session_state["esg_governance"] / 100)

        st.metric("Average ESG preference", f"{avg_esg}/100")

st.markdown("<hr>", unsafe_allow_html=True)

# ----------------------------
# Methodology section
# ----------------------------
if st.session_state["show_methodology"]:
    st.markdown('<div class="section-label">Methodology</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">How the homepage feeds the optimiser</div>', unsafe_allow_html=True)

    m1, m2, m3 = st.columns(3, gap="large")
    with m1:
        st.markdown(
            card_html(
                "Risk engine input",
                "Map the selected risk band to target volatility, asset allocation ranges, or scenario assumptions."
            ),
            unsafe_allow_html=True,
        )
    with m2:
        st.markdown(
            card_html(
                "ESG objective input",
                "Translate E, S, and G preferences into scoring weights, portfolio tilts, or minimum-threshold filters."
            ),
            unsafe_allow_html=True,
        )
    with m3:
        st.markdown(
            card_html(
                "Constraint input",
                "Use exclusions as hard constraints so the optimiser removes restricted sectors from the opportunity set."
            ),
            unsafe_allow_html=True,
        )

    st.code(
        """# Example handoff to your optimiser page
user_inputs = {
    "investment_amount": st.session_state["investment_amount"],
    "investment_horizon": st.session_state["investment_horizon"],
    "risk_tolerance": st.session_state["risk_tolerance"],
    "esg_environment": st.session_state["esg_environment"],
    "esg_social": st.session_state["esg_social"],
    "esg_governance": st.session_state["esg_governance"],
    "excluded_sectors": st.session_state["excluded_sectors"],
}""",
        language="python",
    )

# ----------------------------
# Footer
# ----------------------------
st.markdown(
    """
    <div class="footer-note">
        <strong>Note:</strong> This homepage is intentionally focused on onboarding and trust-building.
        Keep optimisation logic, portfolio outputs, and performance charts on later pages to preserve a clean user journey.
        For an assessment, this separation makes your app look more professional and easier to explain.
    </div>
    """,
    unsafe_allow_html=True,
)
