# 2018 KAKAO BLIND
# [3차] 방금그곡
# https://programmers.co.kr/learn/courses/30/lessons/17683

import re


def sound(melody):
    result = ''
    sharp_check = re.compile('[A-G]#?')
    melody = sharp_check.findall(melody)
    for pitch in melody:
        if len(pitch) == 2:
            result += pitch[0].lower()
        else:
            result += pitch
    return result

def duration(t1, t2):
    h1, m1 = map(int, t1.split(':'))
    h2, m2 = map(int, t2.split(':'))
    return 60 * (h2 - h1) + (m2 - m1)

def make_song(time, melody):
    result = ''
    for i in range(time):
        result += melody[i%len(melody)]
    return result

def solution(m, musicinfos):
    answer = ''
    max_music_time = -1
    m = sound(m)
    for musicinfo in musicinfos:
        music = musicinfo.split(',')
        music_time = duration(music[0], music[1])
        music_title = music[2]
        music_melody = make_song(music_time, sound(music[3]))

        if (music_melody.find(m) != -1) and (music_time > max_music_time):
            max_music_time = music_time
            answer = music_title

    if max_music_time == -1:
        answer = '(None)'
    return answer

m = "ABCDEFG"
musicinfos = ['12:00,12:14,HELLO,CDEFGAB', '13:00,13:05,WORLD,ABCDEF']
a = solution(m, musicinfos)
print(a)