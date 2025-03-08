from abc import ABC
from abc import abstractmethod
import random

from hands import rock
from hands import paper
from hands import scissors
from score import Score

CHOICES = {
    "g": rock, 
    "p": paper, 
    "c": scissors
}

class Player(ABC):
    """プレイヤーの基底クラス"""
    def __init__(self):
        self.hand = None # Handクラスのインスタンス
    
    @abstractmethod
    def choice_hand(self):
        """抽象メソッド"""
        pass


class User(Player):
    """ユーザのクラス"""

    def __init__(self):
        print("あなたの手をアルファベットで入力してください")
        super().__init__()
        self.score = Score()

    def choice_hand(self):
        """
        ユーザの手を選択するメソッド。
        妥当な手が選択されるまでループする。
        """
        choices = "".join("{}: {}\n".format(key, hand.name) for key, hand in CHOICES.items())
        choice = ""
        while choice not in CHOICES:
            choice = input("{}".format(choices)).lower()
            if choice not in CHOICES:
                print(f'{" ".join(CHOICES)} のいずれかを入力してください\n')
        self.hand = CHOICES[choice]
        


class CPU(Player):
    """コンピュータのクラス"""
    
    def choice_hand(self):
        self.hand = random.choice(list(CHOICES.values()))