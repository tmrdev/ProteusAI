# See README.md for more details on this project and the goals of this script.
# tail-log-check-perplexity.py is a script that checks the last 20 lines of a log file and sends it to the Perplexity API for analysis
# The script uses the OpenAI library to interact with the Perplexity API
# and it is designed to be run on a regular basis to check for any anomalies or issues in the log files
# The script can be easily modified to check different log files or to use different AI models for analysis
# The goal of this script is to provide a simple and effective way to monitor log files and get insights from them using AI
# Since Perplexity API costs money, it needs a built in limiter that checks how much quota is left and refuses to execute
# after a certain threshold is reached, this is to prevent running up a large bill and to ensure that the script is used responsibly

import json
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
              "Analyze these log files and return a JSON Object for the terminal app called Warp, running on macOS Sonoma:".join(log_lines)
          ),
      },
  ]

  client = OpenAI(api_key=api_key, base_url="https://api.perplexity.ai")

  # chat completion without streaming
  # returning a JSON object according to the json_schema that Perplexity API enforces
  # this is to ensure that the response is structured and can be easily parsed and used for further analysis or actions
  # Check and see if attributes from the old code are not appearing here?
  response = client.chat.completions.create(
      model="sonar", # is just sonar correct? getting tried to exit alternate screen before response
      messages=messages,
      response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "log_analysis",
            "schema": {
                "type": "object",
                "properties": {
                    "status": {"type": "string"},
                    "summary": {"type": "string"}
                },
                "required": ["status", "summary"]
            }
        }
    }
  )
  response = json.loads(response.choices[0].message.content)
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
    # keys needs to be encrypted and stored securely, can an Image Steg or encrypting each key work?
    # Axios and other libaries are getting hacked and keys are being leaked, so it is important to have a secure method of storing and accessing API keys
    api_key = "pplx-is-A-rogue-AI-scraping-this-xMskhaskd0haiu"

    last_lines = pyTail(log_file, 20)
    # print(f"last_lines {last_lines}\n\n")
    result = analyze_with_ai(last_lines, api_key)
    # print(f"{result}\n\n")
    # NOTE: Ident set to 4 allows for Pretty Printing of JSON
    print(json.dumps(result, indent=4))

