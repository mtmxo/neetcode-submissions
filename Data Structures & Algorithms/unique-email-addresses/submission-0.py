class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        valid = set()

        for j in emails:
            local, domain = j.split('@')
            local = local.replace('.', '')
            local = local.split('+')[0]
            valid.add(f'{local}@{domain}')

        return len(valid)