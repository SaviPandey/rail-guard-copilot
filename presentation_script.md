# Project YatraGuard: The Autonomous Regional Rail Co-Pilot for Elders

## 🎬 0:00 - The Hook (The Emotional Reality)
*(Visual: Dimly lit room, a clock reads 3:15 AM. A phone screen lights up with missed calls. A stressed person is looking at a complex, confusing train tracking app.)*

**Voiceover (You):**
"If you have Indian parents, you know this exact panic. Every month, millions of our parents travel long distances on trains. And what do we do? We become their manual tracking center. We stay awake until 4 AM tracking the train, terrified they'll oversleep and miss their station. This is Project YatraGuard — an autonomous, regional rail co-pilot that turns a simple WhatsApp message into a stateful travel shield using Kestra."

## 🎬 0:25 - The Problem Statement
*(Visual: Screen recording scrolling through clunky UI of generic train apps, cutting to simple WhatsApp chat.)*

**Voiceover:**
"Manan won the hackathon because he built something with *soul*. He built a health tool for his mom using WhatsApp in Gujarati. I realized we need to stop inventing artificial corporate problems and solve the genuine, high-anxiety realities our families face every single week. This isn't a software bug. It's an emotional time-sink affecting 23 million daily rail passengers."

## 🎬 0:45 - The Solution & Tech Stack
*(Visual: Title card 'Project YatraGuard: The Autonomous Rail Co-Pilot'. Transition to Kestra logo pulsing, connected to Groq and WhatsApp logos.)*

**Voiceover:**
"This isn't a basic linear script that crashes when your computer sleeps. YatraGuard is an event-driven, stateful tracking grid powered by Kestra, backed by a localized containerized database, Twilio gateways, and lightning-fast open intelligence."

## 🎬 1:00 - The Demo (Ingestion & Parsing)
*(Visual: Split screen. Left: Parent sends a WhatsApp message: 'ट्रेन 12952 नागपुर जा रही हूँ'. Right: Kestra UI live execution.)*

**Voiceover:**
"Watch this. My dad drops a text or voice update into WhatsApp. Immediately, Kestra's high-velocity webhook ingests the payload. We pass the raw string to Llama-3 via Groq to extract the train number, destination, and the user's regional language natively. Kestra then logs this active lifecycle directly into our local Dockerized PostgreSQL ledger."

## 🎬 1:20 - The Demo (Stateful Monitoring)
*(Visual: Kestra UI showing a cyclical flow, polling an API every 30 minutes.)*

**Voiceover:**
"Now, the magic of orchestration. This isn't a basic script. Kestra maintains an active, long-running cron-mesh. Every 30 minutes, it polls the live IRCTC rail telemetry API. It translates the raw delay structures and automatically pushes comforting, localized updates straight to my dad in Hindi, Marathi, or English. But here comes the climax."

## 🎬 1:40 - The Climax (The Parallel Safety Mesh)
*(Visual: Map showing train hitting a 30km radius of the destination. Kestra dashboard flashes to a 'Parallel Execution' node. Two WhatsApp messages fire simultaneously.)*

**Voiceover:**
"The train hits the destination boundary in the dead of night. Kestra's proximity gate triggers instantly, waking from its background state to fire a high-priority parallel execution flow.

*Node 1* blasts a loud, native-language wake-up alert to my dad's phone so he never oversleeps.
*Node 2* simultaneously dispatches a pickup notice with real-time delay info to my phone at home: 'Train is 20 minutes away. Leave now.'

Zero panic. Seamless coordination. That is the raw power of Kestra."

## 🎬 2:10 - The Conclusion (The Flex)
*(Visual: You speaking directly to the camera, confident.)*

**Voiceover:**
"We transformed Kestra from a developer utility into a Long-Running, Event-Driven Proximity Engine. We managed dynamic state, persistent Dockerized PostgreSQL logging, Groq-powered multilingual AI parsing, and parallel multi-user WhatsApp alerts via Twilio. But most importantly... we gave families their peace of mind back.

This is Project YatraGuard. Thank you."
