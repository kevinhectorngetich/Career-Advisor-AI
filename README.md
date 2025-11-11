# 🤖 AI Career Software Advisor

Your intelligent AI Career Software Advisor powered by GPT-5 and RAG (Retrieval-Augmented Generation) technology. Get personalized guidance for your software development career path, technical skills, and industry insights.

![AI Career Advisor](path/to/your/screenshot.png)

## ✨ Features

- **💬 Multi-turn Conversations**: Maintains context across multiple exchanges for natural dialogue
- **🖼️ Image Input Support**: Upload and analyze images (resumes, diagrams, code screenshots) alongside text
- **🧠 Intelligent Document Retrieval**: RAG-powered knowledge base access for accurate, context-aware responses
- **📚 Comprehensive Career Guidance**:
  - Personalized career guidance for software developers
  - Technical skill recommendations and learning paths
  - Industry insights and market trends
  - Code review and best practices advice
  - Interview preparation and tips
  - Resume and portfolio optimization
  - Salary negotiation strategies
  - Technology stack recommendations
- **🗑️ Clear Conversation History**: Reset chat anytime for a fresh start
- **⚡ Real-time Responses**: Fast, streaming responses powered by GPT-5

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- OpenAI API account with API key
- Vector Store ID (created from your uploaded documents)

### Installation

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd "AI Assistant"
   ```

2. **Create a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Copy the `.env.example` file to `.env`:

   ```bash
   cp .env.example .env
   ```

   Then edit `.env` and add your credentials:

   ```
   OPENAI_API_KEY=your_actual_api_key_here
   VECTOR_STORE_ID=your_actual_vector_store_id_here
   ```

### Setting Up Your Vector Store

1. **Prepare your documents**

   - Place your career guidance documents, resume templates, interview guides, etc. in the `data/` folder
   - Supported formats: PDF, TXT, DOCX, MD

2. **Create a Vector Store in OpenAI**

   - Go to [OpenAI Platform](https://platform.openai.com/)
   - Navigate to the Storage section
   - Create a new Vector Store
   - Upload your documents from the `data/` folder
   - Copy the Vector Store ID (format: `vs_xxxxxxxxxxxxx`)
   - Add it to your `.env` file

3. **Get your OpenAI API Key**
   - Go to [OpenAI API Keys](https://platform.openai.com/api-keys)
   - Create a new API key
   - Copy it and add to your `.env` file

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

## 📁 Project Structure

```
AI Assistant/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not tracked in git)
├── .env.example          # Example environment variables template
├── .gitignore            # Git ignore file
├── README.md             # This file
├── data/                 # Your documents for the vector store
│   ├── resume_guide.pdf
│   ├── interview_tips.md
│   └── ... (your career guidance documents)
└── venv/                 # Virtual environment (not tracked in git)
```

## 🛠️ Technologies Used

- **[Streamlit](https://streamlit.io/)** - Web application framework
- **[OpenAI GPT-5](https://openai.com/)** - Advanced language model for intelligent responses
- **[OpenAI Responses API](https://platform.openai.com/docs/)** - Real-time API with RAG support
- **[Python-dotenv](https://github.com/theskumar/python-dotenv)** - Environment variable management
- **[Pillow](https://python-pillow.org/)** - Image processing library

## 💡 How It Works

1. **Input Processing**: Your queries (text and images) are processed and formatted for GPT-5
2. **RAG Enhancement**: Relevant documents are retrieved from your vector store based on the query
3. **Context Integration**: Retrieved information is combined with your question for better context
4. **Smart Response**: GPT-5 generates contextually aware, expert-level career advice
5. **Conversation Memory**: Chat history is maintained throughout your session for coherent multi-turn conversations

## 🎯 Use Cases

- **Job Seekers**: Get help with resume optimization, interview prep, and job search strategies
- **Career Switchers**: Receive guidance on transitioning between tech roles or specializations
- **Students**: Learn about software engineering career paths and skill development
- **Professionals**: Get advice on advancing to senior roles, salary negotiation, and skill gaps
- **Entrepreneurs**: Understand tech stack choices and hiring strategies

## 🔒 Security Notes

- Never commit your `.env` file to version control
- Keep your OpenAI API key secure and don't share it
- The `.gitignore` file is configured to exclude sensitive files
- Consider using Streamlit secrets for production deployment

## 📝 Configuration

### Streamlit Configuration

You can customize the app's appearance by creating a `.streamlit/config.toml` file:

```toml
[theme]
primaryColor = "#FF4B4B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"

[server]
maxUploadSize = 200
```

## 🚢 Deployment

### Deploy to Streamlit Cloud

1. Push your code to GitHub (make sure `.env` is in `.gitignore`)
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your GitHub repository
4. Add your secrets in the Streamlit Cloud dashboard:
   - `OPENAI_API_KEY`
   - `VECTOR_STORE_ID`
5. Deploy!

### Deploy to Other Platforms

The app can also be deployed to:

- Heroku
- AWS (EC2, ECS, Lambda)
- Google Cloud Platform
- Azure

Make sure to set environment variables in your deployment platform's configuration.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Troubleshooting

### Common Issues

**Error: "OpenAI API Key is not set"**

- Make sure your `.env` file exists and contains `OPENAI_API_KEY=your_key`
- Verify the `.env` file is in the same directory as `app.py`

**Error: "Vector Store ID is not set"**

- Ensure you've created a vector store in OpenAI platform
- Add the vector store ID to your `.env` file

**Images not uploading**

- Check file size (max 200MB per file)
- Supported formats: JPG, JPEG, PNG, WEBP

**Slow responses**

- Large documents in vector store may slow retrieval
- Consider optimizing your document set

## 📧 Support

For issues, questions, or suggestions, please open an issue on GitHub or contact [your-email@example.com]

## 🙏 Acknowledgments

- OpenAI for the GPT-5 API and Vector Store capabilities
- Streamlit for the amazing web framework
- The open-source community for the excellent Python libraries

---

**Built with ❤️ by [Your Name]**
