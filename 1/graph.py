def word_chain(words):
    graph = {}
    # Create a dictionary of words, where value for each key is a list of another words,
    # which meet condition (their first letter starts as last letter of the key word)
    for word in words:
        graph[word] = []
        for another_word in words:
            if word != another_word and word[-1] == another_word[0]:
                graph[word].append(another_word)

    # print(graph)
    longest_chain = []
    for node in graph:
        current_chain = bfs(graph, node)
        if len(current_chain) > len(longest_chain):
            longest_chain = current_chain

    print(len(longest_chain), longest_chain)


# https://favtutor.com/blogs/breadth-first-search-python
def bfs(graph, start):
    visited = [start]
    queue = [start]

    while queue:  # Creating loop to visit each node
        m = queue.pop(0)

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    # Now in visited we have a full path from start node
    # there can be however some neighbours which do not satisfy the
    # conditions of starting with the same letter as last letter of the previous word
    return remove_wrong_neighbours(visited)


def remove_wrong_neighbours(chain):
    if len(chain) > 1:
        updated_chain = [chain[-1]]
        last_correct_chain_index = len(chain) - 1
        for i in range(len(chain) - 2, -1, -1):
            current_last_char = chain[i][-1]
            previously_correct_first_char = chain[last_correct_chain_index][0]
            if current_last_char == previously_correct_first_char:
                last_correct_chain_index = i
                updated_chain.append(chain[i])

        updated_chain.reverse()
        return updated_chain
    else:
        return chain


word_chain({'goose', 'dog', 'ethanol'})
word_chain({'why', 'new', 'neural', 'moon'})
