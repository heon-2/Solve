function solution(array, n) {
  let small = [];
  let big = [];
  array.map((elem) => (elem > n ? big.push(elem) : small.push(elem)));
  small.sort((a, b) => a - b);
  big.sort((a, b) => a - b);
  if (small.length === 0 && big.length !== 0) {
    return big[0];
  } else if (big.length === 0 && small.length !== 0) {
    return small.at(-1);
  } else {
    let answer =
      Math.abs(small.at(-1) - n) > Math.abs(big.at(0) - n)
        ? big[0]
        : small.at(-1);
    return answer;
  }
}

/*
[풀이 일자] : 2024.04.19
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 
[문제 풀이] : 배열을 순회하며 기준값보다 큰 값 작은 값을 분리함.
이후 조건문에 따라, (기준값보다 큰 배열의 첫번째 요소)와(기준값보다 작은 배열의 마지막 요소) 중 기준값에 더 가까운 값을 리턴 
[배운 점] : 자바스크립트가 미숙해서 그런지 코드를 보며 심각함을 느꼈다.
어찌저찌 풀어내긴 했지만 언능 열심히 공부해야겠는걸?


*/

function solution(array, n) {
  array.sort((a, b) => Math.abs(n - a) - Math.abs(n - b) || a - b);
  return array[0];
}
