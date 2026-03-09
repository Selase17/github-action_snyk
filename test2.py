import os
import pickle
import sqlite3
import subprocess
from flask import Flask, request

app = Flask(__name__)

# 🚨 CRITICAL VULNERABILITY 1: Hardcoded API Key & Password
API_KEY = "sk-CRITICAL-LEAKED-KEY-987654"
DB_PASSWORD = "Admin123!"

# 🚨 CRITICAL VULNERABILITY 2: Remote Code Execution via HTTP Request
@app.route("/rce", methods=["POST"])
def remote_execute():
    code = request.form.get("code")  # User-provided code
    return str(eval(code))  # 🔥 Full RCE via exposed HTTP endpoint!

# 🚨 CRITICAL VULNERABILITY 3: SQL Injection
@app.route("/user", methods=["GET"])
def get_user():
    username = request.args.get("username")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    # 🔥 Exploitable SQL injection
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    return str(cursor.fetchall())

# 🚨 CRITICAL VULNERABILITY 4: Command Injection
@app.route("/cmd", methods=["POST"])
def execute_command():
    user_input = request.form.get("cmd")
    
    # 🔥 Full system compromise possible!
    result = subprocess.check_output(f"bash -c '{user_input}'", shell=True)
    return result.decode()

if __name__ == "__main__":
    print(f"⚠️  Running vulnerable server on http://localhost:5000")
    print(f"⚠️  API Key: {API_KEY}")

    app.run(host="0.0.0.0", port=5000, debug=True)  # Debug mode exposes even more risk!
