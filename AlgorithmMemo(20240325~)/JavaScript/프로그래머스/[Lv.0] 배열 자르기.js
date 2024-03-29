function solution(numbers, num1, num2) {
  var answer = [];
  answer = numbers.slice(num1, num2 + 1);
  return answer;
}

/*
[풀이 일자] : 2024.03.29
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 수학
[문제 풀이] : 
[배운 점] : .slice()로 배열 자르기. 말 그대로 자르기. 

자바스크립트 Array.prototype
slice 는 배열을 얕은 복사 해서 새로운 배열로 반환
splice 는 배열의 기존 요소를 추가, 변경, 삭제해 원본 배열을 변경

*/
