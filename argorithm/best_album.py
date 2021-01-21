from collections import defaultdict


def solution(genres, plays):
    answer = []
    # 장르별 재생횟수 합계 구한 뒤 내림차순 정렬
    genre_play_dict = defaultdict(lambda: 0)
    for genre, play in zip(genres, plays):
        genre_play_dict[genre] += play
    sorted_genre_play_dict = sorted(genre_play_dict.items(), key=lambda x: x[1], reverse=True)

    # 장르별 재생횟수 내림차순
    genre_play_list_dict = defaultdict(lambda: [])
    for index, genre_play_tuple in enumerate(zip(genres, plays)):
        genre_play_list_dict[genre_play_tuple[0]].append((index, genre_play_tuple[1]))

    for genre in sorted_genre_play_dict:
        answer += (sorted(genre_play_list_dict[genre[0]], key=lambda x: x[1], reverse=True)[:2])
    return [x[0] for x in answer]


if __name__ == '__main__':
    real_answer = solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500])
    print(real_answer)
