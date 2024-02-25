def main():
    # 1

    def groundhog_day(strings):
        for i in range(1, len(strings)):
            diff_count = sum([1 for j in range(len(strings[i])) if strings[i][j] != strings[i - 1][j]])
            if diff_count > 2:
                diff_indices = [j for j in range(len(strings[i])) if strings[i][j] != strings[i - 1][j]]
                return (i, diff_indices)

        return (0, 0)

    strings = ["abcde", "abxde", "xxxyz", "xyzxy"]
    result = groundhog_day(strings)
    print(result)

    # 2
    def gears(gears_list, n, m):
        for gear1 in gears_list:
            for gear2 in gears_list:
                if gear1 != gear2 and gear1[0] / gear1[1] == n / m and gear2[0] / gear2[1] == n / m:
                    return gear1, gear2
        return (None, None)

    gears_list = [[20, 5], [30, 8], [25, 6], [40, 10]]
    n = 4
    m = 1

    result = gears(gears_list, n, m)
    if result != (None, None):
        print("Найдены подходящие шестерёнки:", result)
    else:
        print("Подходящие шестерёнки не найдены.")


if __name__ == "__main__":
    main()
