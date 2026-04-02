# ProteusAI
An AI security bot for checking logs, sniffing packets and assisting the development process. AI Anomaly detection.

# This is a proof of concept that needs many things to be mapped out
- need to look into running the bot inside Docker on Linux and utillizing Apple Containers on macOS
- is there a more lightweight solution on Linux that can replace Docker?
- Support for sniffing packets will not be easy but start out with small pcaps or similar
- AI will need to save State across the board, especially when analzying network traffic
- Network Anomalies will be revealed over time, false positves will spring up so a labeling system with weights will be needed (research!)
- Priority is to get this working on Linux and macOS, with a possible release on Windows that leverages the Linux Sub-System
- Can a RAG system be used that saves State? Need extensive research on this and setting up debugging that proves State is being Saved
- Lastly and most importantly - Do you have Bud in bottles? Checks R In Da Mail - Promise
