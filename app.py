import streamlit as st
from supabase import create_client, Client

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Smartphone Usage & Online Safety",
    page_icon=None,
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
    .main {
        background-color: #f7f8fa;
    }

    .title {
        font-size: 38px;
        font-weight: 700;
        color: #1f2937;
        margin-bottom: 8px;
    }

    .subtitle {
        font-size: 18px;
        color: #6b7280;
        margin-bottom: 25px;
    }

    .card {
        background: white;
        padding: 22px;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        margin-bottom: 18px;
    }

    .section-title {
        font-size: 27px;
        font-weight: 650;
        color: #1f2937;
        margin-top: 10px;
        margin-bottom: 15px;
    }

    .tip {
        background: #f0fdf4;
        border-left: 5px solid #16a34a;
        padding: 14px;
        margin: 10px 0;
        border-radius: 6px;
    }

    .warning {
        background: #fff7ed;
        border-left: 5px solid #ea580c;
        padding: 14px;
        margin: 10px 0;
        border-radius: 6px;
    }
</style>
""", unsafe_allow_html=True)


# ---------------- SUPABASE CONNECTION ----------------
supabase = None

try:
    if "SUPABASE_URL" in st.secrets and "SUPABASE_KEY" in st.secrets:
        supabase: Client = create_client(
            st.secrets["SUPABASE_URL"],
            st.secrets["SUPABASE_KEY"]
        )
except Exception:
    supabase = None


# ---------------- SIDEBAR ----------------
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Home",
        "Smartphone Usage",
        "Online Safety",
        "Women Safety",
        "Safety Quiz",
        "Participation",
        "Feedback",
        "Records"
    ]
)


# =========================================================
# HOME
# =========================================================

if page == "Home":

    st.markdown(
        '<div class="title">Smartphone Usage and Online Safety</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Awareness and digital safety resource for Women Self Help Groups</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">
    <h3>About the Project</h3>
    <p>
    This platform is designed to help women understand smartphone usage,
    digital services and online safety practices. It provides simple guides,
    safety awareness activities, quizzes and participation facilities.
    </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
        <h3>Smartphone Usage</h3>
        <p>Learn smartphone basics, applications, internet usage and digital payments.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h3>Online Safety</h3>
        <p>Learn how to identify scams, phishing, fake accounts and unsafe links.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <h3>Women Safety</h3>
        <p>Learn important online safety practices and available support options.</p>
        </div>
        """, unsafe_allow_html=True)

    st.info("Use the navigation menu to explore the different sections.")


# =========================================================
# SMARTPHONE USAGE
# =========================================================

