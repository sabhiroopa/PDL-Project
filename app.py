import streamlit as st
import pandas as pd
import os
import html
from datetime import date

# ============================================================
# KARUVELAM360
# End-to-End Seemai Karuvelam Eradication & Monitoring Platform
# Tamil Nadu
# ============================================================

st.set_page_config(
    page_title="Karuvelam360",
    page_icon="🌱",
    layout="wide"
)

# ============================================================
# PATHS
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")
IMAGE_DIR = os.path.join(BASE_DIR, "images")

BEFORE_DIR = os.path.join(IMAGE_DIR, "before")
AFTER_DIR = os.path.join(IMAGE_DIR, "after")
ACTION_DIR = os.path.join(IMAGE_DIR, "actions")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(BEFORE_DIR, exist_ok=True)
os.makedirs(AFTER_DIR, exist_ok=True)
os.makedirs(ACTION_DIR, exist_ok=True)

SITES_FILE = os.path.join(DATA_DIR, "sites.csv")
MONITORING_FILE = os.path.join(DATA_DIR, "monitoring.csv")
SCHEMES_FILE = os.path.join(DATA_DIR, "schemes.csv")
PROJECT_SITES_FILE = os.path.join(DATA_DIR, "project_sites.csv")
ALERTS_FILE = os.path.join(DATA_DIR, "alerts.csv")
ALERT_ACTIONS_FILE = os.path.join(DATA_DIR, "alert_actions.csv")


# ============================================================
# INITIAL DATA
# ============================================================

def initialize_files():

    if not os.path.exists(SITES_FILE):

        sites = pd.DataFrame([
            {
                "Site ID": "PJ001",
                "District": "Madurai",
                "Taluk": "Melur",
                "Village": "Demo Village 1",
                "Latitude": 10.0324,
                "Longitude": 78.3394,
                "Area (ha)": 25.5,
                "Infestation": "High",
                "Risk": "High",
                "Status": "Infested",
                "Clearance Method": "Not Cleared",
                "Budget Allocated": 500000,
                "Budget Used": 0,
                "Biomass (tonnes)": 0,
                "Clearance Date": "",
                "Officer Name": "",
                "Clearance Remarks": "",
                "Before Image": "",
                "After Image": "",
                "AI Prediction": "",
                "AI Confidence": "",
                "Officer Decision": "",
                "Verification Remarks": ""
            },
            {
                "Site ID": "PJ002",
                "District": "Ramanathapuram",
                "Taluk": "Ramanathapuram",
                "Village": "Demo Village 2",
                "Latitude": 9.3639,
                "Longitude": 78.8395,
                "Area (ha)": 18.2,
                "Infestation": "High",
                "Risk": "Medium",
                "Status": "Cleared",
                "Clearance Method": "Mechanical Removal",
                "Budget Allocated": 400000,
                "Budget Used": 350000,
                "Biomass (tonnes)": 12.5,
                "Clearance Date": "2026-01-15",
                "Officer Name": "Demo Officer",
                "Clearance Remarks": "Mechanical removal completed",
                "Before Image": "",
                "After Image": "",
                "AI Prediction": "",
                "AI Confidence": "",
                "Officer Decision": "",
                "Verification Remarks": ""
            },
            {
                "Site ID": "PJ003",
                "District": "Sivagangai",
                "Taluk": "Karaikudi",
                "Village": "Demo Village 3",
                "Latitude": 10.0732,
                "Longitude": 78.7808,
                "Area (ha)": 10.5,
                "Infestation": "Medium",
                "Risk": "Medium",
                "Status": "Cleared",
                "Clearance Method": "Manual Removal",
                "Budget Allocated": 250000,
                "Budget Used": 220000,
                "Biomass (tonnes)": 7.2,
                "Clearance Date": "2026-02-10",
                "Officer Name": "Demo Officer",
                "Clearance Remarks": "Manual eradication completed",
                "Before Image": "",
                "After Image": "",
                "AI Prediction": "",
                "AI Confidence": "",
                "Officer Decision": "",
                "Verification Remarks": ""
            },
            {
                "Site ID": "PJ004",
                "District": "Thoothukudi",
                "Taluk": "Tiruchendur",
                "Village": "Demo Village 4",
                "Latitude": 8.4973,
                "Longitude": 78.1198,
                "Area (ha)": 8.2,
                "Infestation": "Low",
                "Risk": "Low",
                "Status": "Cleared",
                "Clearance Method": "Root Removal",
                "Budget Allocated": 180000,
                "Budget Used": 160000,
                "Biomass (tonnes)": 4.1,
                "Clearance Date": "2026-03-05",
                "Officer Name": "Demo Officer",
                "Clearance Remarks": "Root removal completed",
                "Before Image": "",
                "After Image": "",
                "AI Prediction": "",
                "AI Confidence": "",
                "Officer Decision": "",
                "Verification Remarks": ""
            },
            {
                "Site ID": "PJ005",
                "District": "Tirunelveli",
                "Taluk": "Nanguneri",
                "Village": "Demo Village 5",
                "Latitude": 8.7139,
                "Longitude": 77.7567,
                "Area (ha)": 15.4,
                "Infestation": "High",
                "Risk": "High",
                "Status": "Monitoring",
                "Clearance Method": "Mechanical Removal",
                "Budget Allocated": 300000,
                "Budget Used": 280000,
                "Biomass (tonnes)": 9.8,
                "Clearance Date": "2026-03-20",
                "Officer Name": "Demo Officer",
                "Clearance Remarks": "Site under monitoring",
                "Before Image": "",
                "After Image": "",
                "AI Prediction": "",
                "AI Confidence": "",
                "Officer Decision": "",
                "Verification Remarks": ""
            }
        ])

        sites.to_csv(
            SITES_FILE,
            index=False
        )

    if not os.path.exists(MONITORING_FILE):

        pd.DataFrame(
            columns=[
                "Monitoring ID",
                "Site ID",
                "Inspection Date",
                "Officer Name",
                "New Shoots",
                "Regrowth Percentage",
                "Site Condition",
                "Regrowth Severity",
                "Observations",
                "Action Required"
            ]
        ).to_csv(
            MONITORING_FILE,
            index=False
        )

    if not os.path.exists(SCHEMES_FILE):

        pd.DataFrame(
            columns=[
                "Scheme ID",
                "Scheme Name",
                "Department",
                "Financial Year",
                "District",
                "Project Officer",
                "Start Date",
                "End Date",
                "Target Area (ha)",
                "Cleared Area (ha)",
                "Budget Allocated",
                "Budget Released",
                "Budget Utilized",
                "Project Status",
                "Remarks"
            ]
        ).to_csv(
            SCHEMES_FILE,
            index=False
        )

    if not os.path.exists(PROJECT_SITES_FILE):

        pd.DataFrame(
            columns=[
                "Project Site ID",
                "Scheme ID",
                "Site ID",
                "Linked Date",
                "Linked By",
                "Remarks"
            ]
        ).to_csv(
            PROJECT_SITES_FILE,
            index=False
        )

    if not os.path.exists(ALERTS_FILE):

        pd.DataFrame(
            columns=[
                "Alert ID",
                "Site ID",
                "Alert Date",
                "Alert Type",
                "Severity",
                "Message",
                "Action Required",
                "Status"
            ]
        ).to_csv(
            ALERTS_FILE,
            index=False
        )

    if not os.path.exists(ALERT_ACTIONS_FILE):

        pd.DataFrame(
            columns=[
                "Action ID",
                "Alert ID",
                "Site ID",
                "Action Date",
                "Officer Name",
                "Action Taken",
                "Action Remarks",
                "Evidence Image",
                "Action Status"
            ]
        ).to_csv(
            ALERT_ACTIONS_FILE,
            index=False
        )


initialize_files()


# ============================================================
# LOAD FUNCTIONS
# ============================================================

def load_sites():
    return pd.read_csv(SITES_FILE)


def load_monitoring():
    return pd.read_csv(MONITORING_FILE)


def load_schemes():
    return pd.read_csv(SCHEMES_FILE)


def load_project_sites():
    return pd.read_csv(PROJECT_SITES_FILE)


def load_alerts():
    return pd.read_csv(ALERTS_FILE)


def load_alert_actions():
    return pd.read_csv(ALERT_ACTIONS_FILE)


# ============================================================
# SAVE FUNCTIONS
# ============================================================

def save_sites(df):
    df.to_csv(
        SITES_FILE,
        index=False
    )


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def show_table(df):

    if df.empty:
        st.info("No records available.")
        return

    table_html = df.to_html(
        index=False,
        escape=True,
        border=0
    )

    st.markdown(
        """
        <div style="
            overflow-x:auto;
            border:1px solid #dddddd;
            border-radius:8px;
            padding:5px;
        ">
        """
        + table_html
        + """
        </div>
        """,
        unsafe_allow_html=True
    )


def safe_number(series):

    return pd.to_numeric(
        series,
        errors="coerce"
    ).fillna(0)


