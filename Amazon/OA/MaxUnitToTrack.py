class MaxUnit2Track:
    def sol(self, input, T):
        input.sort(key=lambda x : x[1], reverse=True)
        ans = 0
        for b, u in input:
            if T == 0:
                return ans
            bs = min(b, T)
            ans += bs * u
            T -= bs
        return ans
    def sol_greedy(self, input, T):
        arr = [0] * 1001
        ans = 0
        for b in input:
            arr[b[1]] = b[0]
        for u in range(1000, 0, -1):
            bs = min(arr[u], T)
            ans += bs * u
            T -= bs
        return ans
test = MaxUnit2Track()
# print(test.sol([[1,3], [2,2], [3,1]], 4))
print(test.sol_greedy([[1,3], [2,2], [3,1]], 4))