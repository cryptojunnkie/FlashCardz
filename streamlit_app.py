import streamlit as st
from gtts import gTTS
import tempfile
import re

# Set the page configuration for wide mode
st.set_page_config(
    layout='wide',
    page_title='My Security+ Study Material Journey ',
    page_icon=':heavy_plus_sign:'  # This is an emoji shortcode. Could be a URL too.
)

# Function to strip HTML tags
def strip_html(html_text):
    clean = re.compile('<.*?>')  # Regex to match all HTML tags
    return re.sub(clean, '', html_text)  # Replace HTML tags with an empty string

# Flashcard data
flashcards = {
    "Cybersecurity Objectives": {
        "What do most people think cybersecurity is": (
            "<br><br>They imagine hackers trying to break "
            "into an organization's system and steal sensitive information, ranging from "
            "social security numbers and credit cards to top-secret information. Although "
            "protecting sensitive information from unauthorized disclosure is certainly one "
            "element of a cybersecurity program, it is important to understand that cybersecurity "
            "actually has 3 complementary objectives."
            "<br><br>The 3 key objectives of cybersecurity"
            "programs are referred to as the <strong>C.I.A. Triad</strong>:"
            "<ul>"
            "<li>Confidentiality</li>"
            "<li>Integrity</li>"
            "<li>Availability</li>"
        )
    },
    "CIA Triad": {
        "Confidentiality": "Ensuring that sensitive information is accessed only by an authorized person and kept away from those not authorized to possess it.",
        "Integrity": "Assuring the accuracy and reliability of information and systems. Checks if data or systems have been altered.",
        "Availability": "Ensuring that data and resources are available to authorized users when needed."
    },
    "Confidentiality": {
        "What is Confidentiality": (
            "<ul>"
            "<li>Confidentiality refers to the measures taken to ensure that sensitive information is not disclosed to unauthorized individuals, entities, or processes.</li>"
            "<li>Involves preserving authorized restrictions on information access and disclosure, including means for protecting personal privacy and proprietary information.</li>"
            "<br><strong>Here's a breakdown of what this entails:</strong>"
            "<li><strong>Access Controls:</strong> Mechanisms such as passwords, biometric verification, or access cards that limit resource access to authorized personnel to prevent unauthorized access to information.</li>"
            "<li><strong>Encryption:</strong> The process of encoding information in such a way that only authorized parties can read it. If an unauthorized party intercepts the encrypted data, they will not be able to interpret it without the encryption key.</li>"
            "<li><strong>Secure Communication:</strong> Using secure protocols like SSL/TLS for transmitting data to prevent interception by unauthorized entities.</li>"
            "<li><strong>Policies and Procedures:</strong> Establishing guidelines for who has access to information and under what conditions, and what the protocols are for handling and sharing that information.</li>"
            "<li><strong>Training and Awareness:</strong> Educating employees and users about the importance of confidentiality and how to ensure it is maintained.</li>"
            "<li><strong>Data Classification:</strong> Categorizing data based on its level of sensitivity and the impact to the organization if it is disclosed or improperly accessed.</li>"
            "</ul>"
        )
    },
    "Integrity": {
        "What is Integrity": (
            "<ul>"
            "<li>Integrity refers to the trustworthiness and veracity of data or resources.</li>"
            "<li>It is about protecting data from unauthorized changes to ensure that it is reliable and correct.</li>"
            "<br><strong>Here are key aspects of Integrity within IT security:</strong>"
            "<li>Data Accuracy</li>"
            "<li>Data Consistency</li>"
            "<li>Data Trustworthiness</li>"
            "<br><strong>Various methods and mechanisms are used, such as:</strong>"
            "<li>Checksums and Cryptographic Hash Functions: These are algorithms that produce a short, fixed-size bit string from arbitrary-length strings of data. If the data changes, so will the hash value, which can be used to detect changes or corruption.</li>"
            "<li><strong>Digital Signatures:</strong> Provide a means to verify that a message, document, or other data file comes from a specific entity and has not been altered.</li>"
            "<li><strong>Access Controls:</strong> Limit data access to authorized users to prevent unauthorized modifications.</li>"
            "</ul>"
        )
    },
    "Availability": {
        "What is Availability": (
            "<ul>"
            "<li>Availability refers to ensuring that data, systems, and services are accessible to authorized users when needed.</li>"
            "<strong><br>Here’s how availability is maintained in IT:</strong>"
            "<li>Redundancy: Creating multiple copies of data or system components that can take over in case of a failure.</li>"
            "<li>Fault Tolerance: Building systems that can continue operating properly even if some of their components fail.</li>"
            "<li>Backup Systems: Regularly backing up data and systems to enable recovery in case of data loss or corruption.</li>"
            "<li>Disaster Recovery Plans: Having a plan in place to recover from significant adverse events, such as natural disasters, power outages, or cyberattacks.</li>"
            "<li>The goal of ensuring availability is to prevent service disruptions due to system failures, infrastructure problems, or malicious attacks like Distributed Denial of Service (DDoS).</li>"
            "</ul>"
        )
    },
    "Non-repudiation": {  # New section for Non-repudiation
        "What is Non-repudiation": (
            "<ul>"
            "<li>It ensures that a party in a communication cannot deny the authenticity of their signature on a document or the sending of a message that they originated.</li>"
            "<li>It can be implemented using digital signatures.</li>"
            "<li>Digital signatures use cryptographic techniques, a digital signature binds a person to the digital data they send.</li>"
            "</ul>"
        )
    },
    "EXAM NOTE" :{  # New section for section summary
        "Remember the main components of the CIA triad security model are confidentiality, integrity, and availability. Also know that nonrepudiation is the assurance that something cannot be denied by someone.": (
            ""
        )
    },
}

# Function to generate audio and return the file path
def generate_audio(text):
    tts = gTTS(text=text, lang='en')
    audio_file_path = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
    tts.save(audio_file_path.name)
    return audio_file_path.name

# Streamlit app layout
st.title("CompTIA Security+ Study Guide")
st.subheader("Flashcards")

# Color picker for background color
bg_color = st.color_picker("Choose a background color for the flashcards:", value="#D9D9D9")

# Display the flashcards with the selected background color
for title, content in flashcards.items():
    st.markdown(
        f"""
        <div style="border: 0.5px solid #000000; border-radius: 10px; background-color: {bg_color}; padding: 20px; margin: 10px 0; 
                     box-shadow: rgba(0, 0, 0, 0.15) 2.4px 2.4px 3.2px;">
            <h4 style="text-align: center;">{title}</h4>
            {"<br>".join([f"<strong>{key}</strong>: {description}" for key, description in content.items()])}
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button(f"Read '{title}' aloud"):
        # Prepare the content to be read aloud, stripping HTML tags
        audio_text = "\n".join([
            f"{key}: {strip_html(description)}" for key, description in content.items()
        ])
        audio_file_path = generate_audio(audio_text)
        st.audio(audio_file_path)  # Streamlit audio player to play the generated audio immediately
