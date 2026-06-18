class Solution:
    def reorganizeString(self, s: str) -> str:

        freq = Counter(s)

        heap = [(-cnt , i) for i , cnt in freq.items()]

        heapq.heapify(heap)

        res = ''

        prev_cnt , prev_chr = 0 , ''

        while heap :

            neg_count , i = heapq.heappop(heap) 
            res += i 
            neg_count += 1

            if prev_cnt < 0:
                heapq.heappush(heap , (prev_cnt , prev_chr))

            prev_cnt , prev_chr = neg_count , i


        if len(res) == len(s) :
            return res
        else:
            return ''

                



        