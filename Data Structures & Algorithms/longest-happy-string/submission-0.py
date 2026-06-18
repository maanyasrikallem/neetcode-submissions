class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        freq = {
            'a' : a,
            'b' : b,
            'c' : c
        }
        

        res = []

        heap = [(-cnt,i) for i,cnt in freq.items() if cnt>0]

        heapq.heapify(heap)

        while heap :

            cur_cnt , cur_chr = heapq.heappop(heap)        

            if len(res)>=2 and res[-1] == res[-2] == cur_chr:

                if not heap:
                    break

                nxt_cnt , nxt_chr = heapq.heappop(heap)

                res.append(nxt_chr)

                if nxt_cnt + 1 < 0 :

                    heapq.heappush(heap , (nxt_cnt+1 , nxt_chr))

                heapq.heappush(heap , (cur_cnt , cur_chr))

            else :

                res.append(cur_chr) 

                if cur_cnt+1 < 0:

                    heapq.heappush(heap , (cur_cnt+1 , cur_chr))

        return ''.join(res)

        