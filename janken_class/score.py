class Score:
    def __init__(self):
        self.win = 0
        self.lose = 0
    
    def increment_win(self):
        self.win += 1
    
    def increment_lose(self):
        self.lose += 1
    
    def show(self):
        print("あなたの成績は {}勝 {}敗 でした".format(self.win, self.lose))