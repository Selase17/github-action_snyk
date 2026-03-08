import os
import subprocess
import pickle
import hashlib
import sqlite3
from flask import Flask, request

app = Flask(__name__)

# -------------------------------------------------------
# VULNERABILITY 1: Hardcoded credentials
# -------------------------------------------------------
DB_PASSWORD = "admin123"
SECRET_KEY = "hardcoded_secret_key_1234"
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"


# -------------------------------------------------------
# VULNERABILITY 2: SQL Injection
# -------------------------------------------------------
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # Directly interpolating user input into SQL query
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchall()


# -------------------------------------------------------
# VULNERABILITY 3: Command Injection
# -------------------------------------------------------
def ping_host(host):
    # User input passed directly to shell command
    os.system(f"ping -c 1 {host}")


def list_files(directory):
    # Another command injection via subprocess
    subprocess.call("ls -la " + directory, shell=True)


# -------------------------------------------------------
# VULNERABILITY 4: Insecure Deserialization
# -------------------------------------------------------
def load_user_data(data):
    # Deserializing untrusted data with pickle is dangerous
    return pickle.loads(data)


# -------------------------------------------------------
# VULNERABILITY 5: Weak Hashing Algorithm (MD5)
# -------------------------------------------------------
def hash_password(password):
    # MD5 is cryptographically broken
    return hashlib.md5(password.encode()).hexdigest()


def hash_password_sha1(password):
    # SHA1 is also considered weak
    return hashlib.sha1(password.encode()).hexdigest()


# -------------------------------------------------------
# VULNERABILITY 6: Path Traversal
# -------------------------------------------------------
def read_file(filename):
    # No sanitization of filename allows path traversal (e.g., ../../etc/passwd)
    with open(filename, "r") as f:
        return f.read()


# -------------------------------------------------------
# VULNERABILITY 7: XSS - Reflected Input (Flask)
# -------------------------------------------------------
@app.route("/search")
def search():
    query = request.args.get("q", "")
    # User input reflected directly into response without sanitization
    return f"<h1>Search results for: {query}</h1>"


# -------------------------------------------------------
# VULNERABILITY 8: Debug Mode Enabled in Production
# -------------------------------------------------------
if __name__ == "__main__":
    # Running Flask in debug mode exposes sensitive info
    app.run(debug=True, host="0.0.0.0", port=5000)