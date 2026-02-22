# Ghayrah-Shield v0.1-Alpha
**Local AI-Driven Content Protection & Infrastructure Defense**

## Philosophy
The Ghayrah-Shield is a sovereign security layer designed to enforce moral boundaries on a technical level. It operates on a **Zero-Trust** basis: all visual analysis is performed locally via Ollama.

## Technical Stack
- **Engine:** Python 3.12
- **Vision AI:** Moondream (Lightweight Vision Model)
- **Infrastructure:** Linux (X11/NMCLI)
- **Hard Enforcement:** Automatic Network Kill-Switch (BANG-Protocol)

## Core Features
- **Real-time Screen Scanning:** Monitors the visual output every 0.5s.
- **Pre-emptive Blur:** Complemented by a Browser Extension to hide content before rendering.
- **Hard-Kill:** Immediate network termination upon detection of indecency.
- **Mission Logging:** Transparent auditing of all security events in `mission_log.json`.

## Usage
1. Install requirements: `pip install requests`
2. Pull Vision Model: `ollama pull moondream`
3. Run the Shield: `python3 shield_core.py`

---
*Developed by Architect-DNA (contract@architect-dna.ch)*
