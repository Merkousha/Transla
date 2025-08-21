#!/usr/bin/env python3
"""
Test script for OpenAI-compatible service connection
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

def test_openai_connection():
    """
    Test the connection to OpenAI-compatible service
    """
    print("🔧 Testing OpenAI-Compatible Service Connection")
    print("=" * 50)
    
    # Load environment variables
    load_dotenv()
    
    # Get API key
    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL", "gpt-4o")
    base_url = os.getenv("OPENAI_BASE_URL", "https://api.avalai.ir/v1")
    
    print(f"API Key: {'✅ Set' if api_key else '❌ Not set'}")
    print(f"Model: {model}")
    print(f"Endpoint: {base_url}")
    
    if not api_key:
        print("\n❌ Error: OPENAI_API_KEY is not set!")
        print("Please set your API key in the .env file:")
        print("OPENAI_API_KEY=your-api-key-here")
        return False
    
    try:
        # Initialize OpenAI client
        client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )
        
        print("\n✅ OpenAI client initialized successfully")
        
        # Test simple request
        print("🔄 Testing simple request...")
        
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Say 'Hello from OpenAI-compatible service!' in Persian"}
            ],
            max_tokens=50
        )
        
        result = response.choices[0].message.content
        print(f"✅ Response received: {result}")
        
        # Test translation
        print("\n🔄 Testing translation...")
        
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": """You are a professional translator specializing in software and technical documentation. Translate from English to Persian.

IMPORTANT: DO NOT translate technical software terms - keep them in English:
- Programming concepts: Run, Build, Deploy, Debug, Compile, Execute, Test
- Software patterns: Domain Driven Design, MVC, MVP, MVVM
- Development terms: Sprint, Backlog, User Story, Bug, Feature, Release
- Technical terms: API, SDK, Framework, Library, Module, Package
- Code-related: Function, Method, Class, Object, Variable, Parameter
- Tools: Git, Docker, Kubernetes, Jenkins, Jira, VS Code
- Platforms: AWS, Azure, Google Cloud, GitHub, GitLab
- Languages: Python, JavaScript, Java, C#, TypeScript, React
- Databases: MySQL, PostgreSQL, MongoDB, Redis, SQLite
- Protocols: HTTP, HTTPS, REST, GraphQL, WebSocket, SSH
- File formats: JSON, XML, CSV, YAML, Markdown, HTML, CSS

Examples: "Run the application" → "اپلیکیشن را Run کنید", "Build the project" → "پروژه را Build کنید", "API endpoint" → "API endpoint"

Only provide the translation, no explanations."""},
                {"role": "user", "content": "Translate: 'Run the application and build the project. Check the API endpoint and debug any issues.'"}
            ],
            max_tokens=150
        )
        
        result = response.choices[0].message.content
        print(f"✅ Translation test: {result}")
        
        print("\n🎉 All tests passed! OpenAI-compatible service is working correctly.")
        return True
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nPossible issues:")
        print("1. Invalid API key")
        print("2. Network connection problem")
        print("3. Service temporarily unavailable")
        print("4. Rate limiting")
        return False

def main():
    """
    Main function
    """
    success = test_openai_connection()
    
    if success:
        print("\n🚀 You can now run the translator:")
        print("python openai_translator.py")
    else:
        print("\n❌ Please fix the issues before running the translator.")

if __name__ == "__main__":
    main()
