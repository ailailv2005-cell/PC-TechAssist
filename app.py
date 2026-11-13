import streamlit as st
import streamlit.components.v1 as components

# Basic Page Configuration
st.set_page_config(
    page_title="PC TechAssist",
    page_icon="⚡",
    layout="wide"
)

# Professional Custom Styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0b0f19 0%, #111827 100%);
        color: #f3f4f6;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 6px;
        background-color: rgba(17, 24, 39, 0.9);
        padding: 8px;
        border-radius: 12px;
        border: 1px solid rgba(55, 65, 81, 0.5);
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #1f2937;
        border-radius: 8px;
        padding: 8px 14px;
        color: #9ca3af;
        font-weight: 700;
        font-size: 13px;
        border: 1px solid transparent;
        transition: all 0.3s ease;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #374151;
        color: #ffffff;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%) !important;
        color: #ffffff !important;
        border: 1px solid #60a5fa !important;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);
    }
    .cyber-card {
        background: linear-gradient(145deg, #161e2e 0%, #0f172a 100%);
        border: 1px solid #3b82f6;
        padding: 20px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
        margin-bottom: 20px;
    }
    .metric-card {
        background: rgba(31, 41, 55, 0.6);
        border: 1px solid rgba(59, 130, 246, 0.3);
        padding: 15px;
        border-radius: 12px;
        text-align: center;
    }
    .stButton>button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 24px;
        border: none;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(16, 185, 129, 0.5);
    }
    [data-testid="stSidebar"] {
        background-color: #0d1322;
        border-right: 1px solid #1f2937;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### ⚙️ Control Panel")
    st.info("Workshop Management & Hardware Engineering Diagnostics.")
    st.markdown("---")
    st.markdown("👨‍💻 **Developer:** Montazer Thamer Yousif")
    st.markdown("🏫 **Major:** Computer Assembly & Maintenance")
    st.markdown("📚 **Institution:** Al-Muthanna Evening Vocational Preparatory School")
    st.markdown("---")
    st.caption("Version: 17.0 (Stable English Release)")

# Main Navigation Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🚀 Dashboard", 
    "🛠️ Hardware Diagnostics", 
    "📋 Workshop Tickets", 
    "📦 Spare Parts", 
    "💡 Feedback & Suggestions",
    "⚡ ESD Safety"
])

