function solution(order) {
  var answer = [...order.toString().matchAll(/[3|6|9]/g)].length;
  return answer;
}

/*
[풀이 일자] : 2024.04.01
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 
[문제 풀이] : matchAll() 메서드는 정규표현식과 일치하는 모든 문자열을 배열로 반환한다.
[배운 점] : -
*/