elif page == "Smartphone Usage":

    st.markdown(
        '<div class="section-title">Smartphone Usage Guide</div>',
        unsafe_allow_html=True
    )

    topics = [
        "Smartphone Basics",
        "Calling and Contacts",
        "WhatsApp",
        "Internet and Google Search",
        "Apps",
        "Photos and Videos",
        "UPI and Online Payments",
        "Privacy Settings",
        "Password and PIN Safety",
        "Phone Security"
    ]

    selected_topic = st.selectbox(
        "Select a topic",
        topics
    )

    if selected_topic == "Smartphone Basics":
        st.subheader("Smartphone Basics")
        st.write("Learn how to use the main features of a smartphone.")
        st.write("• Lock and unlock the phone.")
        st.write("• Adjust volume and brightness.")
        st.write("• Connect to Wi-Fi or mobile data.")
        st.write("• Check battery and storage.")
        st.write("• Keep the operating system updated.")

        with st.expander("Basic Safety Checklist"):
            st.checkbox("I use a screen lock.")
            st.checkbox("I keep my phone updated.")
            st.checkbox("I know how to lock my phone.")
            st.checkbox("I check apps before installing them.")

    elif selected_topic == "Calling and Contacts":
        st.subheader("Calling and Contacts")
        st.write("• Save important contacts.")
        st.write("• Avoid unknown callers asking for personal information.")
        st.write("• Block suspicious numbers.")
        st.write("• Do not share OTPs during phone calls.")

    elif selected_topic == "WhatsApp":
        st.subheader("WhatsApp Safety")
        st.write("• Do not share OTPs.")
        st.write("• Avoid opening unknown links.")
        st.write("• Use two-step verification.")
        st.write("• Check privacy settings.")
        st.write("• Block and report suspicious accounts.")

        with st.expander("Safe or Unsafe?"):
            answer = st.radio(
                "Someone sends you an unknown link and asks you to click it.",
                ["Safe", "Unsafe"]
            )

            if st.button("Check Answer"):
                if answer == "Unsafe":
                    st.success("Correct. Avoid unknown or suspicious links.")
                else:
                    st.error("Incorrect. Unknown links can be dangerous.")

    elif selected_topic == "Internet and Google Search":
        st.subheader("Internet and Search")
        st.write("• Use trusted websites.")
        st.write("• Check website addresses carefully.")
        st.write("• Do not download unknown files.")
        st.write("• Avoid entering personal information on suspicious websites.")

    elif selected_topic == "Apps":
        st.subheader("Safe App Usage")
        st.write("• Download applications from official app stores.")
        st.write("• Check the developer name and reviews.")
        st.write("• Review requested permissions.")
        st.write("• Uninstall applications you no longer need.")

    elif selected_topic == "Photos and Videos":
        st.subheader("Photos and Videos")
        st.write("• Avoid sharing private photographs publicly.")
        st.write("• Check who can view your photos.")
        st.write("• Be careful before forwarding images.")
        st.write("• Do not share someone else's private image without permission.")

    elif selected_topic == "UPI and Online Payments":
        st.subheader("UPI and Online Payment Safety")

        st.markdown("""
        <div class="warning">
        Never share your UPI PIN, OTP, ATM PIN or banking password with anyone.
        </div>
        """, unsafe_allow_html=True)

        st.write("• You do not need to enter a UPI PIN to receive money.")
        st.write("• Verify the recipient before sending money.")
        st.write("• Do not scan unknown QR codes.")
        st.write("• Contact your bank immediately if fraud occurs.")

    elif selected_topic == "Privacy Settings":
        st.subheader("Privacy Settings")
        st.write("Review privacy settings for:")
        st.write("• WhatsApp")
        st.write("• Instagram")
        st.write("• Facebook")
        st.write("• Google Account")

        with st.expander("Privacy Checklist"):
            st.checkbox("My profile information is limited.")
            st.checkbox("My location is not shared unnecessarily.")
            st.checkbox("I review app permissions.")
            st.checkbox("I use two-factor authentication where available.")

    elif selected_topic == "Password and PIN Safety":
        st.subheader("Password and PIN Safety")
        st.write("• Use strong and unique passwords.")
        st.write("• Do not use easily guessed information.")
        st.write("• Never share passwords or PINs.")
        st.write("• Use two-factor authentication where available.")

        password = st.text_input(
            "Practice: Enter a sample password (do not enter your real password)",
            type="password"
        )

        if password:
            if len(password) < 8:
                st.warning("This sample password is short.")
            else:
                st.success("This sample password has a reasonable length. Use a unique password in real accounts.")

    elif selected_topic == "Phone Security":
        st.subheader("Phone Security")
        st.write("• Keep screen lock enabled.")
        st.write("• Install system updates.")
        st.write("• Use trusted security features.")
        st.write("• Avoid connecting to unknown devices.")
        st.write("• Back up important information.")

    st.markdown("---")

    st.subheader("Quick Smartphone Knowledge Check")

    q1 = st.radio(
        "1. Should you share your OTP with another person?",
        ["Yes", "No"]
    )

    q2 = st.radio(
        "2. Where should you preferably download apps from?",
        ["Unknown websites", "Official app store"]
    )

    if st.button("Check Smartphone Answers"):
        score = 0

        if q1 == "No":
            score += 1

        if q2 == "Official app store":
            score += 1

        st.success(f"Your score is {score}/2")


