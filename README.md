# Book Translator - ترجمه‌کننده کتاب

An automated book translation program that uses artificial intelligence to translate PDF books and save the results to Word documents.

## 🌟 Features

- 📖 Read PDF files
- 🤖 Translation using OpenAI-Compatible Service (GPT-4o)
- 📝 Save results to Word documents
- 🔄 Split text into smaller sections for better translation
- 📊 Display translation progress
- 🎯 Preserve original text structure and formatting
- ⚡ Support for async/await for better performance
- 🔗 **Page Overlap** - Maintain text continuity between pages
- 💻 **Technical Term Preservation** - Keep software terms in English

## 🚀 Quick Start

### 1. Prerequisites

- Python 3.10 or newer
- An OpenAI-compatible API key (Avalai, OpenAI, Azure OpenAI, or a local service)
- Poppler or another PDF reader is **not** required—`PyPDF2` handles parsing internally

### 2. Installation

```bash
# Create and activate a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### 3. Configuration

```bash
# Copy environment template
cp .env.example .env            # macOS/Linux
copy .env.example .env          # Windows PowerShell

# Edit the new .env file with your API key and optional overrides
OPENAI_API_KEY=your-api-key-here
OPENAI_MODEL=gpt-4o
OPENAI_BASE_URL=https://api.avalai.ir/v1
```

### 4. Test Connection

```bash
# Test OpenAI-compatible service connection
python test_openai.py
```

### 5. Run Translator

```bash
# Translate your PDF book
python openai_translator.py
```

## 💻 Technical Term Preservation

The translator is specifically designed for software and technical documentation. It preserves technical terms in English while translating the surrounding text to Persian.

### Preserved Terms Include:

#### Programming Concepts
- Run, Build, Deploy, Debug, Compile, Execute, Test, Refactor, Optimize

#### Software Patterns
- Domain Driven Design, MVC, MVP, MVVM, Repository Pattern, Factory Pattern

#### Development Terms
- Sprint, Backlog, User Story, Epic, Bug, Feature, Hotfix, Release

#### Technical Terms
- API, SDK, Framework, Library, Module, Package, Dependency, Version

#### Code-related Terms
- Function, Method, Class, Object, Variable, Parameter, Return, Import, Export

#### Tools & Platforms
- Git, Docker, Kubernetes, Jenkins, Jira, VS Code, IntelliJ
- AWS, Azure, Google Cloud, Heroku, DigitalOcean, GitHub, GitLab, Bitbucket

#### Programming Languages
- Python, JavaScript, Java, C#, TypeScript, React, Angular, Vue, Node.js

#### Databases
- MySQL, PostgreSQL, MongoDB, Redis, SQLite, Oracle, SQL Server

#### Protocols & Formats
- HTTP, HTTPS, REST, GraphQL, WebSocket, TCP, UDP, SSH, FTP
- JSON, XML, CSV, YAML, Markdown, HTML, CSS, SVG, PNG, JPG

### Translation Examples:

| English | Persian Translation |
|---------|-------------------|
| "Run the application" | "اپلیکیشن را Run کنید" |
| "Build the project" | "پروژه را Build کنید" |
| "Domain Driven Design principles" | "اصول Domain Driven Design" |
| "Deploy to production" | "Deploy کردن به production" |
| "Create a new branch" | "ایجاد یک branch جدید" |
| "Merge the changes" | "Merge کردن تغییرات" |
| "Debug the issue" | "Debug کردن مشکل" |
| "API endpoint" | "API endpoint" |
| "Database connection" | "اتصال Database" |
| "Git repository" | "Git repository" |
| "REST API" | "REST API" |
| "JSON response" | "پاسخ JSON" |
| "Unit test" | "Unit test" |
| "Pull request" | "Pull request" |

## 📋 Configuration

### Environment Variables

```bash
# Required
OPENAI_API_KEY=your-api-key-here

# Optional (defaults shown)
OPENAI_MODEL=gpt-4o
OPENAI_BASE_URL=https://api.avalai.ir/v1
```

### Customization

You can modify the translator behavior by editing `openai_translator.py`:

```python
# Change default model
translator = OpenAIBookTranslator(model="gpt-3.5-turbo")

