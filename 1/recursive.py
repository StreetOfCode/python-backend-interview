def permutation(words):
    if len(words) <= 1:
        return [words]

    current_permutation = []

    for i, word in enumerate(words):
        remaining_words = words[:i] + words[i + 1:]
        for perm in permutation(remaining_words):
            current_permutation.append([word] + perm)
    return current_permutation


def get_valid_chain(words):
    if len(words) <= 1:
        return words

    for i in range(1, len(words)):
        if words[i][0] != words[i - 1][-1]:
            return words[:i]

    return words


def word_chain(words):
    longest_chain = []
    for perm in permutation(words):
        valid_chain = get_valid_chain(perm)
        if len(valid_chain) > len(longest_chain):
            longest_chain = valid_chain

    print(len(longest_chain), longest_chain)


word_chain(["dog", "ethanol", "goose"])
word_chain(["why", "new", "neural", "moon"])
