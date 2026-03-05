---
name: gogcli
description: "Google Workspace CLI for Gmail, Calendar, Drive, Sheets, Docs, Slides, Contacts, Tasks, People, Groups, Keep."
author: luccast
---

# gogcli - Google Workspace CLI

CLI tool for managing Google Workspace services from terminal.

## Installation

### Via Homebrew
```bash
brew install steipete/tap/gogcli
```

### Build from Source
```bash
git clone https://github.com/steipete/gogcli.git
cd gogcli
make
sudo make install
```

## Setup

**Step 1: Get OAuth Credentials**
1. Google Cloud Console → APIs & Services → OAuth consent screen
2. Create Desktop app
3. Authorized redirect: `http://localhost:8085/callback`
4. Enable APIs (Gmail, Calendar, Drive, etc.)
5. Download credentials JSON

**Step 2: Authorize**
```bash
./bin/gog auth add you@gmail.com ~/Downloads/client_secret_....json
```

## Commands

### Gmail
```bash
gog gmail search 'is:unread' --max 5
gog gmail send 'recipient@gmail.com' --subject 'Hello' --body 'Message'
gog gmail labels list
```

### Calendar
```bash
gog calendar events list --max 50
gog calendar events create 'Meeting' --start '2026-01-30T10:00'
```

### Drive
```bash
gog drive ls --query 'pdf' --max 20
gog drive upload ~/Documents/file.pdf
```

### Tasks
```bash
gog tasks list
gog tasks add --title 'Task' --due '2026-01-30'
```

## Notes

- Use `--json` flag for scripting
- Credentials: `~/.config/gog/`
- Check auth: `gog auth list`
