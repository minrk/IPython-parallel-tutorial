def ngrams_parallel(view, fnames, n=1):
    """Compute ngrams in parallel
    
    view - An IPython DirectView
    fnames - The filenames containing the split data.
    """

    ar = view.map_async(ngrams, fnames, [n] * len(fnames))
    counts = {}
    for engine_count in ar:
        for gram, count in engine_count.items():
            if gram not in counts:
                counts[gram] = 0
            counts[gram] += count
    return counts
