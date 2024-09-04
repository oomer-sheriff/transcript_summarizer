import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

openai.api_key = 'your_openai_api_key_here'

# In-memory storage for transcripts and summaries
transcripts = {}
summaries = {}
chat_histories = {}

@app.route('/upload_transcript', methods=['POST'])
def upload_transcript():
    transcript_id = str(len(transcripts) + 1)
    transcript = request.json['transcript']
    transcripts[transcript_id] = transcript
    return jsonify({"transcript_id": transcript_id})

@app.route('/summarize_opening_remarks', methods=['POST'])
def summarize_opening_remarks():
    transcript_id = request.json['transcript_id']
    transcript = transcripts.get(transcript_id)
    
    if not transcript:
        return jsonify({"error": "Transcript not found"}), 404

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Summarize the opening remarks of the following transcript:\n\n{transcript}",
        max_tokens=150
    )
    summary = response.choices[0].text.strip()
    summaries[transcript_id] = {"opening_remarks": summary}

    return jsonify({"summary": summary, "tokens": response.usage.total_tokens})

@app.route('/summarize_qa', methods=['POST'])
def summarize_qa():
    transcript_id = request.json['transcript_id']
    transcript = transcripts.get(transcript_id)
    
    if not transcript:
        return jsonify({"error": "Transcript not found"}), 404

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Summarize the questions and answers in the following transcript, including the persons involved:\n\n{transcript}",
        max_tokens=300
    )
    summary = response.choices[0].text.strip()
    if transcript_id in summaries:
        summaries[transcript_id]["qa"] = summary
    else:
        summaries[transcript_id] = {"qa": summary}

    return jsonify({"summary": summary, "tokens": response.usage.total_tokens})

@app.route('/chat', methods=['POST'])
def chat():
    transcript_id = request.json['transcript_id']
    question = request.json['question']
    
    transcript = transcripts.get(transcript_id)
    if not transcript:
        return jsonify({"error": "Transcript not found"}), 404

    chat_history = chat_histories.get(transcript_id, [])
    chat_history.append(f"Human: {question}")

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Based on the following transcript and chat history, answer this question: {question}\n\nTranscript: {transcript}\n\nChat History: {' '.join(chat_history)}",
        max_tokens=150
    )
    answer = response.choices[0].text.strip()
    chat_history.append(f"AI: {answer}")
    chat_histories[transcript_id] = chat_history

    return jsonify({"answer": answer, "tokens": response.usage.total_tokens})

if __name__ == '__main__':
    app.run(debug=True)