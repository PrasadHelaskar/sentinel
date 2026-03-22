# 🛡️ Sentinel

Sentinel is a lightweight automation observability service designed to monitor test execution artifacts, analyze reports, detect failures, and deliver actionable notifications.

It provides a centralized intelligence layer on top of CI/CD automation pipelines.

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)]()
[![CI](https://github.com/PrasadHelaskar/sentinel/actions/workflows/sentinel.yml/badge.svg)](https://github.com/PrasadHelaskar/sentinel/actions)
[![Architecture](https://img.shields.io/badge/Architecture-Modular-blueviolet)]()
[![Design](https://img.shields.io/badge/Design-Extensible-6f42c1)]()
[![Automation](https://img.shields.io/badge/Automation-Observability-critical)]()
[![Scheduler](https://img.shields.io/badge/Scheduler-Cron%20Supported-orange)]()
[![Notifications](https://img.shields.io/badge/Notifications-Slack%20Enabled-4A154B?logo=slack&logoColor=white)]()
[![Status](https://img.shields.io/badge/Status-Active-success)]()

## 📌 Overview

Modern automation environments often operate across multiple repositories and pipelines. While CI systems execute tests reliably, they do not provide centralized visibility into automation health across projects.

- Sentinel addresses this gap by:
- Monitoring automation run artifacts
- Parsing structured test reports
- Detecting failure conditions
- Preventing duplicate processing
- Delivering real-time notifications

## 🏗 Architecture
```bash
CI Pipeline (GitHub Actions / Cron)
            │
            ▼
     Test Artifacts (HTML Reports)
            │
            ▼
        Sentinel Core
     ┌─────────────────────┐
     │  Repo Monitor       │
     │  Report Parser      │
     │  log Parser         │
     │  Run State Tracker  │
     └─────────────────────┘
            │
            ▼
     Notification Layer
     ├── Console
     └── Slack
```

## 🚀 Features
Repository Monitoring

- Detects new automation artifacts
- Supports scheduled or CI-triggered execution
- Prevents reprocessing of previously handled runs

### Report Parsing

- Parses pytest HTML reports using BeautifulSoup and extracts:
- Total test count
- Passed tests
- Failed tests
- Skipped tests
- Execution duration

The parser is modular and can be extended to support other report formats.

### Failure Detection
- Identifies failure conditions
- Triggers notifications only when necessary
- Avoids duplicate alerts

### Notification Engine

Currently supported:
- Console output
- Slack webhook integration

The notification layer is extensible for additional integrations.

### Log Intelligence

Sentinel analyzes automation logs to extract meaningful failure signals.

Instead of sending raw logs, Sentinel identifies:

- Failed test names
- Assertion errors
- Exception traces
- Relevant log snippets

This provides actionable failure context in notifications.

## 📂 Project Structure

```bash
sentinel/
│
├── app/
│   ├── main.py
│   ├── core/
│   │   ├── config.py
│   │   └── state_manager.py
│   │
│   ├── github/
│   │   └── client.py
│   │
│   ├── services/
│   │   ├── artifact_service.py
│   │   ├── log_parser.py
│   │   ├── repo_monitor.py
│   │   ├── report_parser.py
│   │   └── summarizer.py
│   │
│   ├── notifier/
│   │       ├── console_notifier.py
│   │       └── slack_notifier.py
│   │
│   └── utils/
│
├── artifacts/
├── data/
│    └── processed_runs.json
├── requirements.txt 
└── README.md
```

## 🛠 Technology Stack

- Python 3.10+
- BeautifulSoup
- GitHub Actions
- Cron scheduling
- Slack Webhooks
- JSON-based state persistence

## ⚙️ Installation
### Clone the repository
```bash
git clone https://github.com/PrasadHelaskar/sentinel.git

cd sentinel
```

### Create virtual environment
```bash
python -m venv venv

source venv/bin/activate      # Linux / WSL

venv\Scripts\activate         # Windows
```

### Install dependencies
```bash
pip install -r requirements.txt
```

## ▶️ Running Sentinel

```bash
python -m app.main
```
Execution flow:

1. Scan configured repositories
2. Detect new test reports
3. Parse report statistics
4. Evaluate failure conditions
5. Send notifications if required

### ⏰ Scheduled Execution Example
Run every day at 7.30 PM

```bash
30 13 * * * python3 /path/to/sentinel/app/main.py
```

## 🔐 Slack Integration

1. Create a Slack Incoming Webhook
2. Configure environment variable:
```bash
    export SLACK_WEBHOOK_URL="your-webhook-url"
```
3. Enable Slack notifier in configuration

## 🧠 Design Principles

### Idempotent Processing
A processed_runs.json registry ensures:
- Safe repeated execution
- No duplicate alerting
- Clean monitoring lifecycle

### Modular Architecture
Core services are separated into:
- Monitoring
- Parsing
- Detection
- Notification

This enables independent extension of each component.

### Extensibility
The system is structured to support:

- Additional report formats
- Additional notification channels
- Persistent storage backends
- Parallel repository scanning

---

Sentinel is designed to serve as a foundational observability layer for automation ecosystems, enabling structured monitoring and controlled failure intelligence across CI environments.
