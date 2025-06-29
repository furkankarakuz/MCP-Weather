# MCP-Weather 🌦️

This project provides a server built with the Model Completion Protocol (MCP), designed to deliver up-to-date weather information in response to real-time queries. By integrating the OpenWeather API, the server allows AI models to fetch accurate weather data based on location input and return structured responses. This tool enables enhanced interaction between language models and live environmental data sources.

![image](https://github.com/user-attachments/assets/174a0ea6-54e1-4005-ab6e-6ea87325f91e)

---

## 🔍 What is MCP?

Model Context Protocol (MCP) is an open-source protocol that enables AI models to securely connect to various data sources and applications. In other words, it acts as a kind of "connection protocol." Developed by Anthropic, MCP allows AI agents to access, interact with, and utilize your files, databases, applications, and other tools.
[Learn more: [Medium Article](https://medium.com/@furkankarakuz/mcp-nedir-mcp-server-nas%C4%B1l-kurulur-664549be9020)]

---

## 🔧 Installation & Run

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

Note : Make sure you have a valid API key from [OpenWeather](https://openweathermap.org/)
```
OPENWEATHER_API_KEY=YOUR_API_KEY
```

4. **Run the server:**

```bash
uv run mcp install main.py
```

## 📜 License

This project is licensed under the Apache License 2.0
