# 🕷️ Aiden - The Microsoft Graph Spider Agent

**I crawl into your projects as a submodule and deliver Microsoft Graph superpowers.**

Like a spider waiter ready to hand out packages of goodies - email automation, Teams integration, SharePoint access, calendar management - all through Microsoft Graph API.

## 🎯 Purpose

When added to any project as a submodule, Aiden becomes your Microsoft 365 automation layer. No complex setup, no authentication headaches - just import and use.

## 🎁 Available Goodie Packages

### 📧 Email Package
```python
from aiden import email
email.send_email("user@company.com", "Subject", "Body content")
inbox = email.get_inbox()
```

### 💬 Teams Package
```python
from aiden import teams
teams_list = teams.get_teams()
channels = teams.get_channels(team_id)
teams.post_message(team_id, channel_id, "Hello from Aiden!")
```

### 📅 Calendar Package
```python
from aiden import calendar
events = calendar.get_events()
calendar.create_event("user@company.com", "Meeting", "2025-01-01T10:00:00", "2025-01-01T11:00:00")
```

### 📂 SharePoint Package
```python
from aiden import sharepoint
sites = sharepoint.get_sites()
lists = sharepoint.get_lists(site_id)
```

## 🚀 Quick Start

### As Submodule (Recommended)
```bash
git submodule add https://github.com/HelixAutomations/project-aiden.git aiden
cd aiden && pip install -r requirements.txt
```

### Direct Installation
```bash
git clone https://github.com/HelixAutomations/project-aiden.git
cd project-aiden
pip install -e .
```

### Usage
```python
# Import specific goodies
from aiden import email, teams, calendar

# Or import the main spider
from aiden import aiden

# Show available packages
from aiden import deliver_goodies
deliver_goodies()
```

## 🏗️ Infrastructure

### Azure Setup ✅
- **Subscription**: Project Aiden (d9c4388d-2d77-4922-96cb-f113a52d0383)
- **Key Vault**: kv-aiden with authentication secrets
- **App Registration**: Aiden with Graph API permissions
- **Resource Groups**: code, data, ai, infra, devops, logs

### Authentication ✅
- Azure Key Vault integration
- Client credentials flow
- Automatic token management
- No manual credential handling

## 🎭 Philosophy

**Be ruthlessly brief. Crawl out. Deliver amazing things.**

Aiden doesn't just integrate with Microsoft Graph - Aiden IS your Graph API layer. Add me to any project and watch the magic happen.