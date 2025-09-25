import requests
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

# Get credentials from Key Vault
credential = DefaultAzureCredential()
client = SecretClient(vault_url="https://kv-aiden.vault.azure.net/", credential=credential)

client_id = client.get_secret("aiden-client-id").value
client_secret = client.get_secret("aiden-client-secret").value
tenant_id = client.get_secret("aiden-tenant-id").value

# Get access token
token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
token_data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'scope': 'https://graph.microsoft.com/.default'
}

token_response = requests.post(token_url, data=token_data)
access_token = token_response.json()['access_token']

# List all Teams
teams_url = "https://graph.microsoft.com/v1.0/groups?$filter=resourceProvisioningOptions/Any(x:x eq 'Team')"
headers = {'Authorization': f'Bearer {access_token}'}

teams_response = requests.get(teams_url, headers=headers)
print(f"Teams Status: {teams_response.status_code}")

if teams_response.status_code == 200:
    teams = teams_response.json()['value']
    print(f"\nFound {len(teams)} teams:")

    for team in teams:
        print(f"\nTeam: {team['displayName']}")
        team_id = team['id']

        # Get channels for this team
        channels_url = f"https://graph.microsoft.com/v1.0/teams/{team_id}/channels"
        channels_response = requests.get(channels_url, headers=headers)

        if channels_response.status_code == 200:
            channels = channels_response.json()['value']
            print(f"  Channels ({len(channels)}):")
            for channel in channels:
                print(f"    - {channel['displayName']}")
        else:
            print(f"  Channels error: {channels_response.status_code}")
            print(f"  Error: {channels_response.text}")
else:
    print(f"Error: {teams_response.text}")