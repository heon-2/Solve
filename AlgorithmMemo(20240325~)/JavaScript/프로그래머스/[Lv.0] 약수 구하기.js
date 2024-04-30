function solution(n) {
  var answer = [];
  for (i = 1; i <= n; i++) {
    if (n % i === 0) {
      answer.push(i);
    }
  }
  return answer;
}

/*
[풀이 일자] : 2024.04.14
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : -
[문제 풀이] : 단순 조건문으로 약수인지 아닌지를 확인하며 풀었다. 
[배운 점] : -
*/
