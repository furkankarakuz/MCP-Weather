# MCP-Weather 🌦️

This project provides a server built with the Model Completion Protocol (MCP), designed to deliver up-to-date weather information in response to real-time queries. By integrating the OpenWeather API, the server allows AI models to fetch accurate weather data based on location input and return structured responses. This tool enables enhanced interaction between language models and live environmental data sources.
MCP-Weather enables AI agents to query live weather data automatically, securely, and in a standardized way, thanks to MCP.

![weather](https://github.com/user-attachments/assets/ab270f78-9531-448b-b2a2-784f8ac13e5c)

---

## 🔍 What is MCP?

Model Context Protocol (MCP) is an open-source protocol that enables AI models to securely connect to various data sources and applications. In other words, it acts as a kind of "connection protocol." Developed by Anthropic, MCP allows AI agents to access, interact with, and utilize your files, databases, applications, and other tools.
[Learn more: [Medium Article](https://medium.com/@furkankarakuz/mcp-nedir-mcp-server-nas%C4%B1l-kurulur-664549be9020)]

---

## ⚙️ How It Works

This app standardizes the weather data in JSON format to ensure compatibility with AI tools like Claude Desktop.

- When the user or AI queries something about the weather, Claude automatically triggers the `get_weather` tool.
- If the query isn't related to the weather, the tool remains inactive.
- The triggering process is fully handled by Claude itself.

This design transforms it from a simple weather app into a protocol-based, AI-integrated tool.

Note : Unlike regular weather apps where the user manually queries weather information, MCP-Weather works as a protocol-based tool. It standardizes weather data in JSON and operates within the MCP framework. AI models like Claude Desktop automatically trigger it based on the user’s question, without manual intervention. This makes it a seamlessly integrated backend service rather than a standalone weather app.

---

## 🛠️ Installation & Run

1. **Clone the repository:**

```bash
git clone https://github.com/furkankarakuz/MCP-Weather.git
cd MCP-Weather
```

2. **Install dependencies:**

```bash
uv venv
.venv\Scripts\activate
uv pip install .
```

3. **Set your OpenWeather API Key:**

Define OPENWEATHER_API_KEY in the .env file (you can check the Open Weather official site for API KEY and documentation).

```
OPENWEATHER_API_KEY=YOUR_API_KEY
```

4. **Run the server:**

```bash
uv run mcp install main.py
```

As a result, the json file will look something like the following:
```
{
  "mcpServers": {
    "Weather": {
      "command": "C:\\Users\\furkan\\.local\\bin\\uv.EXE",
      "args": [
        "run",
        "--with",
        "mcp[cli],requests",
        "mcp",
        "run",
        "C:\\Users\\furkan\\Desktop\\MCP-Weather\\main.py"
      ]
    }
  }
}
```

Note : After this command, the MCP Server installation is complete and the claude_desktop_config.json file is created again. (If the file does not contain “requests”, you can add it manually).

---

## 💻 Run with Claude Desktop
1. The Claud Desktop application opens. The “Weather” option should appear in the File > Settings > Developer tab and in the settings on the chat screen.

![1](https://github.com/user-attachments/assets/17eeeef2-11d9-43be-9243-e5847aa576d1)

2. When we click on “Weather” in the chat section, the `get_weather` tool defined in main.py is listed as active.

![2](https://github.com/user-attachments/assets/9c5207cc-6f06-4506-a236-d59b4a574e9d)

3. The `get_weather` operation starts when the question “What is the weather in London?” is asked.

![3](https://github.com/user-attachments/assets/4aa2f0b3-dc42-48ea-b4f0-b6ebf44d4558)

4. After validation, the response is returned with the parameters and return result of `get_weather`.

![4](https://github.com/user-attachments/assets/cafd1c14-4074-45f5-98c6-aaf5df66c714)
![5](https://github.com/user-attachments/assets/812d30cf-b754-4571-8959-32f7e57c5c72)
![6](https://github.com/user-attachments/assets/b704a71f-e394-438a-9134-71224ea77b46)

5. Result

> The weather in London is quite pleasant right now - it's 27°C (80°F) with scattered clouds. It feels like about 27°C as well, so not too humid. There's a light breeze at about 5 m/s, and humidity is at a comfortable 33%. Perfect weather for being out and about!

---

## 📜 License

This project is licensed under the Apache License 2.0
