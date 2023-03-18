class BrowserHistory:
    def __init__(self, homepage: str):
        self.p, self.end = 0, 0
        self.history = [homepage]

    def visit(self, url: str) -> None:
        self.p += 1
        if len(self.history) == self.p:
            self.history.append(None)
        self.history[self.p] = url
        self.end = self.p

    def back(self, steps: int) -> str:
        self.p = max(0, self.p - steps)
        return self.history[self.p]

    def forward(self, steps: int) -> str:
        self.p = min(self.end, self.p + steps)
        return self.history[self.p]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
