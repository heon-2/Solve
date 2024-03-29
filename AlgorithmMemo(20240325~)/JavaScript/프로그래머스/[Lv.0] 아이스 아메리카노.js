function solution(money) {
  var answer = [];
  answer.push(Math.floor(money / 5500));
  answer.push(money % 5500);
  return answer;
}

/*
[풀이 일자] : 2024.03.29
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 
[문제 풀이] : 
[배운 점] : 단순 몫과 나눗셈.
*/
