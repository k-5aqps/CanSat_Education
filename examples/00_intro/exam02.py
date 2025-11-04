print("グー，チョキ，パーを入力")
a = input("A:")
b = input("B:")

if a == "グー":
    if b == "グー":
        winner = "引き分け"
    elif b == "チョキ":
        winner = "Aさん"
    elif b == "パー":
        winner = "Bさん"
elif a == "チョキ":
    if b == "グー":
        winner = "Bさん"
    elif b == "チョキ":
        winner = "引き分け"
    elif b == "パー":
        winner = "Aさん"
elif a == "パー":
    if b == "グー":
        winner = "Aさん"
    elif b == "チョキ":
        winner = "Bさん"
    elif b == "パー":
        winner = "引き分け"

if winner != "引き分け":
    print(f"判定結果 >>> {winner}の勝ち")
else:
    print(f"判定結果 >>> {winner}")