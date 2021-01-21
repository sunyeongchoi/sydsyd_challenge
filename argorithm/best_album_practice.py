from collections import defaultdict
from operator import itemgetter


def solution(genres, plays):
    genre_play_dict = defaultdict(lambda: 0)
    for genre, play in zip(genres, plays):
        genre_play_dict[genre] += play

    genre_rank = [genre for genre, play in sorted(genre_play_dict.items(), key=itemgetter(1), reverse=True)]
    print(genre_rank)

    final_dict = defaultdict(lambda: [])
    print(final_dict)
    for i, genre_play_tuple in enumerate(zip(genres, plays)):
        print(genre_play_tuple)
        final_dict[genre_play_tuple[0]].append((genre_play_tuple[1], i))
    print(final_dict)

    answer = []
    for genre in genre_rank:
        one_genre_list = sorted(final_dict[genre], key=itemgetter(0), reverse=True)
        print(one_genre_list)
        if len(one_genre_list) > 1:
            answer.append(one_genre_list[0][1])
            answer.append(one_genre_list[1][1])
        else:
            answer.append(one_genre_list[0][1])

    return answer


if __name__ == '__main__':
    real_answer = solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500])
    print(real_answer)
