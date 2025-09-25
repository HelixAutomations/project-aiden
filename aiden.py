"""
Aiden - The Microsoft Graph Spider Agent

I crawl into your projects as a submodule and deliver Graph API superpowers.
Like a spider waiter ready to hand out packages of goodies.
"""

import requests
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
from typing import Dict, List, Optional, Any
import json
from datetime import datetime


class AidenSpider:
    """The core spider that delivers Microsoft Graph capabilities"""

    def __init__(self, vault_url: str = "https://kv-aiden.vault.azure.net/"):
        self.vault_url = vault_url
        self.access_token = None
        self.credentials = {}
        self._authenticate()

    def _authenticate(self):
        """Crawl out and get authenticated"""
        try:
            credential = DefaultAzureCredential()
            client = SecretClient(vault_url=self.vault_url, credential=credential)

            self.credentials = {
                'client_id': client.get_secret("aiden-app-id").value,
                'client_secret': client.get_secret("aiden-email-secret-value").value,
                'tenant_id': "7fbc252f-3ce5-460f-9740-4e1cb8bf78b8"  # Helix Automations tenant
            }

            # Get access token
            token_url = f"https://login.microsoftonline.com/{self.credentials['tenant_id']}/oauth2/v2.0/token"
            token_data = {
                'grant_type': 'client_credentials',
                'client_id': self.credentials['client_id'],
                'client_secret': self.credentials['client_secret'],
                'scope': 'https://graph.microsoft.com/.default'
            }

            response = requests.post(token_url, data=token_data)
            response_data = response.json()

            if 'access_token' in response_data:
                self.access_token = response_data['access_token']
                print("🕷️ Aiden spider authenticated and ready to crawl")
            else:
                print(f"🚫 Token error: {response_data}")
                raise Exception(f"Authentication failed: {response_data}")

        except Exception as e:
            print(f"🚫 Spider authentication failed: {e}")
            raise

    @property
    def headers(self) -> Dict[str, str]:
        """Standard Graph API headers"""
        return {'Authorization': f'Bearer {self.access_token}'}

    def _graph_request(self, method: str, url: str, data: Optional[Dict] = None) -> Dict:
        """Make Graph API requests with error handling"""
        full_url = f"https://graph.microsoft.com/v1.0/{url}"

        if method.upper() == 'GET':
            response = requests.get(full_url, headers=self.headers)
        elif method.upper() == 'POST':
            response = requests.post(full_url, headers=self.headers, json=data)
        elif method.upper() == 'PUT':
            response = requests.put(full_url, headers=self.headers, json=data)
        elif method.upper() == 'DELETE':
            response = requests.delete(full_url, headers=self.headers)

        if response.status_code in [200, 201, 202, 204]:
            return response.json() if response.content else {"status": "success"}
        else:
            raise Exception(f"Graph API error {response.status_code}: {response.text}")


class EmailGoodie(AidenSpider):
    """Email automation goodie package"""

    def send_email(self, to_email: str, subject: str, body: str, from_email: str = "automations@helix-law.com") -> Dict:
        """Send email through Graph API"""
        email_data = {
            "message": {
                "subject": subject,
                "body": {
                    "contentType": "Text",
                    "content": body
                },
                "toRecipients": [
                    {
                        "emailAddress": {
                            "address": to_email
                        }
                    }
                ]
            }
        }

        result = self._graph_request('POST', f"users/{from_email}/sendMail", email_data)
        print(f"📧 Email sent to {to_email}")
        return result

    def get_inbox(self, user_email: str = "automations@helix-law.com", top: int = 10) -> List[Dict]:
        """Get inbox messages"""
        result = self._graph_request('GET', f"users/{user_email}/messages?$top={top}")
        return result.get('value', [])


class TeamsGoodie(AidenSpider):
    """Teams integration goodie package"""

    def get_teams(self) -> List[Dict]:
        """Get all teams"""
        result = self._graph_request('GET', "groups?$filter=resourceProvisioningOptions/Any(x:x eq 'Team')")
        return result.get('value', [])

    def get_channels(self, team_id: str) -> List[Dict]:
        """Get channels for a team"""
        result = self._graph_request('GET', f"teams/{team_id}/channels")
        return result.get('value', [])

    def post_message(self, team_id: str, channel_id: str, message: str) -> Dict:
        """Post message to Teams channel"""
        message_data = {
            "body": {
                "contentType": "text",
                "content": message
            }
        }

        result = self._graph_request('POST', f"teams/{team_id}/channels/{channel_id}/messages", message_data)
        print(f"💬 Message posted to Teams channel")
        return result

    def get_messages(self, team_id: str, channel_id: str, top: int = 20) -> List[Dict]:
        """Get messages from Teams channel"""
        result = self._graph_request('GET', f"teams/{team_id}/channels/{channel_id}/messages?$top={top}")
        return result.get('value', [])


class CalendarGoodie(AidenSpider):
    """Calendar automation goodie package"""

    def get_events(self, user_email: str = "automations@helix-law.com", days: int = 7) -> List[Dict]:
        """Get calendar events"""
        result = self._graph_request('GET', f"users/{user_email}/events?$top=50")
        return result.get('value', [])

    def create_event(self, user_email: str, subject: str, start_time: str, end_time: str, attendees: List[str] = None) -> Dict:
        """Create calendar event"""
        event_data = {
            "subject": subject,
            "start": {
                "dateTime": start_time,
                "timeZone": "UTC"
            },
            "end": {
                "dateTime": end_time,
                "timeZone": "UTC"
            }
        }

        if attendees:
            event_data["attendees"] = [
                {"emailAddress": {"address": email, "name": email}}
                for email in attendees
            ]

        result = self._graph_request('POST', f"users/{user_email}/events", event_data)
        print(f"📅 Calendar event created: {subject}")
        return result


class SharePointGoodie(AidenSpider):
    """SharePoint integration goodie package"""

    def get_sites(self) -> List[Dict]:
        """Get SharePoint sites"""
        result = self._graph_request('GET', "sites?search=*")
        return result.get('value', [])

    def get_lists(self, site_id: str) -> List[Dict]:
        """Get lists from SharePoint site"""
        result = self._graph_request('GET', f"sites/{site_id}/lists")
        return result.get('value', [])


# Main Aiden instance - ready to be imported and used
aiden = AidenSpider()

# Goodie packages ready for delivery
email = EmailGoodie()
teams = TeamsGoodie()
calendar = CalendarGoodie()
sharepoint = SharePointGoodie()

def deliver_goodies():
    """Show what goodies Aiden can deliver"""
    print("🕷️ Aiden Spider - Available Goodie Packages:")
    print("📧 email - Send emails, read inbox")
    print("💬 teams - Access Teams, post messages, read channels")
    print("📅 calendar - Manage events, schedule meetings")
    print("📂 sharepoint - Access sites, lists, documents")
    print("\nUsage: from aiden import email, teams, calendar, sharepoint")

if __name__ == "__main__":
    deliver_goodies()