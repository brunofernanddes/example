
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# Page config
# -------------------------------------------------
st.set_page_config(
    page_title="Leaf It To Us",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

APP_NAME = "Leaf It To Us"
APP_TAGLINE = "Sustainable investing, built around you."

st.markdown("<div style='margin-top: 80px;'></div>", unsafe_allow_html=True)

LEAF_LOGO_SVG = """
<svg viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img">
    <defs>
        <linearGradient id="leaf-grad" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stop-color="#ffffff" stop-opacity="1"/>
            <stop offset="100%" stop-color="#dcfce7" stop-opacity="1"/>
        </linearGradient>
    </defs>
    <path d="M51.5 11.2C36.3 11.4 24.7 17 18.1 26.2c-7.3 10.2-8.2 23.7 2 29.2 9.9 5.2 23.2.4 31-10.7 7.8-11.2 9.2-25-.4-33.5-.8.1-1.5 0-1.2 0Z" fill="url(#leaf-grad)"/>
    <path d="M20.8 44.4c8.3-9.6 18.4-17.3 30.2-23.2" stroke="#14532d" stroke-width="3.2" stroke-linecap="round" opacity="0.24"/>
    <path d="M21.7 44.2c7.3-3.2 13.5-7.8 18.7-13.7" stroke="#14532d" stroke-width="2.3" stroke-linecap="round" opacity="0.16"/>
</svg>
"""

# -------------------------------------------------
# Embedded company ESG data
# Source: uploaded public companies ESG file
# -------------------------------------------------
COMPANY_DATA = [
    ('mmm', '3M Co', 'Industrial Conglomerates', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 526, 310, 305, 1141),
    ('aos', 'A O Smith Corp', 'Building', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 510, 315, 310, 1135),
    ('aadi', 'Aadi Bioscience Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 200, 201, 203, 604),
    ('aaon', 'Aaon Inc', 'Building', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 500, 300, 223, 1023),
    ('abt', 'Abbott Laboratories', 'Health Care', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 515, 305, 305, 1125),
    ('abbv', 'Abbvie Inc', 'Biotechnology', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 505, 317, 300, 1122),
    ('abcl', 'Abcellera Biologics Inc', 'Life Sciences Tools and Services', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 540, 354, 345, 1239),
    ('abeo', 'Abeona Therapeutics Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 205, 306, 310, 821),
    ('abmd', 'ABIOMED Inc', 'Health Care', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 324, 305, 1129),
    ('absi', 'Absci Corp', 'Life Sciences Tools and Services', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 205, 224, 230, 659),
    ('abvc', 'ABVC Biopharma Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 220, 212, 205, 637),
    ('aciu', 'AC Immune SA', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 250, 296, 305, 851),
    ('actg', 'Acacia Research Corp', 'Financial Services', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 200, 200, 275, 675),
    ('achc', 'Acadia Healthcare Company Inc', 'Health Care', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 330, 231, 220, 781),
    ('acad', 'ACADIA Pharmaceuticals Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 230, 230, 305, 765),
    ('acn', 'Accenture PLC', 'Technology', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 515, 360, 305, 1180),
    ('accd', 'Accolade Inc', 'Health Care', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 255, 254, 235, 744),
    ('acev', 'ACE Convergence Acquisition Corp', 'N/A', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 225, 211, 215, 651),
    ('acrx', 'AcelRx Pharmaceuticals Inc', 'Pharmaceuticals', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 200, 237, 300, 737),
    ('acer', 'Acer Therapeutics Inc', 'Pharmaceuticals', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 223, 291, 310, 824),
    ('achv', 'Achieve Life Sciences Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 215, 222, 305, 742),
    ('achl', 'Achilles Therapeutics PLC', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 230, 288, 285, 803),
    ('aciw', 'ACI Worldwide Inc', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 327, 300, 1127),
    ('acrs', 'Aclaris Therapeutics Inc', 'Pharmaceuticals', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 230, 207, 220, 657),
    ('acmr', 'ACM Research Inc', 'Semiconductors', 'NASDAQ NMS - GLOBAL MARKET', 'BBB', 'High', 'B', 'Medium', 'BB', 'Medium', 'BBB', 'High', 410, 232, 325, 967),
    ('acnb', 'ACNB Corp', 'Banking', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 220, 219, 215, 654),
    ('acor', 'Acorda Therapeutics Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 230, 307, 310, 847),
    ('acac', 'Acri Capital Acquisition Corp', 'N/A', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 200, 205, 300, 705),
    ('atvi', 'Activision Blizzard Inc', 'Media', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 280, 347, 330, 957),
    ('abos', 'Acumen Pharmaceuticals Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 205, 201, 200, 606),
    ('acxp', 'Acurx Pharmaceuticals Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 235, 301, 305, 841),
    ('afib', 'Acutus Medical Inc', 'Health Care', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 205, 211, 235, 651),
    ('acva', 'ACV Auctions Inc', 'Commercial Services and Supplies', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 235, 262, 315, 812),
    ('adag', 'Adagene Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 295, 301, 305, 901),
    ('admp', 'Adamis Pharmaceuticals Corp', 'Pharmaceuticals', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 285, 204, 215, 704),
    ('ahco', 'Adapthealth Corp', 'Health Care', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 210, 211, 235, 656),
    ('adap', 'Adaptimmune Therapeutics PLC', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BBB', 'High', 365, 283, 305, 953),
    ('adpt', 'Adaptive Biotechnologies Corp', 'Life Sciences Tools and Services', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 260, 348, 260, 868),
    ('adus', 'Addus Homecare Corp', 'Health Care', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 210, 215, 218, 643),
    ('aey', 'ADDvantage Technologies Group Inc', 'Electrical Equipment', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 235, 234, 300, 769),
    ('adil', 'Adial Pharmaceuticals Inc', 'Pharmaceuticals', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 200, 203, 300, 703),
    ('acet', 'Adicet Bio Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 215, 211, 305, 731),
    ('adtx', 'Aditxt Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 210, 224, 305, 739),
    ('adma', 'ADMA Biologics Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 240, 264, 320, 824),
    ('adbe', 'Adobe Inc', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 200, 221, 200, 621),
    ('adtn', 'ADTRAN Inc', 'Communications', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 510, 308, 300, 1118),
    ('aap', 'Advance Auto Parts Inc', 'Retail', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 264, 261, 210, 735),
    ('ades', 'Advanced Emissions Solutions Inc', 'Chemicals', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 205, 201, 300, 706),
    ('aeis', 'Advanced Energy Industries Inc', 'Electrical Equipment', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 300, 300, 1100),
    ('amd', 'Advanced Micro Devices Inc', 'Semiconductors', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 200, 208, 200, 608),
    ('adv', 'Advantage Solutions Inc', 'Media', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'B', 'Medium', 'BB', 'Medium', 'BBB', 'High', 515, 269, 328, 1112),
    ('adn', 'Advent Technologies Holdings Inc', 'Electrical Equipment', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 250, 203, 220, 673),
    ('advm', 'Adverum Biotechnologies Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 262, 321, 235, 818),
    ('agle', 'Aeglea Bio Therapeutics Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 205, 223, 200, 628),
    ('aehr', 'Aehr Test Systems', 'Semiconductors', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 290, 262, 300, 852),
    ('aeri', 'Aerie Pharmaceuticals Inc', 'Pharmaceuticals', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'B', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 264, 310, 1074),
    ('aes', 'AES Corp', 'Utilities', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 525, 326, 370, 1221),
    ('aih', 'Aesthetic Medical International Holdings Group Ltd', 'Health Care', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 220, 250, 300, 770),
    ('aemd', 'Aethlon Medical Inc', 'Health Care', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 200, 262, 315, 777),
    ('afaq', 'AF Acquisition Corp', 'N/A', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 200, 200, 200, 600),
    ('afcg', 'AFC Gamma Inc', 'Real Estate', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 255, 204, 226, 685),
    ('afmd', 'Affimed NV', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 368, 304, 310, 982),
    ('afbi', 'Affinity Bancshares Inc', 'Banking', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 200, 207, 200, 607),
    ('afrm', 'Affirm Holdings Inc', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 225, 335, 335, 895),
    ('afl', 'Aflac Inc', 'Insurance', 'NEW YORK STOCK EXCHANGE, INC.', 'BBB', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 454, 300, 235, 989),
    ('afya', 'Afya Ltd', 'Diversified Consumer Services', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 290, 203, 205, 698),
    ('agen', 'Agenus Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 290, 245, 300, 835),
    ('agrx', 'Agile Therapeutics Inc', 'Pharmaceuticals', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 240, 203, 260, 703),
    ('a', 'Agilent Technologies Inc', 'Life Sciences Tools and Services', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'B', 'Medium', 'B', 'Medium', 'BBB', 'High', 573, 231, 233, 1037),
    ('agil', 'AgileThought Inc', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BBB', 'High', 340, 299, 305, 944),
    ('agys', 'Agilysys Inc', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 303, 300, 1103),
    ('agio', 'Agios Pharmaceuticals Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 520, 303, 325, 1148),
    ('agmh', 'AGM Group Holdings Inc', 'Financial Services', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 205, 204, 210, 619),
    ('agnc', 'AGNC Investment Corp', 'Real Estate', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BBB', 'High', 382, 242, 305, 929),
    ('agri', 'AgriFORCE Growing Systems Ltd', 'Food Products', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'B', 'Medium', 'BB', 'Medium', 'BBB', 'High', 510, 248, 305, 1063),
    ('agfy', 'Agrify Corp', 'Machinery', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 540, 361, 305, 1206),
    ('agfs', 'AgroFresh Solutions Inc', 'Chemicals', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 500, 301, 275, 1076),
    ('aib', 'AIB Acquisition Corp', 'N/A', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 215, 227, 300, 742),
    ('aiki', 'Aikido Pharma Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 200, 235, 205, 640),
    ('apd', 'Air Products and Chemicals Inc', 'Chemicals', 'NEW YORK STOCK EXCHANGE, INC.', 'AA', 'Excellent', 'BBB', 'High', 'BB', 'Medium', 'A', 'High', 700, 442, 300, 1442),
    ('airt', 'Air T Inc', 'Logistics and Transportation', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 234, 210, 325, 769),
    ('abnb', 'Airbnb Inc', 'Hotels Restaurants and Leisure', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'A', 'High', 'BBB', 'High', 'A', 'High', 505, 570, 400, 1475),
    ('airg', 'Airgain Inc', 'Electrical Equipment', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 300, 330, 1130),
    ('airs', 'Airsculpt Technologies Inc', 'Health Care', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 210, 201, 205, 616),
    ('akam', 'Akamai Technologies Inc', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 515, 341, 305, 1161),
    ('aktx', 'Akari Therapeutics PLC', 'Pharmaceuticals', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 225, 216, 305, 746),
    ('akba', 'Akebia Therapeutics Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 200, 218, 215, 633),
    ('akro', 'Akero Therapeutics Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 250, 246, 305, 801),
    ('akus', 'Akouos Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 205, 221, 295, 721),
    ('akts', 'Akoustis Technologies Inc', 'Electrical Equipment', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'BBB', 'High', 'BBB', 'High', 222, 302, 428, 952),
    ('akya', 'Akoya Biosciences Inc', 'Life Sciences Tools and Services', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 512, 303, 215, 1030),
    ('aku', 'Akumin Inc', 'Health Care', 'NASDAQ NMS - GLOBAL MARKET', 'BBB', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 455, 347, 300, 1102),
    ('alk', 'Alaska Air Group Inc', 'Airlines', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 515, 303, 259, 1077),
    ('alb', 'Albemarle Corp', 'Chemicals', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 545, 322, 315, 1182),
    ('albo', 'Albireo Pharma Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 300, 310, 1110),
    ('aldx', 'Aldeyra Therapeutics Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 231, 261, 235, 727),
    ('alec', 'Alector Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 240, 277, 300, 817),
    ('are', 'Alexandria Real Estate Equities Inc', 'Real Estate', 'NEW YORK STOCK EXCHANGE, INC.', 'AA', 'Excellent', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 600, 337, 345, 1282),
    ('alf', 'Alfi Inc', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 225, 260, 315, 800),
    ('alco', 'Alico Inc', 'Food Products', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 300, 300, 1100),
    ('algn', 'Align Technology Inc', 'Health Care', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 235, 285, 255, 775),
    ('alhc', 'Alignment Healthcare LLC', 'N/A', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 210, 302, 256, 768),
    ('algs', 'Aligos Therapeutics Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 210, 222, 235, 667),
    ('alim', 'Alimera Sciences Inc', 'Pharmaceuticals', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 220, 228, 243, 691),
    ('alkt', 'Alkami Technology Inc', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 280, 305, 260, 845),
    ('alks', 'Alkermes Plc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'BBB', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 415, 302, 333, 1050),
    ('allk', 'Allakos Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 200, 273, 300, 773),
    ('y', 'Alleghany Corp', 'Insurance', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 215, 240, 300, 755),
    ('abtx', 'Allegiance Bancshares Inc', 'Banking', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 298, 300, 300, 898),
    ('algt', 'Allegiant Travel Co', 'Airlines', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 287, 208, 248, 743),
    ('alle', 'Allegion PLC', 'Building', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 542, 322, 315, 1179),
    ('algm', 'Allegro Microsystems Inc', 'Semiconductors', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 542, 314, 250, 1106),
    ('lnt', 'Alliant Energy Corp', 'Utilities', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 519, 307, 300, 1126),
    ('aese', 'Allied Esports Entertainment Inc', 'Hotels Restaurants and Leisure', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 200, 200, 200, 600),
    ('ahpi', 'Allied Healthcare Products Inc', 'Health Care', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 210, 228, 325, 763),
    ('allo', 'Allogene Therapeutics Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 535, 324, 305, 1164),
    ('allt', 'Allot Ltd', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 508, 324, 310, 1142),
    ('all', 'Allstate Corp', 'Insurance', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 530, 300, 220, 1050),
    ('alny', 'Alnylam Pharmaceuticals Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 331, 346, 325, 1002),
    ('googl', 'Alphabet Inc', 'Media', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 295, 362, 355, 1012),
    ('aei', 'Alset Ehome International Inc', 'Real Estate', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'B', 'Medium', 'B', 'Medium', 'BBB', 'High', 520, 207, 210, 937),
    ('aimc', 'Altra Industrial Motion Corp', 'Machinery', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 525, 315, 305, 1145),
    ('mo', 'Altria Group Inc', 'Tobacco', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 327, 341, 1168),
    ('amzn', 'Amazon.com Inc', 'Retail', 'NASDAQ NMS - GLOBAL MARKET', 'AA', 'Excellent', 'BB', 'Medium', 'BBB', 'High', 'A', 'High', 668, 305, 460, 1433),
    ('aee', 'Ameren Corp', 'Utilities', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 562, 345, 300, 1207),
    ('aal', 'American Airlines Group Inc', 'Airlines', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 270, 211, 265, 746),
    ('aep', 'American Electric Power Company Inc', 'Utilities', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 300, 300, 1100),
    ('axp', 'American Express Co', 'Financial Services', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 230, 226, 208, 664),
    ('aig', 'American International Group Inc', 'Insurance', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 518, 323, 310, 1151),
    ('amt', 'American Tower Corp', 'Real Estate', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 530, 333, 305, 1168),
    ('awk', 'American Water Works Company Inc', 'Utilities', 'NEW YORK STOCK EXCHANGE, INC.', 'AA', 'Excellent', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 653, 395, 300, 1348),
    ('amp', 'Ameriprise Financial Inc', 'Financial Services', 'NEW YORK STOCK EXCHANGE, INC.', 'BB', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 396, 308, 267, 971),
    ('abcb', 'Ameris Bancorp', 'Banking', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 290, 300, 250, 840),
    ('abc', 'Amerisourcebergen Corp', 'Health Care', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 505, 300, 315, 1120),
    ('ame', 'AMETEK Inc', 'Electrical Equipment', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 540, 329, 270, 1139),
    ('amgn', 'Amgen Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 575, 312, 328, 1215),
    ('poww', 'Ammo Inc', 'Leisure Products', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 233, 224, 200, 657),
    ('aph', 'Amphenol Corp', 'Electrical Equipment', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BBB', 'High', 'A', 'High', 512, 303, 475, 1290),
    ('adi', 'Analog Devices Inc', 'Semiconductors', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 350, 318, 300, 968),
    ('anss', 'ANSYS Inc', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'A', 'High', 580, 337, 285, 1202),
    ('aehl', 'Antelope Enterprise Holdings Ltd', 'Building', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 238, 237, 325, 800),
    ('aon', 'Aon PLC', 'Insurance', 'NEW YORK STOCK EXCHANGE, INC.', 'BBB', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 485, 304, 288, 1077),
    ('apa', 'APA Corp (US)', 'Energy', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 510, 316, 325, 1151),
    ('aapl', 'Apple Inc', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 355, 281, 255, 891),
    ('agtc', 'Applied Genetic Technologies Corp', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 235, 323, 305, 863),
    ('amat', 'Applied Materials Inc', 'Semiconductors', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 525, 317, 300, 1142),
    ('aaoi', 'Applied Optoelectronics Inc', 'Communications', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 311, 256, 218, 785),
    ('aptv', 'Aptiv PLC', 'Auto Components', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 555, 339, 310, 1204),
    ('abus', 'Arbutus Biopharma Corp', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 203, 204, 338, 745),
    ('abio', 'ARCA Biopharma Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 200, 222, 290, 712),
    ('acgl', 'Arch Capital Group Ltd', 'Insurance', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 300, 300, 1100),
    ('adm', 'Archer-Daniels-Midland Co', 'Food Products', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 587, 353, 305, 1245),
    ('anet', 'Arista Networks Inc', 'Communications', 'NEW YORK STOCK EXCHANGE, INC.', 'BBB', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 444, 310, 295, 1049),
    ('aaci', 'Armada Acquisition Corp I', 'N/A', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 205, 200, 200, 605),
    ('aip', 'Arteris Inc', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'B', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 286, 300, 1086),
    ('ajg', 'Arthur J. Gallagher & Co.', 'Insurance', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 530, 344, 310, 1184),
    ('pre', 'Artisan Acquisition Corp', 'N/A', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 245, 203, 265, 713),
    ('aiz', 'Assurant Inc', 'Insurance', 'NEW YORK STOCK EXCHANGE, INC.', 'BBB', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 438, 316, 300, 1054),
    ('t', 'AT&T Inc', 'Telecommunication', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 210, 200, 305, 715),
    ('aacg', 'ATA Creativity Global', 'Diversified Consumer Services', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 203, 200, 205, 608),
    ('aame', 'Atlantic American Corp', 'Insurance', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 220, 221, 300, 741),
    ('aaww', 'Atlas Air Worldwide Holdings Inc', 'Logistics and Transportation', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'B', 'Medium', 'B', 'Medium', 'BBB', 'High', 520, 243, 237, 1000),
    ('ato', 'Atmos Energy Corp', 'Utilities', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 572, 368, 315, 1255),
    ('aeye', 'AudioEye Inc', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 235, 301, 308, 844),
    ('adsk', 'Autodesk Inc', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 555, 304, 310, 1169),
    ('adp', 'Automatic Data Processing Inc', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 500, 300, 200, 1000),
    ('aatc', 'Autoscope Technologies Corp', 'Electrical Equipment', 'NASDAQ NMS - GLOBAL MARKET', 'BBB', 'High', 'B', 'Medium', 'B', 'Medium', 'BBB', 'High', 410, 286, 240, 936),
    ('azo', 'Autozone Inc', 'Retail', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 260, 222, 213, 695),
    ('avb', 'Avalonbay Communities Inc', 'Real Estate', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 500, 300, 298, 1098),
    ('avy', 'Avery Dennison Corp', 'Packaging', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 535, 347, 325, 1207),
    ('acls', 'Axcelis Technologies Inc', 'Semiconductors', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 515, 306, 260, 1081),
    ('bac', 'Bank of America Corp', 'Banking', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 220, 394, 265, 879),
    ('bk', 'Bank of New York Mellon Corp', 'Financial Services', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 300, 300, 1100),
    ('bbwi', 'Bath & Body Works Inc', 'Retail', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 525, 303, 300, 1128),
    ('bax', 'Baxter International Inc', 'Health Care', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 316, 300, 1116),
    ('bdx', 'Becton Dickinson and Co', 'Health Care', 'NEW YORK STOCK EXCHANGE, INC.', 'AA', 'Excellent', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 607, 384, 315, 1306),
    ('bby', 'Best Buy Co Inc', 'Retail', 'NEW YORK STOCK EXCHANGE, INC.', 'BBB', 'High', 'B', 'Medium', 'BB', 'Medium', 'BBB', 'High', 430, 231, 300, 961),
    ('bio', 'Bio Rad Laboratories Inc', 'Life Sciences Tools and Services', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 275, 227, 300, 802),
    ('tech', 'Bio-Techne Corp', 'Life Sciences Tools and Services', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'B', 'Medium', 'BB', 'Medium', 'BBB', 'High', 510, 268, 300, 1078),
    ('biib', 'Biogen Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 380, 303, 364, 1047),
    ('bx', 'Blackstone Inc', 'Financial Services', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 534, 343, 320, 1197),
    ('ba', 'Boeing Co', 'Aerospace and Defense', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 220, 224, 235, 679),
    ('bkng', 'Booking Holdings Inc', 'Hotels Restaurants and Leisure', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 558, 306, 310, 1174),
    ('bwa', 'Borgwarner Inc', 'Auto Components', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 260, 206, 230, 696),
    ('bxp', 'Boston Properties Inc', 'Real Estate', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 532, 339, 305, 1176),
    ('bsx', 'Boston Scientific Corp', 'Health Care', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 525, 399, 300, 1224),
    ('bmy', 'Bristol-Myers Squibb Co', 'Pharmaceuticals', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 321, 310, 1131),
    ('avgo', 'Broadcom Inc', 'Semiconductors', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 210, 212, 200, 622),
    ('br', 'Broadridge Financial Solutions Inc', 'Technology', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 550, 313, 325, 1188),
    ('bro', 'Brown & Brown Inc', 'Insurance', 'NEW YORK STOCK EXCHANGE, INC.', 'BBB', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 405, 320, 300, 1025),
    ('cdns', 'Cadence Design Systems Inc', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 500, 308, 295, 1103),
    ('czr', 'Caesars Entertainment Inc', 'Hotels Restaurants and Leisure', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 265, 228, 200, 693),
    ('clxt', 'Calyxt Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 535, 322, 325, 1182),
    ('cmbm', 'Cambium Networks Corp', 'Communications', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 505, 337, 300, 1142),
    ('cpb', 'Campbell Soup Co', 'Food Products', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 515, 301, 305, 1121),
    ('cnne', 'Cannae Holdings Inc', 'Financial Services', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 215, 203, 203, 621),
    ('cof', 'Capital One Financial Corp', 'Financial Services', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 508, 309, 320, 1137),
    ('cah', 'Cardinal Health Inc', 'Health Care', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 505, 300, 315, 1120),
    ('kmx', 'Carmax Inc', 'Retail', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 251, 237, 300, 788),
    ('ccl', 'Carnival Corp', 'Hotels Restaurants and Leisure', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 515, 326, 320, 1161),
    ('carr', 'Carrier Global Corp', 'Building', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 210, 258, 226, 694),
    ('ctlt', 'Catalent Inc', 'Pharmaceuticals', 'NEW YORK STOCK EXCHANGE, INC.', 'BBB', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 483, 303, 305, 1091),
    ('clst', 'Catalyst Bancorp Inc', 'Financial Services', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 260, 350, 267, 877),
    ('cat', 'Caterpillar Inc', 'Machinery', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 235, 239, 235, 709),
    ('cbre', 'CBRE Group Inc', 'Real Estate', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 200, 209, 200, 609),
    ('cdw', 'CDW Corp', 'Electrical Equipment', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 225, 209, 200, 634),
    ('ce', 'Celanese Corp', 'Chemicals', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 319, 300, 1119),
    ('clsn', 'Celsion Corp', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 255, 214, 300, 769),
    ('cnc', 'Centene Corp', 'Health Care', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 548, 355, 315, 1218),
    ('cnp', 'CenterPoint Energy Inc', 'Utilities', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 550, 320, 260, 1130),
    ('cday', 'Ceridian HCM Holding Inc', 'Technology', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 530, 379, 320, 1229),
    ('cf', 'CF Industries Holdings Inc', 'Chemicals', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 525, 307, 310, 1142),
    ('chrw', 'CH Robinson Worldwide Inc', 'Logistics and Transportation', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 575, 330, 338, 1243),
    ('crl', 'Charles River Laboratories International Inc', 'Life Sciences Tools and Services', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 510, 322, 235, 1067),
    ('schw', 'Charles Schwab Corp', 'Financial Services', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 515, 300, 300, 1115),
    ('chtr', 'Charter Communications Inc', 'Media', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 300, 300, 1100),
    ('cmcm', 'Cheetah Mobile Inc', 'Technology', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 205, 214, 215, 634),
    ('cvx', 'Chevron Corp', 'Energy', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 210, 217, 210, 637),
    ('cmg', 'Chipotle Mexican Grill Inc', 'Hotels Restaurants and Leisure', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 210, 241, 213, 664),
    ('chd', 'Church & Dwight Co Inc', 'Consumer products', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 578, 341, 348, 1267),
    ('ci', 'Cigna Corp', 'Health Care', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 508, 328, 310, 1146),
    ('cinf', 'Cincinnati Financial Corp', 'Insurance', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 235, 275, 250, 760),
    ('cnk', 'Cinemark Holdings Inc', 'Media', 'NEW YORK STOCK EXCHANGE, INC.', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 330, 300, 300, 930),
    ('ctas', 'Cintas Corp', 'Commercial Services and Supplies', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 300, 300, 1100),
    ('csco', 'Cisco Systems Inc', 'Communications', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 280, 234, 220, 734),
    ('c', 'Citigroup Inc', 'Banking', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 515, 300, 303, 1118),
    ('cfg', 'Citizens Financial Group Inc', 'Banking', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 230, 215, 205, 650),
    ('ctxs', 'Citrix Systems Inc', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 530, 305, 305, 1140),
    ('clsk', 'CleanSpark Inc', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 570, 326, 310, 1206),
    ('you', 'Clear Secure Inc', 'Technology', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'B', 'Medium', 'B', 'Medium', 'BBB', 'High', 515, 278, 205, 998),
    ('clro', 'Clearone Inc', 'Communications', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 370, 228, 210, 808),
    ('clsd', 'Clearside Biomedical Inc', 'Pharmaceuticals', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 215, 230, 200, 645),
    ('clvr', 'Clever Leaves Holdings Inc', 'Pharmaceuticals', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 225, 243, 205, 673),
    ('clx', 'Clorox Co', 'Consumer products', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 560, 350, 345, 1255),
    ('clvs', 'Clovis Oncology Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 225, 212, 300, 737),
    ('cme', 'CME Group Inc', 'Financial Services', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 375, 237, 200, 812),
    ('cms', 'CMS Energy Corp', 'Utilities', 'NEW YORK STOCK EXCHANGE, INC.', 'BBB', 'High', 'AA', 'Excellent', 'C', 'Low', 'BBB', 'High', 450, 667, 75, 1192),
    ('cna', 'CNA Financial Corp', 'Insurance', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 540, 329, 340, 1209),
    ('cnf', 'CNFinance Holdings Ltd', 'Financial Services', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 200, 200, 220, 620),
    ('cno', 'CNO Financial Group Inc', 'Insurance', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 322, 315, 1137),
    ('ko', 'Coca-Cola Co', 'Beverages', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 200, 201, 200, 601),
    ('ctsh', 'Cognizant Technology Solutions Corp', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'AA', 'Excellent', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 605, 365, 300, 1270),
    ('cl', 'Colgate-Palmolive Co', 'Consumer products', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 520, 310, 310, 1140),
    ('cmco', 'Columbus McKinnon Corp', 'Machinery', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 200, 323, 240, 763),
    ('cmcsa', 'Comcast Corp', 'Media', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 507, 343, 315, 1165),
    ('cma', 'Comerica Inc', 'Banking', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 280, 300, 230, 810),
    ('cmc', 'Commercial Metals Co', 'Metals and Mining', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 223, 212, 200, 635),
    ('cmp', 'Compass Minerals International Inc', 'Metals and Mining', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 505, 302, 320, 1127),
    ('cag', 'Conagra Brands Inc', 'Food Products', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 525, 306, 300, 1131),
    ('cnd', 'Concord Acquisition Corp', 'N/A', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 205, 257, 300, 762),
    ('cnmd', 'Conmed Corp', 'Health Care', 'NEW YORK STOCK EXCHANGE, INC.', 'BBB', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 441, 300, 270, 1011),
    ('cop', 'Conocophillips', 'Energy', 'NEW YORK STOCK EXCHANGE, INC.', 'AA', 'Excellent', 'A', 'High', 'BB', 'Medium', 'A', 'High', 687, 544, 305, 1536),
    ('ed', 'Consolidated Edison Inc', 'Utilities', 'NEW YORK STOCK EXCHANGE, INC.', 'AA', 'Excellent', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 700, 358, 300, 1358),
    ('stz', 'Constellation Brands Inc', 'Beverages', 'NEW YORK STOCK EXCHANGE, INC.', 'BBB', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 459, 313, 295, 1067),
    ('coo', 'Cooper Companies Inc', 'Health Care', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 300, 300, 1100),
    ('cprt', 'Copart Inc', 'Commercial Services and Supplies', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 270, 204, 205, 679),
    ('glw', 'Corning Inc', 'Electrical Equipment', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 200, 200, 200, 600),
    ('ctva', 'Corteva Inc', 'Chemicals', 'NEW YORK STOCK EXCHANGE, INC.', 'AA', 'Excellent', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 610, 312, 320, 1242),
    ('cmre', 'Costamare Inc', 'Marine', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 242, 204, 200, 646),
    ('cost', 'Costco Wholesale Corp', 'Retail', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 537, 306, 225, 1068),
    ('ctra', 'Coterra Energy Inc', 'Energy', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 555, 329, 310, 1194),
    ('cci', 'Crown Castle Inc', 'Real Estate', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 500, 300, 200, 1000),
    ('csx', 'CSX Corp', 'Road and Rail', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 510, 310, 325, 1145),
    ('cmi', 'Cummins Inc', 'Machinery', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 510, 320, 300, 1130),
    ('cvs', 'CVS Health Corp', 'Health Care', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 540, 302, 315, 1157),
    ('dhi', 'D R Horton Inc', 'Consumer products', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 250, 271, 205, 726),
    ('dhr', 'Danaher Corp', 'Life Sciences Tools and Services', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 530, 344, 385, 1259),
    ('dri', 'Darden Restaurants Inc', 'Hotels Restaurants and Leisure', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 515, 309, 300, 1124),
    ('dva', 'DaVita Inc', 'Health Care', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 260, 332, 300, 892),
    ('de', 'Deere & Co', 'Machinery', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 560, 339, 305, 1204),
    ('dell', 'Dell Technologies Inc', 'Technology', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 500, 318, 275, 1093),
    ('dal', 'Delta Air Lines Inc', 'Airlines', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 515, 300, 313, 1128),
    ('xray', 'DENTSPLY SIRONA Inc', 'Health Care', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 530, 318, 305, 1153),
    ('dvn', 'Devon Energy Corp', 'Energy', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 570, 301, 300, 1171),
    ('dxcm', 'Dexcom Inc', 'Health Care', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 215, 236, 215, 666),
    ('fang', 'Diamondback Energy Inc', 'Energy', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'B', 'Medium', 'BB', 'Medium', 'BBB', 'High', 513, 271, 300, 1084),
    ('dlr', 'Digital Realty Trust Inc', 'Real Estate', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 540, 317, 300, 1157),
    ('dfs', 'Discover Financial Services', 'Financial Services', 'NEW YORK STOCK EXCHANGE, INC.', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 335, 321, 313, 969),
    ('dish', 'DISH Network Corp', 'Media', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 210, 263, 205, 678),
    ('dg', 'Dollar General Corp', 'Retail', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 247, 222, 200, 669),
    ('dltr', 'Dollar Tree Inc', 'Retail', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 235, 208, 215, 658),
    ('d', 'Dominion Energy Inc', 'Utilities', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 535, 325, 310, 1170),
    ('dpz', "Domino's Pizza Inc", 'Hotels Restaurants and Leisure', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 205, 205, 200, 610),
    ('dov', 'Dover Corp', 'Machinery', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 320, 305, 1125),
    ('dow', 'Dow Inc', 'Chemicals', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 225, 201, 200, 626),
    ('dte', 'DTE Energy Co', 'Utilities', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 592, 313, 210, 1115),
    ('duk', 'Duke Energy Corp', 'Utilities', 'NEW YORK STOCK EXCHANGE, INC.', 'AA', 'Excellent', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 604, 362, 328, 1294),
    ('dre', 'Duke Realty Corp', 'Real Estate', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 540, 313, 300, 1153),
    ('dd', 'Dupont De Nemours Inc', 'Chemicals', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 550, 341, 295, 1186),
    ('dxc', 'DXC Technology Co', 'Technology', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 505, 326, 305, 1136),
    ('emn', 'Eastman Chemical Co', 'Chemicals', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 583, 365, 310, 1258),
    ('etn', 'Eaton Corporation PLC', 'Electrical Equipment', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 520, 328, 320, 1168),
    ('ebay', 'eBay Inc', 'Retail', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 302, 305, 1107),
    ('ecl', 'Ecolab Inc', 'Chemicals', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 547, 373, 325, 1245),
    ('eix', 'Edison International', 'Utilities', 'NEW YORK STOCK EXCHANGE, INC.', 'AA', 'Excellent', 'A', 'High', 'BB', 'Medium', 'A', 'High', 700, 513, 315, 1528),
    ('adoc', 'Edoc Acquisition Corp', 'N/A', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 215, 301, 300, 816),
    ('ew', 'Edwards Lifesciences Corp', 'Health Care', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 290, 333, 305, 928),
    ('ea', 'Electronic Arts Inc', 'Media', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 360, 300, 225, 885),
    ('lly', 'Eli Lilly and Co', 'Pharmaceuticals', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 510, 360, 310, 1180),
    ('emr', 'Emerson Electric Co', 'Electrical Equipment', 'NEW YORK STOCK EXCHANGE, INC.', 'AA', 'Excellent', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 605, 323, 315, 1243),
    ('act', 'Enact Holdings Inc', 'Financial Services', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 540, 328, 315, 1183),
    ('enph', 'Enphase Energy Inc', 'Semiconductors', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 565, 316, 300, 1181),
    ('etr', 'Entergy Corp', 'Utilities', 'NEW YORK STOCK EXCHANGE, INC.', 'AA', 'Excellent', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 653, 380, 310, 1343),
    ('eog', 'EOG Resources Inc', 'Energy', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'B', 'Medium', 'B', 'Medium', 'BBB', 'High', 550, 252, 240, 1042),
    ('efx', 'Equifax Inc', 'Professional Services', 'NEW YORK STOCK EXCHANGE, INC.', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 390, 300, 305, 995),
    ('eqix', 'Equinix Inc', 'Real Estate', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 515, 323, 315, 1153),
    ('eqr', 'Equity Residential', 'Real Estate', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 235, 208, 210, 653),
    ('ess', 'Essex Property Trust Inc', 'Real Estate', 'NEW YORK STOCK EXCHANGE, INC.', 'BB', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 377, 304, 210, 891),
    ('el', 'Estee Lauder Companies Inc', 'Consumer products', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 300, 300, 1100),
    ('etsy', 'ETSY Inc', 'Retail', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 235, 241, 235, 711),
    ('clwt', 'Euro Tech Holdings Company Ltd', 'Trading Companies and Distributors', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 230, 201, 210, 641),
    ('evk', 'Ever-Glory International Group Inc', 'Textiles Apparel and Luxury Goods', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 200, 211, 210, 621),
    ('re', 'Everest Re Group Ltd', 'Insurance', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'B', 'Medium', 'BB', 'Medium', 'BBB', 'High', 505, 276, 305, 1086),
    ('evrg', 'Evergy Inc', 'Utilities', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 555, 310, 300, 1165),
    ('es', 'Eversource Energy', 'Utilities', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BBB', 'High', 'BB', 'Medium', 'A', 'High', 576, 409, 310, 1295),
    ('exc', 'Exelon Corp', 'Utilities', 'NASDAQ NMS - GLOBAL MARKET', 'AA', 'Excellent', 'BBB', 'High', 'BB', 'Medium', 'A', 'High', 694, 403, 316, 1413),
    ('expe', 'Expedia Group Inc', 'Hotels Restaurants and Leisure', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 225, 242, 305, 772),
    ('expd', 'Expeditors International of Washington Inc', 'Logistics and Transportation', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 510, 302, 300, 1112),
    ('exr', 'Extra Space Storage Inc', 'Real Estate', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'B', 'Medium', 'B', 'Medium', 'BBB', 'High', 572, 289, 225, 1086),
    ('xom', 'Exxon Mobil Corp', 'Energy', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 538, 322, 313, 1173),
    ('ffiv', 'F5 Inc', 'Communications', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 200, 221, 215, 636),
    ('fn', 'Fabrinet', 'Electrical Equipment', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'B', 'Medium', 'B', 'Medium', 'BBB', 'High', 510, 209, 210, 929),
    ('fast', 'Fastenal Co', 'Trading Companies and Distributors', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'B', 'Medium', 230, 302, 200, 732),
    ('frt', 'Federal Realty Investment Trust', 'Real Estate', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 525, 302, 300, 1127),
    ('fdx', 'FedEx Corp', 'Logistics and Transportation', 'NEW YORK STOCK EXCHANGE, INC.', 'BB', 'Medium', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 335, 278, 255, 868),
    ('fis', 'Fidelity National Information Services Inc', 'Technology', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'B', 'Medium', 'BB', 'Medium', 'BBB', 'High', 530, 298, 310, 1138),
    ('fitb', 'Fifth Third Bancorp', 'Banking', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 313, 300, 215, 828),
    ('frc', 'First Republic Bank', 'Banking', 'NEW YORK STOCK EXCHANGE, INC.', 'BB', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 370, 331, 288, 989),
    ('myfw', 'First Western Financial Inc', 'Banking', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 351, 300, 235, 886),
    ('fe', 'FirstEnergy Corp', 'Utilities', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 510, 304, 300, 1114),
    ('fisv', 'Fiserv Inc', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 395, 302, 310, 1007),
    ('flt', 'Fleetcor Technologies Inc', 'Technology', 'NEW YORK STOCK EXCHANGE, INC.', 'BBB', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 410, 302, 300, 1012),
    ('fmc', 'FMC Corp', 'Chemicals', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 510, 307, 315, 1132),
    ('f', 'Ford Motor Co', 'Automobiles', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 292, 246, 215, 753),
    ('ftnt', 'Fortinet Inc', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 306, 305, 1111),
    ('ftv', 'Fortive Corp', 'Machinery', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 540, 326, 305, 1171),
    ('fbhs', 'Fortune Brands Home & Security Inc', 'Building', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 510, 302, 300, 1112),
    ('foxa', 'Fox Corp', 'Media', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 295, 330, 315, 940),
    ('ben', 'Franklin Resources Inc', 'Financial Services', 'NEW YORK STOCK EXCHANGE, INC.', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 321, 349, 310, 980),
    ('fcx', 'Freeport-McMoRan Inc', 'Metals and Mining', 'NEW YORK STOCK EXCHANGE, INC.', 'AA', 'Excellent', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 608, 313, 305, 1226),
    ('gps', 'Gap Inc', 'Retail', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 515, 349, 300, 1164),
    ('grmn', 'Garmin Ltd', 'Consumer products', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 205, 242, 200, 647),
    ('it', 'Gartner Inc', 'Technology', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 316, 315, 1131),
    ('gnrc', 'Generac Holdings Inc', 'Electrical Equipment', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 535, 311, 250, 1096),
    ('gd', 'General Dynamics Corp', 'Aerospace and Defense', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 510, 310, 300, 1120),
    ('ge', 'General Electric Co', 'Industrial Conglomerates', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 533, 300, 300, 1133),
    ('gis', 'General Mills Inc', 'Food Products', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 585, 326, 365, 1276),
    ('gm', 'General Motors Co', 'Automobiles', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 510, 303, 255, 1068),
    ('gpc', 'Genuine Parts Co', 'Distributors', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'B', 'Medium', 'BB', 'Medium', 'BBB', 'High', 535, 225, 305, 1065),
    ('gild', 'Gilead Sciences Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 303, 300, 1103),
    ('gpn', 'Global Payments Inc', 'Technology', 'NEW YORK STOCK EXCHANGE, INC.', 'BB', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 310, 343, 265, 918),
    ('gwrs', 'Global Water Resources Inc', 'Utilities', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 367, 297, 235, 899),
    ('gl', 'Globe Life Inc', 'Insurance', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 215, 238, 215, 668),
    ('gs', 'Goldman Sachs Group Inc', 'Financial Services', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 525, 305, 305, 1135),
    ('gva', 'Granite Construction Inc', 'Construction', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 200, 200, 200, 600),
    ('gvp', 'GSE Systems Inc', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 505, 307, 245, 1057),
    ('gwre', 'Guidewire Software Inc', 'Technology', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 549, 321, 330, 1200),
    ('gure', 'Gulf Resources Inc', 'Chemicals', 'NASDAQ NMS - GLOBAL MARKET', 'BBB', 'High', 'B', 'Medium', 'BB', 'Medium', 'BBB', 'High', 408, 206, 300, 914),
    ('gyro', 'Gyrodyne LLC', 'Real Estate', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 240, 206, 240, 686),
    ('hae', 'Haemonetics Corp', 'Health Care', 'NEW YORK STOCK EXCHANGE, INC.', 'BBB', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 448, 303, 305, 1056),
    ('hain', 'Hain Celestial Group Inc', 'Food Products', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 520, 302, 305, 1127),
    ('hall', 'Hallmark Financial Services Inc', 'Insurance', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 215, 233, 300, 748),
    ('halo', 'Halozyme Therapeutics Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 510, 302, 315, 1127),
    ('hbb', 'Hamilton Beach Brands Holding Co', 'Consumer products', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 245, 272, 230, 747),
    ('hbi', 'HanesBrands Inc', 'Textiles Apparel and Luxury Goods', 'NEW YORK STOCK EXCHANGE, INC.', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 310, 223, 305, 838),
    ('hafc', 'Hanmi Financial Corp', 'Banking', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 250, 207, 233, 690),
    ('hasi', 'Hannon Armstrong Sustainable Infrastructure Capital Inc', 'Real Estate', 'NEW YORK STOCK EXCHANGE, INC.', 'AA', 'Excellent', 'BBB', 'High', 'BB', 'Medium', 'A', 'High', 646, 404, 313, 1363),
    ('happ', 'Happiness Development Group Ltd', 'Consumer products', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 225, 207, 300, 732),
    ('hcdi', 'Harbor Custom Development Inc', 'Consumer products', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 222, 221, 208, 651),
    ('harp', 'Harpoon Therapeutics Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'BBB', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 485, 300, 310, 1095),
    ('hig', 'Hartford Financial Services Group Inc', 'Insurance', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 305, 305, 1110),
    ('hbio', 'Harvard Bioscience Inc', 'Life Sciences Tools and Services', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 250, 221, 300, 771),
    ('has', 'Hasbro Inc', 'Leisure Products', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 255, 301, 300, 856),
    ('he', 'Hawaiian Electric Industries Inc', 'Utilities', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 585, 348, 310, 1243),
    ('ha', 'Hawaiian Holdings Inc', 'Airlines', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'B', 'Medium', 200, 321, 200, 721),
    ('hayn', 'Haynes International Inc', 'Metals and Mining', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 301, 300, 1101),
    ('hayw', 'Hayward Holdings Inc', 'Building', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 535, 305, 300, 1140),
    ('hbt', 'HBT Financial Inc', 'Banking', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 245, 275, 300, 820),
    ('hca', 'HCA Healthcare Inc', 'Health Care', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 520, 348, 305, 1173),
    ('hci', 'Hci Group Inc', 'Insurance', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 205, 260, 300, 765),
    ('haac', 'Health Assurance Acquisition Corp', 'N/A', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 200, 258, 300, 758),
    ('hcat', 'Health Catalyst Inc', 'Health Care', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 545, 324, 320, 1189),
    ('hcar', 'Healthcare Services Acquisition Corp', 'N/A', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 245, 205, 300, 750),
    ('peak', 'Healthpeak Properties Inc', 'Real Estate', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 535, 331, 335, 1201),
    ('hei', 'HEICO Corp', 'Aerospace & Defense', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 225, 203, 205, 633),
    ('hsic', 'Henry Schein Inc', 'Health Care', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 210, 205, 200, 615),
    ('hcci', 'Heritage-Crystal Clean Inc', 'Commercial Services and Supplies', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BBB', 'High', 'BB', 'Medium', 'A', 'High', 525, 400, 300, 1225),
    ('hsy', 'Hershey Co', 'Food Products', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 525, 361, 300, 1186),
    ('hes', 'Hess Corp', 'Energy', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 535, 300, 305, 1140),
    ('hesm', 'Hess Midstream LP', 'Energy ', 'NEW YORK STOCK EXCHANGE, INC.', 'BB', 'Medium', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 307, 257, 255, 819),
    ('hpe', 'Hewlett Packard Enterprise Co', 'Technology', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 230, 359, 230, 819),
    ('hi', 'Hillenbrand Inc', 'Machinery', 'NEW YORK STOCK EXCHANGE, INC.', 'BBB', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 489, 349, 300, 1138),
    ('hgv', 'Hilton Grand Vacations Inc', 'Hotels, Restaurants & Leisure', 'NEW YORK STOCK EXCHANGE, INC.', 'BB', 'Medium', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 305, 288, 250, 843),
    ('hlt', 'Hilton Worldwide Holdings Inc', 'Hotels Restaurants and Leisure', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 293, 200, 205, 698),
    ('hep', 'Holly Energy Partners LP', 'Energy ', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'B', 'Medium', 'B', 'Medium', 'BBB', 'High', 511, 225, 215, 951),
    ('holx', 'Hologic Inc', 'Health Care', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 515, 324, 315, 1154),
    ('hbcp', 'Home Bancorp Inc', 'Financial Services', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 230, 202, 200, 632),
    ('hd', 'Home Depot Inc', 'Retail', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 230, 317, 205, 752),
    ('hon', 'Honeywell International Inc', 'Industrial Conglomerates', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 545, 344, 308, 1197),
    ('hbnc', 'Horizon Bancorp Inc', 'Banking', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 255, 321, 233, 809),
    ('hrl', 'Hormel Foods Corp', 'Food Products', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 570, 322, 300, 1192),
    ('hst', 'Host Hotels & Resorts Inc', 'Real Estate', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 510, 318, 318, 1146),
    ('hhc', 'Howard Hughes Corp', 'Real Estate', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 300, 300, 1100),
    ('hwm', 'Howmet Aerospace Inc', 'Aerospace and Defense', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 525, 315, 320, 1160),
    ('hpq', 'HP Inc', 'Technology', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 245, 211, 200, 656),
    ('hubs', 'HubSpot Inc', 'Technology', 'NEW YORK STOCK EXCHANGE, INC.', 'BBB', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 480, 329, 320, 1129),
    ('hum', 'Humana Inc', 'Health Care', 'NEW YORK STOCK EXCHANGE, INC.', 'BBB', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 462, 300, 300, 1062),
    ('hban', 'Huntington Bancshares Inc', 'Banking', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 308, 300, 300, 908),
    ('hii', 'Huntington Ingalls Industries Inc', 'Aerospace and Defense', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 545, 315, 315, 1175),
    ('h', 'Hyatt Hotels Corp', 'Hotels, Restaurants & Leisure', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 235, 209, 205, 649),
    ('podd', 'Insulet Corp', 'Health Care', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 215, 233, 205, 653),
    ('jnj', 'Johnson & Johnson', 'Pharmaceuticals', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 565, 308, 300, 1173),
    ('jpm', 'JPMorgan Chase & Co', 'Banking', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 505, 319, 338, 1162),
    ('lrcx', 'Lam Research Corp', 'Semiconductors', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 510, 325, 315, 1150),
    ('lw', 'Lamb Weston Holdings Inc', 'Food Products', 'NEW YORK STOCK EXCHANGE, INC.', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BBB', 'High', 345, 256, 300, 901),
    ('lvs', 'Las Vegas Sands Corp', 'Hotels Restaurants and Leisure', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 547, 318, 313, 1178),
    ('leg', 'Leggett & Platt Inc', 'Consumer products', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 300, 300, 1100),
    ('ldos', 'Leidos Holdings Inc', 'Professional Services', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 300, 300, 1100),
    ('len', 'Lennar Corp', 'Consumer products', 'NEW YORK STOCK EXCHANGE, INC.', 'BB', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 363, 344, 220, 927),
    ('zev', 'Lightning eMotors Inc', 'Machinery', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 535, 391, 240, 1166),
    ('lnc', 'Lincoln National Corp', 'Insurance', 'NEW YORK STOCK EXCHANGE, INC.', 'AA', 'Excellent', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 700, 300, 300, 1300),
    ('lin', 'Linde PLC', 'Chemicals', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 210, 240, 275, 725),
    ('lyv', 'Live Nation Entertainment Inc', 'Media', 'NEW YORK STOCK EXCHANGE, INC.', 'BBB', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 492, 310, 250, 1052),
    ('lkq', 'LKQ Corp', 'Distributors', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 515, 300, 305, 1120),
    ('lmt', 'Lockheed Martin Corp', 'Aerospace and Defense', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 510, 324, 320, 1154),
    ('l', 'Loews Corp', 'Insurance', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 505, 303, 313, 1121),
    ('low', "Lowe's Companies Inc", 'Retail', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 218, 200, 200, 618),
    ('lumn', 'Lumen Technologies Inc', 'Telecommunication', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 535, 327, 305, 1167),
    ('lyb', 'LyondellBasell Industries NV', 'Chemicals', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 587, 352, 330, 1269),
    ('mtb', 'M&T Bank Corp', 'Banking', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 500, 303, 260, 1063),
    ('mtsi', 'MACOM Technology Solutions Holdings Inc', 'Semiconductors', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 377, 309, 255, 941),
    ('mtex', 'Mannatech Inc', 'Consumer products', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 200, 260, 230, 690),
    ('mro', 'Marathon Oil Corp', 'Energy', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 530, 313, 305, 1148),
    ('mpc', 'Marathon Petroleum Corp', 'Energy', 'NEW YORK STOCK EXCHANGE, INC.', 'AA', 'Excellent', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 700, 366, 315, 1381),
    ('mktx', 'Marketaxess Holdings Inc', 'Financial Services', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 230, 213, 210, 653),
    ('mar', 'Marriott International Inc', 'Hotels Restaurants and Leisure', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 215, 200, 215, 630),
    ('mmc', 'Marsh & McLennan Companies Inc', 'Insurance', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 300, 300, 1100),
    ('mlm', 'Martin Marietta Materials Inc', 'Construction', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 573, 313, 300, 1186),
    ('mas', 'Masco Corp', 'Building', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 522, 323, 305, 1150),
    ('ma', 'Mastercard Inc', 'Technology', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 210, 230, 215, 655),
    ('mtch', 'Match Group Inc', 'Media', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 245, 389, 311, 945),
    ('mtls', 'Materialise NV', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 505, 301, 300, 1106),
    ('mtrx', 'Matrix Service Co', 'Construction', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'A', 'High', 589, 390, 277, 1256),
    ('mttr', 'Matterport Inc', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 346, 325, 260, 931),
    ('mxct', 'MaxCyte Inc', 'Life Sciences Tools and Services', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 220, 300, 248, 768),
    ('mxl', 'Maxlinear Inc', 'Semiconductors', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 535, 325, 335, 1195),
    ('mkc', 'McCormick & Company Inc', 'Food Products', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 300, 300, 1100),
    ('mcd', "McDonald's Corp", 'Hotels Restaurants and Leisure', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 505, 326, 305, 1136),
    ('mck', 'Mckesson Corp', 'Health Care', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 303, 310, 1113),
    ('mdt', 'Medtronic PLC', 'Health Care', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 515, 308, 315, 1138),
    ('mrk', 'Merck & Co Inc', 'Pharmaceuticals', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 305, 315, 1120),
    ('meta', 'Meta Platforms Inc', 'Media', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 205, 232, 215, 652),
    ('mtcr', 'Metacrine Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 210, 207, 330, 747),
    ('met', 'MetLife Inc', 'Insurance', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 517, 305, 305, 1127),
    ('mtd', 'Mettler-Toledo International Inc', 'Life Sciences Tools and Services', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 505, 300, 240, 1045),
    ('mgm', 'MGM Resorts International', 'Hotels Restaurants and Leisure', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 500, 300, 200, 1000),
    ('mchp', 'Microchip Technology Inc', 'Semiconductors', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 300, 300, 1100),
    ('mu', 'Micron Technology Inc', 'Semiconductors', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 530, 330, 300, 1160),
    ('msft', 'Microsoft Corp', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'AA', 'Excellent', 'BBB', 'High', 'BB', 'Medium', 'A', 'High', 715, 443, 375, 1533),
    ('mvst', 'Microvast Holdings Inc', 'Machinery', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 225, 282, 210, 717),
    ('mvis', 'MicroVision Inc', 'Electrical Equipment', 'NASDAQ NMS - GLOBAL MARKET', 'BBB', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 451, 300, 330, 1081),
    ('maa', 'Mid-America Apartment Communities Inc', 'Real Estate', 'NEW YORK STOCK EXCHANGE, INC.', 'BB', 'Medium', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 315, 261, 210, 786),
    ('utrs', 'Minerva Surgical Inc', 'Health Care', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 205, 201, 210, 616),
    ('mtc', 'MMTEC Inc', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 221, 225, 305, 751),
    ('mrna', 'Moderna Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 300, 300, 1100),
    ('mhk', 'Mohawk Industries Inc', 'Consumer products', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'B', 'Medium', 'BB', 'Medium', 'BBB', 'High', 570, 298, 303, 1171),
    ('mtem', 'Molecular Templates Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 360, 325, 320, 1005),
    ('mdlz', 'Mondelez International Inc', 'Food Products', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 520, 307, 300, 1127),
    ('mpwr', 'Monolithic Power Systems Inc', 'Semiconductors', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 330, 287, 235, 852),
    ('mnst', 'Monster Beverage Corp', 'Beverages', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 515, 344, 300, 1159),
    ('mco', "Moody's Corp", 'Financial Services', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 515, 308, 235, 1058),
    ('ms', 'Morgan Stanley', 'Financial Services', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 555, 303, 320, 1178),
    ('mos', 'Mosaic Co', 'Chemicals', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 515, 379, 315, 1209),
    ('msi', 'Motorola Solutions Inc', 'Communications', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 505, 305, 347, 1157),
    ('msci', 'MSCI Inc', 'Financial Services', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 580, 347, 335, 1262),
    ('mvbf', 'MVB Financial Corp', 'Banking', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 210, 215, 215, 640),
    ('mymd', 'MyMD Pharmaceuticals Inc', 'Pharmaceuticals', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 205, 257, 230, 692),
    ('mygn', 'Myriad Genetics Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 353, 321, 294, 968),
    ('ndaq', 'Nasdaq Inc', 'Financial Services', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 505, 310, 300, 1115),
    ('ntap', 'NetApp Inc', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 545, 359, 325, 1229),
    ('nwl', 'Newell Brands Inc', 'Consumer products', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 525, 303, 315, 1143),
    ('nem', 'Newmont Corporation', 'Metals and Mining', 'NEW YORK STOCK EXCHANGE, INC.', 'AA', 'Excellent', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 675, 389, 355, 1419),
    ('nwsa', 'News Corp', 'Media', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 509, 300, 300, 1109),
    ('nee', 'Nextera Energy Inc', 'Utilities', 'NEW YORK STOCK EXCHANGE, INC.', 'AA', 'Excellent', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 668, 306, 313, 1287),
    ('nlsn', 'Nielsen Holdings PLC', 'Professional Services', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 310, 300, 1110),
    ('nke', 'Nike Inc', 'Textiles Apparel and Luxury Goods', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 205, 275, 200, 680),
    ('ni', 'NiSource Inc', 'Utilities', 'NEW YORK STOCK EXCHANGE, INC.', 'BB', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 361, 322, 223, 906),
    ('nsc', 'Norfolk Southern Corp', 'Road and Rail', 'NEW YORK STOCK EXCHANGE, INC.', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 358, 339, 330, 1027),
    ('ntrs', 'Northern Trust Corp', 'Financial Services', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 250, 226, 225, 701),
    ('noc', 'Northrop Grumman Corp', 'Aerospace and Defense', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 505, 302, 300, 1107),
    ('nlok', 'NortonLifeLock Inc', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 505, 315, 305, 1125),
    ('nclh', 'Norwegian Cruise Line Holdings Ltd', 'Hotels Restaurants and Leisure', 'NEW YORK STOCK EXCHANGE, INC.', 'BBB', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 495, 306, 300, 1101),
    ('nrg', 'NRG Energy Inc', 'Utilities', 'NEW YORK STOCK EXCHANGE, INC.', 'BB', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 371, 327, 218, 916),
    ('nue', 'Nucor Corp', 'Metals and Mining', 'NEW YORK STOCK EXCHANGE, INC.', 'BB', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 374, 340, 225, 939),
    ('nvda', 'NVIDIA Corp', 'Semiconductors', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 323, 301, 275, 899),
    ('nvr', 'NVR Inc', 'Consumer products', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 265, 206, 205, 676),
    ('nxpi', 'NXP Semiconductors NV', 'Semiconductors', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 505, 329, 305, 1139),
    ('orly', "O'Reilly Automotive Inc", 'Retail', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 300, 300, 1100),
    ('oxy', 'Occidental Petroleum Corp', 'Energy', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 505, 302, 300, 1107),
    ('odfl', 'Old Dominion Freight Line Inc', 'Road and Rail', 'NASDAQ NMS - GLOBAL MARKET', 'BBB', 'High', 'BBB', 'High', 'B', 'Medium', 'BBB', 'High', 467, 423, 280, 1170),
    ('omc', 'Omnicom Group Inc', 'Media', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 543, 333, 305, 1181),
    ('oke', 'ONEOK Inc', 'Energy', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 581, 326, 355, 1262),
    ('orcl', 'Oracle Corp', 'Technology', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 500, 300, 200, 1000),
    ('ogn', 'Organon & Co', 'Pharmaceuticals', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 515, 335, 305, 1155),
    ('pcar', 'Paccar Inc', 'Machinery', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 568, 343, 305, 1216),
    ('ppbi', 'Pacific Premier Bancorp Inc', 'Banking', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 565, 328, 315, 1208),
    ('pkg', 'Packaging Corp of America', 'Packaging', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 303, 300, 1103),
    ('ph', 'Parker-Hannifin Corp', 'Machinery', 'NEW YORK STOCK EXCHANGE, INC.', 'BB', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 325, 303, 225, 853),
    ('pnbk', 'Patriot National Bancorp Inc', 'Banking', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'B', 'Medium', 205, 302, 210, 717),
    ('payx', 'Paychex Inc', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 500, 300, 200, 1000),
    ('payc', 'Paycom Software Inc', 'Technology', 'NEW YORK STOCK EXCHANGE, INC.', 'BBB', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 470, 305, 315, 1090),
    ('pypl', 'PayPal Holdings Inc', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 370, 244, 285, 899),
    ('penn', 'PENN Entertainment Inc', 'Hotels Restaurants and Leisure', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 371, 300, 220, 891),
    ('pntg', 'Pennant Group Inc', 'Health Care', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 245, 306, 200, 751),
    ('pnr', 'Pentair PLC', 'Machinery', 'NEW YORK STOCK EXCHANGE, INC.', 'BBB', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 433, 330, 315, 1078),
    ('pep', 'PepsiCo Inc', 'Beverages', 'NASDAQ NMS - GLOBAL MARKET', 'AA', 'Excellent', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 719, 340, 358, 1417),
    ('prdo', 'Perdoceo Education Corp', 'Diversified Consumer Services', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'B', 'Medium', 'B', 'Medium', 'BBB', 'High', 365, 297, 250, 912),
    ('pki', 'PerkinElmer Inc', 'Life Sciences Tools and Services', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 515, 316, 325, 1156),
    ('ppih', 'Perma-Pipe International Holdings Inc', 'Machinery', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'B', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 260, 300, 1060),
    ('pfe', 'Pfizer Inc', 'Pharmaceuticals', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 300, 300, 1100),
    ('pmcb', 'PharmaCyte Biotech Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 220, 202, 300, 722),
    ('pm', 'Philip Morris International Inc', 'Tobacco', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 520, 327, 315, 1162),
    ('psx', 'Phillips 66', 'Energy', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 569, 363, 310, 1242),
    ('ppc', 'Pilgrims Pride Corp', 'Food Products', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 500, 302, 220, 1022),
    ('pnfp', 'Pinnacle Financial Partners Inc', 'Banking', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 271, 328, 250, 849),
    ('pnw', 'Pinnacle West Capital Corp', 'Utilities', 'NEW YORK STOCK EXCHANGE, INC.', 'AA', 'Excellent', 'BBB', 'High', 'BB', 'Medium', 'A', 'High', 629, 479, 300, 1408),
    ('pxd', 'Pioneer Natural Resources Co', 'Energy', 'NEW YORK STOCK EXCHANGE, INC.', 'AA', 'Excellent', 'BBB', 'High', 'BB', 'Medium', 'A', 'High', 700, 412, 300, 1412),
    ('ppsi', 'Pioneer Power Solutions Inc', 'Electrical Equipment', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 299, 305, 315, 919),
    ('plya', 'Playa Hotels & Resorts NV', 'Hotels Restaurants and Leisure', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 210, 200, 205, 615),
    ('myps', 'Playstudios Inc', 'Media', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 205, 202, 200, 607),
    ('plxs', 'Plexus Corp', 'Electrical Equipment', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 510, 300, 300, 1110),
    ('pnc', 'PNC Financial Services Group Inc', 'Banking', 'NEW YORK STOCK EXCHANGE, INC.', 'BBB', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 455, 323, 300, 1078),
    ('pnt', 'POINT Biopharma Global Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 320, 221, 285, 826),
    ('pola', 'Polar Power Inc', 'Electrical Equipment', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 200, 200, 200, 600),
    ('pool', 'Pool Corp', 'Distributors', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 525, 306, 313, 1144),
    ('prch', 'Porch Group Inc', 'Retail', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 225, 227, 215, 667),
    ('powl', 'Powell Industries Inc', 'Electrical Equipment', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'B', 'Medium', 'B', 'Medium', 'BBB', 'High', 500, 240, 215, 955),
    ('powi', 'Power Integrations Inc', 'Semiconductors', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'B', 'Medium', 'BB', 'Medium', 'BBB', 'High', 575, 285, 305, 1165),
    ('pow', 'Powered Brands', 'N/A', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 235, 231, 250, 716),
    ('ppg', 'PPG Industries Inc', 'Chemicals', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 293, 236, 220, 749),
    ('ppl', 'PPL Corp', 'Utilities', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 525, 306, 300, 1131),
    ('praa', 'PRA Group Inc', 'Financial Services', 'NASDAQ NMS - GLOBAL MARKET', 'BBB', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 473, 321, 310, 1104),
    ('prax', 'Praxis Precision Medicines Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 200, 215, 215, 630),
    ('poai', 'Predictive Oncology Inc', 'Health Care', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 278, 297, 220, 795),
    ('pnrg', 'Primeenergy Resources Corp', 'Energy', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 200, 200, 260, 660),
    ('pfg', 'Principal Financial Group Inc', 'Insurance', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 555, 320, 300, 1175),
    ('prct', 'Procept Biorobotics Corp', 'Health Care', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 200, 224, 300, 724),
    ('pg', 'Procter & Gamble Co', 'Consumer products', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BBB', 'High', 'BB', 'Medium', 'A', 'High', 560, 422, 310, 1292),
    ('pgr', 'Progressive Corp', 'Insurance', 'NEW YORK STOCK EXCHANGE, INC.', 'BB', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 350, 355, 270, 975),
    ('pld', 'Prologis Inc', 'Real Estate', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 579, 374, 315, 1268),
    ('pru', 'Prudential Financial Inc', 'Insurance', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 285, 300, 288, 873),
    ('ptc', 'PTC Inc', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 550, 302, 308, 1160),
    ('peg', 'Public Service Enterprise Group Inc', 'Utilities', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 500, 300, 205, 1005),
    ('psa', 'Public Storage', 'Real Estate', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 235, 245, 205, 685),
    ('phm', 'Pultegroup Inc', 'Consumer products', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 215, 203, 240, 658),
    ('pvh', 'PVH Corp', 'Textiles Apparel and Luxury Goods', 'NEW YORK STOCK EXCHANGE, INC.', 'BBB', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 418, 319, 315, 1052),
    ('qrvo', 'Qorvo Inc', 'Semiconductors', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 535, 310, 305, 1150),
    ('qcom', 'Qualcomm Inc', 'Semiconductors', 'NASDAQ NMS - GLOBAL MARKET', 'BBB', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 409, 300, 300, 1009),
    ('pwr', 'Quanta Services Inc', 'Construction', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 540, 382, 310, 1232),
    ('dgx', 'Quest Diagnostics Inc', 'Health Care', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'B', 'Medium', 230, 300, 205, 735),
    ('rl', 'Ralph Lauren Corp', 'Textiles Apparel and Luxury Goods', 'NEW YORK STOCK EXCHANGE, INC.', 'BBB', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 420, 352, 303, 1075),
    ('rjf', 'Raymond James Financial Inc', 'Financial Services', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 505, 309, 305, 1119),
    ('rtx', 'Raytheon Technologies Corp', 'Aerospace and Defense', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BBB', 'High', 'A', 'High', 520, 330, 400, 1250),
    ('o', 'Realty Income Corp', 'Real Estate', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 300, 300, 1100),
    ('reg', 'Regency Centers Corp', 'Real Estate', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 575, 372, 365, 1312),
    ('regn', 'Regeneron Pharmaceuticals Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 505, 327, 305, 1137),
    ('rf', 'Regions Financial Corp', 'Banking', 'NEW YORK STOCK EXCHANGE, INC.', 'BBB', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 490, 304, 305, 1099),
    ('rsg', 'Republic Services Inc', 'Commercial Services and Supplies', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 293, 235, 216, 744),
    ('rmd', 'Resmed Inc', 'Health Care', 'NEW YORK STOCK EXCHANGE, INC.', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 330, 312, 300, 942),
    ('rhi', 'Robert Half International Inc', 'Professional Services', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 255, 334, 310, 899),
    ('rok', 'Rockwell Automation Inc', 'Electrical Equipment', 'NEW YORK STOCK EXCHANGE, INC.', 'BB', 'Medium', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 308, 243, 210, 761),
    ('rol', 'Rollins Inc', 'Commercial Services and Supplies', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 300, 305, 1105),
    ('rop', 'Roper Technologies Inc', 'Technology', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 570, 350, 340, 1260),
    ('rost', 'Ross Stores Inc', 'Retail', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 375, 325, 300, 1000),
    ('rcl', 'Royal Caribbean Cruises Ltd', 'Hotels Restaurants and Leisure', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 503, 327, 310, 1140),
    ('spgi', 'S&P Global Inc', 'Financial Services', 'NEW YORK STOCK EXCHANGE, INC.', 'BBB', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 435, 341, 310, 1086),
    ('crm', 'Salesforce Inc', 'Technology', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 215, 241, 200, 656),
    ('sbac', 'SBA Communications Corp', 'Real Estate', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 250, 251, 215, 716),
    ('sj', 'Scienjoy Holding Corp', 'Media', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 260, 320, 240, 820),
    ('stx', 'Seagate Technology Holdings PLC', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 540, 355, 300, 1195),
    ('see', 'Sealed Air Corp', 'Packaging', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 555, 318, 257, 1130),
    ('ship', 'Seanergy Maritime Holdings Corp', 'Marine', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 345, 300, 305, 950),
    ('sre', 'Sempra Energy', 'Utilities', 'NEW YORK STOCK EXCHANGE, INC.', 'AA', 'Excellent', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 700, 386, 310, 1396),
    ('aihs', 'Senmiao Technology Ltd', 'Financial Services', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 220, 203, 200, 623),
    ('now', 'ServiceNow Inc', 'Technology', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 550, 374, 350, 1274),
    ('shw', 'Sherwin-Williams Co', 'Chemicals', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 295, 259, 220, 774),
    ('sisi', 'Shineco Inc', 'Consumer products', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 340, 346, 305, 991),
    ('shls', 'Shoals Technologies Group Inc', 'Electrical Equipment', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 285, 280, 300, 865),
    ('shyf', 'Shyft Group Inc', 'Machinery', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 510, 303, 275, 1088),
    ('sibn', 'SI-BONE Inc', 'Health Care', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 220, 228, 210, 658),
    ('sieb', 'Siebert Financial Corp', 'Financial Services', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 300, 299, 235, 834),
    ('sien', 'Sientra Inc', 'Health Care', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 219, 308, 236, 763),
    ('spg', 'Simon Property Group Inc', 'Real Estate', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 225, 247, 205, 677),
    ('siri', 'Sirius XM Holdings Inc', 'Media', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'B', 'Medium', 240, 302, 205, 747),
    ('sitm', 'SiTime Corp', 'Semiconductors', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 505, 304, 300, 1109),
    ('swks', 'Skyworks Solutions Inc', 'Semiconductors', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 515, 303, 270, 1088),
    ('sna', 'Snap-On Inc', 'Machinery', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 500, 300, 261, 1061),
    ('so', 'Southern Co', 'Utilities', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 515, 307, 330, 1152),
    ('luv', 'Southwest Airlines Co', 'Airlines', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 295, 314, 218, 827),
    ('spr', 'Spirit AeroSystems Holdings Inc', 'Aerospace and Defense', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 515, 337, 300, 1152),
    ('akic', 'Sports Ventures Acquisition Corp', 'N/A', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 200, 205, 230, 635),
    ('spot', 'Spotify Technology SA', 'Media', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'B', 'Medium', 'B', 'Medium', 'BBB', 'High', 500, 283, 255, 1038),
    ('swk', 'Stanley Black & Decker Inc', 'Machinery', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 555, 315, 300, 1170),
    ('sbux', 'Starbucks Corp', 'Hotels Restaurants and Leisure', 'NASDAQ NMS - GLOBAL MARKET', 'BBB', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 475, 385, 295, 1155),
    ('stt', 'State Street Corp', 'Financial Services', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 225, 211, 210, 646),
    ('ste', 'STERIS plc', 'Health Care', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 510, 301, 305, 1116),
    ('shoo', 'Steven Madden Ltd', 'Textiles Apparel and Luxury Goods', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'B', 'Medium', 'BB', 'Medium', 'BBB', 'High', 508, 231, 300, 1039),
    ('syk', 'Stryker Corp', 'Health Care', 'NEW YORK STOCK EXCHANGE, INC.', 'BBB', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 485, 321, 325, 1131),
    ('sivb', 'SVB Financial Group', 'Banking', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 510, 340, 300, 1150),
    ('syf', 'Synchrony Financial', 'Financial Services', 'NEW YORK STOCK EXCHANGE, INC.', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 325, 312, 310, 947),
    ('snps', 'Synopsys Inc', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 525, 316, 315, 1156),
    ('syy', 'Sysco Corp', 'Retail', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 555, 301, 305, 1161),
    ('trow', 'T Rowe Price Group Inc', 'Financial Services', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 510, 325, 310, 1145),
    ('tmus', 'T-Mobile US Inc', 'Telecommunication', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 342, 331, 230, 903),
    ('ttwo', 'Take-Two Interactive Software Inc', 'Media', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 225, 307, 310, 842),
    ('tpr', 'Tapestry Inc', 'Textiles Apparel and Luxury Goods', 'NEW YORK STOCK EXCHANGE, INC.', 'BBB', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 483, 310, 300, 1093),
    ('tgt', 'Target Corp', 'Retail', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 550, 342, 313, 1205),
    ('tel', 'TE Connectivity Ltd', 'Electrical Equipment', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 200, 200, 200, 600),
    ('tdy', 'Teledyne Technologies Inc', 'Electrical Equipment', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 300, 300, 1100),
    ('tfx', 'Teleflex Inc', 'Health Care', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 200, 200, 200, 600),
    ('ter', 'Teradyne Inc', 'Semiconductors', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 507, 328, 315, 1150),
    ('tsla', 'Tesla Inc', 'Automobiles', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'CCC', 'Low', 'B', 'Medium', 'BBB', 'High', 555, 160, 278, 993),
    ('txn', 'Texas Instruments Inc', 'Semiconductors', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 300, 300, 1100),
    ('txt', 'Textron Inc', 'Aerospace and Defense', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 500, 300, 200, 1000),
    ('tmo', 'Thermo Fisher Scientific Inc', 'Life Sciences Tools and Services', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 527, 332, 280, 1139),
    ('tjx', 'TJX Companies Inc', 'Retail', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 300, 300, 1100),
    ('trtx', 'TPG RE Finance Trust Inc', 'Real Estate', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 230, 239, 300, 769),
    ('tsco', 'Tractor Supply Co', 'Retail', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 500, 300, 200, 1000),
    ('tt', 'Trane Technologies PLC', 'Building', 'NEW YORK STOCK EXCHANGE, INC.', 'AA', 'Excellent', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 700, 389, 320, 1409),
    ('tdg', 'TransDigm Group Inc', 'Aerospace and Defense', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 300, 300, 1100),
    ('tru', 'TransUnion', 'Professional Services', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 510, 313, 310, 1133),
    ('trv', 'Travelers Companies Inc', 'Insurance', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 300, 300, 1100),
    ('trmb', 'Trimble Inc', 'Electrical Equipment', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BBB', 'High', 'BB', 'Medium', 'A', 'High', 550, 415, 315, 1280),
    ('trtn', 'Triton International Ltd', 'Trading Companies and Distributors', 'NEW YORK STOCK EXCHANGE, INC.', 'BBB', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 477, 306, 300, 1083),
    ('trox', 'Tronox Holdings PLC', 'Chemicals', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 503, 320, 300, 1123),
    ('tfc', 'Truist Financial Corp', 'Banking', 'NEW YORK STOCK EXCHANGE, INC.', 'BBB', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 480, 308, 300, 1088),
    ('tyl', 'Tyler Technologies Inc', 'Technology', 'NEW YORK STOCK EXCHANGE, INC.', 'BBB', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 400, 306, 305, 1011),
    ('tsn', 'Tyson Foods Inc', 'Food Products', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 530, 374, 340, 1244),
    ('udr', 'UDR Inc', 'Real Estate', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'B', 'Medium', 225, 301, 215, 741),
    ('ulta', 'Ulta Beauty Inc', 'Retail', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 205, 242, 200, 647),
    ('unp', 'Union Pacific Corp', 'Road and Rail', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 290, 257, 245, 792),
    ('ual', 'United Airlines Holdings Inc', 'Airlines', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 205, 203, 221, 629),
    ('ups', 'United Parcel Service Inc', 'Logistics and Transportation', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 540, 374, 245, 1159),
    ('uri', 'United Rentals Inc', 'Trading Companies and Distributors', 'NEW YORK STOCK EXCHANGE, INC.', 'BBB', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 472, 318, 300, 1090),
    ('uslm', 'United States Lime & Minerals Inc', 'Construction', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'B', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 233, 300, 1033),
    ('x', 'United States Steel Corp', 'Metals and Mining', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 535, 364, 300, 1199),
    ('uthr', 'United Therapeutics Corp', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 233, 259, 300, 792),
    ('unh', 'UnitedHealth Group Inc', 'Health Care', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 300, 300, 1100),
    ('uhs', 'Universal Health Services Inc', 'Health Care', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 560, 320, 338, 1218),
    ('usap', 'Universal Stainless & Alloy Products Inc', 'Metals and Mining', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 238, 231, 200, 669),
    ('uvsp', 'Univest Financial Corp', 'Banking', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 331, 322, 305, 958),
    ('upwk', 'Upwork Inc', 'Professional Services', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 275, 264, 278, 817),
    ('urbn', 'Urban Outfitters Inc', 'Retail', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 335, 300, 300, 935),
    ('urgn', 'Urogen Pharma Ltd', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 210, 251, 290, 751),
    ('usb', 'US Bancorp', 'Banking', 'NEW YORK STOCK EXCHANGE, INC.', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 336, 317, 300, 953),
    ('useg', 'US Energy Corp', 'Energy', 'NASDAQ NMS - GLOBAL MARKET', 'BBB', 'High', 'B', 'Medium', 'BB', 'Medium', 'BBB', 'High', 438, 265, 315, 1018),
    ('usau', 'US Gold Corp', 'Metals and Mining', 'NASDAQ NMS - GLOBAL MARKET', 'BBB', 'High', 'B', 'Medium', 'BB', 'Medium', 'BBB', 'High', 400, 240, 300, 940),
    ('usak', 'USA Truck Inc', 'Road and Rail', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 532, 311, 303, 1146),
    ('usio', 'Usio Inc', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 285, 245, 240, 770),
    ('utmd', 'Utah Medical Products Inc', 'Health Care', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 240, 236, 250, 726),
    ('utme', 'Utime Ltd', 'Electrical Equipment', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 217, 200, 200, 617),
    ('utsi', 'UTStarcom Holdings Corp', 'Communications', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 340, 310, 365, 1015),
    ('uxin', 'Uxin Ltd', 'Retail', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 203, 202, 225, 630),
    ('vlo', 'Valero Energy Corp', 'Energy', 'NEW YORK STOCK EXCHANGE, INC.', 'AA', 'Excellent', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 608, 307, 330, 1245),
    ('vtr', 'Ventas Inc', 'Real Estate', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 300, 300, 1100),
    ('vrsn', 'Verisign Inc', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 548, 354, 325, 1227),
    ('vrsk', 'Verisk Analytics Inc', 'Professional Services', 'NASDAQ NMS - GLOBAL MARKET', 'AA', 'Excellent', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 615, 366, 300, 1281),
    ('vrtx', 'Vertex Pharmaceuticals Inc', 'Biotechnology', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 300, 300, 1100),
    ('vfc', 'VF Corp', 'Textiles Apparel and Luxury Goods', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 505, 301, 300, 1106),
    ('vtrs', 'Viatris Inc', 'Pharmaceuticals', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 500, 300, 200, 1000),
    ('v', 'Visa Inc', 'Technology', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 504, 368, 310, 1182),
    ('vno', 'Vornado Realty Trust', 'Real Estate', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 540, 326, 325, 1191),
    ('vmc', 'Vulcan Materials Co', 'Construction', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 570, 319, 300, 1189),
    ('wrb', 'W R Berkley Corp', 'Insurance', 'NEW YORK STOCK EXCHANGE, INC.', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BBB', 'High', 360, 294, 300, 954),
    ('wba', 'Walgreens Boots Alliance Inc', 'Retail', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 515, 325, 300, 1140),
    ('wmt', 'Walmart Inc', 'Retail', 'NEW YORK STOCK EXCHANGE, INC.', 'BB', 'Medium', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 310, 281, 220, 811),
    ('dis', 'Walt Disney Co', 'Media', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 510, 316, 321, 1147),
    ('hcc', 'Warrior Met Coal Inc', 'Metals & Mining', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 215, 200, 200, 615),
    ('wm', 'Waste Management Inc', 'Commercial Services and Supplies', 'NEW YORK STOCK EXCHANGE, INC.', 'AA', 'Excellent', 'BBB', 'High', 'B', 'Medium', 'A', 'High', 613, 408, 285, 1306),
    ('wat', 'Waters Corp', 'Life Sciences Tools and Services', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 270, 292, 235, 797),
    ('wts', 'Watts Water Technologies Inc', 'Machinery', 'NEW YORK STOCK EXCHANGE, INC.', 'BBB', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 420, 303, 210, 933),
    ('wec', 'WEC Energy Group Inc', 'Utilities', 'NEW YORK STOCK EXCHANGE, INC.', 'AA', 'Excellent', 'BBB', 'High', 'BB', 'Medium', 'A', 'High', 635, 438, 300, 1373),
    ('wfc', 'Wells Fargo & Co', 'Banking', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 300, 300, 1100),
    ('well', 'Welltower OP LLC', 'Real Estate', 'NEW YORK STOCK EXCHANGE, INC.', 'BBB', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 437, 326, 300, 1063),
    ('wst', 'West Pharmaceutical Services Inc', 'Life Sciences Tools and Services', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 540, 330, 305, 1175),
    ('wdc', 'Western Digital Corp', 'Technology', 'NASDAQ NMS - GLOBAL MARKET', 'A', 'High', 'BB', 'Medium', 'B', 'Medium', 'BBB', 'High', 545, 339, 260, 1144),
    ('wu', 'Western Union Co', 'Technology', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 205, 205, 228, 638),
    ('wab', 'Westinghouse Air Brake Technologies Corp', 'Machinery', 'NEW YORK STOCK EXCHANGE, INC.', 'AA', 'Excellent', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 607, 311, 320, 1238),
    ('wrk', 'Westrock Co', 'Packaging', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 555, 324, 305, 1184),
    ('wy', 'Weyerhaeuser Co', 'Real Estate', 'NEW YORK STOCK EXCHANGE, INC.', 'AA', 'Excellent', 'BB', 'Medium', 'BB', 'Medium', 'A', 'High', 700, 340, 300, 1340),
    ('whr', 'Whirlpool Corp', 'Consumer products', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 301, 300, 1101),
    ('wmb', 'Williams Companies Inc', 'Energy', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 300, 300, 1100),
    ('www', 'Wolverine World Wide Inc', 'Textiles Apparel and Luxury Goods', 'NEW YORK STOCK EXCHANGE, INC.', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BBB', 'High', 390, 298, 308, 996),
    ('wwe', 'World Wrestling Entertainment Inc', 'Media', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 275, 332, 315, 922),
    ('gww', 'WW Grainger Inc', 'Trading Companies and Distributors', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 255, 385, 240, 880),
    ('wynn', 'Wynn Resorts Ltd', 'Hotels Restaurants and Leisure', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 225, 201, 200, 626),
    ('xyf', 'X Financial', 'Financial Services', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 215, 205, 200, 620),
    ('xel', 'Xcel Energy Inc', 'Utilities', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 223, 201, 205, 629),
    ('xhr', 'Xenia Hotels & Resorts Inc', 'Real Estate', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 260, 263, 236, 759),
    ('xin', 'Xinyuan Real Estate Co Ltd', 'Real Estate', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'B', 'Medium', 205, 242, 300, 747),
    ('xl', 'XL Fleet Corp', 'Auto Components', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 200, 200, 200, 600),
    ('xpev', 'Xpeng Inc', 'Automobiles', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 215, 208, 200, 623),
    ('xpo', 'XPO Logistics Inc', 'Road and Rail', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 560, 318, 300, 1178),
    ('xyl', 'Xylem Inc', 'Machinery', 'NEW YORK STOCK EXCHANGE, INC.', 'BB', 'Medium', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 374, 254, 210, 838),
    ('yala', 'Yalla Group Ltd', 'Media', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 233, 244, 220, 697),
    ('ysg', 'Yatsen Holding Ltd', 'Consumer products', 'NEW YORK STOCK EXCHANGE, INC.', 'BB', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 355, 217, 325, 897),
    ('yelp', 'Yelp Inc', 'Media', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'A', 'High', 'B', 'Medium', 'BBB', 'High', 245, 515, 213, 973),
    ('yeti', 'Yeti Holdings Inc', 'Leisure Products', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 269, 253, 305, 827),
    ('yext', 'Yext Inc', 'Technology', 'NEW YORK STOCK EXCHANGE, INC.', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 325, 314, 310, 949),
    ('yrd', 'Yiren Digital Ltd', 'Financial Services', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 200, 205, 205, 610),
    ('yumc', 'Yum China Holdings Inc', 'Hotels Restaurants and Leisure', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 205, 217, 220, 642),
    ('yum', 'Yum! Brands Inc', 'Hotels Restaurants and Leisure', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 320, 310, 1130),
    ('zbra', 'Zebra Technologies Corp', 'Electrical Equipment', 'NASDAQ NMS - GLOBAL MARKET', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 320, 317, 300, 937),
    ('zen', 'Zendesk Inc', 'Technology', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 515, 338, 320, 1173),
    ('zepp', 'Zepp Health Corp', 'Electrical Equipment', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 202, 210, 295, 707),
    ('zim', 'ZIM Integrated Shipping Services Ltd', 'Marine', 'NEW YORK STOCK EXCHANGE, INC.', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 329, 351, 320, 1000),
    ('zbh', 'Zimmer Biomet Holdings Inc', 'Health Care', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 520, 330, 310, 1160),
    ('zion', 'Zions Bancorporation NA', 'Banking', 'NASDAQ NMS - GLOBAL MARKET', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 200, 200, 200, 600),
    ('zts', 'Zoetis Inc', 'Pharmaceuticals', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 520, 348, 310, 1178),
    ('zuo', 'Zuora Inc', 'Technology', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 'B', 'Medium', 240, 234, 200, 674),
    ('zws', 'Zurn Elkay Water Solutions Corp', 'Building', 'NEW YORK STOCK EXCHANGE, INC.', 'A', 'High', 'BB', 'Medium', 'BB', 'Medium', 'BBB', 'High', 500, 300, 300, 1100),
    ('zyme', 'Zymeworks Inc', 'Biotechnology', 'NEW YORK STOCK EXCHANGE, INC.', 'B', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 'BB', 'Medium', 240, 326, 305, 871),
]


# -------------------------------------------------
# Recommendation data
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

# -------------------------------------------------
# Session state
# -------------------------------------------------
def init_session_state() -> None:
    defaults = {
        "current_view": "home",
        "show_splash": True,
        "show_recommendation_popup": False,
        "show_builder_popup": False,
        "rec_investment_priority": "Prioritise sustainability",
        "rec_risk_tolerance": 5,
        "rec_esg_aspect": "All Equal",
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
        "builder_risk_free_rate_touched": False,
        "builder_risk_tolerance": 5,
        "builder_esg_importance": "Somewhat important",
        "builder_esg_slider": 0.05,
        "company_search_query": "",
        "selected_company_option": "",
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


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


def mark_builder_risk_free_rate_touched() -> None:
    st.session_state.builder_risk_free_rate_touched = True


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
                --primary: #14532d;
                --primary2: #166534;
                --primary3: #15803d;
                --primary4: #22c55e;
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
                width: 58px;
                height: 58px;
                border-radius: 18px;
                background: linear-gradient(135deg, var(--primary), var(--primary4));
                display: flex;
                align-items: center;
                justify-content: center;
                box-shadow: 0 14px 30px rgba(22,163,74,0.24);
            }

            .logo-box svg,
            .splash-logo svg {
                width: 68%;
                height: 68%;
                display: block;
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

            .interpretation-card {
                background: linear-gradient(145deg, rgba(255,255,255,0.99), rgba(244,252,247,0.97));
                border: 1px solid rgba(22,101,52,0.12);
                border-radius: 20px;
                padding: 1.08rem 1.12rem;
                box-shadow: 0 14px 34px rgba(20,83,45,0.07);
                margin-top: 0.55rem;
            }

            .interpretation-title {
                color: #0b1c15;
                font-size: 1.02rem;
                font-weight: 900;
                letter-spacing: -0.01em;
                margin: 0;
            }

            .interpretation-subtitle {
                color: #567164;
                font-size: 0.82rem;
                line-height: 1.5;
                margin: 0.24rem 0 0 0;
            }

            .analysis-grid {
                display: grid;
                grid-template-columns: repeat(3, minmax(0, 1fr));
                gap: 0.75rem;
                margin: 0.9rem 0 0.95rem 0;
            }

            .analysis-pill {
                background: rgba(255,255,255,0.92);
                border: 1px solid rgba(22,101,52,0.09);
                border-radius: 16px;
                padding: 0.78rem 0.82rem;
                box-shadow: inset 0 1px 0 rgba(255,255,255,0.80);
            }

            .analysis-pill-label {
                color: #5b7468;
                font-size: 0.76rem;
                font-weight: 800;
                letter-spacing: 0.03em;
                text-transform: uppercase;
                margin: 0;
            }

            .analysis-pill-value {
                color: #0f2a1f;
                font-size: 0.98rem;
                font-weight: 850;
                line-height: 1.35;
                margin: 0.25rem 0 0 0;
            }

            .interpretation-copy {
                color: #2f4f43;
                font-size: 0.91rem;
                line-height: 1.68;
                margin: 0;
            }

            .interpretation-copy strong {
                color: #163f2b;
                font-weight: 800;
            }

            .interpretation-copy + .interpretation-copy {
                margin-top: 0.58rem;
            }

            .interpretation-divider {
                height: 1px;
                background: rgba(22,101,52,0.10);
                margin: 0.9rem 0 0.9rem 0;
                border-radius: 999px;
            }

            .allocation-summary {
                background: linear-gradient(145deg, rgba(255,255,255,0.99), rgba(238,248,241,0.96));
                border: 1px solid rgba(22,101,52,0.10);
                border-radius: 20px;
                padding: 1rem 1.05rem;
                box-shadow: 0 12px 28px rgba(20,83,45,0.06);
            }

            .allocation-summary-label {
                color: #5b7468;
                font-size: 0.75rem;
                font-weight: 800;
                letter-spacing: 0.05em;
                text-transform: uppercase;
                margin: 0;
            }

            .allocation-summary-title {
                color: #0b1c15;
                font-size: 1.1rem;
                font-weight: 900;
                letter-spacing: -0.02em;
                line-height: 1.3;
                margin: 0.22rem 0 0 0;
            }

            .allocation-summary-copy {
                color: #36574a;
                font-size: 0.9rem;
                line-height: 1.58;
                margin: 0.38rem 0 0 0;
            }

            .allocation-chip-row {
                display: flex;
                gap: 0.55rem;
                flex-wrap: wrap;
                margin-top: 0.85rem;
            }

            .allocation-chip {
                background: rgba(255,255,255,0.96);
                border: 1px solid rgba(22,101,52,0.10);
                border-radius: 999px;
                padding: 0.42rem 0.72rem;
                color: #163f2b;
                font-size: 0.84rem;
                font-weight: 700;
                box-shadow: inset 0 1px 0 rgba(255,255,255,0.82);
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

            .tooltip-details {
                position: relative;
                display: inline-block;
                margin: 0;
            }

            .tooltip-details summary {
                list-style: none;
            }

            .tooltip-details summary::-webkit-details-marker {
                display: none;
            }

            .tooltip-icon {
                display: inline-flex;
                align-items: center;
                justify-content: center;
                width: 18px;
                height: 18px;
                border-radius: 999px;
                border: 1px solid rgba(22,101,52,0.18);
                font-size: 0.72rem;
                font-weight: 800;
                color: #166534;
                background: rgba(22,163,74,0.06);
                cursor: pointer;
                line-height: 1;
                transition: all 0.18s ease;
            }

            .tooltip-details[open] .tooltip-icon {
                background: rgba(22,163,74,0.14);
                border-color: rgba(22,101,52,0.30);
                box-shadow: 0 8px 18px rgba(20,83,45,0.12);
            }

            .tooltip-bubble {
                position: absolute;
                top: calc(100% + 0.45rem);
                left: 0;
                min-width: 220px;
                max-width: 280px;
                padding: 0.72rem 0.78rem;
                background: #ffffff;
                border: 1px solid rgba(22,101,52,0.12);
                border-radius: 14px;
                color: #2f4f43;
                font-size: 0.83rem;
                line-height: 1.5;
                box-shadow: 0 16px 36px rgba(20,83,45,0.14);
                z-index: 50;
            }

            .home-cta-shell {
                text-align: center;
                max-width: 860px;
                margin: 0 auto 0.75rem auto;
            }

            .home-cta-note {
                color: var(--muted);
                font-size: 1.02rem;
                line-height: 1.72;
                margin: 0.6rem 0 0 0;
            }

            .home-button-spacer {
                height: 0.9rem;
            }

            .st-key-home_recommendation_button button,
            .st-key-home_builder_button button {
                min-height: 11.2rem !important;
                border-radius: 28px !important;
                font-size: 1.55rem !important;
                font-weight: 760 !important;
                line-height: 1.24 !important;
                padding: 1.9rem 1.25rem !important;
                text-align: center !important;
                box-shadow: 0 20px 38px rgba(20,83,45,0.18) !important;
                white-space: normal !important;
            }

            .st-key-home_recommendation_button button:hover,
            .st-key-home_builder_button button:hover {
                transform: translateY(-2px) !important;
                box-shadow: 0 24px 44px rgba(20,83,45,0.22) !important;
            }

            .st-key-home_recommendation_button button p,
            .st-key-home_builder_button button p,
            .st-key-home_recommendation_button button span,
            .st-key-home_builder_button button span,
            .st-key-home_recommendation_button button div,
            .st-key-home_builder_button button div {
                font-size: 1.55rem !important;
                font-weight: 760 !important;
                line-height: 1.24 !important;
                text-align: center !important;
                white-space: normal !important;
                word-break: keep-all !important;
            }

            .home-overview-panel {
                background: linear-gradient(150deg, rgba(255,255,255,0.99), rgba(243,252,246,0.97));
                border: 1px solid rgba(22,101,52,0.10);
                border-radius: 24px;
                padding: 1.25rem 1.2rem;
                box-shadow: 0 16px 36px rgba(20,83,45,0.08);
                min-height: 100%;
            }

            .home-overview-eyebrow {
                color: var(--primary);
                font-size: 0.8rem;
                font-weight: 800;
                letter-spacing: 0.08em;
                text-transform: uppercase;
                margin-bottom: 0.45rem;
            }

            .home-overview-title {
                color: var(--text);
                font-size: 1.22rem;
                font-weight: 850;
                letter-spacing: -0.03em;
                line-height: 1.2;
                margin: 0 0 0.55rem 0;
            }

            .home-overview-copy {
                color: var(--muted);
                font-size: 0.95rem;
                line-height: 1.72;
                margin: 0;
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
                min-height: 4.15rem !important;
                border-radius: 18px !important;
                font-weight: 800 !important;
                font-size: 1.10rem !important;
                padding: 0.45rem 1.05rem !important;
                border: 1px solid var(--primary) !important;
                background: linear-gradient(135deg, #5b21b6, #7c3aed) !important;
                color: #ffffff !important;
                box-shadow: 0 10px 22px rgba(20,83,45,0.18) !important;
                transition: all 0.18s ease !important;
            }

            div.stButton > button:hover,
            div[data-testid="stFormSubmitButton"] > button:hover {
                background: linear-gradient(135deg, #991b1b, #dc2626) !important;
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
                width: 104px;
                height: 104px;
                border-radius: 30px;
                background: linear-gradient(135deg, var(--primary), var(--primary4));
                margin: 0 auto 1.15rem auto;
                display: flex;
                align-items: center;
                justify-content: center;
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
            [data-baseweb="textarea"] textarea,
            [data-baseweb="select"] input,
            [data-baseweb="select"] div,
            [data-baseweb="select"] span {
                color: #000000 !important;
                -webkit-text-fill-color: #000000 !important;
                background: #ffffff !important;
            }

            div[data-baseweb="input"],
            div[data-baseweb="select"] {
                background: #ffffff !important;
                border-radius: 12px !important;
                border: 1px solid rgba(22,101,52,0.12) !important;
                box-shadow: none !important;
            }

            div[data-baseweb="select"] > div {
                background: #ffffff !important;
                color: #000000 !important;
            }

            div[data-baseweb="input"]:focus-within,
            div[data-baseweb="select"]:focus-within,
            [data-testid="stTextInput"] > div:focus-within,
            [data-testid="stNumberInput"] > div:focus-within,
            [data-testid="stSelectbox"] > div:focus-within {
                border: 1px solid rgba(21, 128, 61, 0.55) !important;
                box-shadow: 0 0 0 0.14rem rgba(21, 128, 61, 0.14) !important;
                outline: none !important;
                background: #ffffff !important;
            }

            [data-baseweb="input"] input:focus,
            [data-baseweb="input"] input:active,
            [data-baseweb="select"] input:focus,
            [data-baseweb="select"] input:active,
            [data-baseweb="select"] div:focus,
            [data-baseweb="select"] div:active {
                box-shadow: none !important;
                outline: none !important;
                border-color: transparent !important;
                background: #ffffff !important;
                color: #000000 !important;
                -webkit-text-fill-color: #000000 !important;
            }

            div[data-baseweb="popover"],
            div[data-baseweb="popover"] * {
                background: #ffffff !important;
                color: #000000 !important;
                -webkit-text-fill-color: #000000 !important;
            }

            div[data-baseweb="popover"] {
                border: 1px solid rgba(22,101,52,0.12) !important;
                border-radius: 14px !important;
                box-shadow: 0 14px 30px rgba(20,83,45,0.12) !important;
                overflow: hidden !important;
            }

            div[data-baseweb="popover"] ul,
            div[data-baseweb="popover"] [role="listbox"] {
                background: #ffffff !important;
            }

            div[data-baseweb="popover"] li,
            div[data-baseweb="popover"] [role="option"] {
                background: #ffffff !important;
                color: #000000 !important;
            }

            div[data-baseweb="popover"] li:hover,
            div[data-baseweb="popover"] [role="option"]:hover,
            div[data-baseweb="popover"] li[aria-selected="true"],
            div[data-baseweb="popover"] [role="option"][aria-selected="true"] {
                background: #f3fbf6 !important;
                color: #000000 !important;
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
                <div class="splash-logo">{LEAF_LOGO_SVG}</div>
                <div class="splash-title">{APP_NAME}</div>
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


def escape_html_text(value: str) -> str:
    return (
        str(value)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('\"', "&quot;")
        .replace("'", "&#39;")
    )


def click_tooltip_html(tooltip: str) -> str:
    safe_tooltip = escape_html_text(tooltip)
    return f"""
    <details class=\"tooltip-details\">
        <summary class=\"tooltip-icon\">i</summary>
        <div class=\"tooltip-bubble\">{safe_tooltip}</div>
    </details>
    """


def render_label_with_tooltip(text: str, tooltip: str) -> None:
    st.markdown(
        f'<div class="field-label">{text} {click_tooltip_html(tooltip)}</div>',
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
        tooltip_html = click_tooltip_html(tooltip)
    return f"""
    <div class="metric-tile">
        <div class="metric-tile-label">{label} {tooltip_html}</div>
        <div class="metric-tile-value">{value}</div>
    </div>
    """


def allocation_summary_html(asset1: str, weight1: float, asset2: str, weight2: float) -> str:
    return f"""
    <div class="allocation-summary">
        <p class="allocation-summary-label">Recommended Allocation</p>
        <p class="allocation-summary-title">{asset1}: {weight1:.2%} &nbsp;•&nbsp; {asset2}: {weight2:.2%}</p>
        <p class="allocation-summary-copy">The live portfolio recommendation keeps the allocation visible in one clean summary block, while the key performance metrics remain easy to scan below.</p>
        <div class="allocation-chip-row">
            <span class="allocation-chip">{asset1}: {weight1:.2%}</span>
            <span class="allocation-chip">{asset2}: {weight2:.2%}</span>
        </div>
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


def efficient_frontier_indices(risks: np.ndarray, returns: np.ndarray, eligible_mask: np.ndarray | None = None) -> np.ndarray:
    if eligible_mask is None:
        candidate_indices = np.arange(len(risks))
    else:
        candidate_indices = np.where(eligible_mask)[0]

    if candidate_indices.size == 0:
        return np.array([], dtype=int)

    ordered_indices = candidate_indices[np.lexsort((-returns[candidate_indices], risks[candidate_indices]))]

    frontier_indices = []
    best_return = -np.inf
    for idx in ordered_indices:
        current_return = float(returns[idx])
        if current_return > best_return + 1e-12:
            frontier_indices.append(int(idx))
            best_return = current_return

    return np.array(frontier_indices, dtype=int)


def frontier_overlap_ratio(primary_indices: np.ndarray, secondary_indices: np.ndarray) -> float:
    if primary_indices.size == 0 or secondary_indices.size == 0:
        return 0.0

    primary_set = set(int(idx) for idx in primary_indices.tolist())
    secondary_set = set(int(idx) for idx in secondary_indices.tolist())
    shared = len(primary_set.intersection(secondary_set))
    base = max(1, min(len(primary_set), len(secondary_set)))
    return float(shared / base)


def build_frontier_plot_arrays(
    risks_pct: np.ndarray,
    returns_pct: np.ndarray,
    frontier_indices: np.ndarray,
    x_shift: float = 0.0,
    y_shift: float = 0.0,
) -> tuple[np.ndarray, np.ndarray, dict]:
    if frontier_indices.size == 0:
        return np.array([], dtype=float), np.array([], dtype=float), {}

    plotted_risks = np.array(risks_pct[frontier_indices], dtype=float)
    plotted_returns = np.array(returns_pct[frontier_indices], dtype=float)
    point_lookup = {}

    if abs(x_shift) > 1e-12 or abs(y_shift) > 1e-12:
        ramp = np.linspace(0.30, 1.00, frontier_indices.size)
        plotted_risks = plotted_risks + x_shift * ramp
        plotted_returns = plotted_returns + y_shift * ramp
        for pos, idx in enumerate(frontier_indices):
            point_lookup[int(idx)] = (float(plotted_risks[pos]), float(plotted_returns[pos]))
    else:
        for pos, idx in enumerate(frontier_indices):
            point_lookup[int(idx)] = (float(plotted_risks[pos]), float(plotted_returns[pos]))

    return plotted_risks, plotted_returns, point_lookup


def compute_portfolio_path_from_weights(
    weights_w1,
    exp_return1_pct: float,
    exp_return2_pct: float,
    std_dev1_pct: float,
    std_dev2_pct: float,
    correlation: float,
    esg_score1: float,
    esg_score2: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    weights_arr = np.array(weights_w1, dtype=float, ndmin=1)
    weights_arr = np.clip(weights_arr, 0.0, 1.0)
    weights_w2 = 1.0 - weights_arr

    r1 = exp_return1_pct / 100.0
    r2 = exp_return2_pct / 100.0
    s1 = std_dev1_pct / 100.0
    s2 = std_dev2_pct / 100.0
    esg1 = esg_score1 / 100.0
    esg2 = esg_score2 / 100.0

    portfolio_returns = weights_arr * r1 + weights_w2 * r2
    portfolio_variances = (
        (weights_arr ** 2) * (s1 ** 2)
        + (weights_w2 ** 2) * (s2 ** 2)
        + 2.0 * weights_arr * weights_w2 * s1 * s2 * correlation
    )
    portfolio_risks = np.sqrt(np.maximum(portfolio_variances, 0.0))
    portfolio_esg = weights_arr * esg1 + weights_w2 * esg2

    return portfolio_returns * 100.0, portfolio_risks * 100.0, portfolio_esg * 100.0


def build_esg_tilted_weights(base_weights, esg_preference_fraction: float, esg_score1: float, esg_score2: float):
    weights_arr = np.array(base_weights, dtype=float, ndmin=1)
    weights_arr = np.clip(weights_arr, 0.0, 1.0)

    anchor_weight = 1.0 if esg_score1 >= esg_score2 else 0.0
    esg_gap_fraction = abs(float(esg_score1) - float(esg_score2)) / 100.0
    tilt_strength = float(np.clip(0.18 + 0.74 * esg_preference_fraction * max(esg_gap_fraction, 0.20), 0.0, 0.88))

    if anchor_weight >= 0.5:
        emphasis_profile = 0.28 + 0.72 * np.power(weights_arr, 0.92)
        adjusted_weights = weights_arr + tilt_strength * (1.0 - weights_arr) * emphasis_profile
    else:
        emphasis_profile = 0.28 + 0.72 * np.power(1.0 - weights_arr, 0.92)
        adjusted_weights = weights_arr - tilt_strength * weights_arr * emphasis_profile

    adjusted_weights = np.clip(adjusted_weights, 0.0, 1.0)

    if np.isscalar(base_weights):
        return float(adjusted_weights[0])
    return adjusted_weights


def apply_frontier_visibility_lift(
    base_risks_pct: np.ndarray,
    base_returns_pct: np.ndarray,
    esg_risks_pct: np.ndarray,
    esg_returns_pct: np.ndarray,
    esg_preference_fraction: float,
) -> tuple[np.ndarray, np.ndarray]:
    if len(base_risks_pct) == 0 or len(esg_risks_pct) == 0 or esg_preference_fraction <= 0.0:
        return np.array(esg_risks_pct, dtype=float), np.array(esg_returns_pct, dtype=float)

    comparison_count = min(len(base_risks_pct), len(esg_risks_pct))
    if comparison_count == 0:
        return np.array(esg_risks_pct, dtype=float), np.array(esg_returns_pct, dtype=float)

    risk_span = max(float(np.max(base_risks_pct) - np.min(base_risks_pct)), 1e-9)
    return_span = max(float(np.max(base_returns_pct) - np.min(base_returns_pct)), 1e-9)

    norm_gap = np.mean(
        np.sqrt(
            ((esg_risks_pct[:comparison_count] - base_risks_pct[:comparison_count]) / risk_span) ** 2
            + ((esg_returns_pct[:comparison_count] - base_returns_pct[:comparison_count]) / return_span) ** 2
        )
    )

    if norm_gap >= 0.08:
        return np.array(esg_risks_pct, dtype=float), np.array(esg_returns_pct, dtype=float)

    lift_scale = (0.08 - norm_gap) / 0.08
    x_lift = 0.028 * risk_span * lift_scale * (0.70 + 0.30 * esg_preference_fraction)
    y_lift = 0.020 * return_span * lift_scale * (0.70 + 0.30 * esg_preference_fraction)
    ramp = np.linspace(0.35, 1.00, len(esg_risks_pct))

    lifted_risks = np.array(esg_risks_pct, dtype=float) + x_lift * ramp
    lifted_returns = np.array(esg_returns_pct, dtype=float) + y_lift * ramp
    return lifted_risks, lifted_returns


def build_dual_frontier_display(result: dict) -> dict:
    portfolio_returns = np.array(result["portfolio_returns"], dtype=float)
    portfolio_risks = np.array(result["portfolio_risks"], dtype=float)
    portfolio_esg = np.array(result["portfolio_esg"], dtype=float)

    if portfolio_returns.size == 0 or portfolio_risks.size == 0:
        empty = np.array([], dtype=float)
        return {
            "without_curve_risks": empty,
            "without_curve_returns": empty,
            "without_frontier_risks": empty,
            "without_frontier_returns": empty,
            "with_curve_risks": empty,
            "with_curve_returns": empty,
            "with_frontier_risks": empty,
            "with_frontier_returns": empty,
            "with_performance": empty,
            "rf_point": (0.0, 0.0),
            "without_tangency_point": (0.0, 0.0),
            "with_tangency_point": (0.0, 0.0),
            "with_tangency_idx": 0,
            "visual_gap": 0.0,
        }

    def upper_branch_indices(risks_arr: np.ndarray, performance_arr: np.ndarray) -> np.ndarray:
        min_risk_idx = int(np.argmin(risks_arr))
        left_branch = np.arange(0, min_risk_idx + 1, dtype=int)
        right_branch = np.arange(min_risk_idx, len(risks_arr), dtype=int)

        left_best = float(np.max(performance_arr[left_branch])) if left_branch.size > 0 else -np.inf
        right_best = float(np.max(performance_arr[right_branch])) if right_branch.size > 0 else -np.inf

        if right_best >= left_best:
            return right_branch
        return left_branch[::-1]

    without_curve_risks = np.array(portfolio_risks * 100.0, dtype=float)
    without_curve_returns = np.array(portfolio_returns * 100.0, dtype=float)
    without_indices = upper_branch_indices(portfolio_risks, portfolio_returns)
    without_frontier_risks = np.array(without_curve_risks[without_indices], dtype=float)
    without_frontier_returns = np.array(without_curve_returns[without_indices], dtype=float)

    rf = float(result.get("risk_free_rate_input", 0.0)) / 100.0
    esg_preference_fraction = float(np.clip(result.get("esg_preference_fraction", 0.0), 0.0, 1.0))
    required_esg = float(result.get("required_esg", float(np.mean(portfolio_esg))))

    esg_gap_fraction = abs(float(result.get("esg_score1_input", 0.0)) - float(result.get("esg_score2_input", 0.0))) / 100.0
    return_gap_fraction = abs(float(result.get("exp_return1_input", 0.0)) - float(result.get("exp_return2_input", 0.0))) / 100.0
    adjustment_scale = 0.18 + 0.72 * esg_gap_fraction + 0.48 * return_gap_fraction
    with_performance_full = portfolio_returns + esg_preference_fraction * adjustment_scale * (portfolio_esg - required_esg)

    with_curve_risks = np.array(portfolio_risks * 100.0, dtype=float)
    with_curve_returns = np.array(with_performance_full * 100.0, dtype=float)
    with_indices = upper_branch_indices(portfolio_risks, with_performance_full)
    with_frontier_risks = np.array(with_curve_risks[with_indices], dtype=float)
    with_frontier_returns = np.array(with_curve_returns[with_indices], dtype=float)

    with_sharpes = np.where(portfolio_risks > 1e-12, (with_performance_full - rf) / portfolio_risks, -np.inf)
    with_tangency_idx = int(np.argmax(with_sharpes))

    without_tangency_point = (
        float(without_curve_risks[result["max_sharpe_idx"]]),
        float(without_curve_returns[result["max_sharpe_idx"]]),
    )
    with_tangency_point = (
        float(with_curve_risks[with_tangency_idx]),
        float(with_curve_returns[with_tangency_idx]),
    )

    comparison_count = min(len(without_frontier_risks), len(with_frontier_risks))
    if comparison_count > 0:
        without_sample_idx = np.linspace(0, len(without_frontier_risks) - 1, comparison_count).astype(int)
        with_sample_idx = np.linspace(0, len(with_frontier_risks) - 1, comparison_count).astype(int)
        risk_span = max(float(np.max(without_frontier_risks) - np.min(without_frontier_risks)), 1e-9)
        return_span = max(
            float(
                max(np.max(without_frontier_returns), np.max(with_frontier_returns))
                - min(np.min(without_frontier_returns), np.min(with_frontier_returns))
            ),
            1e-9,
        )
        visual_gap = float(
            np.mean(
                np.sqrt(
                    ((with_frontier_risks[with_sample_idx] - without_frontier_risks[without_sample_idx]) / risk_span) ** 2
                    + ((with_frontier_returns[with_sample_idx] - without_frontier_returns[without_sample_idx]) / return_span) ** 2
                )
            )
        )
    else:
        visual_gap = 0.0

    return {
        "without_curve_risks": without_curve_risks,
        "without_curve_returns": without_curve_returns,
        "without_frontier_risks": without_frontier_risks,
        "without_frontier_returns": without_frontier_returns,
        "with_curve_risks": with_curve_risks,
        "with_curve_returns": with_curve_returns,
        "with_frontier_risks": with_frontier_risks,
        "with_frontier_returns": with_frontier_returns,
        "with_performance": np.array(with_performance_full * 100.0, dtype=float),
        "rf_point": (0.0, float(rf * 100.0)),
        "without_tangency_point": without_tangency_point,
        "with_tangency_point": with_tangency_point,
        "with_tangency_idx": with_tangency_idx,
        "visual_gap": visual_gap,
    }


def build_frontier_interpretation(result: dict) -> str:
    asset1 = str(result.get("asset1", "Asset 1")).strip() or "Asset 1"
    asset2 = str(result.get("asset2", "Asset 2")).strip() or "Asset 2"

    opt_w1 = float(result.get("opt_w1", 0.0))
    opt_w2 = float(result.get("opt_w2", 0.0))
    opt_return = float(result.get("opt_return", 0.0) * 100.0)
    opt_risk = float(result.get("opt_risk", 0.0) * 100.0)
    opt_esg = float(result.get("opt_esg", 0.0) * 100.0)
    opt_sharpe = float(result.get("opt_sharpe", 0.0))

    required_esg = float(result.get("required_esg", 0.0) * 100.0)
    correlation = float(result.get("correlation", 0.0))

    max_sharpe_idx = int(result.get("max_sharpe_idx", 0))
    portfolio_returns = np.array(result.get("portfolio_returns", []), dtype=float)
    portfolio_risks = np.array(result.get("portfolio_risks", []), dtype=float)
    portfolio_esg = np.array(result.get("portfolio_esg", []), dtype=float)

    if portfolio_returns.size > 0 and 0 <= max_sharpe_idx < portfolio_returns.size:
        base_return = float(portfolio_returns[max_sharpe_idx] * 100.0)
        base_risk = float(portfolio_risks[max_sharpe_idx] * 100.0)
        base_esg = float(portfolio_esg[max_sharpe_idx] * 100.0)
    else:
        base_return = opt_return
        base_risk = opt_risk
        base_esg = opt_esg

    if opt_w1 >= 0.70:
        allocation_sentence = f"Your portfolio is mainly invested in <strong>{asset1}</strong> ({opt_w1 * 100.0:.1f}%), with {opt_w2 * 100.0:.1f}% in <strong>{asset2}</strong>."
    elif opt_w2 >= 0.70:
        allocation_sentence = f"Your portfolio is mainly invested in <strong>{asset2}</strong> ({opt_w2 * 100.0:.1f}%), with {opt_w1 * 100.0:.1f}% in <strong>{asset1}</strong>."
    else:
        allocation_sentence = f"Your portfolio is spread across both assets, with {opt_w1 * 100.0:.1f}% in <strong>{asset1}</strong> and {opt_w2 * 100.0:.1f}% in <strong>{asset2}</strong>."

    performance_sentence = (
        f"Based on your current inputs, the portfolio is targeting <strong>{opt_return:.2f}% expected return</strong> "
        f"with <strong>{opt_risk:.2f}% risk</strong>. Its Sharpe ratio is <strong>{opt_sharpe:.2f}</strong>, "
        f"which means the return is being judged against the amount of risk taken."
    )

    if opt_esg >= required_esg + 5.0:
        esg_sentence = (
            f"The ESG score is <strong>{opt_esg:.2f}/100</strong>, which is comfortably above your current ESG target of "
            f"<strong>{required_esg:.2f}/100</strong>."
        )
    elif opt_esg >= required_esg:
        esg_sentence = (
            f"The ESG score is <strong>{opt_esg:.2f}/100</strong>, which meets your current ESG target of "
            f"<strong>{required_esg:.2f}/100</strong>."
        )
    else:
        esg_sentence = (
            f"The ESG score is <strong>{opt_esg:.2f}/100</strong>, which is below your current ESG target of "
            f"<strong>{required_esg:.2f}/100</strong>."
        )

    return_gap = opt_return - base_return
    risk_gap = opt_risk - base_risk
    esg_lift = opt_esg - base_esg

    if abs(return_gap) < 0.15 and abs(risk_gap) < 0.15:
        tradeoff_sentence = "Compared with the highest Sharpe portfolio, your ESG-focused portfolio is very similar financially, so you are not giving up much to reflect your sustainability preference."
    elif return_gap >= 0.15 and risk_gap <= 0.15:
        tradeoff_sentence = "Compared with the highest Sharpe portfolio, your ESG-focused portfolio is offering slightly stronger return without meaningfully increasing risk."
    elif return_gap >= -0.15 and risk_gap > 0.15:
        tradeoff_sentence = "Compared with the highest Sharpe portfolio, your ESG-focused portfolio keeps return fairly close, but it does take on more risk."
    elif return_gap < -0.15 and risk_gap <= 0.15:
        tradeoff_sentence = f"Compared with the highest Sharpe portfolio, your ESG-focused portfolio gives up a little expected return, but keeps risk close while improving ESG by <strong>{max(esg_lift, 0.0):.2f}</strong> points."
    else:
        tradeoff_sentence = "Compared with the highest Sharpe portfolio, your ESG-focused portfolio is making a clearer trade-off: it is prioritising sustainability, but with lower expected return and higher risk."

    if correlation <= -0.20:
        diversification_sentence = "The two assets are moving differently enough that diversification is helping reduce risk in a meaningful way."
    elif correlation <= 0.35:
        diversification_sentence = "The two assets still provide some diversification, which helps smooth overall portfolio risk."
    else:
        diversification_sentence = "The two assets are moving quite similarly, so diversification is limited and the portfolio may be less cushioned against swings."

    return f"""
    <div class="interpretation-card">
        <p class="interpretation-title">Portfolio Analysis</p>
        <p class="interpretation-subtitle">This summary updates live as your portfolio inputs change.</p>
        <div class="interpretation-divider"></div>
        <p class="interpretation-copy">{allocation_sentence}</p>
        <p class="interpretation-copy">{performance_sentence}</p>
        <p class="interpretation-copy">{esg_sentence} {tradeoff_sentence}</p>
        <p class="interpretation-copy">{diversification_sentence}</p>
    </div>
    """


# -------------------------------------------------
# Company search helpers
# -------------------------------------------------
def company_option_label(company_tuple) -> str:
    ticker, name, industry, exchange, e_grade, e_level, s_grade, s_level, g_grade, g_level, total_grade, total_level, e_score, s_score, g_score, total_score = company_tuple
    return f"{name} ({ticker.upper()})"


def company_search_score(query: str, company_tuple) -> int:
    ticker, name, industry, exchange, e_grade, e_level, s_grade, s_level, g_grade, g_level, total_grade, total_level, e_score, s_score, g_score, total_score = company_tuple
    q = query.strip().lower()
    if not q:
        return -1

    ticker_l = str(ticker).lower()
    name_l = str(name).lower()
    industry_l = str(industry).lower()
    exchange_l = str(exchange).lower()
    combined = f"{name_l} {ticker_l} {industry_l} {exchange_l}"

    if q == ticker_l:
        return 5000
    if q == name_l:
        return 4900
    if ticker_l.startswith(q):
        return 4000 - len(name_l)
    if name_l.startswith(q):
        return 3500 - len(name_l)
    if q in name_l:
        return 2500 - name_l.find(q)
    if q in ticker_l:
        return 2200 - ticker_l.find(q)
    if q in industry_l:
        return 1500 - industry_l.find(q)
    if q in exchange_l:
        return 1200 - exchange_l.find(q)

    parts = [p for p in q.split() if p]
    if parts and all(p in combined for p in parts):
        return 1000 - len(name_l)

    return -1


def get_company_matches(query: str, limit: int = 30):
    q = query.strip()
    if not q:
        return []

    scored = []
    for company in COMPANY_DATA:
        score = company_search_score(q, company)
        if score >= 0:
            scored.append((score, company_option_label(company), company))

    scored.sort(key=lambda item: (-item[0], item[1].lower()))
    return [item[2] for item in scored[:limit]]


def get_company_by_option_label(label: str):
    if not label:
        return None
    for company in COMPANY_DATA:
        if company_option_label(company) == label:
            return company
    return None


def render_company_profile(company_tuple) -> None:
    if company_tuple is None:
        return

    ticker, name, industry, exchange, e_grade, e_level, s_grade, s_level, g_grade, g_level, total_grade, total_level, e_score, s_score, g_score, total_score = company_tuple

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="mini-header">Company ESG Profile</div>', unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="asset-card">
            <div class="asset-card-title">{name} ({ticker.upper()})</div>
            <p class="asset-card-copy">
                Industry: {industry}<br>
                Exchange: {exchange}<br>
                Overall ESG Grade: <strong>{total_grade}</strong> · {total_level}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div style='height:0.6rem;'></div>", unsafe_allow_html=True)

    m1, m2, m3, m4 = st.columns(4, gap="small")
    with m1:
        st.markdown(result_tile("Environmental", f"{e_grade} · {e_level}"), unsafe_allow_html=True)
    with m2:
        st.markdown(result_tile("Social", f"{s_grade} · {s_level}"), unsafe_allow_html=True)
    with m3:
        st.markdown(result_tile("Governance", f"{g_grade} · {g_level}"), unsafe_allow_html=True)
    with m4:
        st.markdown(result_tile("Total ESG", f"{total_grade} · {total_level}"), unsafe_allow_html=True)


# -------------------------------------------------
# Portfolio computations
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
    def lookup(asset_label: str):
        ticker = asset_label.split("(")[-1].replace(")", "").strip().lower()
        for row in COMPANY_DATA:
            if row[0] == ticker:
                return row
        return None

    row1 = lookup(asset1)
    row2 = lookup(asset2)
    exp_return1 = ASSET_DATA_LOOKUP.get(asset1, {"expected_return": 0.0, "std_dev": 0.0})["expected_return"]
    std_dev1 = ASSET_DATA_LOOKUP.get(asset1, {"expected_return": 0.0, "std_dev": 0.0})["std_dev"]
    exp_return2 = ASSET_DATA_LOOKUP.get(asset2, {"expected_return": 0.0, "std_dev": 0.0})["expected_return"]
    std_dev2 = ASSET_DATA_LOOKUP.get(asset2, {"expected_return": 0.0, "std_dev": 0.0})["std_dev"]

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
        "company_row1": row1,
        "company_row2": row2,
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

    esg_preference_fraction = float(np.clip(esg_slider / 0.10, 0.0, 1.0))
    required_esg = float(np.min(portfolio_esg) + esg_preference_fraction * (np.max(portfolio_esg) - np.min(portfolio_esg)))
    esg_constrained_mask = portfolio_esg >= (required_esg - 1e-12)

    efficient_idx_without_esg_full = efficient_frontier_indices(portfolio_risks, portfolio_returns)
    efficient_idx_with_esg = efficient_frontier_indices(portfolio_risks, portfolio_returns, esg_constrained_mask)
    if efficient_idx_with_esg.size == 0:
        efficient_idx_with_esg = efficient_idx_without_esg_full.copy()

    efficient_idx_with_esg_set = set(int(idx) for idx in efficient_idx_with_esg.tolist())
    efficient_idx_without_esg_display = np.array(
        [int(idx) for idx in efficient_idx_without_esg_full if int(idx) not in efficient_idx_with_esg_set],
        dtype=int,
    )
    frontier_overlap = frontier_overlap_ratio(efficient_idx_without_esg_full, efficient_idx_with_esg)
    frontiers_share_points = bool(frontier_overlap > 0.0)
    frontiers_need_visual_separation = bool(frontier_overlap >= 0.20)

    opt_w1 = float(weights[optimal_idx])
    opt_w2 = float(1 - opt_w1)

    return {
        "asset1": asset1,
        "asset2": asset2,
        "exp_return1_input": float(exp_return1),
        "exp_return2_input": float(exp_return2),
        "std_dev1_input": float(std_dev1),
        "std_dev2_input": float(std_dev2),
        "esg_score1_input": float(esg_score1),
        "esg_score2_input": float(esg_score2),
        "correlation": float(correlation),
        "risk_free_rate_input": float(risk_free_rate),
        "esg_preference_fraction": esg_preference_fraction,
        "weights": weights,
        "portfolio_returns": portfolio_returns,
        "portfolio_risks": portfolio_risks,
        "portfolio_esg": portfolio_esg,
        "portfolio_sharpes": portfolio_sharpes,
        "max_sharpe_idx": max_sharpe_idx,
        "optimal_idx": optimal_idx,
        "efficient_idx_without_esg_full": efficient_idx_without_esg_full,
        "efficient_idx_without_esg_display": efficient_idx_without_esg_display,
        "efficient_idx_with_esg": efficient_idx_with_esg,
        "frontier_overlap_ratio": frontier_overlap,
        "frontiers_share_points": frontiers_share_points,
        "frontiers_need_visual_separation": frontiers_need_visual_separation,
        "required_esg": required_esg,
        "opt_w1": opt_w1,
        "opt_w2": opt_w2,
        "opt_return": float(portfolio_returns[optimal_idx]),
        "opt_risk": float(portfolio_risks[optimal_idx]),
        "opt_esg": float(portfolio_esg[optimal_idx]),
        "opt_sharpe": float(portfolio_sharpes[optimal_idx]),
    }


# -------------------------------------------------
# Recommendation asset stats lookup
# -------------------------------------------------
ASSET_DATA_LOOKUP = {
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
# Live popup renderers
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
                for row, asset_label, exp_return, std_dev in [
                    (result["company_row1"], result["asset1"], result["exp_return1"], result["std_dev1"]),
                    (result["company_row2"], result["asset2"], result["exp_return2"], result["std_dev2"]),
                ]:
                    if row is None:
                        st.markdown(
                            f"""
                            <div class="asset-card">
                                <div class="asset-card-title">{asset_label}</div>
                                <p class="asset-card-copy">
                                    Expected return: {exp_return:.2f}%<br>
                                    Standard deviation: {std_dev:.2f}%
                                </p>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )
                    else:
                        ticker, name, industry, exchange, e_grade, e_level, s_grade, s_level, g_grade, g_level, total_grade, total_level, e_score, s_score, g_score, total_score = row
                        st.markdown(
                            f"""
                            <div class="asset-card">
                                <div class="asset-card-title">{name} ({ticker.upper()})</div>
                                <p class="asset-card-copy">
                                    Industry: {industry}<br>
                                    ESG Grade: <strong>{total_grade}</strong> · {total_level}<br>
                                    Expected return: {exp_return:.2f}% · Standard deviation: {std_dev:.2f}%
                                </p>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )
                    st.markdown("<div style='height:0.65rem;'></div>", unsafe_allow_html=True)

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
                        '<div class="popup-subtitle">The popup remains open while you refine the inputs on the page.</div>',
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
                    '<div class="popup-subtitle">This output updates live while you keep editing the inputs behind it.</div>',
                    unsafe_allow_html=True,
                )
            with header_right:
                st.button("Close", key="close_builder_popup_btn", use_container_width=True, on_click=hide_builder_popup)

            st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

            metric_c1, metric_c2, metric_c3, metric_c4 = st.columns(4, gap="small")
            with metric_c1:
                st.markdown(result_tile("Expected Return", f'{result["opt_return"]:.2%}'), unsafe_allow_html=True)
            with metric_c2:
                st.markdown(
                    result_tile(
                        "Portfolio Risk",
                        f'{result["opt_risk"]:.2%}',
                        tooltip="Portfolio risk is characterised by standard deviation.",
                    ),
                    unsafe_allow_html=True,
                )
            with metric_c3:
                st.markdown(result_tile("Portfolio ESG Score", f'{result["opt_esg"] * 100:.2f}/100'), unsafe_allow_html=True)
            with metric_c4:
                st.markdown(result_tile("Sharpe Ratio", f'{result["opt_sharpe"]:.2f}'), unsafe_allow_html=True)

            st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
            st.markdown('<div class="mini-header">Efficient Frontiers</div>', unsafe_allow_html=True)

            fig, ax = plt.subplots(figsize=(9.6, 5.6), dpi=180, constrained_layout=True)
            fig.patch.set_facecolor("white")

            frontier_display = build_dual_frontier_display(result)
            without_curve_risks = frontier_display["without_curve_risks"]
            without_curve_returns = frontier_display["without_curve_returns"]
            without_frontier_risks = frontier_display["without_frontier_risks"]
            without_frontier_returns = frontier_display["without_frontier_returns"]
            with_curve_risks = frontier_display["with_curve_risks"]
            with_curve_returns = frontier_display["with_curve_returns"]
            with_frontier_risks = frontier_display["with_frontier_risks"]
            with_frontier_returns = frontier_display["with_frontier_returns"]
            rf_x, rf_y = frontier_display["rf_point"]
            without_tangency_x, without_tangency_y = frontier_display["without_tangency_point"]
            with_tangency_x, with_tangency_y = frontier_display["with_tangency_point"]

            if len(without_curve_risks) > 0:
                ax.plot(
                    without_curve_risks,
                    without_curve_returns,
                    linewidth=1.8,
                    color="#60a5fa",
                    alpha=0.55,
                    zorder=1,
                )
            if len(without_frontier_risks) > 0:
                ax.plot(
                    without_frontier_risks,
                    without_frontier_returns,
                    linewidth=2.6,
                    color="#2563eb",
                    zorder=3,
                )

            if len(with_curve_risks) > 0:
                ax.plot(
                    with_curve_risks,
                    with_curve_returns,
                    linewidth=1.8,
                    color="#86efac",
                    alpha=0.58,
                    zorder=1,
                )
            if len(with_frontier_risks) > 0:
                ax.plot(
                    with_frontier_risks,
                    with_frontier_returns,
                    linewidth=2.7,
                    color="#16a34a",
                    zorder=4,
                )

            ax.plot(
                [rf_x, without_tangency_x],
                [rf_y, without_tangency_y],
                linestyle=(0, (3, 3)),
                linewidth=1.8,
                color="#2563eb",
                alpha=0.9,
                zorder=2,
            )
            ax.plot(
                [rf_x, with_tangency_x],
                [rf_y, with_tangency_y],
                linestyle=(0, (3, 3)),
                linewidth=1.8,
                color="#14b8a6",
                alpha=0.9,
                zorder=2,
            )

            ax.scatter(rf_x, rf_y, s=38, color="#94a3b8", edgecolors="white", linewidths=0.8, zorder=5)
            ax.scatter(
                without_tangency_x,
                without_tangency_y,
                s=84,
                color="#2563eb",
                edgecolors="white",
                linewidths=1.0,
                zorder=6,
            )
            ax.scatter(
                with_tangency_x,
                with_tangency_y,
                s=84,
                color="#16a34a",
                edgecolors="white",
                linewidths=1.0,
                zorder=6,
            )

            if len(without_frontier_risks) > 0:
                without_label_idx = min(len(without_frontier_risks) - 1, max(0, int(len(without_frontier_risks) * 0.58)))
                ax.annotate(
                    "Mean-Variance Frontier\n(Without ESG)",
                    (without_frontier_risks[without_label_idx], without_frontier_returns[without_label_idx]),
                    xytext=(26, 18),
                    textcoords="offset points",
                    fontsize=8.6,
                    color="#1d4ed8",
                    weight="bold",
                    bbox=dict(boxstyle="round,pad=0.30", fc="white", ec="#bfdbfe", alpha=0.98),
                    arrowprops=dict(arrowstyle="-", color="#2563eb", lw=1.05, alpha=0.95),
                )

            if len(with_frontier_risks) > 0:
                with_label_idx = min(len(with_frontier_risks) - 1, max(0, int(len(with_frontier_risks) * 0.68)))
                ax.annotate(
                    "Mean-Variance Frontier\n(With Given ESG)",
                    (with_frontier_risks[with_label_idx], with_frontier_returns[with_label_idx]),
                    xytext=(20, -34),
                    textcoords="offset points",
                    fontsize=8.6,
                    color="#15803d",
                    weight="bold",
                    bbox=dict(boxstyle="round,pad=0.30", fc="white", ec="#bbf7d0", alpha=0.98),
                    arrowprops=dict(arrowstyle="-", color="#16a34a", lw=1.05, alpha=0.95),
                )

            ax.annotate(
                "Tangency Portfolio\n(Without ESG)",
                (without_tangency_x, without_tangency_y),
                xytext=(-118, 12),
                textcoords="offset points",
                fontsize=8.5,
                color="#1d4ed8",
                weight="bold",
                bbox=dict(boxstyle="round,pad=0.28", fc="white", ec="#bfdbfe", alpha=0.98),
                arrowprops=dict(arrowstyle="->", color="#2563eb", lw=1.0, alpha=0.9),
            )
            ax.annotate(
                "Tangency Portfolio\n(With Given ESG)",
                (with_tangency_x, with_tangency_y),
                xytext=(12, -34),
                textcoords="offset points",
                fontsize=8.5,
                color="#15803d",
                weight="bold",
                bbox=dict(boxstyle="round,pad=0.28", fc="white", ec="#bbf7d0", alpha=0.98),
                arrowprops=dict(arrowstyle="->", color="#16a34a", lw=1.0, alpha=0.9),
            )

            all_x = np.concatenate([without_curve_risks, with_curve_risks, np.array([rf_x])]) if len(without_curve_risks) + len(with_curve_risks) > 0 else np.array([0.0])
            all_y = np.concatenate([without_curve_returns, with_curve_returns, np.array([rf_y])]) if len(without_curve_returns) + len(with_curve_returns) > 0 else np.array([0.0])
            x_span = max(float(np.max(all_x) - np.min(all_x)), 1.0)
            y_span = max(float(np.max(all_y) - np.min(all_y)), 1.0)
            ax.set_xlim(left=0.0, right=float(np.max(all_x) + 0.07 * x_span))
            ax.set_ylim(bottom=float(min(rf_y, np.min(all_y)) - 0.08 * y_span), top=float(np.max(all_y) + 0.08 * y_span))
            ax.set_xlabel("Portfolio Risk (%)")
            ax.set_ylabel("Portfolio Performance (%)")
            ax.set_title("Efficient Frontiers")
            style_modern_axes(ax)
            st.pyplot(fig)
            plt.close(fig)
            st.markdown(build_frontier_interpretation(result), unsafe_allow_html=True)



# -------------------------------------------------
# Screens
# -------------------------------------------------
def render_home() -> None:
    st.markdown(
        f"""
        <div class="brand-row">
            <div class="logo-box">{LEAF_LOGO_SVG}</div>
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
        hero_panel = st.container(border=True)
        with hero_panel:
            st.markdown(
                """
                <div class="home-cta-shell">
                    <div class="section-label">Get Started</div>
                    <div class="section-title">Choose how you want to build your portfolio</div>
                    <div class="home-cta-note">
                        Start with a guided recommendation or move straight into a fully customised portfolio build.
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.markdown('<div class="home-button-spacer"></div>', unsafe_allow_html=True)
            btn1, btn2 = st.columns(2, gap="large")
            with btn1:
                st.button(
                    "Give Me a Portfolio Recommendation",
                    key="home_recommendation_button",
                    type="primary",
                    use_container_width=True,
                    on_click=open_recommendation,
                )
            with btn2:
                st.button(
                    "Build Your Customised Portfolio",
                    key="home_builder_button",
                    use_container_width=True,
                    on_click=open_builder,
                )
    with right:
        st.markdown(
            """
            <div class="home-overview-panel">
                <div class="home-overview-eyebrow">App Overview</div>
                <div class="home-overview-title">Build ESG-aware portfolios with a simple, guided workflow.</div>
                <p class="home-overview-copy">
                    This app helps investors compare financial return, portfolio risk, and sustainability priorities in one place.
                    You can either receive a guided recommendation or build a fully customised portfolio using your own assumptions,
                    then explore how the efficient frontiers and portfolio analysis change live as you adjust the inputs.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<div style='height:1.8rem;'></div>", unsafe_allow_html=True)
    st.markdown('<div class="section-label">Why this app?</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">An investment app that prioritises ESG preferences</div>', unsafe_allow_html=True)
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
        render_card("Environmental (E)", "Environmental factors consider climate risk, carbon emissions, resource use, pollution, and broader ecological sustainability.")
    with c2:
        render_card("Social (S)", "Social factors focus on how organisations treat people, including labour standards, diversity, community impact, health, safety, and human rights.")
    with c3:
        render_card("Governance (G)", "Governance factors examine how organisations are led, including board quality, executive accountability, transparency, ethics, and shareholder rights.")


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
            ["Prioritise sustainability", "Prioritise financial growth", "Balanced return and sustainability"],
            key="rec_investment_priority",
            horizontal=False,
            label_visibility="collapsed",
        )
        render_custom_label("Risk Tolerance")
        st.slider("Risk Tolerance", min_value=1, max_value=10, key="rec_risk_tolerance", label_visibility="collapsed")
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
    st.button("Generate Portfolio Recommendation", type="primary", use_container_width=True, on_click=show_recommendation_popup)


def render_builder_screen() -> None:
    inject_tool_text_css()
    st.button("← Back", on_click=open_home, use_container_width=False)
    render_page_header(
        "Build Your Customised Portfolio",
        "Build a personalised ESG-aware portfolio. The recommendation opens in a live popup-style panel on this same screen and updates as you change the inputs.",
    )

    if st.session_state.show_builder_popup:
        render_builder_popup()
        st.markdown("<div style='height:1.05rem;'></div>", unsafe_allow_html=True)

    st.session_state.builder_asset_choice = "Input my own assets"

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-label">Company Search</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Search Company ESG Profile</div>', unsafe_allow_html=True)
    st.text_input(
        "Search Company",
        key="company_search_query",
        placeholder="Type a company name, ticker, industry, or exchange",
        label_visibility="collapsed",
    )
    matches = get_company_matches(st.session_state.company_search_query, limit=40)
    option_labels = [company_option_label(c) for c in matches]
    if option_labels:
        if st.session_state.selected_company_option not in option_labels:
            st.session_state.selected_company_option = option_labels[0]
        st.selectbox(
            "Matching companies",
            options=option_labels,
            key="selected_company_option",
            label_visibility="collapsed",
        )
        selected_company = get_company_by_option_label(st.session_state.selected_company_option)
        render_company_profile(selected_company)
    else:
        if st.session_state.company_search_query.strip():
            st.info("No company matches found yet. Keep typing to narrow the search.")
        else:
            st.info(f"Search across all {len(COMPANY_DATA)} companies to view an ESG profile.")

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-label">Step 1</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Enter Asset Assumptions</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")
    with col1:
        asset1_value = st.text_input("Asset 1 Name", key="builder_asset1")
        asset1_name_prefix = asset1_value.strip() if asset1_value.strip() else "Asset 1"
        st.number_input(f"{asset1_name_prefix} Expected Return (%)", min_value=0.0, max_value=100.0, step=0.1, key="builder_exp_return1")
        st.number_input(f"{asset1_name_prefix} Standard Deviation (%)", min_value=0.0, max_value=100.0, step=0.1, key="builder_std_dev1")
        st.number_input(f"{asset1_name_prefix} ESG Score (0–100)", min_value=0.0, max_value=100.0, step=1.0, key="builder_esg_score1")
    with col2:
        asset2_value = st.text_input("Asset 2 Name", key="builder_asset2")
        asset2_name_prefix = asset2_value.strip() if asset2_value.strip() else "Asset 2"
        st.number_input(f"{asset2_name_prefix} Expected Return (%)", min_value=0.0, max_value=100.0, step=0.1, key="builder_exp_return2")
        st.number_input(f"{asset2_name_prefix} Standard Deviation (%)", min_value=0.0, max_value=100.0, step=0.1, key="builder_std_dev2")
        st.number_input(f"{asset2_name_prefix} ESG Score (0–100)", min_value=0.0, max_value=100.0, step=1.0, key="builder_esg_score2")

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-label">Step 2</div>', unsafe_allow_html=True)
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
            value=float(st.session_state.builder_risk_free_rate),
            step=0.01,
            key="builder_risk_free_rate",
            on_change=mark_builder_risk_free_rate_touched,
            label_visibility="collapsed",
        )
        render_custom_label("Risk Tolerance")
        st.slider("Risk Tolerance", min_value=1, max_value=10, key="builder_risk_tolerance", label_visibility="collapsed")
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
        lambda_map = {"Not important": 0.00, "Somewhat important": 0.05, "Very important": 0.10}
        preferred_lambda = lambda_map[st.session_state.builder_esg_importance]
        if abs(st.session_state.builder_esg_slider - preferred_lambda) > 1e-9 and not st.session_state.show_builder_popup:
            st.session_state.builder_esg_slider = preferred_lambda
        st.slider("ESG preference weight", min_value=0.00, max_value=0.10, step=0.01, key="builder_esg_slider")
        st.markdown(
            """
            <div class="tool-note">
                Higher ESG weight increases the influence of sustainability scores in the portfolio recommendation.
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<div style='height:1rem;'></div>", unsafe_allow_html=True)
    st.button("Generate Portfolio Recommendation", type="primary", use_container_width=True, on_click=show_builder_popup)


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
