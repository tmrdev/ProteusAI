# Command executed in Terminal for connecting to ollama models
# SSH Tunnel With Forwarding To ollama at port 11434
# SSH Tunnels should be temporary and only used to quickly test an AI API endpoint
# autossh -M 0 -v -N -o "ServerAliveInterval 30" -o "ServerAliveCountMax 3" -L 11434:localhost:11434 username@domain.com

# ProteusAI - will change to GIAS (Ghost In A Shell) or GITS (Ghost In The Shell)
An AI security bot for checking logs, sniffing packets and assisting the development process. AI Anomaly detection.

# WireGuard - VPN is now being used for interfaceing with open source AI models like gemma, hermes, jarvis
# All AI infrastructure should be inside a VPN Cloud, this will evolve in the future, the future is encrypted private networks, meshed, multi-levels

# Working on an update for sniffing network traffic, there will be multiple ways to sniff traffic

# For now it will be: 

1) Saving PCAP files and then parsing them out to CSV / JSON and other methods and analzying

2) Live MCP Server which will be more complicated and intense, so the first method will be easy to implement as a starting point

3) Will need dedicated workstations / servers analyzing network traffic, which requires massive amounts of storage

4) Need to focus on how AI Agents play their role, may need as many as 10 agents or more, starting out simple and scaling up

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
