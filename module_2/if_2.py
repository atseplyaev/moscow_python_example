
def string_validate(left_str, right_str):
    print(f"left string - {left_str}")
    print(f"right string - {right_str}")
    if not isinstance(left_str, str) or not isinstance(left_str, str):
        return 0

    if left_str == right_str:
        return 1

    if len(left_str) > len(right_str):
        return 2

    if right_str == "learn":
        return 3

    return

print(string_validate("lol", "lol"))
print(string_validate("lolk", "kek"))
print(string_validate("pytho", "learn"))
print(string_validate(None, "kek"))
print(string_validate("lol", "kek"))

