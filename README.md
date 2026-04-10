# 🏙️ NavNagar – Generative AI City Assistant

**NavNagar** is a **Generative AI-powered City Assistant** built using **LangChain Agents, Mistral LLM, and Streamlit**, designed to provide real-time **weather updates** 🌡️ and **latest news** 📰 for any Indian city.

---

## 🚀 Features

* 🌦️ **Weather Information**

  * Get real-time weather data using OpenWeather API
* 📰 **Latest News**

  * Fetch current news using Tavily Search API
* 🧠 **AI Agent System**

  * Powered by LangChain Agents + Mistral LLM
* 🔧 **Tool Calling**

  * Automatically selects the right tool based on user query
* 💬 **Interactive Chat UI**

  * Modern chat interface built with Streamlit + custom HTML/CSS
* ⚡ **Real-Time Responses**

  * Fast and dynamic API-driven outputs

---

## 🏗️ Tech Stack

* **Frontend:** Streamlit (Custom UI + HTML/CSS)
* **Backend:** Python
* **LLM:** Mistral (via LangChain)
* **Agent Framework:** LangChain
* **APIs Used:**

  * OpenWeather API
  * Tavily Search API
* **Libraries:**

  * dotenv
  * requests

---

## 📂 Project Structure

```bash
├── app.py              # Streamlit frontend
├── Agents.py           # Agent + Tools + LLM setup
├── .env                # API keys (not included)
├── requirements.txt    # Dependencies
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/navnagar.git
cd navnagar
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Setup Environment Variables

Create a `.env` file:

```env
OPENWEATHER_API_KEY=your_openweather_api_key
TAVILY_API_KEY=your_tavily_api_key
MISTRAL_API=your_mistral_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 💡 How It Works

1. User enters a query (e.g., *"Weather in Delhi"* or *"News in Mumbai"*)
2. LangChain Agent processes the input
3. Agent decides which tool to call:

   * `get_weather()` → Weather API
   * `get_news()` → Tavily API
4. Tool fetches real-time data
5. Response is displayed in chat UI

---

## 🧠 Architecture

```
User → Streamlit UI → LangChain Agent → Tool Selection
     → API Call → Response → UI Display
```

---

## 🔮 Future Improvements

* 🧠 Add conversation memory
* 🌍 Expand to global cities
* 🏨 Travel & hotel recommendations
* 🗺️ Maps integration
* 📊 More intelligent tools
* ☁️ Deployment (Streamlit Cloud / Render)

---

## 👨‍💻 Author

**Devansh Kumar Tiwari**

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!

---
