function solution(n) {
  let answer = 0;
  for (i = 1; i <= n; i++) {
    if (i % 2 == 0) {
      answer += i;
    }
  }

  return answer;
}
/*
[풀이 일자] : 2024.03.25
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 수학
[문제 풀이] : -
[배운 점] : 반복문 돌릴 때, n이하라고 조건이 나와있어서 n까지 돌려야하면 i <= n 이렇게 써야한다. -> i < n 과 i <= n 헷갈리지 않기.
*/
