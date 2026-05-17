# 🎤 YatraGuard — 3-Minute Hackathon Pitch & Video Demo Script

This script is structured to help you deliver a high-energy, emotionally resonant, and technically flawless presentation that will capture the judges' attention immediately.

---

## ⏱️ Section 1: The Hook (0:00 - 0:45)
**Visual Cue:** Show a split-screen slide. Left side: A screenshot of a messaging feed crowded with panicked family calls. Right side: A senior citizen sitting peacefully looking out of a train window.

*   **Speaker:** 
    "A few weeks ago, we observed our elderly neighbor, Sharma Uncle, preparing for a 14-hour overnight train journey alone. He was clutching a paper notebook filled with numbers, visibly anxious about how he would know if his station arrived at 3 AM in the middle of the night. His children were calling him every hour, draining his phone battery just to check his live location. 
    
    This is the anxious reality for millions of India's 140 million senior citizens who face severe app-friction, spam-heavy interfaces, and the constant stress of traveling alone. 
    
    Why should our elders live in anxiety when modern orchestration can act as their silent digital guardian? That morning, we built **YatraGuard**—an autonomous regional rail co-pilot that turns a simple WhatsApp message into a stateful, 24-hour travel shield."

---

## 💻 Section 2: Live Demo Walkthrough (0:45 - 2:00)
**Visual Cue:** Play a screen recording of your Twilio WhatsApp Sandbox interface in real-time, showing the conversational flow.

*   **Speaker:**
    "The beauty of YatraGuard is **zero friction**. There is no app to download, no accounts to create, and no memory-hogging installations. It runs entirely where elders are already comfortable: **WhatsApp**.

    Let’s watch a live journey begin. The passenger simply texts their train number and destination in their native language—for example, *'नमस्ते, ट्रेन 12952 नागपुर जा रही हूँ'*.
    
    Behind the scenes, Kestra's event-driven webhook gateway intercepts the message. An AI parsing model instantly extracts the train number, destination, and passenger's preferred language: **Hindi**.
    
    YatraGuard registers the journey state inside a PostgreSQL database and instantly responds on WhatsApp with a localized, multi-lingual confirmation card and a quick-command command pad."

**Visual Cue:** Show the WhatsApp quick-commands (1 to 9). Highlight Option 5 (Video Guide) and Option 9 (AI Storyteller).

*   **Speaker:**
    "Passengers aren't left alone. By replying with single-digit commands, they get instant utility:
    *   **Option 5** delivers a highly polished, high-definition local safety guide video compiled dynamically in their language, showing them exactly how to navigate their journey securely.
    *   **Option 9** launches our **AI Storyteller**, which prompts Groq to weave rich, cultural folklore, historical facts, and culinary stories about upcoming stations, turning a boring journey into a fascinating tour guide experience."

---

## ⚙️ Section 3: Technical Underpinnings (2:00 - 2:30)
**Visual Cue:** Show a clean high-level architecture diagram featuring Kestra, PostgreSQL, Twilio, and Groq.

*   **Speaker:**
    "How does this scale? YatraGuard is built entirely on a **stateful, long-running Kestra orchestration mesh**:
    1.  **Stateful Polling:** Every 30 minutes, Kestra’s schedule cron queries live IRCTC telemetry APIs, updating the passenger's live delay and platform status in our Postgres database.
    2.  **The Proximity Gate:** When telemetry shows the train entering a 30km radius of the destination, Kestra executes a **parallel dual-alarm**:
        *   An urgent wakeup notification rings on the elder's phone: *'⏰ Wake up! Gather your bags, family is on the way!'*
        *   Simultaneously, a pickup alert is dispatched to the family coordinator's phone, showing the train's precise live delay and platform details so they can leave for the station exactly on time.
    3.  **Automatic Purges:** A daily cleanup cron purges stale journeys, maintains ledger health, and compiles analytics."

---

## 🏆 Section 4: The Impact & Close (2:30 - 3:00)
**Visual Cue:** Show a final slide with a big, warm smile of an Indian grandmother/grandfather traveling, with the YatraGuard contact QR code.

*   **Speaker:**
    "YatraGuard isn't just a technical integration; it is a **human-centric bridge** across the digital divide. By combining the enterprise-grade stateful orchestration of **Kestra**, the low-latency intelligence of LLMs, and the absolute accessibility of WhatsApp, we have created a digital guardian that stands guard over elders like Sharma Uncle, giving their families absolute peace of mind.
    
    Let's keep our railways safe, our elders independent, and our families connected. 
    
    Thank you!"
