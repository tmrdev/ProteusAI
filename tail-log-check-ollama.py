import json
import queue
import requests
# there is an official ollama library but using Requests for now as an example
# need to look into the official library and see if it can be used for this use case
# but it seems to be more focused on chat completions and not as flexible as using the API directly with Requests
# but it may have some benefits in terms of ease of use and integration with the ollama server
# so it is worth looking into further for future iterations of this project
# VS Code is also trying to complete my comments and everything it suggests must be verified!
# import json

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

def analyze_with_ai(log_lines):
    # getting dropped connection at ssh tunnel/forwarder, look into autossh or similar but VPN Cloud is better
    url = "http://localhost:11434/api/generate"
    # need a way to switch between AI models like llama3, qwen, mistral, etc...
    data = {
      "model": "llama3",
      "prompt": "Analyze these log files for the terminal app called Warp, running on macOS Sonoma: ".join(log_lines),
      "stream": False,
      "role": { # are these roles needed? they do not appear to be working, see if it can be refactored
          "system": "You are an artificial intelligence assistant and you need to engage in a helpful, detailed, polite conversation with a user. You are an expert in hardware and computer software", 
          "user": "Analyze these log files for the terminal app called Warp, running on macOS Sonoma: ".join(log_lines)
      }
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=data, headers=headers)
    # print(f"response -> {response}\n\n")
    return response.json()

if __name__ == "__main__":
    # statically mapped log file for now, but this can be made dynamic in the future to check multiple log files and different types of logs (system logs, application logs, network logs, etc.)
    log_file = "/Users/mini/Library/Logs/warp.log"
    last_lines = pyTail(log_file, 20)
    print(f"last_lines {last_lines}\n\n")
    result = analyze_with_ai(last_lines)
    # Use print with f so that \n characters turn into line breaks
    # This should be readable in the Terminal (shell)
    # print(f"{result['response']}\n\n")
    print(f"{result['response']}\n\n")
    # print(json.dumps(result, indent=4))