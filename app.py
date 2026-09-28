from flask import Flask, request, render_template_string
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

HTML = """
<!DOCTYPE html>
<html>
<head>
<style>
body { font-family: Arial; background: linear-gradient(135deg, #667eea, #764ba2); display:flex; justify-content:center; align-items:center; min-height:100vh; margin:0; padding:20px; }
.card { background:white; padding:35px; border-radius:20px; box-shadow:0 10px 30px rgba(0,0,0,0.3); width:420px; }
h2 { text-align:center; color:#333; margin-bottom:20px; }
input {
  width:100%;
  padding:14px;
  margin:8px 0;
  border-radius:12px;
  border:2px solid #ddd;
  font-size:15px;
  box-sizing: border-box;
  border-left: 6px solid #ddd;
}
input:focus { border-color:#667eea; outline:none; background:#f8f9ff; }
/* Your colourful style - FIXED */
input[name=\"MedInc\"] { border-left-color: #ff6b6b; }
input[name=\"HouseAge\"] { border-left-color: #20c997; }
input[name=\"AveRooms\"] { border-left-color: #ffc107; }
input[name=\"AveBedrms\"] { border-left-color: #845ef7; }
input[name=\"Population\"] { border-left-color: #339af0; }
input[name=\"AveOccup\"] { border-left-color: #ff922b; }
input[name=\"Latitude\"] { border-left-color: #f06595; }
input[name=\"Longitude\"] { border-left-color: #51cf66; }
button { width:100%; padding:16px; background:linear-gradient(135deg, #667eea, #764ba2); color:white; border:none; border-radius:12px; cursor:pointer; font-size:18px; font-weight:bold; margin-top:15px; }
.result { text-align:center; margin-top:20px; font-weight:bold; color:#2f9e44; font-size:20px; background:#e8f5e9; padding:15px; border-radius:10px; }
label{font-weight:bold; font-size:13px; color:#555; margin-top:5px; display:block;}
</style>
</head>
<body>
<div class="card">
<h2>🏠 House Price Prediction</h2>
<form method="post">
<label>💰 Median Income (1-15)</label>
<input name="MedInc" placeholder="e.g. 8.3" type="number" step="any" value="8.3" required>
<label>🏠 House Age</label>
<input name="HouseAge" placeholder="e.g. 41" type="number" step="any" value="41" required>
<label>🛏️ Average Rooms</label>
<input name="AveRooms" placeholder="e.g. 6" type="number" step="any" value="6" required>
<label>🛌 Average Bedrooms</label>
<input name="AveBedrms" placeholder="e.g. 1.2" type="number" step="any" value="1.2" required>
<label>👨‍👩‍👧 Population</label>
<input name="Population" placeholder="e.g. 322" type="number" step="any" value="322" required>
<label>👥 Average Occupancy</label>
<input name="AveOccup" placeholder="e.g. 2.5" type="number" step="any" value="2.5" required>
<label>🌎 Latitude</label>
<input name="Latitude" placeholder="e.g. 34.2" type="number" step="any" value="34.2" required>
<label>🗺️ Longitude</label>
<input name="Longitude" placeholder="e.g. -118.5" type="number" step="any" value="-118.5" required>
<button>✨ Predict Price</button>
</form>
<div class="result">{{ result }}</div>
</div>
</body>
</html>
"""

@app.route('/', methods=['GET','POST'])
def home():
    result = ""
    if request.method == 'POST':
        # CORRECT ORDER - 8 features for California Housing
        vals = [
            float(request.form['MedInc']),
            float(request.form['HouseAge']),
            float(request.form['AveRooms']),
            float(request.form['AveBedrms']),
            float(request.form['Population']),
            float(request.form['AveOccup']),
            float(request.form['Latitude']),
            float(request.form['Longitude'])
        ]
        pred = model.predict([vals])[0]
        result = f"💰 Predicted: ${pred*100000:,.2f}"
    return render_template_string(HTML, result=result)

if __name__ == '__main__':
    app.run(debug=True)