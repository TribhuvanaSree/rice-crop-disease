from flask import Flask, request, render_template, jsonify,send_from_directory
import subprocess
import pandas as pd
import time

app = Flask(__name__)
data = pd.read_excel(r"D:\epics work\Book1.xlsx")
current_row = 0

# Serve static CSS files
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get_data', methods=['POST'])
def get_data():
    try:
        # Use subprocess to execute the Python script
        print("here")
        result = subprocess.check_output(['python', 'link2.py'], universal_newlines=True, stderr=subprocess.STDOUT)
        print("here1")
    except subprocess.CalledProcessError as e:
        result = f"Error: {e.output}"
    
    return result
@app.route('/get_data_mois', methods=['POST'])
def get_data_mois():
    try:
        # Use subprocess to execute the Python script
        print("here")
        result = subprocess.check_output(['python', 'linkmois.py'], universal_newlines=True, stderr=subprocess.STDOUT)
        print("here1")
    except subprocess.CalledProcessError as e:
        result = f"Error: {e.output}"
    
    return result
@app.route('/get_data_ph', methods=['POST'])
def get_data_ph():
    try:
        # Use subprocess to execute the Python script
        print("here")
        result =subprocess.check_output(['python', 'linkPh.py'], universal_newlines=True, stderr=subprocess.STDOUT)
        print("here1")
    except subprocess.CalledProcessError as e:
        result = f"Error: {e.output}"
    
    return result
@app.route('/get_data_ec', methods=['POST'])
def get_data_ec():
    try:
        # Use subprocess to execute the Python script
        print("here")
        result = subprocess.check_output(['python', 'linkEc.py'], universal_newlines=True, stderr=subprocess.STDOUT)
        print("here1")
    except subprocess.CalledProcessError as e:
        result = f"Error: {e.output}"
    
    return result
@app.route('/get_data_npk', methods=['POST'])
def get_data_npk():
    try:
        # Use subprocess to execute the Python script
        print("here")
        result = subprocess.check_output(['python', 'linkNPK.py'], universal_newlines=True, stderr=subprocess.STDOUT)
        print("here1")
    except subprocess.CalledProcessError as e:
        result = f"Error: {e.output}"
    
    return result

@app.route('/datta', methods=['POST'])
def datta():
    try:
        # Use subprocess to execute the Python script
        print("here")
        result = subprocess.check_output(['python', 'link.py'], universal_newlines=True, stderr=subprocess.STDOUT)
        print("here1")
    except subprocess.CalledProcessError as e:
        result = f"Error: {e.output}"
    
    return result

if __name__ == "__main__":
    app.run(debug=True)