# Flask Medical Information Extractor and Summarizer

This repository provides a Flask-based API to extract detailed medical information and generate summaries from input text using OpenAI's GPT-3.5-Turbo model. The API processes medical text to identify critical details such as patient information, diagnosis, symptoms, medications, and more. It integrates OpenAI's function-calling capabilities for structured data extraction.

---

## **Features**

1. **Medical Information Extraction:**
   - Extracts structured information like patient ID, diagnosis, symptoms, medications, and recommendations from medical text.

2. **Summarization:**
   - Combines extracted information into a comprehensive summary of the input text.

3. **Flask REST API:**
   - Exposes an endpoint for sending medical text and receiving structured data and summaries.

4. **OpenAI Integration:**
   - Leverages OpenAI GPT-3.5-Turbo model for language understanding and function-based structured data extraction.

---

## **Endpoints**

### 1. `/summarize` (GET or POST)
- **Description:** Extracts detailed medical information and generates a summary from input text.
- **Request:**
  - `GET`: Pass text as a query parameter.
  - `POST`: Send a JSON payload with the `text` field.
- **Response:** JSON object with extracted medical information and summary.

---

## **Repository Structure**

- **`app.py`:** Main Flask application containing the API logic, OpenAI integration, and data extraction functions.
- **`requirements.txt`:** List of dependencies to set up the environment.

---

## **Setup Instructions**

### 1. **Clone the Repository**
```bash
git clone <repository_url>
cd <repository_folder>
```

### 2. **Install Dependencies**
Ensure you have Python installed, then install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3. **Set OpenAI API Key**
- Update the `OPENAI_KEY` variable in `app.py` with your OpenAI API key:
  ```python
  OPENAI_KEY = "your_openai_api_key_here"
  ```

### 4. **Run the Application**
Start the Flask application:
```bash
python app.py
```
The application will run on `http://127.0.0.1:5000` by default.

---

## **Usage Examples**

### **1. POST Request**
**Request:**
```bash
curl -X POST http://127.0.0.1:5000/summarize \
-H "Content-Type: application/json" \
-d '{"text": "Patient John Doe, ID 12345, was diagnosed with Type 2 Diabetes. Symptoms include frequent urination, excessive thirst, and fatigue. Recommended medications: Metformin, 500mg daily."}'
```

**Response:**
```json
{
  "Patient Id": "12345",
  "Date of Appointment": "",
  "Diagnosis": "Type 2 Diabetes",
  "Causing Agent": "",
  "Primary Affected Area": "",
  "Infection Types": "",
  "Risk Factors": "",
  "Symptoms": "frequent urination, excessive thirst, fatigue",
  "Diagnostic Methods": "",
  "Recommendations": "",
  "Medications": "Metformin",
  "Dosage": "500mg daily",
  "Summary": "Patient John Doe, ID 12345, was diagnosed with Type 2 Diabetes..."
}
```

### **2. GET Request**
**Request:**
```bash
curl "http://127.0.0.1:5000/summarize?text=Patient+Jane+Doe,+ID+67890,+complained+of+chest+pain+and+shortness+of+breath.+She+was+diagnosed+with+a+respiratory+infection+caused+by+Streptococcus+pneumoniae."
```

**Response:**
```json
{
  "Patient Id": "67890",
  "Date of Appointment": "",
  "Diagnosis": "respiratory infection",
  "Causing Agent": "Streptococcus pneumoniae",
  "Primary Affected Area": "Respiratory system",
  "Infection Types": "",
  "Risk Factors": "",
  "Symptoms": "chest pain, shortness of breath",
  "Diagnostic Methods": "",
  "Recommendations": "",
  "Medications": "",
  "Dosage": "",
  "Summary": "Patient Jane Doe, ID 67890, was diagnosed with a respiratory infection caused by Streptococcus pneumoniae..."
}
```

---

## **Customization**

- **Model Version:**
  Update the `model` parameter in the `response_one` and `response_two` functions to use a different GPT model:
  ```python
  model = 'gpt-4'  # Replace with your desired model version
  ```

- **Extracted Fields:**
  Modify the `extract_function1` and `extract_function2` dictionaries to change the fields being extracted.

---

## **Dependencies**

- Python 3.7+
- Flask
- OpenAI Python Library

Install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## **Notes**

- Ensure your OpenAI API key has access to the selected GPT model.
- The application is configured for educational purposes. For production deployment, consider securing the API and optimizing performance.

---

## **License**
This project is licensed under the MIT License.
