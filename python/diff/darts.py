def discover_shortest_path(outstanding_score, path, shortest_path_length):

    # if score is reduced to 0, return full path
    if outstanding_score == 0:
        return [path]

    # if the path has been longer than the shortest path, abort it and return an empty list
    if len(path) > shortest_path_length:
        return []

    paths = []

    # try all possiblities of different scores
    for base_score in [50, 25, 3, 2, 1]:

        count = outstanding_score // base_score

        if count < 1:
            continue

        if base_score in [50, 25]:  # when it's bull and outer
            count = min(1, count)
            description = "bull" if base_score == 50 else "outer"
            path.append({"score": base_score, "name": description})
        else:
            count = min(20, count)
            prefix = "s"
            if base_score == 3:
                prefix = "t"
            elif base_score == 2:
                prefix = "d"
            path.append({"score": base_score * count, "name": prefix + str(count)})

        # process the next throw
        visited_paths = discover_shortest_path(
            outstanding_score - base_score * count,
            path,
            shortest_path_length,
        )
        print('visited_paths:{}'.format(visited_paths))

        for p in visited_paths:
            path_length = len(p)
            if 1 <= path_length <= shortest_path_length:
                # save the path if its length is no larger than shortest length
                paths.append(sorted(p, key=lambda x: x["score"], reverse=True))
                # if find the new shortest length, use it for the next search
                if path_length < shortest_path_length:
                    shortest_path_length = path_length

        path.pop()

    return paths


def find_min_throws(score):

    throws = discover_shortest_path(score, [], score)

    # get the combination with the least throws
    min_throw_count = min([len(t) for t in throws])
    min_throws = [t for t in throws if len(t) == min_throw_count]
    print('min_throws:{}'.format(min_throws))

    # sort throws by the highest score in each throw
    filtered_throws = min_throws
    for i in range(min_throw_count):
        max_score = max(t[i]["score"] for t in filtered_throws)
        filtered_throws = [t for t in filtered_throws if t[i]["score"] == max_score]

    response = [i["name"] for i in filtered_throws[0]]
    return response


if __name__ == "__main__":
    # print(find_min_throws(161))
    # print(find_min_throws(170))
    print(find_min_throws(148))