# =========================================================
# ONLINE SAFETY
# =========================================================

elif page == "Online Safety":

    st.markdown(
        '<div class="section-title">Online Safety for Women</div>',
        unsafe_allow_html=True
    )

    safety_topics = [
        "OTP and PIN Safety",
        "Phishing",
        "Online Scams",
        "Fake Profiles",
        "Cyberbullying",
        "Online Harassment",
        "Social Media Privacy",
        "Location Safety"
    ]

    topic = st.selectbox(
        "Select a safety topic",
        safety_topics
    )

    safety_content = {
        "OTP and PIN Safety": [
            "Never share OTPs.",
            "Never share UPI PINs.",
            "Never share ATM PINs.",
            "Banks generally do not ask for your confidential authentication details by phone."
        ],
        "Phishing": [
            "Do not open suspicious links.",
            "Check the website address.",
            "Do not enter passwords on unknown websites.",
            "Be careful with urgent messages."
        ],
        "Online Scams": [
            "Do not trust guaranteed prize or lottery messages.",
            "Do not send money to unknown people.",
            "Verify requests through official channels.",
            "Contact the bank quickly if you suspect financial fraud."
        ],
        "Fake Profiles": [
            "Check the account carefully.",
            "Do not share personal information.",
            "Block and report suspicious profiles.",
            "Avoid accepting requests from unknown people."
        ],
        "Cyberbullying": [
            "Do not respond emotionally.",
            "Save evidence such as screenshots.",
            "Block and report the account.",
            "Seek help from trusted people."
        ],
        "Online Harassment": [
            "Save messages and screenshots.",
            "Block the person when appropriate.",
            "Report the account/platform.",
            "Use appropriate official support channels."
        ],
        "Social Media Privacy": [
            "Review privacy settings.",
            "Limit personal information.",
            "Be careful with public posts.",
            "Avoid sharing sensitive documents."
        ],
        "Location Safety": [
            "Avoid unnecessary live location sharing.",
            "Review location permissions.",
            "Be careful when posting your current location publicly.",
            "Disable unnecessary location access."
        ]
    }

    for item in safety_content[topic]:
        st.markdown(f"• {item}")

    st.markdown("---")

    st.subheader("What Would You Do?")

    scenario = st.selectbox(
        "You receive a message saying you won a prize and must pay a fee immediately. What should you do?",
        [
            "Pay immediately",
            "Share OTP",
            "Ignore and verify through an official source",
            "Forward it to friends"
        ]
    )

    if st.button("Check Safety Answer"):
        if scenario == "Ignore and verify through an official source":
            st.success("Correct. Verify suspicious offers through trusted official sources.")
        else:
            st.error("This is unsafe. Do not send money or confidential information.")


# =========================================================
# WOMEN SAFETY
# =========================================================

