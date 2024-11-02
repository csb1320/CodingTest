const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [n, m] = input[0].split(' ').map(Number);
const trees = input[1].split(' ').map(Number);

// 이진 탐색을 위한 시작점, 끝점
let start = 0;
let end = Math.max(...trees);

let result = 0;
while (start <= end) {
    let total = 0; // 가져갈 나무의 길이
    const mid = Math.floor((start + end) / 2); // 절단기 높이
    
    for (let i = 0; i < trees.length; i++) {
        if (trees[i] > mid) { // 절단기보다 주어진 나무가 길면 자른 나머지를 total에 추가
            total += trees[i] - mid;
        }
    }
    
    // 이분 탐색
    if (total < m) { // 가져가야 하는 길이 m보다 작은 길이이면
        end = mid - 1; // mid 기준 왼쪽 부분 탐색
    } else { // 가져가야 하는 길이 m보다 크거나 같으면
        result = mid; // 절단기 높이를 mid로 설정
        start = mid + 1; // mid 기준 오른쪽 부분 탐색
    }
}

console.log(result);