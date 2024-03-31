function solution(price) {
  let sale = 0;
  if (price >= 100000) {
    sale += 0.05;
  }
  if (price >= 300000) {
    sale += 0.05;
  }
  if (price >= 500000) {
    sale += 0.1;
  }
  return parseInt(price * (1 - sale));
}

/*
[풀이 일자] : 2024.03.31
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 
[문제 풀이] : 단순 조건 반복문.
[배운 점] : 
*/