def generate_id(
    prefix,
    dataframe,
    column
):

    if dataframe.empty:
        return f"{prefix}0001"

    numbers = []

    for value in dataframe[column].astype(str):

        try:

            numbers.append(
                int(
                    value.replace(
                        prefix,
                        ""
                    )
                )
            )

        except Exception:
            pass

    next_number = max(
        numbers,
        default=0
    ) + 1

    return (
        f"{prefix}"
        f"{next_number:04d}"
    )


def create_map_html(map_df):

    markers = []

    for _, row in map_df.iterrows():

        try:

            lat = float(
                row["Latitude"]
            )

            lon = float(
                row["Longitude"]
            )

        except Exception:

            continue

        risk = str(
            row.get(
                "Risk",
                "Low"
            )
        )

        if risk.lower() == "high":

            marker_color = "red"

        elif risk.lower() == "medium":

            marker_color = "orange"

        else:

            marker_color = "green"

        popup = f"""
        <b>Site ID:</b>
        {html.escape(str(row.get("Site ID", "")))}<br>

        <b>District:</b>
        {html.escape(str(row.get("District", "")))}<br>

        <b>Taluk:</b>
        {html.escape(str(row.get("Taluk", "")))}<br>

        <b>Village:</b>
        {html.escape(str(row.get("Village", "")))}<br>

        <b>Infestation:</b>
        {html.escape(str(row.get("Infestation", "")))}<br>

        <b>Risk:</b>
        {html.escape(str(row.get("Risk", "")))}<br>

        <b>Status:</b>
        {html.escape(str(row.get("Status", "")))}
        """

        markers.append(
            f"""
            L.circleMarker(
                [{lat}, {lon}],
                {{
                    color: '{marker_color}',
                    fillColor: '{marker_color}',
                    fillOpacity: 0.8,
                    radius: 9
                }}
            )
            .addTo(map)
            .bindPopup(`{popup}`);
            """
        )

    markers_html = "\n".join(
        markers
    )

    return f"""
    <!DOCTYPE html>

    <html>

    <head>

        <meta charset="utf-8">

        <link
            rel="stylesheet"
            href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
        >

        <script
            src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js">
        </script>

        <style>

            html, body {{
                margin: 0;
                padding: 0;
                height: 100%;
            }}

            #map {{
                height: 650px;
                width: 100%;
                border-radius: 10px;
            }}

        </style>

    </head>

    <body>

        <div id="map"></div>

        <script>

            var map = L.map(
                'map'
            ).setView(
                [10.8505, 78.7047],
                7
            );

            L.tileLayer(
                'https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png',
                {{
                    maxZoom: 19,
                    attribution:
                    '&copy; OpenStreetMap contributors'
                }}
            ).addTo(map);

            {markers_html}

        </script>

    </body>

    </html>
    """


# ============================================================
# LOAD CURRENT DATA
# ============================================================

sites = load_sites()
monitoring = load_monitoring()
schemes = load_schemes()
project_sites = load_project_sites()
alerts = load_alerts()
alert_actions = load_alert_actions()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title(
    "🌱 Karuvelam360"
)

st.sidebar.write(
    "End-to-End Seemai Karuvelam "
    "Eradication & Monitoring Platform"
)

st.sidebar.markdown("---")

module = st.sidebar.selectbox(
    "Select Module",
    [
        "Dashboard",
        "Register New Site",
        "Tamil Nadu Map",
        "Site Details",
        "Clearance",
        "Before / After Evidence",
        "AI Photo Verification",
        "Risk Assessment",
        "Budget Management",
        "Biomass Utilisation",
        "Site History",
        "Monitoring & Regrowth",
        "Government Schemes",
        "Project-Site Linking",
        "SMS Alerts",
        "Officer Action",
        "Government Performance Analytics",
        "District / Taluk / Village Analytics"
    ]
)


# ============================================================
# MODULE 1
# DASHBOARD
# ============================================================

if module == "Dashboard":

    st.title(
        "🌱 Karuvelam360 Dashboard"
    )

    st.subheader(
        "Seemai Karuvelam Eradication & Monitoring"
    )

    total_sites = len(sites)

    cleared = len(
        sites[
            sites["Status"]
            .astype(str)
            .str.lower()
            == "cleared"
        ]
    )

    infested = len(
        sites[
            sites["Status"]
            .astype(str)
            .str.lower()
            == "infested"
        ]
    )

    monitoring_count = len(
        sites[
            sites["Status"]
            .astype(str)
            .str.lower()
            == "monitoring"
        ]
    )

    high_risk = len(
        sites[
            sites["Risk"]
            .astype(str)
            .str.lower()
            == "high"
        ]
    )

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric(
        "Total Sites",
        total_sites
    )

    c2.metric(
        "Cleared",
        cleared
    )

    c3.metric(
        "Infested",
        infested
    )

    c4.metric(
        "Monitoring",
        monitoring_count
    )

    c5.metric(
        "High Risk",
        high_risk
    )

    st.markdown("---")

    st.subheader(
        "📋 Site Overview"
    )

    show_table(
        sites[
            [
                "Site ID",
                "District",
                "Taluk",
                "Village",
                "Area (ha)",
                "Infestation",
                "Risk",
                "Status"
            ]
        ]
    )


# ============================================================
# MODULE 2
# REGISTER NEW SITE
# ============================================================

elif module == "Register New Site":

    st.title(
        "➕ Register New Site"
    )

    with st.form(
        "register_site_form"
    ):

        col1, col2 = st.columns(2)

        with col1:

            site_id = st.text_input(
                "Site ID",
                value=f"PJ{len(sites) + 1:03d}"
            )

            district = st.text_input(
                "District"
            )

            taluk = st.text_input(
                "Taluk"
            )

            village = st.text_input(
                "Village"
            )

            latitude = st.number_input(
                "Latitude",
                value=10.8505,
                format="%.6f"
            )

            longitude = st.number_input(
                "Longitude",
                value=78.7047,
                format="%.6f"
            )

            area = st.number_input(
                "Area (ha)",
                min_value=0.0,
                value=1.0
            )

        with col2:

            infestation = st.selectbox(
                "Infestation",
                [
                    "High",
                    "Medium",
                    "Low"
                ]
            )

            risk = st.selectbox(
                "Risk",
                [
                    "High",
                    "Medium",
                    "Low"
                ]
            )

            status = st.selectbox(
                "Status",
                [
                    "Infested",
                    "Cleared",
                    "Monitoring"
                ]
            )

            clearance_method = st.selectbox(
                "Clearance Method",
                [
                    "Not Cleared",
                    "Manual Removal",
                    "Mechanical Removal",
                    "Root Removal",
                    "Integrated Eradication"
                ]
            )

            budget_allocated = st.number_input(
                "Budget Allocated",
                min_value=0.0,
                value=0.0
            )

            budget_used = st.number_input(
                "Budget Used",
                min_value=0.0,
                value=0.0
            )

            biomass = st.number_input(
                "Biomass (tonnes)",
                min_value=0.0,
                value=0.0
            )

        submitted = st.form_submit_button(
            "Register Site"
        )

    if submitted:

        if not site_id.strip():

            st.error(
                "Site ID is required."
            )

        elif site_id in sites[
            "Site ID"
        ].astype(str).values:

            st.error(
                "Site ID already exists."
            )

        elif not district.strip():

            st.error(
                "District is required."
            )

        elif not taluk.strip():

            st.error(
                "Taluk is required."
            )

        elif not village.strip():

            st.error(
                "Village is required."
            )

        elif budget_used > budget_allocated:

            st.error(
                "Budget Used cannot be greater "
                "than Budget Allocated."
            )

        else:

            new_site = {
                "Site ID": site_id.strip(),
                "District": district.strip(),
                "Taluk": taluk.strip(),
                "Village": village.strip(),
                "Latitude": latitude,
                "Longitude": longitude,
                "Area (ha)": area,
                "Infestation": infestation,
                "Risk": risk,
                "Status": status,
                "Clearance Method": clearance_method,
                "Budget Allocated": budget_allocated,
                "Budget Used": budget_used,
                "Biomass (tonnes)": biomass,
                "Clearance Date": "",
                "Officer Name": "",
                "Clearance Remarks": "",
                "Before Image": "",
                "After Image": "",
                "AI Prediction": "",
                "AI Confidence": "",
                "Officer Decision": "",
                "Verification Remarks": ""
            }

            sites = pd.concat(
                [
                    sites,
                    pd.DataFrame(
                        [new_site]
                    )
                ],
                ignore_index=True
            )

            save_sites(
                sites
            )

            st.success(
                f"Site {site_id} "
                "registered successfully."
            )


# ============================================================
# MODULE 3
# TAMIL NADU MAP
# ============================================================

