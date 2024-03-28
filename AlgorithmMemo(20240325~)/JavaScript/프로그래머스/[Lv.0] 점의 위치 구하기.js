function solution(dot) {
  var answer;
  var x = dot[0];
  var y = dot[1];
  if (x > 0 && y > 0) {
    answer = 1;
  } else if (x < 0 && y > 0) {
    answer = 2;
  } else if (x < 0 && y < 0) {
    answer = 3;
  } else if (x > 0 && y < 0) {
    answer = 4;
  }
  return answer;
}

/*
[풀이 일자] : 2024.03.28
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : -
[문제 풀이] : 단순 조건문
[배운 점] : 아래 코드처럼 구조분해 할당도 가능한 것을 이해함.
*/

const [num, num2] = dot;