elif page == "Women Safety":

    st.markdown(
        '<div class="section-title">Women Safety and Support</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">
    <h3>Important Online Safety Practices</h3>
    <p>Keep personal information private and use strong security settings.</p>
    <p>Save evidence if you experience online harassment or fraud.</p>
    <p>Use official reporting channels for cybercrime and emergencies.</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("If Online Fraud Happens")

    steps = [
        "Stay calm and stop communicating with the suspicious person.",
        "Contact your bank or payment provider quickly if money is involved.",
        "Preserve transaction details and screenshots.",
        "Report the incident through the appropriate official cybercrime channel.",
        "Change affected passwords and enable additional security."
    ]

    for i, step in enumerate(steps, 1):
        st.write(f"{i}. {step}")

    st.subheader("Emergency Information")

    st.info(
        "For emergencies, contact the appropriate local emergency service. "
        "For cybercrime or financial fraud, use official government and banking reporting channels."
    )


# =========================================================
# QUIZ
# =========================================================

elif page == "Safety Quiz":

    st.markdown(
        '<div class="section-title">Online Safety Awareness Quiz</div>',
        unsafe_allow_html=True
    )

    questions = [
        (
            "1. Should you share your OTP with someone who calls you?",
            ["Yes", "No"],
            "No"
        ),
        (
            "2. Is it safe to click every link received from unknown people?",
            ["Yes", "No"],
            "No"
        ),
        (
            "3. Where should you preferably download applications?",
            ["Official app store", "Unknown website"],
            "Official app store"
        ),
        (
            "4. Should you share your UPI PIN to receive money?",
            ["Yes", "No"],
            "No"
        ),
        (
            "5. What should you do with a suspicious social-media account?",
            ["Share personal information", "Block and report"],
            "Block and report"
        )
    ]

    answers = []

    for question, options, correct in questions:
        answers.append(
            st.radio(question, options)
        )

    if st.button("Submit Quiz"):

        score = 0

        for i, answer in enumerate(answers):
            if answer == questions[i][2]:
                score += 1

        st.success(f"Your score: {score}/{len(questions)}")

        if score == len(questions):
            st.success("Excellent awareness.")
        elif score >= 3:
            st.info("Good awareness. Keep learning about online safety.")
        else:
            st.warning("More awareness is recommended. Review the Online Safety section.")


# =========================================================
# PARTICIPATION
# =========================================================

elif page == "Participation":

    st.markdown(
        '<div class="section-title">Participant Registration</div>',
        unsafe_allow_html=True
    )

    with st.form("participant_form"):

        name = st.text_input("Participant Name")

        age_group = st.selectbox(
            "Age Group",
            [
                "Below 18",
                "18-25",
                "26-40",
                "41-60",
                "Above 60"
            ]
        )

        shg_name = st.text_input("Self Help Group Name")

        smartphone_level = st.selectbox(
            "Smartphone Usage Level",
            [
                "Beginner",
                "Basic",
                "Intermediate",
                "Advanced"
            ]
        )

        safety_awareness = st.selectbox(
            "Online Safety Awareness",
            [
                "Low",
                "Basic",
                "Moderate",
                "High"
            ]
        )

        session_attended = st.selectbox(
            "Session Attended",
            [
                "Smartphone Usage",
                "Online Safety",
                "Women Safety",
                "All Sessions"
            ]
        )

        topics_learned = st.text_area(
            "Topics Learned"
        )

        participation = st.selectbox(
            "Would you like to participate in future awareness activities?",
            ["Yes", "No"]
        )

        submitted = st.form_submit_button(
            "Submit Participation"
        )

        if submitted:

            if not name.strip():
                st.error("Please enter participant name.")

            elif supabase is None:
                st.error(
                    "Supabase is not connected yet. Add SUPABASE_URL and SUPABASE_KEY in Streamlit Secrets."
                )

            else:
                try:
                    data = {
                        "name": name,
                        "age_group": age_group,
                        "shg_name": shg_name,
                        "smartphone_level": smartphone_level,
                        "safety_awareness": safety_awareness,
                        "session_attended": session_attended,
                        "topics_learned": topics_learned,
                        "participation": participation
                    }

                    supabase.table("participants").insert(data).execute()

                    st.success(
                        "Participation recorded successfully."
                    )

                except Exception as e:
                    st.error(
                        "Could not save the record. Check your Supabase table columns and connection."
                    )


# =========================================================
# FEEDBACK
# =========================================================

elif page == "Feedback":

    st.markdown(
        '<div class="section-title">Feedback</div>',
        unsafe_allow_html=True
    )

    with st.form("feedback_form"):

        participant_name = st.text_input("Name")

        rating = st.slider(
            "Rate the usefulness of this website",
            1,
            5,
            5
        )

        useful_topic = st.selectbox(
            "Most Useful Topic",
            [
                "Smartphone Usage",
                "Online Safety",
                "Women Safety",
                "Quiz"
            ]
        )

        learning = st.text_area(
            "What did you learn?"
        )
