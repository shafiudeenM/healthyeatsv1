from flask import Flask, request, jsonify
from groq import Groq

app = Flask(__name__)

# Initialize Groq client
client = Groq(
    api_key="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"  # Your API key
)

# Function to generate a 7-day diet plan with calorie details
def get_diet_plan(state, food_allergies, medical_allergies, model="llama3-8b-8192"):
    message = (f"Generate a 7-day diet plan in JSON format based on the following details: "
               f"State: {state}, Food allergies: {food_allergies}, Medical allergies: {medical_allergies}. "
               "Include breakfast, lunch, and dinner for each day along with calorie details for each meal.")

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
        model=model
    )

    return chat_completion.choices[0].message.content

@app.route('/diet-plan', methods=['POST'])
def diet_plan():
    data = request.json
    state = data.get('state')
    food_allergies = data.get('food_allergies', [])
    medical_allergies = data.get('medical_allergies', [])

    # Generate diet plan
    diet_plan_json = get_diet_plan(state, food_allergies, medical_allergies)

    return jsonify(diet_plan_json)
