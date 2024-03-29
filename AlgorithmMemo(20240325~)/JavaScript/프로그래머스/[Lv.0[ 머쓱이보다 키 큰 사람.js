function solution(array, height) {
  var answer = 0;
  for (i = 0; i < array.length; i++) {
    if (array[i] > height) {
      answer += 1;
    }
  }
  return answer;
}
/*
[풀이 일자] : 2024.03.29
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 수학
[문제 풀이] : 
[배운 점] : - 
*/
