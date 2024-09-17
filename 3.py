def restore_password(history: str, alpha: str, max_len: int):
    if len(history) < len(alpha):
        return -1

    alpha = set(alpha)

    current = len(history) - 1
    end_index = len(history)

    required_symbs_stats = {s: 0 for s in set(alpha)}

    while current >= 0:
        if history[current] not in alpha:
            end_index = current
            current = current - 1

            required_symbs_stats = {s: 0 for s in set(alpha)}
            continue

        required_symbs_stats[history[current]] += 1

        if end_index - current > max_len:
            try:
                if required_symbs_stats[history[end_index]]:
                    required_symbs_stats[history[end_index]] -= 1
            except IndexError:
                pass  # handle end_index == len(history)
            end_index -= 1

        if all(value > 0 for value in required_symbs_stats.values()):
            return history[current:end_index]

        current -= 1
    return -1


# print(restore_password(history="abacaba", alpha="abc", max_len=4))
# print(restore_password(history="abacaba", alpha="abc", max_len=3))
# print(restore_password(history="abacxxabcdx", alpha="abcd", max_len=5))
# print(restore_password(history="abcdefghigk", alpha="abcdefghigk", max_len=30))
# print(restore_password(history="asbcdefghigk", alpha="abcdefghigk", max_len=30))
# print(restore_password(history="xabcccxaccxbx", alpha="abc", max_len=50))
print(restore_password(input(), input(), int(input())))
