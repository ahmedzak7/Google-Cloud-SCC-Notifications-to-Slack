# GCP Security Findings to Slack Notification

This Python script automatically sends security findings from Google Cloud Platform (GCP) to a specified Slack channel. It decodes and processes Security Command Center (SCC) findings and extracts relevant information such as project details, severity, and remediation steps. The information is posted to a Slack channel with clear warnings or alerts, depending on the severity.

## Features

- **Severity-based Notification**: The script adds emojis based on the severity of the finding (i.e., `:warning:` for HIGH and `:rotating_light:` for CRITICAL).
- **Project Metadata Extraction**: Extracts the project name and project ID from the GCP metadata provided in the payload.
- **Actionable Insights**: Includes the next steps for addressing the findings directly within the Slack message.

## Prerequisites

To use this script, you will need:
1. **Slack API Token**: A Slack Bot token for posting messages to a specific Slack channel. You can create a Slack bot and generate a token by following Slack’s API documentation: [Slack API](https://api.slack.com/).
2. **Google Cloud Security Command Center**: Ensure that Security Command Center (SCC) notifications are enabled to send findings to a Google Pub/Sub topic.

## Setup

1. **Configure the Environment**: Ensure that your Python environment has the required libraries:
   ```bash
   pip install requests
