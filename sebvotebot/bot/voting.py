class Voting:
    def __init__(self, options):
        self.options = options
        self.scores = {}
        self.clear()

    def clear(self):
        for option in self.options:
            self.scores.update({ option: 0 })

    def vote(self, option):
        print(option)
        if option in self.scores:
            self.scores[option] += 1
            print(self.scores)
            return True
        else:
            return False

    def result(self):
        res =  max(self.scores, key=self.scores.get)
        if self.scores[res] == 0:
            return None
        return res
