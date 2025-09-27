# Aiden Configuration

## Azure Infrastructure
- **Subscription**: Project Aiden (`d9c4388d-2d77-4922-96cb-f113a52d0383`)
- **Tenant**: Helix Automations (`7fbc252f-3ce5-460f-9740-4e1cb8bf78b8`)
- **App Registration**: Aiden (`bee758ec-919c-45b2-9cdf-540c6419561f`)
- **Key Vault**: kv-aiden (`https://kv-aiden.vault.azure.net/`)

## Resource Groups
- `aiden-code` - Application code and functions
- `aiden-data` - Databases and storage
- `aiden-ai` - AI and ML services
- `aiden-infra` - Infrastructure components
- `aiden-devops` - CI/CD and monitoring
- `aiden-logs` - Logging and analytics

## Key Vault Secrets
- `aiden-app-id` - Application ID
- `aiden-email-secret-value` - Client secret for Graph API

## Graph API Permissions
- Mail.Send - Send emails
- Mail.ReadWrite - Read/write emails
- Team.ReadBasic.All - Access Teams
- Channel.ReadBasic.All - Access channels
- Directory.Read.All - Read directory
- (Full permissions list in app registration)

## Environment Configuration
Use `.env` file for local development:
```bash
cp .env.example .env
# Edit .env with your values
```

## Authentication Flow
1. Load credentials from Key Vault or environment
2. Get OAuth2 token using client credentials
3. Use token for all Graph API requests
4. Automatic token refresh handled internally