from icecream import ic
def compress(chars) -> int:
    char_len_map = dict()
    for element in chars:
        size = char_len_map.get(element, 0)
        char_len_map[element] = size + 1
    total_length = []
    for key, value in char_len_map.items():
        if value > 1:
            total_length.extend([key, str(value)])

        else:
            total_length.append(key)
    ic(total_length)
    return len(''.join(total_length))
if __name__ == "__main__":
    print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))