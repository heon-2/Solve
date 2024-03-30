function solution(my_string) {
  var answer = my_string.split("").reverse().join("");
  return answer;
  // var answer = [...my_string].reverse().join('')
}

/*
[풀이 일자] : 2024.03.30
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 
[문제 풀이] : 
[배운 점] : 문자열을 리스트로 만들어서 reverse() 메서드를 사용하면 된다.
[...my_string] 이란 스프레드 문법을 활용하면 된다.
*/
