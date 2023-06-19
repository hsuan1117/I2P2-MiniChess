# for all in baselines
import os
import subprocess

result = []
os.system("make clean")
os.system("make")
for baseline in os.listdir('./baselines/mac-arm'):
    if not os.path.isdir(baseline):
        for player in os.listdir('./build'):
            if not os.path.isdir(player) and player.startswith('player_'):
                print(f'\n=== Testing {player} vs {baseline} ===')
                if "Player1 wins" in subprocess.check_output([
                    './build/main',
                    f"./build/{player}",
                    f"./baselines/mac-arm/{baseline}"
                ]).decode("utf-8"):
                    result.append((player, baseline, True))
                    print('✅ 驗證成功')
                else:
                    result.append((player, baseline, False))
                    print('❌ 驗證失敗')
                print()

                print(f'\n=== Testing {baseline} vs {player} ===')
                if "Player2 wins" in subprocess.check_output([
                    './build/main',
                    f"./baselines/mac-arm/{baseline}",
                    f"./build/{player}"
                ]).decode("utf-8"):
                    result.append((baseline, player, True))
                    print('✅ 驗證成功')
                else:
                    result.append((baseline, player, False))
                    print('❌ 驗證失敗')
                print()

print('\n=== Result ===')
counter = 0
for r in sorted(result, key=lambda x: (x[0] if x[1].startswith('p') else x[1], x[0] if x[0].startswith('p') else x[1])):
    print(f'{r[0].split("/")[-1]} vs {r[1].split("/")[-1]}: {"✅" if r[2] else "❌"}')
    counter += 1
    if counter % 2 == 0:
        print()
