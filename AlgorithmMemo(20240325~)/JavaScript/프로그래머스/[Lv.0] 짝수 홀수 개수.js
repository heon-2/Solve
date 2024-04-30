function solution(num_list) {
  let even = 0;
  let odd = 0;
  num_list.filter((i) => (i % 2 === 0 ? (even += 1) : (odd += 1)));
  return [even, odd];
}

/*
[풀이 일자] : 2024.03.30
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 수학
[문제 풀이] : -
[배운 점] : filter() + 삼항연산을 썼는데 된다는 걸 알았다.
*/
