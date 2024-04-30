function solution(n, k) {
  var answer = 0;
  answer = n * 12000 + k * 2000 - Math.floor(n / 10) * 2000;
  return answer;
}

/*
[풀이 일자] : 2024.03.26
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 수학
[문제 풀이] : -
[배운 점] : Math.floor() 함수를 사용하여 소수점 이하를 버리는 것을 자꾸 까먹는다.
파이썬의 // 가 너무 익숙해서 그런가.

또한 parseInt도 가능.
*/
