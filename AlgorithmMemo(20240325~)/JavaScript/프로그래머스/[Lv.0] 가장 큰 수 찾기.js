function solution(array) {
  let max_number = Math.max(...array);
  return [max_number, array.indexOf(max_number)];
}

/*
[풀이 일자] : 2024.03.27
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 
[문제 풀이] : Math.max로 최댓값을 찾고, indexOf로 인덱스를 찾음.
[배운 점] : -
*/
