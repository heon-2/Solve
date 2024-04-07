function solution(num, k) {
  var answer;
  try {
    answer =
      num
        .toString()
        .split("")
        .findIndex((e) => e == k) + 1;
  } finally {
    return answer === 0 ? -1 : answer;
  }
}

/*
[풀이 일자] : 2024.04.07
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : -
[문제 풀이] : findIndex를 통해 일치하는 것을 확인하기
[배운 점] : findIndex((e) => e ) 이런 형태로 사용해야 하고, 만약 없다면 에러가 아니라 -1을 반환함.
*/
