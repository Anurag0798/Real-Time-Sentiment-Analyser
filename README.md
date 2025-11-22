# Real-Time Sentiment Analyser

A Streamlit-based web app for real-time sentiment analysis, powered by the EURI/GPT-4.1-nano API. Paste any sentence or social media post and instantly receive a sentiment categorization: Positive, Negative, Neutral, Political, or Racist.

## Features

- **Real-Time Sentiment Analysis:**
  Instantly analyze text and classify it into one of five categories.
- **Modern UI with Streamlit:**
  Clean, interactive interface for quick feedback and easy use.
- **API-Based Intelligence:**
  Leverages EURI’s GPT-4.1-nano model for robust natural language understanding.
- **Simple Deployment:**
  Run locally or deploy on Streamlit Cloud with minimal setup.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Anurag0798/Real-Time-Sentiment-Analyser.git

cd Real-Time-Sentiment-Analyser
```

### 2. Create and activate a virtual environment (optional/recommended)

```bash
python -m venv .venv

# On Linux/Mac
source .venv/bin/activate

# On Windows
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your EURI API key

- Obtain your EURI API key from https://euron.one/
- Open `app.py` and paste your key in place of `"Put_your_euri_API_key_here"`:
  ```python
  EURI_API_KEY = "YOUR_API_KEY"
  ```
- **Never commit your API key to a public repository.**

### 5. Run the app

```bash
streamlit run app.py
```
- The app will launch in your browser at `http://localhost:8501` (default).

## Usage

- Enter any sentence, tweet, or post into the text box.
- Click "Analyze Sentiment".
- The model will return one of:
  - **Positive**
  - **Negative**
  - **Neutral**
  - **Political**
  - **Racist**

---

## Project Structure

```
.
├── app.py            # Main Streamlit application
├── requirements.txt  # Dependencies
└── README.md         # Project documentation
```

## Requirements

- Python 3.7+
- streamlit
- requests

Install all requirements with:
```bash
pip install -r requirements.txt
```

## Customization

- **Add More Sentiment Classes:**  
  Modify the prompt in `get_sentiment_from_euri()` function inside `app.py` to extend or refine classes.
- **Change Model:**  
  Change the `"model"` parameter in the payload to use another available model (see EURI API documentation).
- **Integrate with Frontends:**  
  Use the `/predict` handler as a backend for web or mobile apps.

## License

This project is licensed under the MIT License.

## Contributing

Contributions and suggestions are welcome!  
1. Fork the repo  
2. Create a feature branch  
3. Submit a pull request  
4. Open issues for feature requests or bug reports

If you use or enjoy this project, please ⭐ star the repository!