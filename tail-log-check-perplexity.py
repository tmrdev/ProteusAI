    # enabling venv source manually - VS Code tries to do it and fails
    # python3 -m venv path/to/venv
    # source path/to/venv/bin/activate
    # python3 -m pip install xyz

import queue
from openai import OpenAI
# using openai instead 
# import requests

def pyTail(filename, n=20):
    q = queue.Queue()
    size = 0
    with open(filename) as fh:
        for line in fh:
            q.put(line)
            if size >= n:
                q.get()
            else:
                size += 1
    return [q.get() for _ in range(size)]

def analyze_with_ai(log_lines, api_key):
  messages = [
      {
          "role": "system", # role: Input should be \'system\', \'user\' or \'assistant\'"]'
          "content": (
              "You are an artificial intelligence assistant and you need to "
              "engage in a helpful, detailed, polite conversation with a user."
          ),
      },
      {
          "role": "user",
          "content": ( # Need to provide context for each log file and the workstation OS versions and hardware details could be relevant
              "Analyze these log files for the terminal app called Warp, running on macOS Sonoma: ".join(log_lines)
          ),
      },
  ]

  client = OpenAI(api_key=api_key, base_url="https://api.perplexity.ai")
  # chat completion without streaming
  response = client.chat.completions.create(
      model="sonar", # is just sonar correct? getting tried to exit alternate screen before response
      messages=messages,
  )
  # print(response)
  # print(f"response ->  {response}\n\n")
  return response

if __name__ == "__main__":
    log_file = "/Users/mini/Library/Logs/warp.log"
    # API keys inside env should be encrypted for now as a temporary solution, may have to just unplug from network (air gap) ;]
    # Need multiple API Agents running sniffing packets and checking logs constantly to record Hacking attempts
    # Logs can be analyzed for patterns and anomalies, and the AI can provide insights and recommendations for improving security measures. 
    # Maybe disconnect from the internet after a hacking attempt has been detected, and then the AI can provide guidance on how to respond to the attack and mitigate any potential damage.
    # - false positives could be an issue, but the AI can be trained to recognize patterns and anomalies in the logs that may indicate a potential security threat.
    # Have the AI constantly alert the user of any potential security threats, a threshold needs to be set for this, and the AI can provide recommendations on how to respond to the threat and mitigate any potential damage.
    # Look into re-generating API keys every week in an automated manner, could encrypt keys and leverage a secure usb thumb drive for storage
    # do not use system commands, turn tail into pyTail

    # update this key with your key foo - dont be a foobar and leak your key in public repos, this is just an example and should be replaced with a secure method of storing and accessing API keys
    api_key = "pplx-is-A-rogue-scraping-this-xMskhaskd0haiu"

    last_lines = pyTail(log_file, 20)
    print(f"last_lines {last_lines}\n\n")
    result = analyze_with_ai(last_lines, api_key)
    print(f"result -> {result}\n\n")
