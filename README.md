# VoiceAssistant
A Smart AI-Powered Voice Assistant with Advanced NLP & System Automation
Introducing an AI powered voice assistant that seamlessly integrates speech recognition, conversational AI, and system automation to create a more intelligent and responsive user experience. Designed to understand complex commands, retain context, execute system tasks, retrieve real-time information, and respond through voice output, this assistant offers a natural and efficient way to interact with technology.


🔍 Key Features & Capabilities

✅ 🎤 Whisper AI-Powered Speech Recognition
Leverages OpenAI’s Whisper ASR for highly accurate live speech-to-text conversion, effectively handling diverse accents and background noise.

✅ 💬 Conversational AI with Mistral-7B & BlenderBot
Integrates Mistral-7B for context-aware interactions and BlenderBot-400M Distill for dynamic, multi-turn conversations, ensuring fluid and engaging dialogue.

✅ 🧠 Advanced NLP with Context Awareness
Utilizes spaCy’s dependency parsing, semantic similarity scoring, and fuzzy matching to accurately interpret commands, even when involving nuanced phrasing.

✅ 📂 Efficient Program Execution with Voice Commands
Enables system-level automation using Python, allowing users to launch system level applications with voice commands.

✅ 🔍 Real-Time Information Retrieval
Fetches live updates, summaries, and insights using local indexing and external APIs, ensuring fast and relevant responses.

✅ 🔊 Responsive Voice Output
Provides spoken responses, enhancing interaction fluidity and accessibility.

🛠️ Tech Stack & Methodologies Used

🚀 Speech-to-Text: Whisper AI (ASR)

🚀 Conversational AI: Mistral-7B, Facebook BlenderBot-400M Distill

🚀 NLP & Command Processing: spaCy, Fuzzy Matching, Dependency Parsing

🚀 OS-Level Automation: Python (subprocess, os for system commands)

🚀 Data Retrieval: Local indexing & external APIs for intelligent lookups.

🚀 How to Run
1️⃣ Clone the Repository
git clone https://github.com/21F-9108/VoiceAssistant.git
cd VoiceAssistant

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Download spaCy Language Model
python -m spacy download en_core_web_sm

4️⃣ Run the Voice Assistant
streamlit run main.py


