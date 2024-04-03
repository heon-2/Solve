function solution(my_string) {
  return [...new Set(my_string)].join("");
}

/*
[풀이 일자] : 2024.04.03
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : -
[문제 풀이] : Set을 이용해 중복 제거
[배운 점] : ...new Set()을 사용하면 중복을 제거할 수 있음. my_string이란 문자열을 미리 스프레드 연산으로 분리할 필요 없이, 바로 new Set 생성자 함수를 사용하면 됨.

*/
