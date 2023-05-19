# given derived list, return if we can have an oringal list such that
# after the operation we get derived 
# think about the XOR tricks
# if derived comes from ori.i XOR ori.i+1, der.i XOR der.i+1 XOR der.n-1 has to equal to 0
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return reduce(operator.xor, derived)==0
