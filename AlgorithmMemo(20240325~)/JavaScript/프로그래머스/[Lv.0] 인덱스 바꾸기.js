function solution(my_string, num1, num2) {
  let answer = "";
  for (i = 0; i < my_string.length; i++) {
    if (i === num1) {
      answer += my_string[num2];
    } else if (i === num2) {
      answer += my_string[num1];
    } else {
      answer += my_string[i];
    }
  }
  return answer;
}

/*
[풀이 일자] : 2024.04.09
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : -
[문제 풀이] : 인덱스가 num1일땐 원본 문자열의 num2를, num2일땐 원본 문자열의 num1을 붙여준다.
[배운 점] : 아래 코드처럼 바꿀 수도 있음. split으로 배열로 나누고, join으로 다시 붙이기.
*/

function solution(my_string, num1, num2) {
  my_string = my_string.split("");
  [my_string[num1], my_string[num2]] = [my_string[num2], my_string[num1]];
  return my_string.join("");
}
