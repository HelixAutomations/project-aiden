import requests
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

# Get secrets from Key Vault
credential = DefaultAzureCredential()
client = SecretClient(vault_url="https://kv-aiden.vault.azure.net/", credential=credential)

app_id = client.get_secret("aiden-app-id").value
client_secret = client.get_secret("aiden-email-secret-value").value

# Get access token
token_url = "https://login.microsoftonline.com/7fbc252f-3ce5-460f-9740-4e1cb8bf78b8/oauth2/v2.0/token"
token_data = {
    'client_id': app_id,
    'client_secret': client_secret,
    'scope': 'https://graph.microsoft.com/.default',
    'grant_type': 'client_credentials'
}

token_response = requests.post(token_url, data=token_data)
access_token = token_response.json()['access_token']

# Send email
email_url = "https://graph.microsoft.com/v1.0/users/lz@helix-law.com/sendMail"
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

email_data = {
    "message": {
        "subject": "AIDEN Test Email",
        "body": {
            "contentType": "Text",
            "content": "Test email from Project AIDEN automation. Brief and functional."
        },
        "toRecipients": [
            {
                "emailAddress": {
                    "address": "lz@helix-law.com"
                }
            }
        ]
    }
}

response = requests.post(email_url, headers=headers, json=email_data)
print(f"Status: {response.status_code}")
print(f"Response: {response.text}")