elif module == "Tamil Nadu Map":

    st.title(
        "🗺️ Tamil Nadu Karuvelam Site Map"
    )

    st.write(
        "Interactive map showing registered monitoring sites."
    )

    map_df = sites.copy()

    col1, col2, col3 = st.columns(3)

    with col1:

        district_filter = st.selectbox(
            "District",
            [
                "All"
            ]
            +
            sorted(
                sites["District"]
                .dropna()
                .astype(str)
                .unique()
                .tolist()
            )
        )

    with col2:

        risk_filter = st.selectbox(
            "Risk",
            [
                "All",
                "High",
                "Medium",
                "Low"
            ]
        )

    with col3:

        status_filter = st.selectbox(
            "Status",
            [
                "All",
                "Infested",
                "Cleared",
                "Monitoring"
            ]
        )

    if district_filter != "All":

        map_df = map_df[
            map_df["District"]
            == district_filter
        ]

    if risk_filter != "All":

        map_df = map_df[
            map_df["Risk"]
            == risk_filter
        ]

    if status_filter != "All":

        map_df = map_df[
            map_df["Status"]
            == status_filter
        ]

    st.info(
        f"Showing {len(map_df)} site(s)."
    )

    st.components.v1.html(
        create_map_html(map_df),
        height=680
    )

    st.markdown(
        """
        **Legend**

        🔴 High Risk

        🟠 Medium Risk

        🟢 Low Risk
        """
    )


# ============================================================
# MODULE 4
# SITE DETAILS
# ============================================================

elif module == "Site Details":

    st.title(
        "🔎 Site Details"
    )

    selected_site = st.selectbox(
        "Select Site",
        sites["Site ID"]
        .astype(str)
        .tolist()
    )

    site_row = sites[
        sites["Site ID"]
        .astype(str)
        == selected_site
    ]

    if not site_row.empty:

        row = site_row.iloc[0]

        st.subheader(
            f"Site {selected_site}"
        )

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "District",
            str(row["District"])
        )

        c2.metric(
            "Area",
            f"{row['Area (ha)']} ha"
        )

        c3.metric(
            "Risk",
            str(row["Risk"])
        )

        details = pd.DataFrame({
            "Field": row.index,
            "Value": row.values
        })

        show_table(
            details
        )


# ============================================================
# MODULE 5
# CLEARANCE
# ============================================================

elif module == "Clearance":

    st.title(
        "🛠️ Site Clearance"
    )

    selected_site = st.selectbox(
        "Select Site",
        sites["Site ID"]
        .astype(str)
        .tolist()
    )

    site_index = sites.index[
        sites["Site ID"]
        .astype(str)
        == selected_site
    ].tolist()[0]

    current_row = sites.loc[
        site_index
    ]

    st.write(
        f"Current Status: "
        f"**{current_row['Status']}**"
    )

    with st.form(
        "clearance_form"
    ):

        method = st.selectbox(
            "Clearance Method",
            [
                "Manual Removal",
                "Mechanical Removal",
                "Root Removal",
                "Integrated Eradication"
            ]
        )

        clearance_date = st.date_input(
            "Clearance Date",
            value=date.today()
        )

        officer = st.text_input(
            "Officer Name"
        )

        budget_used = st.number_input(
            "Budget Used",
            min_value=0.0,
            value=float(
                pd.to_numeric(
                    current_row[
                        "Budget Used"
                    ],
                    errors="coerce"
                )
                or 0
            )
        )

        biomass = st.number_input(
            "Biomass Removed (tonnes)",
            min_value=0.0,
            value=float(
                pd.to_numeric(
                    current_row[
                        "Biomass (tonnes)"
                    ],
                    errors="coerce"
                )
                or 0
            )
        )

        remarks = st.text_area(
            "Clearance Remarks"
        )

        submit = st.form_submit_button(
            "Update Clearance"
        )

    if submit:

        allocated = float(
            pd.to_numeric(
                current_row[
                    "Budget Allocated"
                ],
                errors="coerce"
            )
            or 0
        )

        if budget_used > allocated:

            st.error(
                "Budget Used cannot exceed "
                "allocated budget."
            )

        elif not officer.strip():

            st.error(
                "Officer name is required."
            )

        else:

            sites.loc[
                site_index,
                "Status"
            ] = "Cleared"

            sites.loc[
                site_index,
                "Clearance Method"
            ] = method

            sites.loc[
                site_index,
                "Clearance Date"
            ] = str(
                clearance_date
            )

            sites.loc[
                site_index,
                "Officer Name"
            ] = officer.strip()

            sites.loc[
                site_index,
                "Budget Used"
            ] = budget_used

            sites.loc[
                site_index,
                "Biomass (tonnes)"
            ] = biomass

            sites.loc[
                site_index,
                "Clearance Remarks"
            ] = remarks

            save_sites(
                sites
            )

            st.success(
                f"Clearance information "
                f"updated for {selected_site}."
            )


# ============================================================
# MODULE 6
# BEFORE / AFTER EVIDENCE
# ============================================================

elif module == "Before / After Evidence":

    st.title(
        "📸 Before / After Evidence"
    )

    selected_site = st.selectbox(
        "Select Site",
        sites["Site ID"]
        .astype(str)
        .tolist()
    )

    site_index = sites.index[
        sites["Site ID"]
        .astype(str)
        == selected_site
    ].tolist()[0]

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(
            "Before Image"
        )

        before_image = st.file_uploader(
            "Upload Before Image",
            type=[
                "jpg",
                "jpeg",
                "png"
            ],
            key=f"before_{selected_site}"
        )

        if before_image is not None:

            extension = os.path.splitext(
                before_image.name
            )[1]

            filename = (
                f"{selected_site}_before"
                f"{extension}"
            )

            path = os.path.join(
                BEFORE_DIR,
                filename
            )

            with open(
                path,
                "wb"
            ) as f:

                f.write(
                    before_image.getbuffer()
                )

            sites.loc[
                site_index,
                "Before Image"
            ] = path

            save_sites(
                sites
            )

            st.image(
                before_image,
                caption="Before",
                width=400
            )

            st.success(
                "Before image saved."
            )

    with col2:

        st.subheader(
            "After Image"
        )

        after_image = st.file_uploader(
            "Upload After Image",
            type=[
                "jpg",
                "jpeg",
                "png"
            ],
            key=f"after_{selected_site}"
        )

        if after_image is not None:

            extension = os.path.splitext(
                after_image.name
            )[1]

            filename = (
                f"{selected_site}_after"
                f"{extension}"
            )

            path = os.path.join(
                AFTER_DIR,
                filename
            )

            with open(
                path,
                "wb"
            ) as f:

                f.write(
                    after_image.getbuffer()
                )

            sites.loc[
                site_index,
                "After Image"
            ] = path

            save_sites(
                sites
            )

            st.image(
                after_image,
                caption="After",
                width=400
            )

            st.success(
                "After image saved."
            )


# ============================================================
# MODULE 7
# AI PHOTO VERIFICATION
# ============================================================

elif module == "AI Photo Verification":

    st.title(
        "🤖 AI Photo Verification"
    )

    st.info(
        "Prototype AI verification. "
        "The current prediction is simulated. "
        "A real trained image classification model "
        "can be connected later."
    )

    selected_site = st.selectbox(
        "Select Site",
        sites["Site ID"]
        .astype(str)
        .tolist()
    )

    site_index = sites.index[
        sites["Site ID"]
        .astype(str)
        == selected_site
    ].tolist()[0]

    uploaded_image = st.file_uploader(
        "Choose an image",
        type=[
            "jpg",
            "jpeg",
            "png"
        ],
        key=f"ai_{selected_site}"
    )

    if uploaded_image is not None:

        st.image(
            uploaded_image,
            caption="Uploaded Image",
            width=450
        )

        if st.button(
            "🔍 Run AI Verification",
            key=f"run_ai_{selected_site}"
        ):

            prediction = (
                "Possible Karuvelam"
            )

            confidence = 87

            st.success(
                f"Prediction: "
                f"**{prediction}**"
            )

            st.metric(
                "AI Confidence",
                f"{confidence}%"
            )

            st.warning(
                "Officer review is required."
            )

            sites.loc[
                site_index,
                "AI Prediction"
            ] = prediction

            sites.loc[
                site_index,
                "AI Confidence"
            ] = f"{confidence}%"

            save_sites(
                sites
            )

    st.markdown("---")

    st.subheader(
        "👮 Officer Verification"
    )

    decision = st.selectbox(
        "Officer Decision",
        [
            "Approve - Karuvelam Present",
            "Reject - Karuvelam Not Present",
            "Send for Manual Review"
        ]
    )

    officer = st.text_input(
        "Officer Name",
        key=f"verification_officer_{selected_site}"
    )

    remarks = st.text_area(
        "Verification Remarks",
        key=f"verification_remarks_{selected_site}"
    )

    if st.button(
        "Save Officer Verification",
        key=f"save_verification_{selected_site}"
    ):

        sites.loc[
            site_index,
            "Officer Decision"
        ] = decision

        sites.loc[
            site_index,
            "Officer Name"
        ] = officer

        sites.loc[
            site_index,
            "Verification Remarks"
        ] = remarks

        save_sites(
            sites
        )

        st.success(
            "Officer verification saved."
        )


# ============================================================
# MODULE 8
# RISK ASSESSMENT
# ============================================================

