# Command executed in Terminal for connecting to ollama models
# SSH Tunnel With Forwarding To ollama at port 11434
# autossh -M 0 -v -N -o "ServerAliveInterval 30" -o "ServerAliveCountMax 3" -L 11434:localhost:11434 username@domain.com

# ProteusAI - may change to GIAS (Ghost In A Shell) or GITS (Ghost In The Shell)
An AI security bot for checking logs, sniffing packets and assisting the development process. AI Anomaly detection.

# Getting Setup
- __Verify requirements.txt exists__

  ```bash
  ls requirements.txt
  ```

- __Create virtual environment__

  ```bash
  python3 -m venv venv
  ```

- __Activate virtual environment__

  ```bash
  source venv/bin/activate
  ```

- __Install dependencies from requirements.txt__

  ```bash
  pip install -r requirements.txt
  ```

- __Deactivate virtual environment__

  ```bash
  deactivate
  ```


# This is a proof of concept that needs many things to be mapped out
- need to look into running the bot inside Docker on Linux and utillizing Apple Containers on macOS
- is there a more lightweight solution on Linux that can replace Docker?
- Support for sniffing packets will not be easy but start out with small pcaps or similar
- Two Main Modes for Sniffing: 1) Dev mode to aid in debugging network connections 2) Security Bot detecting anomalies and hacks
- AI will need to save State across the board, especially when analzying network traffic
- Network Anomalies will be revealed over time, false positves will spring up so a labeling system with weights will be needed (research!)
- Priority is to get this working on Linux and macOS, with a possible release on Windows that leverages the Linux Sub-System
- Can a RAG system be used that saves State? Need extensive research on this and setting up debugging that proves State is being Saved
- Lastly and most importantly - Do you have Bud in bottles? Checks R In Da Mail - Promise
