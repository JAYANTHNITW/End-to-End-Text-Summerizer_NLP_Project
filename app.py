import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from transformers import AutoTokenizer, pipeline
from src.EndtoEndTextSummerizer.config.configuration import ConfigurationManager

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()

    def predict(self, text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 128}

        pipe = pipeline("summarization", model=self.config.model_path, tokenizer=tokenizer)

        print("Dialogue:")
        print(text)

        output = pipe(text, **gen_kwargs)[0]["summary_text"]
        print("\nModel Summary:")
        print(output)

        return output

clApp = PredictionPipeline()

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/summarize", methods=['POST'])
@cross_origin()
def summarize_route():
    try:
        data = request.get_json()
        text_to_summarize = data.get('text', '')

        if not text_to_summarize:
            return jsonify({"error": "Missing 'text' parameter"}), 400

        print(f"Received text to summarize: {text_to_summarize}")

        summary = clApp.predict(text_to_summarize)
        return jsonify({"summary": summary})

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


