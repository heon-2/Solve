// 첫 풀이 -> 시간초과
function solution(n) {
  var answer = 0;
  for (i = 1; i < n + 1; i++) {
    for (j = 1; j < n + 1; j++) {
      if (i * j === n) {
        answer += 1;
      }
    }
  }
  return answer;
}

// 두 번째 풀이
function solution(n) {
  let answer = 0;
  let factors = [];
  for (i = 1; i < n + 1; i++) {
    if (n % i === 0) {
      factors.push(i);
    }
  }
  for (i = 0; i < factors.length; i++) {
    for (j = 0; j < factors.length; j++) {
      if (factors[i] * factors[j] === n) {
        answer += 1;
      }
    }
  }
  return answer;
}

/*
[풀이 일자] : 2024.03.29
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 수학
[문제 풀이] : 곱해서 n이란 숫자가 나오는 순서쌍은 n의 약수들이므로, 약수를 구한 후 2중 for문을 사용해 찾는다.
[배운 점] : 이런 기초적인 문제도 자바스크립트로 다시 풀려고 하니깐, 시간 복잡도를 놓치게 된다. 레벨 0이라 너무 방심했나
*/
