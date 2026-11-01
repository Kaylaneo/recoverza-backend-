import os
import requests

class PayShapRTP:
    def __init__(self):
        self.gateway_url = os.getenv('PAYSHAP_GATEWAY_URL', 'https://api.psd.interbank.co.za/v1/rtp')
        self.api_key = os.getenv('PAYSHAP_API_KEY', 'mock_payshap_key_za')

    def initiate_rtp_request(self, debtor_phone, amount, reference):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "X-Country": "ZA"
        }
        
        payload = {
            "proxy_id": debtor_phone,
            "proxy_type": "MSISDN",
            "amount": f"{amount:.2f}",
            "currency": "ZAR",
            "reference": reference
        }

        # In production, this sends a Request-to-Pay (RTP) to the debtor's banking app:
        # response = requests.post(self.gateway_url, json=payload, headers=headers)
        # return response.json()

        print(f"[MOCK PAYSHAP RTP SENT]: R{amount:.2f} requested from proxy {debtor_phone} with ref {reference}")
        return {
            "status": "INITIATED",
            "transaction_id": "PS-RTP-987654321",
            "amount": amount,
            "reference": reference
        }
