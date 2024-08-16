from flask import Flask, request, jsonify
import openai
from openai import OpenAI
import json

OPENAI_KEY = "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"
openai.api_key=OPENAI_KEY

client = OpenAI(api_key=OPENAI_KEY)

app = Flask(__name__)

extract_function1 = [
    {
        'name': 'extract_medical_info',
        'description': 'Get the medical information from the body of the input text. ',
        'parameters': {
            'type': 'object',
            'properties': {
                'Patient Id': {
                    'type': 'string',
                    'description': 'Patient Id'
                },
                'Date of Appointment': {
                    'type': 'string',
                    'description': 'Date of Appointment'
                },
                'Diagnosis' : {
                    'type': 'string',
                    'description': 'Diagnosis Information'
                    
                },
                'Causing Agent' : {
                    'type': 'string',
                    'description': 'Causing Agent'
                    
                },  
                'Primary Affected Area' : {
                    'type': 'string',
                    'description': 'Primary Affected Area'
                    
                },              
                'Infection Types' : {
                    'type': 'string',
                    'description': 'Infection Types'
                    
                }, 
                'Risk Factors' : {
                    'type': 'string',
                    'description': 'Risk Factors'
                    
                },
                'Symptoms' : {
                    'type': 'string',
                    'description': 'Symptoms'
                    
                }, 
                'Diagnostic Methods' : {
                    'type': 'string',
                    'description': 'Diagnostic Methods'
                    
                }
             
            }
        }
    }
]

extract_function2 = [
    {
        'name': 'extract_medical_info',
        'description': 'Get the medical information from the body of the input text.',
        'parameters': {
            'type': 'object',
            'properties': {
                'Recommendations' : {
                    'type': 'string',
                    'description': 'Recommendations'
                    
                }, 
                'Medications' : {
                    'type': 'string',
                    'description': 'Medications'
                    
                }, 
                'Dosage' : {
                    'type': 'string',
                    'description': 'Dosage'
                    
                },
                'Summary': {
                    'type': 'string',
                    'description': 'Elaborative Summary of the Appointment'
                }               
            }
        }
    }
]


def response_one(text):
    response1 =  client.chat.completions.create(
        model = 'gpt-3.5-turbo-0125',
        messages = [{'role': 'user', 'content': text}],
        functions = extract_function1,
        function_call = 'auto'
        )
    response1 = json.loads(response1.choices[0].message.function_call.arguments)
    return response1

def response_two(text):
    response2 =  client.chat.completions.create(
        model = 'gpt-3.5-turbo-0125',
        messages = [{'role': 'user', 'content': text}],
        functions = extract_function2,
        function_call = 'auto'
        )
    response2 = json.loads(response2.choices[0].message.function_call.arguments)
    return response2


def summarize_text(text):
    # Implement your summarization algorithm here
    # Placeholder: returns the original text
    response1 = response_one(text)
    response2 = response_two(text)
    response1.update(response2)

    return response1


@app.route('/summarize', methods=['GET', 'POST'])
def summarize():
    if request.method == 'POST':
        text = request.json.get('text', '')
    else:
        text = request.args.get('text', '')

    summary = summarize_text(text)  # Replace with your summarization logic
    return jsonify(summary)



if __name__ == '__main__':
    app.run()

