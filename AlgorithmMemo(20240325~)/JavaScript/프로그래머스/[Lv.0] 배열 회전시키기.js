function solution(numbers, direction) {
  if (direction === "right") {
    numbers.unshift(numbers.pop());
  } else {
    numbers.push(numbers.shift());
  }
  return numbers;
}

/*
[풀이 일자] : 2024.04.10
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 
[문제 풀이] : 
[배운 점] : 

unshift : 하나 이상의 요소를 배열 시작 부분에 추가, 변경된 배열의 새 길이를 반환.
shift : 배열의 첫 번째 요소를 제거하고 그 요소를 반환.

push : 맨 마지막에 집어넣고 변경된 배열의 `길이`
pop : 맨 마지막 요소 뽑아내기
*/
