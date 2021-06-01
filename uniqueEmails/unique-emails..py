from typing import List
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = set()
        for email in emails:
            if '+' in email[:email.index('@')]:
                email = email[0:email.index('+')]+email[email.index('@'):]
            email = email[:email.index('@')].replace('.','') + email[email.index('@'):]
            uniqueEmails.add(email)
        return len(uniqueEmails)
s = Solution()
s.numUniqueEmails(['h.e.l.l.o+sldjfskdfj@example.com'])