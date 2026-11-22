"""DA39 reference: Accounts merge by shared email. Open after your own attempt."""
def solve(accounts):
    parent, name = {}, {}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for acc in accounts:
        for email in acc[1:]:
            parent.setdefault(email, email)
            name[email] = acc[0]
            ra, rb = find(acc[1]), find(email)
            if ra != rb:
                parent[rb] = ra
    groups = {}
    for email in parent:
        groups.setdefault(find(email), []).append(email)
    merged = [[name[root]] + sorted(emails) for root, emails in groups.items()]
    return sorted(merged, key=lambda m: m[1])
