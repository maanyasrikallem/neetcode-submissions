class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        parent = {}
        email_to_name = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a,b):
            pa = find(a)
            pb = find(b)

            if pa != pb :
                parent[pa] = pb 

        for account in accounts:
            name = account[0]
            first_email = account[1]

            for email in account[1:]:
                
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name

                union(first_email , email)

        groups = defaultdict(list)

        for email in parent :
            root = find(email)
            groups[root].append(email)    

        res = []    

        for root , emails in groups.items():
            res.append([email_to_name[root]] + sorted(emails))

        return res 


                


        