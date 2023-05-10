def coincidence(lst=None, rng=None):
    result = []
    if lst is None or rng is None:
        return result
    listed_rng = list(rng)
    listed_rng = [i for i in range(listed_rng[0] * 10, (listed_rng[-1] + 1) * 10)]
    for elem in lst:
        if isinstance(elem, (int, float)) and elem * 10 in listed_rng:
            result.append(elem)
    return result