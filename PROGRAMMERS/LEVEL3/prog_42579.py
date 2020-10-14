# PROGRAMMERS LEVEL 3
# 베스트앨범
# https://programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    n = len(genres)
    answer = []
    songs = []
    genre_count = {}
    for i in range(n):
        genre = genres[i]
        play = plays[i]
        songs.append((i, genre, play))
        if genre not in genre_count.keys():
            genre_count[genre] = play
        else:
            genre_count[genre] += play

    songs.sort(key=lambda song: (-genre_count[song[1]], -song[2]))

    for song in songs:
        if genre_count[song[1]] > 0:
            answer.append(song[0])
            genre_count[song[1]] = 0
        elif genre_count[song[1]] == 0:
            answer.append(song[0])
            genre_count[song[1]] = -1
        else:
            continue
    return answer

genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [500, 600, 150, 800, 2500]
a = solution(genres, plays)
print(a)