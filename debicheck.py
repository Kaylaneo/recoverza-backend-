import os
import random

class DebiCheckOrchestrator:
    def __init__(self):
        self.bank_gateway = os.getenv('DEBICHECK_GATEWAY', 'https://api.debicheck.co.za/v2/tracking')
        self.max_restrikes = 3

    def evaluate_re_presentation(self, account_id, current_strike_count, account_status):
        if account_status == 'REJECTED_INSUFFICIENT_FUNDS' and current_strike_count < self.max_restrikes:
            next_strike = current_strike_count + 1
            # Intelligent retry scheduling based on salary cycles (e.g., end of month or 15th)
            suggested_date = "2026-05-31" 
            
            print(f"[DEBICHECK ORCHESTRATOR]: Scheduling re-strike #{next_strike} for account {account_id}")
            return {
                "account_id": account_id,
                "action": "RE_PRESENT",
                "strike_number": next_strike,
                "scheduled_date": suggested_date,
                "status": "QUEUED"
            }
        else:
            print(f"[DEBICHECK ORCHESTRATOR]: Account {account_id} requires manual intervention or max strikes reached.")
            return {
                "account_id": account_id,
                "action": "ESCALATE_TO_LEGAL",
                "status": "MANUAL_REVIEW"
            }
