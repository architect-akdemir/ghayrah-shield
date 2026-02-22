import os
import requests
import base64
import sys
import json
import subprocess
from datetime import datetime

# PROJECT: GHAYRAH-SHIELD v0.1-ALPHA
# IDENT: contract@architect-dna.ch
# MODEL: moondream (Lightweight Vision)
# PHILOSOPHY: PRE-EMPTIVE STRIKE. HARD ENFORCEMENT.

def log_mission(status, detail):
    """Dokumentiert den Vorfall in der mission_log.json."""
    log_file = "mission_log.json"
    timestamp = datetime.now().isoformat()
    try:
        if os.path.exists(log_file):
            with open(log_file, "r+") as f:
                data = json.load(f)
                data["logs"].append({"ts": timestamp, "st": status, "det": detail})
                f.seek(0)
                json.dump(data, f, indent=2)
        else:
            with open(log_file, "w") as f:
                json.dump({"project": "Ghayrah-Shield", "logs": [{"ts": timestamp, "st": status, "det": detail}]}, f, indent=2)
    except Exception:
        pass

def trigger_blackout():
    """Sofortiger Kill-Switch: Netzwerk aus + Visueller Block."""
    print("🚨 [BANG] SECURITY BREACH!")
    # 1. Netzwerk sofort kappen
    os.system("nmcli networking off")
    # 2. Visueller Block (Zenity Overlay) & Monitor aus
    subprocess.Popen(["zenity", "--error", "--text='GHAYRAH VIOLATION: SYSTEM LOCKED'", "--title='SHIELD'"])
    os.system("xset dpms force off") 
    log_mission("BANG", "Indecency detected. Network terminated and screen locked.")

def analyze_image(image_path):
    """KI-Analyse via lokalem Ollama-Server."""
    if not os.path.exists(image_path):
        return "NULL"
    try:
        with open(image_path, "rb") as img_file:
            img_str = base64.b64encode(img_file.read()).decode('utf-8')

        payload = {
            "model": "moondream",
            "prompt": "Is there any nudity, bare skin or indecency? Answer ONLY with 'SAFE' or 'DANGER'.",
            "images": [img_str],
            "stream": False
        }
        
        response = requests.post('http://localhost:11434/api/generate', json=payload, timeout=10)
        return response.json().get('response', '').strip().upper()
    except Exception as e:
        return f"ERROR: {str(e)}"

if __name__ == "__main__":
    target = "test_view.jpg"
    
    if not os.path.exists(target):
        sys.exit(1)

    result = analyze_image(target)
    
    # Trigger-Logik: Erkennt Moondream Gefahr oder Nacktheit?
    if any(k in result for k in ["DANGER", "NUDITY", "INDECENCY", "SKIN"]):
        trigger_blackout()
        sys.exit(0)
    else:
        log_mission("SAFE", "Infrastruktur-Check erfolgreich.")
        print(f"✅ [SYSTEM]: {result}")
