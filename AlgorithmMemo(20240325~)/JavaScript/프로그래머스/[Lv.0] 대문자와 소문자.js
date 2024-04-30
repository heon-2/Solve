function solution(my_string) {
  var answer = "";
  for (i = 0; i < my_string.length; i++) {
    if (my_string[i] === my_string[i].toUpperCase()) {
      answer += my_string[i].toLowerCase();
    } else {
      answer += my_string[i].toUpperCase();
    }
  }
  return answer;
}

/*
[풀이 일자] : 2024.03.27
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 
[문제 풀이] : 
[배운 점] : 파이썬에서는 ord로 대소문자를 판별했는데, 자바스크립트에서는 .toUpperCase() 메서드나 .toLowerCase() 메서드를 사용하면 된다.

*/
