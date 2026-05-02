from flask import Flask, send_from_directory, redirect, request, session
import msal
import requests
import os

app = Flask(__name__, static_folder='.')

app.secret_key = os.urandom(24)

# Graph API config
CLIENT_ID = "481c9288-228c-4b44-a509-7478335bd534"
TENANT_ID = "feb18abf-17ea-4d88-a4ac-05ffcd6ecb8b"
CLIENT_SECRET = os.environ.get("GRAPH_CLIENT_SECRET")
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPES = ["Files.Read.All", "User.Read"]
REDIRECT_URI = "https://algotradez-aios.azurewebsites.net/auth/callback"

@app.route('/')
def index():
    return send_from_directory('.', 'dashboard.html')

@app.route('/auth/login')
def auth_login():
    msal_app = msal.ConfidentialClientApplication(
        CLIENT_ID, authority=AUTHORITY, client_credential=CLIENT_SECRET
    )
    auth_url = msal_app.get_authorization_request_url(SCOPES, redirect_uri=REDIRECT_URI)
    return redirect(auth_url)

@app.route('/auth/callback')
def auth_callback():
    code = request.args.get('code')
    msal_app = msal.ConfidentialClientApplication(
        CLIENT_ID, authority=AUTHORITY, client_credential=CLIENT_SECRET
    )
    result = msal_app.acquire_token_by_authorization_code(code, SCOPES, redirect_uri=REDIRECT_URI)
    session['access_token'] = result.get('access_token')
    return redirect('/')

@app.route('/api/onedrive/files')
def list_onedrive_files():
    token = session.get('access_token')
    if not token:
        return {"error": "Not authenticated"}, 401
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get("https://graph.microsoft.com/v1.0/me/drive/root/children", headers=headers)
    return resp.json()

if __name__ == '__main__':
    app.run()