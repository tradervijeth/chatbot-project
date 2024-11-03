# AI Chatbot with Claude

An intelligent chatbot powered by Anthropic's Claude AI that provides sophisticated, context-aware responses. Features a modern web interface and maintains natural conversations. Built with Python Flask and the Anthropic API.

⚠️ **IMPORTANT:** This chatbot requires your own Anthropic API key to function. You can get one at [https://console.anthropic.com/](https://console.anthropic.com/).

## Features

- 🤖 Claude AI Integration: Powered by Anthropic's state-of-the-art language model
- 🧠 Context Memory: Maintains conversation history for coherent dialogue
- 💬 Natural Conversations: Human-like responses and understanding
- 🎨 Modern UI: Clean, responsive interface with typing indicators
- 🔄 Real-time Updates: Instant message delivery and responses

## Tech Stack

- Backend: Python Flask
- AI: Anthropic's Claude API
- Frontend: HTML, CSS, JavaScript
- API: RESTful endpoints

## Prerequisites

- Python 3.8 or higher
- Anthropic API key ([Get one here](https://console.anthropic.com/))

## Installation

1. Clone the repository:
```bash
git clone https://github.com/tradervijeth/chatbot-project.git
cd chatbot-project
```

2. Create virtual environment:
```bash
python -m venv venv
```

3. Activate virtual environment:
```bash
# Windows
.\venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install flask flask-cors anthropic python-dotenv
```

5. Create a `.env` file in the project root:
```
ANTHROPIC_API_KEY=your_api_key_here
```

**⚠️ NOTE:** Replace `your_api_key_here` with your actual Anthropic API key. The chatbot will not function without a valid API key.

## Usage

1. Make sure your API key is set in `.env`

2. Start the server:
```bash
python app.py
```

3. Open your browser and navigate to:
```
http://localhost:5000
```

4. Start chatting with Claude!

## Project Structure

```
chatbot-project/
├── static/
│   └── css/
│       └── style.css
├── templates/
│   └── index.html
├── chatbot.py      # Claude AI integration
├── app.py          # Flask server
├── .env            # API key configuration
└── requirements.txt
```

## API Usage Notes

- The chatbot uses the Claude-3 Opus model
- Responses are capped at 1024 tokens
- Temperature is set to 0.7 for balanced creativity/consistency
- API calls are rate-limited based on your Anthropic account tier
- Costs are incurred per API call according to Anthropic's pricing

## Troubleshooting

Common issues:
- "No module named 'anthropic'" → Run `pip install anthropic`
- "Invalid API key" → Check your `.env` file has the correct key
- "Rate limit exceeded" → Your API usage has hit the limit
- Script activation issues → Run PowerShell as Administrator and execute:
  ```powershell
  Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

tradervijeth - [GitHub](https://github.com/tradervijeth)

Project Link: https://github.com/tradervijeth/chatbot-project

## Acknowledgments

- Powered by [Anthropic's Claude](https://www.anthropic.com/claude)
- Built with [Flask](https://flask.palletsprojects.com/)