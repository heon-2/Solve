function solution(numbers) {
  numbers.sort((a, b) => a - b);
  let answer = numbers[numbers.length - 1] * numbers[numbers.length - 2];
  return answer;
}

/*
[풀이 일자] : 2024.03.26
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 수학
[문제 풀이] : 
[배운 점] : sort((a,b)=>b-a)를 사용하면 내림차순으로 정렬할 수 있다.

*/
