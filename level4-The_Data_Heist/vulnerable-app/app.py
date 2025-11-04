from flask import Flask, request, send_file, render_template_string
import os
from cryptography.fernet import Fernet
from key import key as KEY

app = Flask(__name__)

# A simple HTML template for the file viewer
TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Innovatech File Viewer</title>
    <style>
      body { font-family: sans-serif; background-color: #f4f4f9; color: #333; text-align: center; margin-top: 50px; }
      h1 { color: #5a5a5a; }
      .container { background-color: #fff; padding: 2em; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); display: inline-block; }
      form { margin-top: 20px; }
      input[type=text] { padding: 10px; border: 1px solid #ddd; border-radius: 4px; width: 250px; }
      input[type=submit] { padding: 10px 20px; background-color: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer; }
      .file-content { text-align: left; background-color: #e9e9f4; border: 1px solid #ccc; padding: 15px; border-radius: 4px; margin-top: 20px; white-space: pre-wrap; font-family: monospace; }
      .error { color: #d9534f; }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>Innovatech Secure File Viewer</h1>
      <p>Enter the name of a file to view its contents.</p>
      <form method="GET">
        <input type="text" name="filename" placeholder="e.g., welcome.txt">
        <input type="submit" value="View File">
      </form>
      {% if error %}
        <p class="error"><strong>Error:</strong> {{ error }}</p>
      {% endif %}
      {% if content %}
        <h3>Contents of {{ filename }}:</h3>
        <div class="file-content">{{ content }}</div>
      {% endif %}
    </div>
  </body>
</html>
"""

def encrypt(text, key):
    f = Fernet(key)
    encrypted = f.encrypt(text.encode())
    return encrypted.decode()

def decrypt(text, key):
    f = Fernet(key)
    decrypted = f.decrypt(text.encode())
    return decrypted.decode()

@app.route('/', methods=['GET'])
def file_viewer():
    filename = request.args.get('filename')
    content = None
    error = None

    if filename:
        
            file_path = os.path.join(os.getcwd(), 'level4-The_Data_Heist/vulnerable-app/files', filename)
            if (".." in filename) or os.path.isabs(filename):
              error = "Invalid filename."
            else:
              try:
                  # Check if the path is a file and exists
                  if os.path.isfile(file_path) and not os.path.islink(file_path):
                      with open(file_path, 'r') as f:
                          c = f.read()
                          content = decrypt(c, KEY)
                  else:
                      error = f"File not found: {filename}"
              except Exception as e:
                  error = "An error occurred while trying to read the file."
            
    return render_template_string(TEMPLATE, filename=filename, content=content, error=error)

if __name__ == '__main__':
    # Create a dummy 'files' directory and a welcome file inside it for the app to read
    if not os.path.exists('level4-The_Data_Heist/vulnerable-app/files'):
        os.makedirs('level4-The_Data_Heist/vulnerable-app/files')
    with open('level4-The_Data_Heist/vulnerable-app/files/welcome.txt', 'w') as f:
        en=encrypt('Welcome to the Innovatech file viewer!', KEY)
        f.write(en)
    
    # This will run the web server on http://127.0.0.1:8080
    app.run(debug=True, port=8080)
