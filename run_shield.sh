#!/bin/bash
while true; do
    # 1. Screenshot erstellen
    import -window root test_view.jpg
    
    # 2. Prüfen ob Datei existiert, dann Scan
    if [ -f test_view.jpg ]; then
        python3 shield_core.py
        rm test_view.jpg
    fi
    
    # 3. Taktfrequenz
    sleep 2
done
