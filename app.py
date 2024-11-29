from flask import Flask, request, jsonify
from joblib import load  
import pandas as pd


app = Flask(__name__)

model = load('model.pkl')  

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    input_data = pd.DataFrame([data])

    prediction = model.predict(input_data)

    crowd_level = int(prediction[0])

    return jsonify({'crowd_level': crowd_level})

# Run the app
if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
