function solution(sides) {
  var summ = sides.reduce((acc, cur) => acc + cur);
  let max_sides = Math.max(...sides);
  var answer = max_sides < summ - max_sides ? 1 : 2;
  return answer;
}

/*
[풀이 일자] : 2024.03.30
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 수학
[문제 풀이] : 단순 구현.
[배운 점] : Math.max()는 있는데, Math.sum()은 없음을 명심하자. reduce()를 사용할 것.


*/
