from hands import rock
from hands import paper
from hands import scissors

class Referee:
    """勝敗を判定するクラス"""

    winning_combinations = {
        # 勝ち手:負け手
        rock: scissors, 
        scissors: paper, 
        paper: rock
    }

    def __init__(self):
        self.game_decided = False
        self.judgment_result = ""

    @classmethod
    def _is_user_judge(cls, user_hand, cpu_hand):
        return cls.winning_combinations[user_hand] == cpu_hand

    def evaluate_judge(self, user, cpu):
        """じゃんけんの勝敗を判定する"""
        if user.hand == cpu.hand:
            self.game_decided = False
            self.judgment_result = "あいこ"
        elif self._is_user_judge(user.hand, cpu.hand):
            user.score.increment_win()
            self.game_decided = True
            self.judgment_result = "勝ち"
        else:
            user.score.increment_lose()
            self.game_decided = True
            self.judgment_result = "負け"