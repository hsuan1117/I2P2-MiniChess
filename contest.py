# for all in baselines
import os
import subprocess

result = []
os.system("make clean")
os.system("make")
files = [file for file in os.listdir('./contest')]
for i in range(len(files)):
    for j in range(i + 1, len(files)):
        player1 = files[i]
        player2 = files[j]
        print(f'\n=== Testing {player1} vs {player2} ===')
        if "Player1 wins" in subprocess.check_output([
            # '/bin/echo',
            './build/main',
            f"./contest/{player1}",
            f"./contest/{player2}"
        ]).decode("utf-8"):
            result.append((player1, player2, f"{player1}贏了 {player2}輸了"))
            print(f"{player1}贏了 {player2}輸了")
        else:
            result.append((player1, player2, f"{player2}贏了 {player1}輸了"))
            print(f"{player2}贏了 {player1}輸了")
        print()

        print(f'\n=== Testing {player2} vs {player1} ===')
        if "Player1 wins" in subprocess.check_output([
            # '/bin/echo',
            './build/main',
            f"./contest/{player2}",
            f"./contest/{player1}"
        ]).decode("utf-8"):
            result.append((player2, player1, f"{player2}贏了 {player1}輸了"))
            print(f"{player2}贏了 {player1}輸了")
        else:
            result.append((player2, player1, f"{player1}贏了 {player2}輸了"))
            print(f"{player1}贏了 {player2}輸了")
        print()

print('\n=== Result ===')
with open("gamelog.txt", "a") as file:
    counter = 0
    for r in sorted(result, key=lambda x: (x[0], x[1])):
        print(f'{r[0]} vs {r[1]}: {r[2]}')
        file.write(f'{r[0]} vs {r[1]}: {r[2]}\n')
        counter += 1
        if counter % 4 == 0:
            print()
            file.write(f'\n')
