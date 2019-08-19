def is_over_100(score, goal_score):
        return score >= goal_score

def lose(score, lose_score):
        if score - lose_score < 0:
                return 0
        return score - lose_score

def play_game(N, win_score, lose_score, goal_score):
        score = 0
        for _ in range(N):
                name = input()
                if name in win_name:
                        score += win_score
                        if is_over_100(score, goal_score):
                                print("I AM NOT IRONMAN!!")
                                return
                else:
                        score = lose(score, lose_score)
        print("I AM IRONMAN!!")
        return


win_name = []
N, P = map(int, input().split())
win_score, lose_score, goal_score = map(int, input().split())
for _ in range(P):
        name, result = input().split()
        if result == "W":
                win_name.append(name)

play_game(N, win_score, lose_score, goal_score)