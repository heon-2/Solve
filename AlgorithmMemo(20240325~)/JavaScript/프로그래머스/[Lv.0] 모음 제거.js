function solution(my_string) {
  return my_string.replace(/a|e|i|o|u/gi, "");
}

/*
[풀이 일자] : 2024.03.31
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 
[문제 풀이] : 정규 표현식을 사용하여 my_stirng에서 모음을 제거.
[배운 점] :/a|e|i|o|u/ 이 부분은 정규 표현식. -> 모음 중 하나를 찾아.
gi 중 g는 global의 약자로 문자열 전체에서 일치하는 사례를 찾기. 원래 replace 가 맨 처음만 찾고 끝내는데, g를 쓰면 문자열 모두 순환 가능.
i는 case-insensitive를 의미. -> 즉, 대소문자를 구분하지 않고 찾는다는 의미. 
*/

function solution(my_string) {
  return my_string.replace(/[aeiou]/gi, "");
}

// 이렇게 정규표현식을 괄호로 적어도 됨. 캡처링이라고 함.
