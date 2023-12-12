class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.token =defaultdict(int)
        self.live = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.token[tokenId] = currentTime + self.live

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.token and self.token[tokenId]> currentTime:
            self.token[tokenId] = currentTime + self.live

    def countUnexpiredTokens(self, currentTime: int) -> int:
        answer = 0 
        for token in self.token:
            if self.token[token]> currentTime:
                answer += 1
        return answer


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)