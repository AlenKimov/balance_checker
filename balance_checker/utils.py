def cut_list(lst: list, n) -> list[list]:
    return [lst[i:i+n] for i in range(0, len(lst), n)]