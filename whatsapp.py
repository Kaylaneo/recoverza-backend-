import os
import requests

class WhatsAppAutomation:
    def __init__(self):
        self.api_url = os.getenv('WHATSAPP_API_URL', 'https://api.whatsapp-provider.co.za/v1/messages')
        self.api_token = os.getenv('WHATSAPP_API_TOKEN', 'mock_token_za')

    def send_payment_reminder(self, phone_number, debtor_name, amount, days_overdue):
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
        
        message = (
            f"Dear {debtor_name}, this is a polite reminder from RecoverZA on behalf of your creditor. "
            f"Your account is currently {days_overdue} days overdue with an outstanding balance of R{amount:.2f}. "
            f"Please arrange payment urgently to avoid further legal action or DebiCheck re-strikes."
        )

        payload = {
            "phone": phone_number,
            "message": message
        }

        # In production, this would make an actual POST request:
        # response = requests.post(self.api_url, json=payload, headers=headers)
        # return response.json()

        print(f"[MOCK WHATSAPP SENT TO {phone_number}]: {message}")
        return {"status": "success", "recipient": phone_number}