elif module == "Risk Assessment":

    st.title(
        "⚠️ Risk Assessment"
    )

    selected_site = st.selectbox(
        "Select Site",
        sites["Site ID"]
        .astype(str)
        .tolist()
    )

    site_index = sites.index[
        sites["Site ID"]
        .astype(str)
        == selected_site
    ].tolist()[0]

    row = sites.loc[
        site_index
    ]

    infestation = str(
        row["Infestation"]
    )

    current_risk = str(
        row["Risk"]
    )

    if infestation == "High":

        calculated_risk = "High"

    elif infestation == "Medium":

        calculated_risk = "Medium"

    else:

        calculated_risk = "Low"

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Infestation",
        infestation
    )

    c2.metric(
        "Current Risk",
        current_risk
    )

    c3.metric(
        "Calculated Risk",
        calculated_risk
    )

    if calculated_risk == "High":

        st.error(
            "🚨 High-risk site. "
            "Immediate attention recommended."
        )

    elif calculated_risk == "Medium":

        st.warning(
            "⚠️ Medium-risk site. "
            "Regular monitoring recommended."
        )

    else:

        st.success(
            "✅ Low-risk site."
        )

    if st.button(
        "Update Risk Based on Infestation"
    ):

        sites.loc[
            site_index,
            "Risk"
        ] = calculated_risk

        save_sites(
            sites
        )

        st.success(
            "Risk assessment updated."
        )


# ============================================================
# MODULE 9
# BUDGET MANAGEMENT
# ============================================================

elif module == "Budget Management":

    st.title(
        "💰 Budget Management"
    )

    budget_df = sites.copy()

    budget_df[
        "Budget Allocated"
    ] = safe_number(
        budget_df[
            "Budget Allocated"
        ]
    )

    budget_df[
        "Budget Used"
    ] = safe_number(
        budget_df[
            "Budget Used"
        ]
    )

    budget_df["Balance"] = (
        budget_df[
            "Budget Allocated"
        ]
        -
        budget_df[
            "Budget Used"
        ]
    )

    total_allocated = budget_df[
        "Budget Allocated"
    ].sum()

    total_used = budget_df[
        "Budget Used"
    ].sum()

    balance = (
        total_allocated
        - total_used
    )

    utilization = (
        total_used
        /
        total_allocated
        *
        100
        if total_allocated > 0
        else 0
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Total Allocated",
        f"₹{total_allocated:,.0f}"
    )

    c2.metric(
        "Total Used",
        f"₹{total_used:,.0f}"
    )

    c3.metric(
        "Balance",
        f"₹{balance:,.0f}"
    )

    c4.metric(
        "Utilization",
        f"{utilization:.1f}%"
    )

    show_table(
        budget_df[
            [
                "Site ID",
                "District",
                "Budget Allocated",
                "Budget Used",
                "Balance"
            ]
        ]
    )


# ============================================================
# MODULE 10
# BIOMASS UTILISATION
# ============================================================

elif module == "Biomass Utilisation":

    st.title(
        "🌱 Biomass Utilisation"
    )

    biomass_df = sites.copy()

    biomass_df[
        "Biomass (tonnes)"
    ] = safe_number(
        biomass_df[
            "Biomass (tonnes)"
        ]
    )

    total_biomass = biomass_df[
        "Biomass (tonnes)"
    ].sum()

    cleared_sites = len(
        biomass_df[
            biomass_df["Status"]
            .astype(str)
            .str.lower()
            == "cleared"
        ]
    )

    c1, c2 = st.columns(2)

    c1.metric(
        "Total Biomass Removed",
        f"{total_biomass:.2f} tonnes"
    )

    c2.metric(
        "Cleared Sites",
        cleared_sites
    )

    show_table(
        biomass_df[
            [
                "Site ID",
                "District",
                "Village",
                "Biomass (tonnes)",
                "Status"
            ]
        ]
    )

    st.info(
        "Biomass utilisation can be expanded "
        "with transport and value-recovery records."
    )


# ============================================================
# MODULE 11
# SITE HISTORY
# ============================================================

elif module == "Site History":

    st.title(
        "📜 Site History / Audit Trail"
    )

    selected_site = st.selectbox(
        "Select Site",
        sites["Site ID"]
        .astype(str)
        .tolist()
    )

    row = sites[
        sites["Site ID"]
        .astype(str)
        == selected_site
    ]

    if not row.empty:

        r = row.iloc[0]

        timeline = []

        timeline.append({
            "Date": "Registration",
            "Event": "Site Registered",
            "Details":
                f"Site registered in "
                f"{r['District']}"
        })

        if str(
            r["Clearance Date"]
        ).strip():

            timeline.append({
                "Date":
                    str(
                        r["Clearance Date"]
                    ),
                "Event":
                    "Clearance",
                "Details":
                    str(
                        r["Clearance Remarks"]
                    )
            })

        if str(
            r["Before Image"]
        ).strip():

            timeline.append({
                "Date":
                    "Evidence",
                "Event":
                    "Before Image Uploaded",
                "Details":
                    str(
                        r["Before Image"]
                    )
            })

        if str(
            r["After Image"]
        ).strip():

            timeline.append({
                "Date":
                    "Evidence",
                "Event":
                    "After Image Uploaded",
                "Details":
                    str(
                        r["After Image"]
                    )
            })

        if str(
            r["AI Prediction"]
        ).strip():

            timeline.append({
                "Date":
                    "AI Verification",
                "Event":
                    "AI Photo Verification",
                "Details":
                    f"{r['AI Prediction']} "
                    f"({r['AI Confidence']})"
            })

        if str(
            r["Officer Decision"]
        ).strip():

            timeline.append({
                "Date":
                    "Verification",
                "Event":
                    "Officer Decision",
                "Details":
                    str(
                        r["Officer Decision"]
                    )
            })

        show_table(
            pd.DataFrame(
                timeline
            )
        )


# ============================================================
# MODULE 12
# MONITORING & REGROWTH
# ============================================================

elif module == "Monitoring & Regrowth":

    st.title(
        "🌿 Monitoring & Regrowth"
    )

    selected_site = st.selectbox(
        "Select Site",
        sites["Site ID"]
        .astype(str)
        .tolist()
    )

    with st.form(
        "monitoring_form"
    ):

        inspection_date = st.date_input(
            "Inspection Date",
            value=date.today()
        )

        officer = st.text_input(
            "Officer Name"
        )

        new_shoots = st.selectbox(
            "New Shoots Observed",
            [
                "Yes",
                "No"
            ]
        )

        regrowth_percentage = st.number_input(
            "Regrowth Percentage",
            min_value=0.0,
            max_value=100.0,
            value=0.0
        )

        condition = st.selectbox(
            "Site Condition",
            [
                "Good",
                "Needs Attention",
                "Poor"
            ]
        )

        observations = st.text_area(
            "Observations"
        )

        submit = st.form_submit_button(
            "Save Monitoring Record"
        )

    if submit:

        if regrowth_percentage >= 50:

            severity = "High"

            action = (
                "Immediate Re-eradication Required"
            )

        elif regrowth_percentage >= 20:

            severity = "Medium"

            action = (
                "Increased Monitoring Required"
            )

        elif new_shoots == "Yes":

            severity = "Medium"

            action = (
                "Follow-up Monitoring Required"
            )

        else:

            severity = "Low"

            action = (
                "Continue Regular Monitoring"
            )

        monitoring = load_monitoring()

        monitoring_id = (
            f"MON-{selected_site}-"
            f"{len(monitoring) + 1:03d}"
        )

        new_record = {
            "Monitoring ID":
                monitoring_id,
            "Site ID":
                selected_site,
            "Inspection Date":
                str(inspection_date),
            "Officer Name":
                officer,
            "New Shoots":
                new_shoots,
            "Regrowth Percentage":
                regrowth_percentage,
            "Site Condition":
                condition,
            "Regrowth Severity":
                severity,
            "Observations":
                observations,
            "Action Required":
                action
        }

        monitoring = pd.concat(
            [
                monitoring,
                pd.DataFrame(
                    [new_record]
                )
            ],
            ignore_index=True
        )

        monitoring.to_csv(
            MONITORING_FILE,
            index=False
        )

        sites = load_sites()

        site_index = sites.index[
            sites["Site ID"]
            .astype(str)
            == selected_site
        ].tolist()[0]

        sites.loc[
            site_index,
            "Status"
        ] = "Monitoring"

        sites.loc[
            site_index,
            "Risk"
        ] = severity

        save_sites(
            sites
        )

        st.success(
            f"Monitoring record "
            f"{monitoring_id} saved."
        )

    st.markdown("---")

    monitoring = load_monitoring()

    site_monitoring = monitoring[
        monitoring["Site ID"]
        .astype(str)
        == selected_site
    ]

    st.subheader(
        "Monitoring History"
    )

    show_table(
        site_monitoring
    )


# ============================================================
# MODULE 13
# GOVERNMENT SCHEMES
# ============================================================