# Change service endpoint
translator = OpenAIBookTranslator(
    api_key="your-key",
    model="gpt-4o",
    base_url="https://api.openai.com/v1"  # Standard OpenAI
)

# Change page overlap
success = translator.translate_book(
    pdf_path="book.pdf",
    output_path="translated_book.docx",
    overlap_paragraphs=2  # More overlap for better context
)
```

## 📊 Output Format

The translator creates a Word document with:

- **Title**: Book Translation
- **Metadata**: 
  - Original Language: English
  - Target Language: Persian
  - Translation Engine: OpenAI-Compatible Service
  - Model: gpt-4o
  - Endpoint: https://api.avalai.ir/v1
  - Page Overlap: Enabled
  - Generation timestamp
- **Content**: 
  - Section headers
  - Original text
  - Translated text
  - Separators between sections

## 🔧 Advanced Settings

### Page Overlap Configuration

```python
# More overlap for better context (default: 1)
overlap_paragraphs = 2

# Less overlap for faster processing
overlap_paragraphs = 0
```

### Chunk Size Configuration

```python
# Modify in split_text_into_chunks method
chunk_size = 3000  # Larger chunks (default: 2000)
chunk_overlap = 300  # More overlap between chunks (default: 200)
```

### Translation Parameters

```python
# Modify in translate_chunk method
temperature = 0.1  # More deterministic (default: 0.3)
max_tokens = 6000  # Longer responses (default: 4000)
```

## 🛠️ Troubleshooting

### Common Issues

1. **API Key Error**
   ```
   ❌ Error: API key is required
   ```
   **Solution**: Set your API key in `.env` file

2. **Connection Error**
   ```
   ❌ Error: Network connection problem
   ```
   **Solution**: Check your internet connection and service status

3. **Rate Limiting**
   ```
   ❌ Error: Rate limit exceeded
   ```
   **Solution**: Wait a few minutes or reduce request frequency

4. **PDF Reading Error**
   ```
   ❌ Error: Error reading PDF
   ```
   **Solution**: Ensure PDF file exists and is not corrupted

### Testing

Run the test script to verify everything is working:

```bash
python test_openai.py
```

Expected output:
```
🔧 Testing OpenAI-Compatible Service Connection
==================================================
API Key: ✅ Set
Model: gpt-4o
Endpoint: https://api.avalai.ir/v1

✅ OpenAI client initialized successfully
🔄 Testing simple request...
✅ Response received: سلام از OpenAI-compatible service!
🔄 Testing translation...
✅ Translation test: اپلیکیشن را Run کنید و پروژه را Build کنید. API endpoint را بررسی کنید و مشکلات را Debug کنید.
🎉 All tests passed! OpenAI-compatible service is working correctly.
```

## 📈 Performance Tips

1. **Use appropriate chunk size**: Larger chunks for better context, smaller for faster processing
2. **Adjust page overlap**: More overlap for better continuity, less for speed
3. **Monitor rate limits**: Add delays between requests if needed
4. **Use SSD storage**: Faster PDF reading and Word document creation

## 🔒 Security Notes

- Never commit your `.env` file to version control
- Keep your API key secure and don't share it
- Use environment variables for sensitive data
- Regularly rotate your API keys

## 🧭 Project Structure

```
.
├── .env.example               # Template for environment variables
├── LICENSE                    # MIT License
├── README.md
├── openai_translator.py       # Main translation script
├── requirements.txt           # Python dependencies
├── test_openai.py             # Connection and translation smoke test
└── translated_book_avalai.docx# Sample output document
```

## 🧪 Testing

The repository doesn't depend on a test framework, but the bundled smoke test helps confirm your credentials and service availability:

```bash
python test_openai.py
```

If you add features, consider contributing automated tests to keep coverage improving.

## 📝 License

This project is open source and available under the [MIT License](./LICENSE).

## 🤝 Contributing

Contributions are welcome! Please review [`CONTRIBUTING.md`](./CONTRIBUTING.md) for guidelines on proposing changes, running checks, and submitting pull requests. By participating, you agree to uphold the expectations outlined in our [`Code of Conduct`](./CODE_OF_CONDUCT.md).

## 📞 Support

If you encounter any issues:

1. Check the troubleshooting section
2. Run the test script to verify connection
3. Check service status
4. Review the error messages for specific guidance

---

**Happy Translating! 🎉**
