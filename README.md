# 🚂 YatraGuard — Autonomous Regional Rail Co-Pilot for Elders

> *"My mom traveled alone from Mumbai to Nagpur. 14 hours. She called me 9 times asking where the train was. I stayed awake till 3 AM to make sure she didn't miss her station. Next morning I started building YatraGuard."*

YatraGuard is a **stateful, long-running Kestra orchestration** that turns a simple WhatsApp message into an autonomous 24-hour travel shield for your parents.

No app to install. Just WhatsApp.

---

## 🧠 How It Works

```
[Parent sends Train Number on WhatsApp]
              │
              ▼
  [Kestra Webhook Ingestion Gateway]
              │
              ▼
     [Groq AI Parsing & Translation]
   Extracts Train No, Destination, Language
              │
              ▼
   [PostgreSQL Active Journey Ledger]
   Registers the journey lifecycle
              │
              ▼
 [30-Minute Dynamic Monitoring Mesh]
   Queries IRCTC Live Train Status API
   Sends localized updates to parent
              │
              ▼
    [Destination Proximity Detection]
   Train is approaching destination...
              │
        ┌─────┴─────┐
        ▼           ▼
[WAKE-UP ALARM]  [FAMILY PICKUP DISPATCH]
 Parent's phone   Family coordinator's phone
 in their language fires simultaneously
```

---

## 🆓 100% Free Stack

| Component        | Tool                         | Cost       |
|------------------|------------------------------|------------|
| WhatsApp Receive | Twilio Sandbox               | Free       |
| WhatsApp Send    | Twilio Sandbox               | Free       |
| Train Live Data  | RapidAPI IRCTC API           | Free tier  |
| AI Parsing       | Groq (llama3-8b-8192)        | Free       |
| Database         | PostgreSQL (local via Docker) | Free       |
| Orchestration    | Kestra                       | Free       |
| Public Webhook   | ngrok                        | Free       |

---

## ⚙️ Setup Instructions

### Step 1 — Get Your API Keys

#### Twilio (WhatsApp Sandbox)
1. Go to [twilio.com](https://twilio.com) → Sign up free
2. Navigate to **Messaging → Try it out → Send a WhatsApp message**
3. Follow the steps to join the sandbox from your phone
4. Copy your **Account SID** and **Auth Token**

#### RapidAPI (IRCTC Indian Railways)
1. Go to [rapidapi.com](https://rapidapi.com) → Sign up free
2. Search for **"IRCTC Indian Railways"** → Subscribe to `irctc1.p.rapidapi.com`
3. Copy your **RapidAPI Key**

---

### Step 2 — Update `docker-compose.yml`

Fill in your secrets in the `kestra` service environment block:

```yaml
SECRET_TWILIO_ACCOUNT_SID: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
SECRET_TWILIO_AUTH_TOKEN:  "your_twilio_auth_token"
SECRET_RAPIDAPI_KEY:       "your_rapidapi_key"
SECRET_FAMILY_PHONE:       "91XXXXXXXXXX"   # No + prefix
```

---

### Step 3 — Start the Stack

```powershell
docker compose up -d
```

Verify Kestra is running at [http://localhost:8080](http://localhost:8080)

---

### Step 4 — Expose Webhook with ngrok

```powershell
ngrok http 8080
```

Copy the `https://xxxx.ngrok.io` URL.

---

### Step 5 — Import Flows into Kestra

In the Kestra UI at [http://localhost:8080](http://localhost:8080):
1. Go to **Flows → Create**
2. Paste the contents of each YAML file:
   - `yatraguard-ingest.yml`
   - `yatraguard-monitor.yml`
   - `yatraguard-cleanup.yml`
3. Save all three flows

---

### Step 6 — Configure Twilio Webhook

In Twilio Console → **WhatsApp Sandbox Settings** → set **"When a message comes in"** to:

```
https://xxxx.ngrok.io/api/v1/executions/webhook/yatraguard/yatraguard-ingest/yatraguard-whatsapp-gateway
```

---

### Step 7 — Test It!

Send a WhatsApp message to your Twilio sandbox number:

```
12952 Nagpur
```

or in Hindi:

```
ट्रेन 12952 नागपुर जा रही हूँ
```

Watch YatraGuard:
1. ✅ Parse the train number and destination
2. ✅ Register the journey in the database
3. ✅ Send a confirmation back in your language
4. ✅ Start the 30-minute monitoring loop
5. ✅ Fire parallel wake-up + pickup alerts when approaching

---

## 📂 File Structure

```
rail-copilot-kestra/
├── docker-compose.yml         # Docker stack with all secrets
├── yatraguard-ingest.yml      # Flow 1: WhatsApp → Parse → Register → Confirm
├── yatraguard-monitor.yml     # Flow 2: 30-min loop → Live data → Alerts
├── yatraguard-cleanup.yml     # Flow 3: Daily cleanup & analytics
└── README.md
```

---

## 🏆 Why This Wins

This project showcases **every advanced Kestra capability**:

| Kestra Feature                 | Used In YatraGuard                            |
|--------------------------------|-----------------------------------------------|
| Long-running stateful workflow | 24-hour journey monitoring loop               |
| Webhook trigger                | WhatsApp message ingestion                    |
| Schedule trigger               | 30-min monitoring + daily cleanup             |
| Python Script tasks            | AI parsing, API calls, DB operations          |
| PostgreSQL plugin              | Journey state persistence                     |
| Secret management              | All API keys secured                          |
| Parallel execution concept     | Wake-up alarm + pickup dispatch simultaneously |

---

*Built with ❤️ to give Indian families peace of mind.*
