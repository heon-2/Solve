function solution(numbers) {
  numbers.sort((a, b) => b - a);
  let cal1 = numbers[0] * numbers[1];
  let cal2 = numbers[numbers.length - 1] * numbers[numbers.length - 2];
  let answer = Math.max(cal1, cal2);
  return answer;
}

/*
[풀이 일자] : 2024.04.02
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 
[문제 풀이] : 
[배운 점] : 자바스크립트에서는 [-1] 이런식으로 접근이 안 됨.
그리고 sort()는 유니코드 기준으로 정렬하기 때문에, 숫자의 오름차순 정렬을 할 때는 array.sort((a,b)=>a-b); 이렇게 되어야함.
*/
