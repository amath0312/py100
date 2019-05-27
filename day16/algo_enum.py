

def how_many_fishes():
    # A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
    # 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
    # B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
    # 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼

    fish = 1
    while True:
        total = fish
        is_enough = True
        for i in range(5):
            if (total - 1) % 5 == 0:
                total = (total - 1) // 5 * 4
            else:
                is_enough = False
                break
        if is_enough:
            return fish
        else:
            fish = fish+1
    
def main():
    print(how_many_fishes())

if __name__ == '__main__':
    main()
    
