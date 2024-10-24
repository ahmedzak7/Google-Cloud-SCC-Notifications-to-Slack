import base64
import json
import requests

# Replace with your actual Slack token
TOKEN = "add-your-slack-token-here"

def send_slack_chat_notification(event, context):
    # Decode the Pub/Sub message and parse it
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    message_json = json.loads(pubsub_message)
    
    # Print the entire payload for debugging
    print("Payload received:", json.dumps(message_json, indent=4))

    # Extract the finding from the payload
    finding = message_json.get('finding', {})
    
    # Extract project details from the resource section of the payload
    resource = message_json.get('resource', {})
    gcp_metadata = resource.get('gcpMetadata', {})
    
    # Extract project name and project ID
    project_name = gcp_metadata.get('projectDisplayName', 'Unknown Project')
    project_id = gcp_metadata.get('project', 'Unknown Project ID').split('/')[-1]

    # Extract next steps from the finding
    next_steps = finding.get('nextSteps', 'No next steps provided.')

    # Extract severity and assign the appropriate emoji
    severity = finding.get('severity', 'N/A')
    if severity == 'HIGH':
        severity_emoji = ":warning:"  # Yellow warning emoji
    elif severity == 'CRITICAL':
        severity_emoji = ":rotating_light:"  # Red alert emoji
    else:
        severity_emoji = ""

    # Send a message to Slack with the extracted details
    response = requests.post("https://slack.com/api/chat.postMessage", data={
        "token": TOKEN,
        "channel": "#scc_findings_alerts",
        "text": (
            f"A {severity} severity finding {severity_emoji} '{finding.get('category', 'Unknown Category')}' "
            f"was detected!\n"
            f"Project Name: {project_name}\n"
            f"Project ID: {project_id}\n"
            f"Next Steps: {next_steps}"
        )
    })

    # Log the response from Slack for debugging
    print("Slack response:", response.text)
