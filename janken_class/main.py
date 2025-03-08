from hands import rock
from hands import paper
from hands import scissors
from player import User
from player import CPU
from referee import Referee

CHOICES = {
    "g": rock, 
    "p": paper, 
    "c": scissors
}


def play_game():
    """じゃんけんゲームを実行する"""
    user = User()
    cpu = CPU()
    referee = Referee()
    
    while True:
        print("\nじゃんけん!!")

        while not referee.game_decided:
            # 手の選択
            user.choice_hand()
            cpu.choice_hand()

            # 手の表示
            print("あなた", user.hand.art)
            print("コンピュータ", cpu.hand.art)

            # 勝敗の判定
            referee.evaluate_judge(user, cpu)
            print("\n{}\n".format(referee.judgment_result))

        # もう一度遊ぶかの確認
        is_replay = input("再戦する場合は何かを入力してEnterキーを押してください: ")
        if not is_replay:
            user.score.show()
            print("またね!!")
            break
        else:
            referee.game_decided = False

    
if __name__ == "__main__":
    play_game()