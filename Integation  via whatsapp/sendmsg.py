import requests

# Your API credentials
ACCESS_TOKEN = "EAATZAXGADJCUBO7Oh9BqoOdYL8B4EHx3eTVcoPMqK8g4IKy81or7KHPycuFncEwUVg97hNNUowuQCZATZCPwArgEhl4Kxtpzzcv6vjqbK9D0rwUP0JZAQg4kuaN0DZCRZBkMvBkkn5iVh4Ph4kZCc9WqLB7Gcb6s0mKqcXZCGmBeiPUgrnRhxMRfGeL5DpY0DRIuqYkKZBr2W4vnV2VIjuABMdURV0ZA1aXCJP4qyXoVZBe"
PHONE_NUMBER_ID = "9458999137546410"
RECIPIENT_PHONE = "923331345455"  # Recipient's WhatsApp number (with country code)

# API URL for sending messages
url = f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages"

# Headers for authentication
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# Message payload
data = {
    "messaging_product": "whatsapp",
    "to": RECIPIENT_PHONE,
    "type": "text",
    "text": {"body": "Hello! This is a test message from WhatsApp API."}
}

# Sending the request
response = requests.post(url, json=data, headers=headers)

# Printing API response
print(response.json())