# --- 1. Dashboard ---
with tab1:
    st.title("⚡ PC TechAssist Platform")
    st.subheader("Maintenance Workshop Management & Hardware Engineering Diagnostics System")
    
    st.markdown("""
    <div class="cyber-card">
        <h3 style="color: #93c5fd; margin-bottom: 10px;">🚀 Engineered & Developed By</h3>
        <h1 style="color: #60a5fa; text-shadow: 0 0 15px rgba(96, 165, 250, 0.5); margin: 10px 0;">Montazer Thamer Yousif</h1>
        <p style="color: #9ca3af; font-size: 1.1em;"><b>Specialization:</b> Computer Assembly & Maintenance | Al-Muthanna Vocational School</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📊 Workshop Performance Overview (Live Stats)")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="metric-card"><h4 style="color:#60a5fa; margin:0;">Devices in Repair</h4><h2 style="color:white; margin:10px 0 0 0;">8</h2></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><h4 style="color:#34d399; margin:0;">Completed Tickets</h4><h2 style="color:white; margin:10px 0 0 0;">42</h2></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><h4 style="color:#fbbf24; margin:0;">Success Rate</h4><h2 style="color:white; margin:10px 0 0 0;">98.5%</h2></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric-card"><h4 style="color:#f87171; margin:0;">Low Stock Parts</h4><h2 style="color:white; margin:10px 0 0 0;">2</h2></div>', unsafe_allow_html=True)

# --- 2. Live Hardware Diagnostics ---
with tab2:
    st.header("🛠️ Advanced Hardware Diagnostics Station")
    st.write("Select the target hardware component and the observed symptom to generate immediate troubleshooting steps:")
    
    col1, col2 = st.columns(2)
    with col1:
        component = st.selectbox(
            "Select Target Hardware Component:",
            [
                "Random Access Memory (RAM)",
                "Processor (CPU) & Cooling Heatsink",
                "Power Supply Unit (PSU)",
                "Graphics Card (GPU)",
                "Motherboard",
                "Storage Drives (HDD / SSD)",
                "System Battery & Clock (CMOS / BIOS)"
            ]
        )
    with col2:
        symptom = st.selectbox(
            "Observed Problem / Symptom:",
            [
                "No boot or intermittent POST beeps",
                "Complete power loss and fans not spinning",
                "Sudden overheating and automatic thermal shutdown",
                "Black screen with no video output",
                "Operating system fails to detect storage drive",
                "Frequent random system reboots",
                "Blue Screen of Death (BSOD) during startup"
            ]
        )

    if st.button("🚀 Run Instant Engineering Diagnostics"):
        st.markdown(f"""
            <div style="background: rgba(16, 185, 129, 0.1); border: 1px solid #10b981; padding: 20px; border-radius: 12px; margin-top: 15px;">
            <h3 style="color: #34d399; margin-top: 0;">✅ Field Diagnostic Results for ({component} — Symptom: {symptom}):</h3>
            """, unsafe_allow_html=True)
        
        if "RAM" in component:
            st.markdown("1. **Remove Memory Modules:** Disconnect power completely and carefully unclip the RAM sticks from their slots.<br>2. **Clean Gold Contacts:** Gently clean the gold contact pins with a soft rubber eraser to remove oxidation.<br>3. **Reseat Modules:** Reinstall the sticks in alternative DIMM slots and ensure the locking latches click firmly into place.")
        elif "CPU" in component:
            st.markdown("1. **CPU Fan Connection:** Verify that the fan cable is securely plugged into the `CPU_FAN` header and spins freely.<br>2. **Thermal Paste Check:** Inspect the thermal compound between the CPU and heatsink; clean and reapply if dried out.<br>3. **Heatsink Mounting:** Ensure even mounting pressure across the processor's Integrated Heat Spreader (IHS).")
        elif "Power" in component:
            st.markdown("1. **Main Power Cables:** Inspect the power cord and verify that the 24-pin ATX and 8-pin EPS connectors are firmly seated.<br>2. **Front Panel Connectors:** Check the motherboard `F_PANEL` power switch pins for proper connection.<br>3. **Power Source Verification:** Test the wall outlet, surge protector, and PSU switch/fuse integrity.")
        elif "HDD" in component or "SSD" in component:
            st.markdown("1. **Data & Power Cables:** Ensure both SATA data and SATA power cables are tightly connected (or verify M.2 NVMe screw seating).<br>2. **BIOS Detection:** Reboot into the BIOS/UEFI menu to verify whether the motherboard detects the drive.<br>3. **Bad Sector Scan:** Run diagnostic disk utilities to check drive health (S.M.A.R.T. status) and bad sectors.")
        elif "CMOS" in component or "BIOS" in component:
            st.markdown("1. **Battery Voltage Check:** Measure the CR2032 coin-cell battery with a multimeter; it should read approximately 3.0V.<br>2. **Reset BIOS Settings:** Remove the battery for 2 minutes or bridge the `CLR_CMOS` jumper to clear corrupted settings.<br>3. **Firmware Stability:** Check if a BIOS update is required to resolve hardware compatibility issues.")
        else:
            st.markdown("1. **Full Visual Inspection:** Check display cables (HDMI/DP) and verify GPU seating in the PCIe slot.<br>2. **Thermal Monitoring:** Monitor component temperatures under load to rule out thermal throttling.<br>3. **Short-Circuit Check:** Ensure proper motherboard standoff placement inside the PC case to prevent electrical shorts.")
        
        st.markdown("</div>", unsafe_allow_html=True)
        st.balloons()

# --- 3. Workshop Tickets Management ---
with tab3:
    st.header("📋 Maintenance & Repair Work Orders (Workshop Tickets)")
    st.write("Track incoming client devices and active repair statuses in the workshop:")
    
    st.markdown("""
    | Ticket ID | Client Name | Device Type | Reported Issue | Current Status | Assigned Technician |
    | :--- | :--- | :--- | :--- | :--- | :--- |
    | **#WRK-101** | Ahmed Ali | HP ProBook Laptop | No power and fails to boot | 🔄 Under Inspection | Montazer Thamer |
    | **#WRK-102** | Karrar Mohammed | Custom PC Desktop | Black screen with POST beeps | ⏳ Awaiting Parts | Workshop Tech |
    | **#WRK-103** | Mustafa Hassan | Dell OptiPlex | Frequent random restarts | ✅ Repaired | Montazer Thamer |
    """, unsafe_allow_html=True)

# --- 4. Spare Parts Inventory ---
with tab4:
    st.header("📦 Spare Parts Inventory Management")
    st.write("Monitor available hardware components and consumable supplies in the workshop:")
    
    st.markdown("""
    | Spare Part / Component | Category | Available Qty | Low-Stock Threshold | Status |
    | :--- | :--- | :--- | :--- | :--- |
    | **Arctic MX-4 Thermal Paste** | Consumables | 15 | 5 | 🟢 In Stock |
    | **8GB DDR4 RAM Modules** | Internal Hardware | 6 | 2 | 🟢 In Stock |
    | **500W Power Supply (PSU)** | Power | 2 | 3 | ⚠️ Low Stock |
    | **CR2032 CMOS Batteries** | General Maintenance | 25 | 10 | 🟢 In Stock |
    """, unsafe_allow_html=True)

# --- 5. Feedback & Suggestions ---
with tab5:
    st.header("💡 Report an Issue or Submit a Feature Suggestion")
    st.write("Write your feedback or report a new hardware issue to send directly to the developer:")

    components.html("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <style>
            body {
                background-color: transparent;
                color: #f3f4f6;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                margin: 0;
                padding: 5px;
            }
            .form-group {
                margin-bottom: 12px;
            }
            label {
                display: block;
                margin-bottom: 5px;
                font-weight: bold;
                color: #f3f4f6;
                font-size: 14px;
            }
            input, textarea {
                width: 100%;
                padding: 10px;
                border-radius: 8px;
                border: 1px solid #374151;
                background: #1f2937;
                color: white;
                box-sizing: border-box;
                font-size: 14px;
            }
            button {
                background: linear-gradient(135deg, #10b981 0%, #059669 100%);
                color: white;
                font-weight: bold;
                padding: 12px 24px;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                width: 100%;
                font-size: 15px;
                box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
            }
            button:hover {
                opacity: 0.95;
            }
        </style>
    </head>
    <body>
        <form action="https://formsubmit.co/ailailv2005@gmail.com" method="POST">
            <input type="hidden" name="_subject" value="New Message from PC TechAssist Workshop!">
            <input type="hidden" name="_captcha" value="false">
            
            <div class="form-group">
                <label>👤 Your Name:</label>
                <input type="text" name="name" required placeholder="Enter your name...">
            </div>
            
            <div class="form-group">
                <label>📧 Your Email:</label>
                <input type="email" name="email" required placeholder="example@gmail.com">
            </div>
            
            <div class="form-group">
                <label>✍️ Suggestion or Issue Details:</label>
                <textarea name="message" required rows="3" placeholder="Describe your suggestion or hardware issue here..."></textarea>
            </div>
            
            <button type="submit">📤 Send to Developer</button>
        </form>
    </body>
    </html>
    """, height=340)

# --- 6. ESD Safety ---
with tab6:
    st.header("⚡ Electrostatic Discharge (ESD) Safety Protocols")
    st.markdown("""
    <div style="background: rgba(239, 68, 68, 0.1); border: 1px solid #ef4444; padding: 20px; border-radius: 12px; color: #fca5a5;">
    <h3>⚠️ Critical Engineering Safety Guidelines for Hardware Protection:</h3>
    <ol>
        <li><b>Grounding & Discharge:</b> Always wear an ESD wrist strap or touch an unpainted grounded metal surface before handling sensitive circuit boards.</li>
        <li><b>Complete Power Disconnect:</b> Unplug the main AC power cable from the wall outlet and discharge residual capacitors before opening the chassis.</li>
        <li><b>Insulated Tools & Workspace:</b> Use insulated screwdrivers and work on an anti-static mat; avoid carpeted or fabric surfaces that generate static electricity.</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)
    
