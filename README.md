# AI Policy Assistant

A modern, multilingual AI-powered chatbot for company policy assistance, built with Flask and integrated with a RAG (Retrieval Augmented Generation) system via n8n workflow automation.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![AI](https://img.shields.io/badge/AI-RAG-orange.svg)
![Languages](https://img.shields.io/badge/Languages-Arabic%20%7C%20English-red.svg)

## 🌟 Features

### 🤖 AI-Powered Chat
- **RAG Integration**: Connected to n8n workflow with Qdrant vector store and Ollama embeddings
- **Smart Responses**: Context-aware answers based on company policies and procedures
- **Session Management**: Persistent chat sessions with unique session IDs
- **Error Handling**: Robust error handling with user-friendly messages

### 🎨 Modern UI/UX
- **Professional Design**: Clean, modern interface with gradient backgrounds
- **Responsive Layout**: Works perfectly on desktop, tablet, and mobile devices
- **Dark/Light Mode**: Seamless theme switching with persistent preferences
- **Animated Interactions**: Smooth transitions and hover effects
- **Typing Indicators**: Real-time typing animations for better UX

### 🌍 Multilingual Support
- **Arabic & English**: Full support for both languages with RTL/LTR layouts
- **Dynamic Switching**: Instant language switching without page reload
- **Localized Content**: All UI elements and messages in both languages
- **Cultural Adaptation**: Proper text direction and formatting

### 💡 Smart Suggestions
- **Pre-defined Questions**: Common policy questions for quick access
- **Interactive Cards**: Click-to-send suggestion questions
- **Context-Aware**: Suggestions hide after chat starts for cleaner interface

### 🔧 Advanced Features
- **Reset Chat**: One-click chat reset with confirmation dialog
- **Formatted Output**: Rich text rendering with markdown-like formatting
- **Message Timestamps**: Time tracking for all messages
- **Auto-resize Input**: Dynamic textarea resizing
- **Keyboard Shortcuts**: Enter to send, Shift+Enter for new lines

## 🏗️ Architecture

### System Overview
The application follows a modern web architecture with clear separation of concerns:

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Web Frontend  │────│   Flask Backend  │────│   n8n RAG API   │
│   (HTML/CSS/JS) │    │     (Python)     │    │   (Automation)  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

### RAG System Integration
Based on the n8n workflow diagram, the system integrates with:

#### Data Ingestion Pipeline:
1. **Document Processing**: Raw documents are processed and chunked
2. **Embedding Generation**: Ollama creates vector embeddings
3. **Vector Storage**: Qdrant stores embeddings for fast retrieval
4. **Indexing**: Documents are indexed for semantic search

#### Chat Inference Pipeline:
1. **User Input**: Chat messages are processed by the Flask backend
2. **Query Embedding**: User queries are embedded using Ollama
3. **Vector Search**: Qdrant performs similarity search
4. **Context Retrieval**: Relevant documents are retrieved
5. **Response Generation**: Groq LLM generates contextual responses
6. **Memory Management**: Conversation history is maintained

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)
- Internet connection (for RAG API integration)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd HR-Assistant-Agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the RAG API endpoint**
   ```python
   # In app.py, update the RAG_API_URL
   RAG_API_URL = "your-n8n-webhook-url"
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

## 📁 Project Structure

```
HR-Assistant-Agent/
├── app.py                 # Flask application and API endpoints
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── static/
│   └── style.css         # Global styles and utilities
└── templates/
    ├── base.html         # Base template with sidebar and navigation
    ├── home.html         # Landing page with features and welcome
    ├── chat.html         # Chat interface with AI integration
    └── settings.html     # User preferences and app settings
```

## 🔧 Configuration

### Environment Variables
```bash
# Optional: Configure Flask settings
export FLASK_ENV=development
export FLASK_DEBUG=True
export FLASK_HOST=0.0.0.0
export FLASK_PORT=5000
```

### RAG API Configuration
Update the `RAG_API_URL` in `app.py` to point to your n8n webhook endpoint:

```python
RAG_API_URL = "https://your-domain.com/webhook/your-webhook-id/chat"
```

## 🎯 Usage

### Starting a Chat
1. Navigate to the chat page
2. Review the suggested questions or type your own
3. Click on suggestion cards or type in the input field
4. Press Enter or click the send button

### Managing Sessions
- **New Session**: Each browser session gets a unique session ID
- **Reset Chat**: Use the reset button in the chat header
- **Session Persistence**: Chat history is maintained during the session

### Language Switching
- Use the settings page to switch between Arabic and English
- Language preference is saved in browser localStorage
- All UI elements update instantly

### Theme Customization
- Toggle between light and dark modes in settings
- Theme preference is automatically saved
- Consistent styling across all pages

## 🛠️ API Endpoints

### Flask Backend Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page |
| `/chat` | GET | Chat interface |
| `/settings` | GET | Settings page |
| `/generate_session` | POST | Generate new session ID |
| `/send_message` | POST | Send message to RAG system |

### Request/Response Format

#### Send Message Request:
```json
{
  "message": "What is the vacation policy?",
  "sessionId": "abc123def456"
}
```

#### Send Message Response:
```json
{
  "reply": "Here is the vacation policy information...",
  "error": false,
  "timestamp": 1234567890
}
```

## 🎨 UI Components

### Chat Interface
- **Header**: Title, reset button, and controls
- **Suggestion Cards**: Interactive question suggestions
- **Message Bubbles**: Styled chat messages with timestamps
- **Input Area**: Auto-resizing textarea with send button
- **Typing Indicator**: Animated dots during AI processing

### Navigation
- **Sidebar**: Fixed navigation with icons and labels
- **Mobile Menu**: Collapsible sidebar for mobile devices
- **Active States**: Visual indicators for current page

### Styling Features
- **Gradient Backgrounds**: Modern gradient designs
- **Box Shadows**: Depth and elevation effects
- **Smooth Animations**: CSS transitions and transforms
- **Responsive Grid**: Flexible layouts for all screen sizes

## 🔒 Security Features

- **Input Validation**: All user inputs are validated and sanitized
- **Error Handling**: Comprehensive error handling with user-friendly messages
- **Session Management**: Secure session ID generation and validation
- **XSS Protection**: HTML escaping for user-generated content
- **Timeout Handling**: Request timeout management for API calls

## 🌐 Browser Support

- **Chrome**: 70+
- **Firefox**: 65+
- **Safari**: 12+
- **Edge**: 79+
- **Mobile Browsers**: iOS Safari, Chrome Mobile

## 📱 Mobile Responsiveness

The application is fully responsive with:
- **Mobile-First Design**: Optimized for mobile devices
- **Touch-Friendly**: Large tap targets and smooth scrolling
- **Collapsible Sidebar**: Space-efficient navigation on mobile
- **Responsive Typography**: Scalable text and spacing

## 🚀 Deployment

### Production Deployment

1. **Configure Production Settings**
   ```python
   # In app.py
   app.run(host="0.0.0.0", port=5000, debug=False)
   ```

2. **Use a WSGI Server**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

3. **Set up Reverse Proxy** (Nginx example)
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;
       
       location / {
           proxy_pass http://127.0.0.1:5000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

### Docker Deployment

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY ../src/requirements.txt .
RUN pip install -r requirements.txt
COPY ../src .
EXPOSE 5000
CMD ["python", "app.py"]
```

## 🔧 Troubleshooting

### Common Issues

1. **Connection Errors**
   - Check RAG_API_URL configuration
   - Verify network connectivity
   - Check n8n webhook status

2. **Session Issues**
   - Clear browser localStorage
   - Refresh the page
   - Check session ID format

3. **Styling Issues**
   - Clear browser cache
   - Check CSS file loading
   - Verify template inheritance

### Debug Mode
Enable debug mode for development:
```python
app.run(debug=True)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Check the troubleshooting section

## 🔮 Future Enhancements

- [ ] User authentication and profiles
- [ ] Chat history persistence
- [ ] File upload for document analysis
- [ ] Voice input/output capabilities
- [ ] Advanced analytics and insights
- [ ] Multi-tenant support
- [ ] API rate limiting
- [ ] Advanced caching strategies

---

**Built with ❤️ for modern AI-powered communication**
