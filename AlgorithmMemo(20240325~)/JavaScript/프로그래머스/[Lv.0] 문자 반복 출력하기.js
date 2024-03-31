function solution(my_string, n) {
  var answer = "";
  for (i = 0; i < my_string.length; i++) {
    for (j = 0; j < n; j++) {
      answer += my_string[i];
    }
  }
  return answer;
}

/*
[풀이 일자] : 2024.03.31
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 
[문제 풀이] : 2중 for문으로 풀이하기.
[배운 점] : repeat() 연산자를 사용하면 문자열을 반복할 수 있음.
*/

function solution(my_string, n) {
  var answer = "";
  for (i = 0; i < my_string.length; i++) {
    answer += my_string[i].repeat(n);
  }
  return answer;
}
// 이렇게도 풀이 가능.