elif module == "Government Schemes":

    st.title(
        "🏛️ Government Schemes & Projects"
    )

    with st.form(
        "scheme_form"
    ):

        col1, col2 = st.columns(2)

        with col1:

            scheme_id = st.text_input(
                "Scheme ID",
                value=f"SCH{len(schemes) + 1:03d}"
            )

            scheme_name = st.text_input(
                "Scheme Name"
            )

            department = st.text_input(
                "Department"
            )

            financial_year = st.text_input(
                "Financial Year",
                value="2026-27"
            )

            district = st.text_input(
                "District"
            )

            officer = st.text_input(
                "Project Officer"
            )

        with col2:

            start_date = st.date_input(
                "Start Date",
                value=date.today()
            )

            end_date = st.date_input(
                "End Date",
                value=date.today()
            )

            target_area = st.number_input(
                "Target Area (ha)",
                min_value=0.0,
                value=0.0
            )

            cleared_area = st.number_input(
                "Cleared Area (ha)",
                min_value=0.0,
                value=0.0
            )

            budget_allocated = st.number_input(
                "Budget Allocated",
                min_value=0.0,
                value=0.0
            )

            budget_released = st.number_input(
                "Budget Released",
                min_value=0.0,
                value=0.0
            )

            budget_utilized = st.number_input(
                "Budget Utilized",
                min_value=0.0,
                value=0.0
            )

            status = st.selectbox(
                "Project Status",
                [
                    "Planned",
                    "Ongoing",
                    "Completed",
                    "Monitoring"
                ]
            )

        remarks = st.text_area(
            "Remarks"
        )

        submit = st.form_submit_button(
            "Create Scheme"
        )

    if submit:

        schemes = load_schemes()

        errors = []

        if scheme_id in schemes[
            "Scheme ID"
        ].astype(str).values:

            errors.append(
                "Scheme ID already exists."
            )

        if not scheme_name.strip():

            errors.append(
                "Scheme Name is required."
            )

        if not officer.strip():

            errors.append(
                "Project Officer is required."
            )

        if end_date < start_date:

            errors.append(
                "End Date cannot be before Start Date."
            )

        if cleared_area > target_area:

            errors.append(
                "Cleared Area cannot exceed Target Area."
            )

        if budget_released > budget_allocated:

            errors.append(
                "Budget Released cannot exceed Budget Allocated."
            )

        if budget_utilized > budget_released:

            errors.append(
                "Budget Utilized cannot exceed Budget Released."
            )

        if errors:

            for error in errors:
                st.error(error)

        else:

            new_scheme = {
                "Scheme ID":
                    scheme_id,
                "Scheme Name":
                    scheme_name,
                "Department":
                    department,
                "Financial Year":
                    financial_year,
                "District":
                    district,
                "Project Officer":
                    officer,
                "Start Date":
                    str(start_date),
                "End Date":
                    str(end_date),
                "Target Area (ha)":
                    target_area,
                "Cleared Area (ha)":
                    cleared_area,
                "Budget Allocated":
                    budget_allocated,
                "Budget Released":
                    budget_released,
                "Budget Utilized":
                    budget_utilized,
                "Project Status":
                    status,
                "Remarks":
                    remarks
            }

            schemes = pd.concat(
                [
                    schemes,
                    pd.DataFrame(
                        [new_scheme]
                    )
                ],
                ignore_index=True
            )

            schemes.to_csv(
                SCHEMES_FILE,
                index=False
            )

            st.success(
                f"Scheme {scheme_id} "
                "created successfully."
            )

    st.markdown("---")

    schemes = load_schemes()

    show_table(
        schemes
    )


# ============================================================
# MODULE 14
# PROJECT-SITE LINKING
# ============================================================

elif module == "Project-Site Linking":

    st.title(
        "🔗 Project ↔ Site Linking"
    )

    schemes = load_schemes()

    project_sites = load_project_sites()

    sites = load_sites()

    if schemes.empty:

        st.warning(
            "Create a Government Scheme first."
        )

    else:

        with st.form(
            "link_site_form"
        ):

            scheme_id = st.selectbox(
                "Select Scheme",
                schemes["Scheme ID"]
                .astype(str)
                .tolist()
            )

            site_id = st.selectbox(
                "Select Site",
                sites["Site ID"]
                .astype(str)
                .tolist()
            )

            linked_by = st.text_input(
                "Linked By"
            )

            remarks = st.text_area(
                "Remarks"
            )

            submit = st.form_submit_button(
                "Link Site to Project"
            )

        if submit:

            duplicate = project_sites[
                (
                    project_sites[
                        "Scheme ID"
                    ].astype(str)
                    == scheme_id
                )
                &
                (
                    project_sites[
                        "Site ID"
                    ].astype(str)
                    == site_id
                )
            ]

            if not duplicate.empty:

                st.error(
                    "This site is already linked."
                )

            elif not linked_by.strip():

                st.error(
                    "Linked By is required."
                )

            else:

                project_site_id = (
                    f"PS"
                    f"{len(project_sites) + 1:04d}"
                )

                new_link = {
                    "Project Site ID":
                        project_site_id,
                    "Scheme ID":
                        scheme_id,
                    "Site ID":
                        site_id,
                    "Linked Date":
                        str(date.today()),
                    "Linked By":
                        linked_by,
                    "Remarks":
                        remarks
                }

                project_sites = pd.concat(
                    [
                        project_sites,
                        pd.DataFrame(
                            [new_link]
                        )
                    ],
                    ignore_index=True
                )

                project_sites.to_csv(
                    PROJECT_SITES_FILE,
                    index=False
                )

                st.success(
                    f"Site {site_id} "
                    f"linked to {scheme_id}."
                )

    st.markdown("---")

    project_sites = load_project_sites()

    show_table(
        project_sites
    )

    if not project_sites.empty:

        st.subheader(
            "📊 Project Analytics"
        )

        selected_scheme = st.selectbox(
            "View Scheme Performance",
            sorted(
                project_sites[
                    "Scheme ID"
                ]
                .astype(str)
                .unique()
                .tolist()
            )
        )

        linked_ids = project_sites[
            project_sites[
                "Scheme ID"
            ].astype(str)
            == selected_scheme
        ][
            "Site ID"
        ].astype(str).tolist()

        linked_data = sites[
            sites[
                "Site ID"
            ].astype(str)
            .isin(linked_ids)
        ]

        total_linked = len(
            linked_data
        )

        total_area = safe_number(
            linked_data[
                "Area (ha)"
            ]
        ).sum()

        high_risk = len(
            linked_data[
                linked_data[
                    "Risk"
                ]
                .astype(str)
                .str.lower()
                == "high"
            ]
        )

        cleared = len(
            linked_data[
                linked_data[
                    "Status"
                ]
                .astype(str)
                .str.lower()
                == "cleared"
            ]
        )

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Linked Sites",
            total_linked
        )

        c2.metric(
            "Linked Area",
            f"{total_area:.2f} ha"
        )

        c3.metric(
            "High Risk",
            high_risk
        )

        c4.metric(
            "Cleared",
            cleared
        )


# ============================================================
# MODULE 15
# SMS ALERTS
# ============================================================

elif module == "SMS Alerts":

    st.title(
        "📱 SMS Alerts"
    )

    sites = load_sites()

    alerts = load_alerts()

    st.info(
        "Prototype SMS alert management. "
        "Actual SMS gateway integration can "
        "be connected later."
    )

    for _, row in sites.iterrows():

        site_id = str(
            row["Site ID"]
        )

        risk = str(
            row["Risk"]
        )

        status = str(
            row["Status"]
        )

        if risk.lower() == "high":

            alert_type = (
                "High Risk Site"
            )

            severity = "High"

            message = (
                f"High-risk Karuvelam site "
                f"{site_id} requires immediate "
                f"field inspection."
            )

            action_required = (
                "Field Inspection Required"
            )

        elif status.lower() == "monitoring":

            alert_type = (
                "Monitoring Alert"
            )

            severity = "Medium"

            message = (
                f"Site {site_id} is under "
                f"monitoring."
            )

            action_required = (
                "Continue Monitoring"
            )

        else:

            continue

        existing = alerts[
            (
                alerts[
                    "Site ID"
                ].astype(str)
                == site_id
            )
            &
            (
                alerts[
                    "Status"
                ].astype(str)
                .str.lower()
                .isin(
                    [
                        "open",
                        "in progress"
                    ]
                )
            )
        ]

        if existing.empty:

            alert_id = generate_id(
                "ALT",
                alerts,
                "Alert ID"
            )

            new_alert = {
                "Alert ID":
                    alert_id,
                "Site ID":
                    site_id,
                "Alert Date":
                    str(date.today()),
                "Alert Type":
                    alert_type,
                "Severity":
                    severity,
                "Message":
                    message,
                "Action Required":
                    action_required,
                "Status":
                    "Open"
            }

            alerts = pd.concat(
                [
                    alerts,
                    pd.DataFrame(
                        [new_alert]
                    )
                ],
                ignore_index=True
            )

    alerts.to_csv(
        ALERTS_FILE,
        index=False
    )

    show_table(
        alerts
    )

    open_alerts = len(
        alerts[
            alerts[
                "Status"
            ]
            .astype(str)
            .str.lower()
            == "open"
        ]
    )

    high_alerts = len(
        alerts[
            alerts[
                "Severity"
            ]
            .astype(str)
            .str.lower()
            == "high"
        ]
    )

    c1, c2 = st.columns(2)

    c1.metric(
        "Open Alerts",
        open_alerts
    )

    c2.metric(
        "High Severity Alerts",
        high_alerts
    )


# ============================================================
# MODULE 16
# OFFICER ACTION
# ============================================================

