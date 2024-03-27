function solution(n, t) {
  var answer = n * 2 ** t;
  return answer;
}

/*
[풀이 일자] : 2024.03.26
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 수학
[문제 풀이] : - 
[배운 점] : -
*/

function solution(n, t) {
  return n * Math.pow(2, t);
}

/* Math.pow(2,t) 이렇게도 가능함.*/
