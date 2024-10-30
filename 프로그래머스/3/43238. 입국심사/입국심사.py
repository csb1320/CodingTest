def solution(n, times):
    left, right = 1, max(times) * n  # 최소 시간, 최대 시간 설정
    answer = right

    while left <= right:
        mid = (left + right) // 2
        total = sum(mid // time for time in times)  # 주어진 시간 동안 심사 가능한 총 인원 수 계산

        if total >= n:  # 모든 사람이 심사를 받을 수 있다면
            answer = mid
            right = mid - 1  # 더 작은 시간으로 탐색
        else:  # 심사를 받기 부족한 경우
            left = mid + 1  # 더 큰 시간으로 탐색

    return answer

