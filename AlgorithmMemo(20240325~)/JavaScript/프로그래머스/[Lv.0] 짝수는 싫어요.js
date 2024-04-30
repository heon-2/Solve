function solution(n) {
  var answer = [];
  for (i = 1; i <= n; i++) {
    if (i % 2 !== 0) {
      answer.push(i);
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
[배운 점] : 사실 if문을 쓰지 않고도 풀이가 가능함. 아래처럼
*/

function solution(n) {
  var answer = [];

  for (let i = 1; i <= n; i += 2) answer.push(i);

  return answer;
}