elif module == "Officer Action":

    st.title(
        "👮 Officer Action & Alert Closure"
    )

    alerts = load_alerts()

    alert_actions = load_alert_actions()

    sites = load_sites()

    open_alerts = alerts[
        alerts[
            "Status"
        ]
        .astype(str)
        .str.lower()
        .isin(
            [
                "open",
                "in progress"
            ]
        )
    ]

    if open_alerts.empty:

        st.success(
            "🎉 No open alerts."
        )

    else:

        selected_alert = st.selectbox(
            "Select Alert",
            open_alerts[
                "Alert ID"
            ]
            .astype(str)
            .tolist()
        )

        alert_row = open_alerts[
            open_alerts[
                "Alert ID"
            ].astype(str)
            == selected_alert
        ].iloc[0]

        site_id = str(
            alert_row["Site ID"]
        )

        st.subheader(
            f"Alert {selected_alert}"
        )

        st.write(
            f"**Site:** {site_id}"
        )

        st.write(
            f"**Severity:** "
            f"{alert_row['Severity']}"
        )

        st.write(
            f"**Message:** "
            f"{alert_row['Message']}"
        )

        with st.form(
            "officer_action_form"
        ):

            officer = st.text_input(
                "Officer Name"
            )

            action_taken = st.selectbox(
                "Action Taken",
                [
                    "Field Inspection",
                    "Manual Removal",
                    "Mechanical Removal",
                    "Root Removal",
                    "Integrated Eradication",
                    "Site Reinspection",
                    "No Action Required",
                    "Other"
                ]
            )

            action_remarks = st.text_area(
                "Action Remarks"
            )

            evidence_image = st.file_uploader(
                "Action Evidence Image",
                type=[
                    "jpg",
                    "jpeg",
                    "png"
                ]
            )

            action_status = st.selectbox(
                "Action Status",
                [
                    "In Progress",
                    "Resolved",
                    "Rejected"
                ]
            )

            submit = st.form_submit_button(
                "Save Officer Action"
            )

        if submit:

            if not officer.strip():

                st.error(
                    "Officer Name is required."
                )

            else:

                evidence_path = ""

                if evidence_image is not None:

                    extension = os.path.splitext(
                        evidence_image.name
                    )[1]

                    action_id_temp = (
                        f"ACT"
                        f"{len(alert_actions) + 1:04d}"
                    )

                    evidence_filename = (
                        f"{action_id_temp}_"
                        f"{site_id}"
                        f"{extension}"
                    )

                    evidence_path = os.path.join(
                        ACTION_DIR,
                        evidence_filename
                    )

                    with open(
                        evidence_path,
                        "wb"
                    ) as f:

                        f.write(
                            evidence_image.getbuffer()
                        )

                action_id = (
                    f"ACT"
                    f"{len(alert_actions) + 1:04d}"
                )

                new_action = {
                    "Action ID":
                        action_id,
                    "Alert ID":
                        selected_alert,
                    "Site ID":
                        site_id,
                    "Action Date":
                        str(date.today()),
                    "Officer Name":
                        officer,
                    "Action Taken":
                        action_taken,
                    "Action Remarks":
                        action_remarks,
                    "Evidence Image":
                        evidence_path,
                    "Action Status":
                        action_status
                }

                alert_actions = pd.concat(
                    [
                        alert_actions,
                        pd.DataFrame(
                            [new_action]
                        )
                    ],
                    ignore_index=True
                )

                alert_actions.to_csv(
                    ALERT_ACTIONS_FILE,
                    index=False
                )

                alerts = load_alerts()

                alert_index = alerts.index[
                    alerts[
                        "Alert ID"
                    ].astype(str)
                    == selected_alert
                ].tolist()[0]

                if action_status == "Resolved":

                    alerts.loc[
                        alert_index,
                        "Status"
                    ] = "Resolved"

                elif action_status == "Rejected":

                    alerts.loc[
                        alert_index,
                        "Status"
                    ] = "Rejected"

                else:

                    alerts.loc[
                        alert_index,
                        "Status"
                    ] = "In Progress"

                alerts.to_csv(
                    ALERTS_FILE,
                    index=False
                )

                if action_status == "Resolved":

                    sites = load_sites()

                    site_indices = sites.index[
                        sites[
                            "Site ID"
                        ].astype(str)
                        == site_id
                    ].tolist()

                    if site_indices:

                        site_index = site_indices[0]

                        if action_taken in [
                            "Manual Removal",
                            "Mechanical Removal",
                            "Root Removal",
                            "Integrated Eradication"
                        ]:

                            sites.loc[
                                site_index,
                                "Status"
                            ] = "Cleared"

                        save_sites(
                            sites
                        )

                st.success(
                    f"Officer action "
                    f"{action_id} saved."
                )

    st.markdown("---")

    show_table(
        load_alert_actions()
    )


# ============================================================
# MODULE 29
# GOVERNMENT PERFORMANCE ANALYTICS
# ============================================================

elif module == "Government Performance Analytics":

    st.title(
        "🏛️ Government Performance Analytics"
    )

    st.write(
        "Overall performance of "
        "Seemai Karuvelam eradication activities."
    )

    sites = load_sites()

    total_sites = len(
        sites
    )

    cleared_sites = len(
        sites[
            sites[
                "Status"
            ]
            .astype(str)
            .str.lower()
            == "cleared"
        ]
    )

    infested_sites = len(
        sites[
            sites[
                "Status"
            ]
            .astype(str)
            .str.lower()
            == "infested"
        ]
    )

    monitoring_sites = len(
        sites[
            sites[
                "Status"
            ]
            .astype(str)
            .str.lower()
            == "monitoring"
        ]
    )

    high_risk_sites = len(
        sites[
            sites[
                "Risk"
            ]
            .astype(str)
            .str.lower()
            == "high"
        ]
    )

    sites[
        "Area (ha)"
    ] = safe_number(
        sites[
            "Area (ha)"
        ]
    )

    sites[
        "Budget Allocated"
    ] = safe_number(
        sites[
            "Budget Allocated"
        ]
    )

    sites[
        "Budget Used"
    ] = safe_number(
        sites[
            "Budget Used"
        ]
    )

    sites[
        "Biomass (tonnes)"
    ] = safe_number(
        sites[
            "Biomass (tonnes)"
        ]
    )

    total_area = sites[
        "Area (ha)"
    ].sum()

    cleared_area = sites.loc[
        sites[
            "Status"
        ]
        .astype(str)
        .str.lower()
        == "cleared",
        "Area (ha)"
    ].sum()

    total_budget = sites[
        "Budget Allocated"
    ].sum()

    budget_used = sites[
        "Budget Used"
    ].sum()

    total_biomass = sites[
        "Biomass (tonnes)"
    ].sum()

    if total_budget > 0:

        budget_utilization = (
            budget_used
            /
            total_budget
            *
            100
        )

    else:

        budget_utilization = 0

    if total_sites > 0:

        clearance_rate = (
            cleared_sites
            /
            total_sites
            *
            100
        )

    else:

        clearance_rate = 0

    st.subheader(
        "📊 Program Overview"
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Total Sites",
        total_sites
    )

    c2.metric(
        "Cleared Sites",
        cleared_sites
    )

    c3.metric(
        "Infested Sites",
        infested_sites
    )

    c4.metric(
        "Monitoring Sites",
        monitoring_sites
    )

    c5, c6, c7, c8 = st.columns(4)

    c5.metric(
        "Total Area",
        f"{total_area:.2f} ha"
    )

    c6.metric(
        "Cleared Area",
        f"{cleared_area:.2f} ha"
    )

    c7.metric(
        "High Risk Sites",
        high_risk_sites
    )

    c8.metric(
        "Clearance Rate",
        f"{clearance_rate:.1f}%"
    )

    st.markdown("---")

    st.subheader(
        "💰 Financial Performance"
    )

    b1, b2, b3 = st.columns(3)

    b1.metric(
        "Budget Allocated",
        f"₹{total_budget:,.0f}"
    )

    b2.metric(
        "Budget Used",
        f"₹{budget_used:,.0f}"
    )

    b3.metric(
        "Budget Utilization",
        f"{budget_utilization:.1f}%"
    )

    st.subheader(
        "🌱 Environmental Impact"
    )

    e1, e2 = st.columns(2)

    e1.metric(
        "Biomass Removed",
        f"{total_biomass:.2f} tonnes"
    )

    e2.metric(
        "Area Cleared",
        f"{cleared_area:.2f} hectares"
    )

    st.subheader(
        "📌 Site Status Summary"
    )

    status_summary = pd.DataFrame({
        "Status": [
            "Cleared",
            "Infested",
            "Monitoring"
        ],
        "Number of Sites": [
            cleared_sites,
            infested_sites,
            monitoring_sites
        ]
    })

    show_table(
        status_summary
    )

    st.subheader(
        "⚠️ Risk Summary"
    )

    risk_summary = (
        sites[
            "Risk"
        ]
        .astype(str)
        .value_counts()
        .reset_index()
    )

    risk_summary.columns = [
        "Risk Level",
        "Number of Sites"
    ]

    show_table(
        risk_summary
    )

    st.subheader(
        "📍 District-wise Performance"
    )

    district_summary = (
        sites
        .groupby(
            "District"
        )
        .agg(
            Total_Sites=(
                "Site ID",
                "count"
            ),
            Total_Area_ha=(
                "Area (ha)",
                "sum"
            ),
            Total_Budget=(
                "Budget Allocated",
                "sum"
            ),
            Budget_Used=(
                "Budget Used",
                "sum"
            ),
            Biomass=(
                "Biomass (tonnes)",
                "sum"
            )
        )
        .reset_index()
    )

    district_cleared = (
        sites[
            sites[
                "Status"
            ]
            .astype(str)
            .str.lower()
            == "cleared"
        ]
        .groupby(
            "District"
        )
        .size()
        .reset_index(
            name="Cleared_Sites"
        )
    )

    district_summary = district_summary.merge(
        district_cleared,
        on="District",
        how="left"
    )

    district_summary[
        "Cleared_Sites"
    ] = (
        district_summary[
            "Cleared_Sites"
        ]
        .fillna(0)
        .astype(int)
    )

    district_summary[
        "Clearance_Rate_%"
    ] = (
        district_summary[
            "Cleared_Sites"
        ]
        /
        district_summary[
            "Total_Sites"
        ]
        *
        100
    ).round(1)

    district_summary[
        "Total_Area_ha"
    ] = district_summary[
        "Total_Area_ha"
    ].round(2)

    district_summary[
        "Total_Budget"
    ] = district_summary[
        "Total_Budget"
    ].round(0)

    district_summary[
        "Budget_Used"
    ] = district_summary[
        "Budget_Used"
    ].round(0)

    district_summary[
        "Biomass"
    ] = district_summary[
        "Biomass"
    ].round(2)

    show_table(
        district_summary
    )

    st.subheader(
        "🧭 Government Decision Support"
    )

    if high_risk_sites > 0:

        st.warning(
            f"⚠️ {high_risk_sites} high-risk "
            "site(s) require attention."
        )

    else:

        st.success(
            "✅ No high-risk sites."
        )

    if budget_utilization > 90:

        st.warning(
            "💰 Budget utilization is above 90%."
        )

    elif budget_utilization > 70:

        st.info(
            "💰 Budget utilization is above 70%."
        )

    else:

        st.info(
            "💰 Budget utilization is below 70%."
        )

    if clearance_rate >= 75:

        st.success(
            "🎯 Overall clearance performance is strong."
        )

    elif clearance_rate >= 50:

        st.info(
            "📈 Clearance performance is moderate."
        )

    else:

        st.warning(
            "🚨 Clearance performance is low."
        )


