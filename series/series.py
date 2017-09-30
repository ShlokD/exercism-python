def slices(sequence, slice):
    if not sequence or slice > len(sequence) or slice == 0:
        raise ValueError('Invalid slice ')

    series = []
    for i in range(0, len(sequence) - slice + 1):
        series.append(list(map(int, list(sequence[i : i + slice]))))

    return series