# 2019 KAKAO INTERN
# 2. 튜플
# https://programmers.co.kr/learn/courses/30/lessons/64065

def is_num(letter):
    if 48 <= ord(letter) <= 57:
        return True
    return False


def solution(s):
    answer = []
    nums = [set()]
    s = s[1: -1]
    temp_num = ''
    for letter in s:
        if letter == '{':
            temp = set()
        elif letter == '}':
            if temp_num != '':
                temp.add(int(temp_num))
                temp_num = ''
            nums.append(temp)
        else:
            if is_num(letter):
                temp_num += letter
            else:  # letter == ','
                if temp_num != '':
                    temp.add(int(temp_num))
                    temp_num = ''
    nums.sort(key=lambda num_set: len(num_set))
    for i in range(1, len(nums)):
        temp = nums[i] - nums[i - 1]
        answer.append(list(temp)[0])
    return answer

s = "{{20,111},{111}}"
a = solution(s)
print(a)