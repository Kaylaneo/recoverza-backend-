from datetime import datetime

class SARSSection11JCompliance:
    def __init__(self):
        # Section 11(j) of the SA Income Tax Act allows a deduction for doubtful debts
        self.allowance_percentage = 0.40  # 40% allowance for general IFRS 9 compliant debt portfolios

    def calculate_doubtful_debt_allowance(self, total_outstanding_book):
        """
        Calculates the tax-deductible allowance for doubtful debts under SARS Section 11(j).
        """
        allowance_amount = total_outstanding_book * self.allowance_percentage
        
        report = {
            "regulation": "SARS Section 11(j)",
            "assessment_date": datetime.utcnow().strftime("%Y-%m-%d"),
            "total_book_value": total_outstanding_book,
            "deductible_allowance": allowance_amount,
            "status": "COMPLIANT"
        }
        
        print(f"[SARS 11(j) COMPLIANCE]: Calculated R{allowance_amount:.2f} deductible allowance.")
        return report
