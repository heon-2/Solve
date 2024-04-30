function solution(array, n) {
  let filter_array = array.filter((i) => i === n);
  return filter_array.length;
}
/*
[풀이 일자] : 2024.03.31
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 
[문제 풀이] : 
[배운 점] : 자바스크립트 배열에서 특정 요소가 몇개 들어있는지를 확인하려면 filter를 사용해 새 배열을 반환하고,
그 배열의 길이가 정답이 된다.
*/
