function solution(my_string) {
  var answer = [...my_string]
    .map((i) => i.toLowerCase())
    .sort()
    .join("");
  return answer;
}

/*
[풀이 일자] : 2024.04.03
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : -
[문제 풀이] : 스프레드 연산자를 사용하여 문자열을 배열로 바꾼뒤에, map 함수를 사용해 각 요소를 소문자로 바꾸고, sort와 join으로 다시 합친다.
[배운 점] : 아래처럼 굳이 map함수를 돌리지 않아도 문자열을 모두 소문자로 바꿔줌 (toLowerCase)를 사용하면.
*/

function solution(my_string) {
  return my_string.toLowerCase().split("").sort().join("");
}
