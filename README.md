
# GCP Security Findings to Slack Notification - Google Cloud Function

This Python script is designed to run as a Google Cloud Function that listens to real-time Google Cloud Security Command Center (SCC) findings via Pub/Sub and sends a detailed notification to a Slack channel. The notification includes project details, severity level, and recommended next steps for remediation.

## Features

- **Severity-based Notifications**: Automatically assigns warning or alert emojis based on the severity of the findings (HIGH or CRITICAL).
- **Google Cloud Function Integration**: The script is deployed as a Google Cloud Function triggered by SCC findings via Pub/Sub.
- **Slack Integration**: Sends formatted messages to a Slack channel with project details and next steps.

## Prerequisites

To use this script, you will need:
1. **Google Cloud Security Command Center (SCC)**: Ensure SCC is enabled, and real-time notifications are configured.
2. **Slack API Token**: A valid Slack Bot token for sending messages to a channel. Follow Slack’s API documentation to create a Slack app.

## Setup

1. **Create a Pub/Sub Topic**: 
   In the Google Cloud Console, create a new Pub/Sub topic that will receive SCC findings. For example:
   ```bash
   gcloud pubsub topics create scc-findings-topic
   ```

2. **Enable SCC Notifications**:
   Set up SCC notifications to publish findings to the Pub/Sub topic using this command:
   ```bash
   gcloud scc notifications create scc-notifier        --organization=YOUR_ORG_ID        --pubsub-topic=projects/YOUR_PROJECT_ID/topics/scc-findings-topic        --filter="severity="HIGH" OR severity="CRITICAL""        --description="Notifications for high and critical severity findings"
   ```

3. **Deploy the Function**:
   - In the Google Cloud Console, navigate to **Cloud Functions**.
   - Create a new function with a Pub/Sub trigger and select the topic created earlier.
   - Set the runtime to Python 3.8 or higher and deploy the script.

4. **Configure Slack**:
   - Add your Slack token as an environment variable or include it directly in the script.
   - Replace the `TOKEN` value in the script with your Slack bot token.

## How It Works

1. **Pub/Sub Trigger**: When a high or critical SCC finding is detected, a Pub/Sub message triggers the Cloud Function.
2. **Message Processing**: The function decodes the Pub/Sub message and extracts key information such as project name, ID, severity, and next steps.
3. **Slack Notification**: The function sends a formatted message to Slack, including emojis to indicate the severity level.

## Example Slack Message

For a HIGH severity finding:

```
A HIGH severity finding :warning: 'IAM_ROLE_HAS_EXCESSIVE_PERMISSIONS' was detected!
Project Name: test-1234
Project ID: 257173341772
Next Steps: Go to https://console.cloud.google.com/iam-admin/iam?project=457173341772 and apply your IAM recommendations.
```

For a CRITICAL severity finding:

```
A CRITICAL severity finding :rotating_light: 'Publicly accessible instance with project-wide SSH key and the ability to assume service accounts.' was detected!
Project Name: test-12345
Project ID: 357173341770
Next Steps: Ensure that the SSH keys are managed securely and access to the instance is properly restricted.
```

## Conclusion

This Cloud Function automates the process of monitoring high-priority security findings in GCP and notifies the right team via Slack with actionable insights. It simplifies the response to security threats, allowing for faster remediation and greater operational efficiency.
