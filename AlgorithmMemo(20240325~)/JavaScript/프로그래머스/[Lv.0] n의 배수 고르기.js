function solution(n, numlist) {
  var answer = [];
  for (i = 0; i < numlist.length; i++) {
    if (numlist[i] % n == 0) {
      answer.push(numlist[i]);
    }
  }
  return answer;
}
/*
[풀이 일자] : 2024.03.27
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 수학
[문제 풀이] : -
[배운 점] : filter를 사용하면 더 간단하게 구현 가능. 


*/

function solution(n, numlist) {
  let answer = numlist.filter((num) => num % n === 0);
  return answer;
}
