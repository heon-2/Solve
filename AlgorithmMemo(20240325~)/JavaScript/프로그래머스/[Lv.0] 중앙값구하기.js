function solution(array) {
  let answer;
  array.sort((a, b) => a - b);
  const median = parseInt(array.length / 2);
  return array[median];
}

/*
[풀이 일자] : 2024.03.26
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 수학
[문제 풀이] : -
[배운 점] : 자바스크립트의 sort()는 놀랍게도 유니코드 기준으로 배열을 정렬하기때문에,
숫자의 오름차순 정렬을 할 때는 array.sort((a,b)=>a-b); 이렇게 되어야함.
*/

function solution(age) {
  age = 20;
  if (0 < age < 100) {
    console.log(1);
  } else {
    console.log(2);
  }
}
