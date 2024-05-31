class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def find_true_email(email):
            local, domain = email.split("@")
            local_no_period = local.replace(".", "")
            local_before_plus = re.sub(r'\+.*', '', local_no_period)
            return local_before_plus + "@" + domain
        
        answer = set()
        for email in emails:
            true = find_true_email(email)
            answer.add(true)
        
        return len(answer)