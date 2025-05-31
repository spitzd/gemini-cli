# Gemini CLI

A simple command-line interface for interacting with Google's Gemini AI model.

## Overview

This Python script provides a straightforward way to interact with Google's Gemini AI model directly from your terminal. It allows you to ask questions or provide prompts and receive AI-generated responses.

## Features

- Simple command-line interface
- Uses the Gemini 2.5 Pro Preview model
- Minimal setup required
- Error handling for common issues

## Requirements

- Python 3.6 or higher
- `google-generativeai` Python package
- A Google AI Studio API key

## Installation

1. Clone this repository or download the `gemini.py` file.

2. Install the required Python package:
   ```bash
   pip install google-generativeai
   ```

3. Get a Gemini API key:
   - Visit [Google AI Studio](https://ai.google.dev/)
   - Create an account or sign in
   - Navigate to the API keys section
   - Create a new API key

4. Set your API key as an environment variable:
   ```bash
   # On Linux/macOS
   export GEMINI_API_KEY='your_api_key_here'
   
   # On Windows (Command Prompt)
   set GEMINI_API_KEY=your_api_key_here
   
   # On Windows (PowerShell)
   $env:GEMINI_API_KEY='your_api_key_here'
   ```

## Usage

Run the script from your terminal:

```bash
python gemini.py
```

When prompted, enter your question or prompt. The script will send your input to the Gemini AI model and display the response.

Example:
```
Enter your question for Gemini: What are the main differences between Python and JavaScript?

Generating response...

[Gemini's response will appear here]
```

## Error Handling

The script includes error handling for:
- Missing API key environment variable
- API request failures

If you encounter an error, the script will display a helpful message explaining the issue.

## Customization

To use a different Gemini model, modify the following line in the script:

```python
model = genai.GenerativeModel('gemini-2.5-pro-preview-05-06')
```

Replace `'gemini-2.5-pro-preview-05-06'` with the desired model name.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgements

This tool uses Google's Generative AI API. For more information, visit [Google AI Studio](https://ai.google.dev/).
