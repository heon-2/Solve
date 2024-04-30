function solution(my_string, letter) {
  var answer = my_string.replaceAll(letter, "");
  return answer;
}

/*
[풀이 일자] : 2024.03.30
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 수학
[문제 풀이] : -
[배운 점] : replace를 사용하면 맨 처음만 대체되고, replaceAll()을 사용하면 모두 대체
*/
