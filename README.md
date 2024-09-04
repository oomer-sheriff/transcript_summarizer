# Transcript Summarizer Project

This project consists of a web application that allows users to upload transcripts, summarize opening remarks and Q&A sessions, and interact with a chatbot based on the transcript content. The project uses a Flask backend with OpenAI's GPT model for text processing and a simple HTML/JavaScript frontend.

## Prerequisites

- Python 3.7+
- Flask
- Flask-CORS
- OpenAI Python library
- A valid OpenAI API key

## Setup

1. Clone the repository or download the project files.

2. Install the required Python packages:
   ```
   pip install flask flask-cors openai
   ```

3. Open the `app.py` file and replace `'your_openai_api_key_here'` with your actual OpenAI API key:
   ```python
   openai.api_key = 'your_actual_api_key'
   ```

4. Ensure that the `index.html` file is in the same directory as `app.py`.

## Running the Application

1. Open a terminal and navigate to the project directory.

2. Start the Flask server by running:
   ```
   python app.py
   ```

3. The server should start running on `http://localhost:5000`.

4. Open a web browser and navigate to `http://localhost:5000` to access the web interface.

## Using the Application

1. **Upload Transcript**: Paste your transcript text into the provided textarea and click "Upload Transcript".

2. **Summarize Opening Remarks**: Navigate to the "Opening remarks summary" section and click "Get topics" to generate a summary.

3. **Summarize Q&A**: Go to the "Question answer summary" section and click "Get topics" to summarize the Q&A portion of the transcript.

4. **Chat with the Transcript**: Use the "Chatbot on transcript content" section to ask questions about the transcript. Type your question and press Enter to get a response.

## Notes

- The application uses in-memory storage for transcripts and summaries. Data will be lost when the server is restarted.
- Be mindful of your OpenAI API usage, as each request consumes tokens which may incur costs.
- This is a basic implementation and may need additional error handling and security measures for production use.

## Troubleshooting

- If you encounter CORS issues, ensure that the Flask-CORS extension is properly installed and configured.
- If the OpenAI API calls fail, double-check that your API key is correct and that you have sufficient credits in your OpenAI account.

(note : Index2.html has better ui, please try both)