# ============================================================
# MODULE 30
# DISTRICT / TALUK / VILLAGE ANALYTICS
# ============================================================

elif module == "District / Taluk / Village Analytics":

    st.title(
        "📍 District / Taluk / Village Analytics"
    )

    st.write(
        "Geographical performance analysis of "
        "Seemai Karuvelam eradication activities."
    )

    sites = load_sites()

    # --------------------------------------------------------
    # PREPARE DATA
    # --------------------------------------------------------

    analytics_df = sites.copy()

    analytics_df[
        "Area (ha)"
    ] = safe_number(
        analytics_df[
            "Area (ha)"
        ]
    )

    analytics_df[
        "Budget Allocated"
    ] = safe_number(
        analytics_df[
            "Budget Allocated"
        ]
    )

    analytics_df[
        "Budget Used"
    ] = safe_number(
        analytics_df[
            "Budget Used"
        ]
    )

    analytics_df[
        "Biomass (tonnes)"
    ] = safe_number(
        analytics_df[
            "Biomass (tonnes)"
        ]
    )

    # --------------------------------------------------------
    # GEOGRAPHICAL COUNTS
    # --------------------------------------------------------

    total_districts = (
        analytics_df[
            "District"
        ]
        .dropna()
        .astype(str)
        .nunique()
    )

    total_taluks = (
        analytics_df[
            "Taluk"
        ]
        .dropna()
        .astype(str)
        .nunique()
    )

    total_villages = (
        analytics_df[
            "Village"
        ]
        .dropna()
        .astype(str)
        .nunique()
    )

    total_sites = len(
        analytics_df
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Districts Covered",
        total_districts
    )

    c2.metric(
        "Taluks Covered",
        total_taluks
    )

    c3.metric(
        "Villages Covered",
        total_villages
    )

    c4.metric(
        "Total Sites",
        total_sites
    )

    # --------------------------------------------------------
    # DISTRICT ANALYTICS
    # --------------------------------------------------------

    st.markdown("---")

    st.subheader(
        "🏛️ District-level Analytics"
    )

    district_summary = (
        analytics_df
        .groupby(
            "District"
        )
        .agg(
            Sites=(
                "Site ID",
                "count"
            ),
            Area_ha=(
                "Area (ha)",
                "sum"
            ),
            Budget_Allocated=(
                "Budget Allocated",
                "sum"
            ),
            Budget_Used=(
                "Budget Used",
                "sum"
            ),
            Biomass_tonnes=(
                "Biomass (tonnes)",
                "sum"
            )
        )
        .reset_index()
    )

    district_cleared = (
        analytics_df[
            analytics_df[
                "Status"
            ]
            .astype(str)
            .str.lower()
            == "cleared"
        ]
        .groupby(
            "District"
        )
        .size()
        .reset_index(
            name="Cleared"
        )
    )

    district_infested = (
        analytics_df[
            analytics_df[
                "Status"
            ]
            .astype(str)
            .str.lower()
            == "infested"
        ]
        .groupby(
            "District"
        )
        .size()
        .reset_index(
            name="Infested"
        )
    )

    district_monitoring = (
        analytics_df[
            analytics_df[
                "Status"
            ]
            .astype(str)
            .str.lower()
            == "monitoring"
        ]
        .groupby(
            "District"
        )
        .size()
        .reset_index(
            name="Monitoring"
        )
    )

    district_high_risk = (
        analytics_df[
            analytics_df[
                "Risk"
            ]
            .astype(str)
            .str.lower()
            == "high"
        ]
        .groupby(
            "District"
        )
        .size()
        .reset_index(
            name="High_Risk"
        )
    )

    district_summary = district_summary.merge(
        district_cleared,
        on="District",
        how="left"
    )

    district_summary = district_summary.merge(
        district_infested,
        on="District",
        how="left"
    )

    district_summary = district_summary.merge(
        district_monitoring,
        on="District",
        how="left"
    )

    district_summary = district_summary.merge(
        district_high_risk,
        on="District",
        how="left"
    )

    for column in [
        "Cleared",
        "Infested",
        "Monitoring",
        "High_Risk"
    ]:

        district_summary[
            column
        ] = (
            district_summary[
                column
            ]
            .fillna(0)
            .astype(int)
        )

    district_summary[
        "Clearance_%"
    ] = (
        district_summary[
            "Cleared"
        ]
        /
        district_summary[
            "Sites"
        ]
        *
        100
    ).round(1)

    district_summary[
        "Area_ha"
    ] = district_summary[
        "Area_ha"
    ].round(2)

    district_summary[
        "Budget_Allocated"
    ] = district_summary[
        "Budget_Allocated"
    ].round(0)

    district_summary[
        "Budget_Used"
    ] = district_summary[
        "Budget_Used"
    ].round(0)

    district_summary[
        "Biomass_tonnes"
    ] = district_summary[
        "Biomass_tonnes"
    ].round(2)

    show_table(
        district_summary
    )

    # --------------------------------------------------------
    # DISTRICT SELECTION
    # --------------------------------------------------------

    st.markdown("---")

    st.subheader(
        "🔎 Explore a District"
    )

    districts = sorted(
        analytics_df[
            "District"
        ]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    if districts:

        selected_district = st.selectbox(
            "Select District",
            districts
        )

        district_data = analytics_df[
            analytics_df[
                "District"
            ].astype(str)
            == selected_district
        ]

        district_sites = len(
            district_data
        )

        district_area = district_data[
            "Area (ha)"
        ].sum()

        district_cleared_count = len(
            district_data[
                district_data[
                    "Status"
                ]
                .astype(str)
                .str.lower()
                == "cleared"
            ]
        )

        district_high_risk_count = len(
            district_data[
                district_data[
                    "Risk"
                ]
                .astype(str)
                .str.lower()
                == "high"
            ]
        )

        district_biomass = district_data[
            "Biomass (tonnes)"
        ].sum()

        if district_sites > 0:

            district_clearance_rate = (
                district_cleared_count
                /
                district_sites
                *
                100
            )

        else:

            district_clearance_rate = 0

        a1, a2, a3, a4, a5 = st.columns(5)

        a1.metric(
            "Sites",
            district_sites
        )

        a2.metric(
            "Area",
            f"{district_area:.2f} ha"
        )

        a3.metric(
            "Cleared",
            district_cleared_count
        )

        a4.metric(
            "High Risk",
            district_high_risk_count
        )

        a5.metric(
            "Clearance",
            f"{district_clearance_rate:.1f}%"
        )

        st.info(
            f"Biomass recorded in "
            f"{selected_district}: "
            f"{district_biomass:.2f} tonnes"
        )

        # ----------------------------------------------------
        # TALUK ANALYTICS
        # ----------------------------------------------------

        st.subheader(
            f"📌 Taluk Analytics — {selected_district}"
        )

        taluk_summary = (
            district_data
            .groupby(
                "Taluk"
            )
            .agg(
                Sites=(
                    "Site ID",
                    "count"
                ),
                Area_ha=(
                    "Area (ha)",
                    "sum"
                ),
                Biomass_tonnes=(
                    "Biomass (tonnes)",
                    "sum"
                )
            )
            .reset_index()
        )

        taluk_cleared = (
            district_data[
                district_data[
                    "Status"
                ]
                .astype(str)
                .str.lower()
                == "cleared"
            ]
            .groupby(
                "Taluk"
            )
            .size()
            .reset_index(
                name="Cleared"
            )
        )

        taluk_high_risk = (
            district_data[
                district_data[
                    "Risk"
                ]
                .astype(str)
                .str.lower()
                == "high"
            ]
            .groupby(
                "Taluk"
            )
            .size()
            .reset_index(
                name="High_Risk"
            )
        )

        taluk_summary = taluk_summary.merge(
            taluk_cleared,
            on="Taluk",
            how="left"
        )

        taluk_summary = taluk_summary.merge(
            taluk_high_risk,
            on="Taluk",
            how="left"
        )

        taluk_summary[
            "Cleared"
        ] = (
            taluk_summary[
                "Cleared"
            ]
            .fillna(0)
            .astype(int)
        )

        taluk_summary[
            "High_Risk"
        ] = (
            taluk_summary[
                "High_Risk"
            ]
            .fillna(0)
            .astype(int)
        )

        taluk_summary[
            "Clearance_%"
        ] = (
            taluk_summary[
                "Cleared"
            ]
            /
            taluk_summary[
                "Sites"
            ]
            *
            100
        ).round(1)

        taluk_summary[
            "Area_ha"
        ] = taluk_summary[
            "Area_ha"
        ].round(2)

        taluk_summary[
            "Biomass_tonnes"
        ] = taluk_summary[
            "Biomass_tonnes"
        ].round(2)

        show_table(
            taluk_summary
        )

        # ----------------------------------------------------
        # TALUK SELECTION
        # ----------------------------------------------------

        taluks = sorted(
            district_data[
                "Taluk"
            ]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )

        if taluks:

            selected_taluk = st.selectbox(
                "Select Taluk",
                taluks
            )

            taluk_data = district_data[
                district_data[
                    "Taluk"
                ].astype(str)
                == selected_taluk
            ]

            st.subheader(
                f"🏘️ Village Analytics — "
                f"{selected_taluk}"
            )

            # ------------------------------------------------
            # VILLAGE ANALYTICS
            # ------------------------------------------------

            village_summary = (
                taluk_data
                .groupby(
                    "Village"
                )
                .agg(
                    Sites=(
                        "Site ID",
                        "count"
                    ),
                    Area_ha=(
                        "Area (ha)",
                        "sum"
                    ),
                    Biomass_tonnes=(
                        "Biomass (tonnes)",
                        "sum"
                    )
                )
                .reset_index()
            )

            village_cleared = (
                taluk_data[
                    taluk_data[
                        "Status"
                    ]
                    .astype(str)
                    .str.lower()
                    == "cleared"
                ]
                .groupby(
                    "Village"
                )
                .size()
                .reset_index(
                    name="Cleared"
                )
            )

            village_infested = (
                taluk_data[
                    taluk_data[
                        "Status"
                    ]
                    .astype(str)
                    .str.lower()
                    == "infested"
                ]
                .groupby(
                    "Village"
                )
                .size()
                .reset_index(
                    name="Infested"
                )
            )

            village_high_risk = (
                taluk_data[
                    taluk_data[
                        "Risk"
                    ]
                    .astype(str)
                    .str.lower()
                    == "high"
                ]
                .groupby(
                    "Village"
                )
                .size()
                .reset_index(
                    name="High_Risk"
                )
            )

            village_summary = village_summary.merge(
                village_cleared,
                on="Village",
                how="left"
            )

            village_summary = village_summary.merge(
                village_infested,
                on="Village",
                how="left"
            )

            village_summary = village_summary.merge(
                village_high_risk,
                on="Village",
                how="left"
            )

            for column in [
                "Cleared",
                "Infested",
                "High_Risk"
            ]:

                village_summary[
                    column
                ] = (
                    village_summary[
                        column
                    ]
                    .fillna(0)
                    .astype(int)
                )

            village_summary[
                "Clearance_%"
            ] = (
                village_summary[
                    "Cleared"
                ]
                /
                village_summary[
                    "Sites"
                ]
                *
                100
            ).round(1)

            village_summary[
                "Area_ha"
            ] = village_summary[
                "Area_ha"
            ].round(2)

            village_summary[
                "Biomass_tonnes"
            ] = village_summary[
                "Biomass_tonnes"
            ].round(2)

            show_table(
                village_summary
            )

            # ------------------------------------------------
            # VILLAGE SITE DETAILS
            # ------------------------------------------------

            villages = sorted(
                taluk_data[
                    "Village"
                ]
                .dropna()
                .astype(str)
                .unique()
                .tolist()
            )

            if villages:

                selected_village = st.selectbox(
                    "Select Village",
                    villages
                )

                village_data = taluk_data[
                    taluk_data[
                        "Village"
                    ].astype(str)
                    == selected_village
                ]

                st.subheader(
                    f"📋 Site Details — "
                    f"{selected_village}"
                )

                village_sites = len(
                    village_data
                )

                village_area = village_data[
                    "Area (ha)"
                ].sum()

                village_cleared_count = len(
                    village_data[
                        village_data[
                            "Status"
                        ]
                        .astype(str)
                        .str.lower()
                        == "cleared"
                    ]
                )

                village_infested_count = len(
                    village_data[
                        village_data[
                            "Status"
                        ]
                        .astype(str)
                        .str.lower()
                        == "infested"
                    ]
                )

                village_high_risk_count = len(
                    village_data[
                        village_data[
                            "Risk"
                        ]
                        .astype(str)
                        .str.lower()
                        == "high"
                    ]
                )

                village_biomass = village_data[
                    "Biomass (tonnes)"
                ].sum()

                if village_sites > 0:

                    village_clearance_rate = (
                        village_cleared_count
                        /
                        village_sites
                        *
                        100
                    )

                else:

                    village_clearance_rate = 0

                v1, v2, v3, v4, v5 = st.columns(5)

                v1.metric(
                    "Sites",
                    village_sites
                )

                v2.metric(
                    "Area",
                    f"{village_area:.2f} ha"
                )

                v3.metric(
                    "Cleared",
                    village_cleared_count
                )

                v4.metric(
                    "High Risk",
                    village_high_risk_count
                )

                v5.metric(
                    "Clearance",
                    f"{village_clearance_rate:.1f}%"
                )

                st.write(
                    f"**Infested Sites:** "
                    f"{village_infested_count}"
                )

                st.write(
                    f"**Biomass Recorded:** "
                    f"{village_biomass:.2f} tonnes"
                )

                show_table(
                    village_data[
                        [
                            "Site ID",
                            "District",
                            "Taluk",
                            "Village",
                            "Area (ha)",
                            "Infestation",
                            "Risk",
                            "Status",
                            "Budget Allocated",
                            "Budget Used",
                            "Biomass (tonnes)"
                        ]
                    ]
                )

    # --------------------------------------------------------
    # GOVERNMENT DECISION SUPPORT
    # --------------------------------------------------------

    st.markdown("---")

    st.subheader(
        "🧭 Geographic Decision Support"
    )

    if not district_summary.empty:

        highest_site_district = district_summary.loc[
            district_summary[
                "Sites"
            ].idxmax(),
            "District"
        ]

        highest_site_count = district_summary[
            "Sites"
        ].max()

        highest_risk_district_data = (
            analytics_df[
                analytics_df[
                    "Risk"
                ]
                .astype(str)
                .str.lower()
                == "high"
            ]
            .groupby(
                "District"
            )
            .size()
        )

        if not highest_risk_district_data.empty:

            highest_risk_district = (
                highest_risk_district_data.idxmax()
            )

            highest_risk_count = (
                highest_risk_district_data.max()
            )

            st.warning(
                f"⚠️ Highest concentration of "
                f"high-risk sites: "
                f"**{highest_risk_district}** "
                f"({highest_risk_count} site(s))."
            )

        st.info(
            f"📍 Highest number of registered "
            f"sites: **{highest_site_district}** "
            f"({highest_site_count} site(s))."
        )

    st.success(
        "✅ District → Taluk → Village "
        "hierarchical analysis is available "
        "for government decision-making."
    )


# ============================================================
# FOOTER
# ============================================================

st.sidebar.markdown("---")

st.sidebar.caption(
    "Karuvelam360 Prototype"
)

st.sidebar.caption(
    "FIND → PLAN → FUND → CLEAR → VERIFY"
)

st.sidebar.caption(
    "→ MONITOR → ALERT → ACT → REPORT → PREDICT"
)

st.sidebar.caption(
    "Tamil Nadu"
)