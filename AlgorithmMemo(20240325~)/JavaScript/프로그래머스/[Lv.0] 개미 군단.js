function solution(hp) {
  let ants = hp;
  let answer = 0;
  if (ants >= 5) {
    answer += parseInt(ants / 5);
    ants = ants % 5;
  }
  if (ants >= 3) {
    answer += parseInt(ants / 3);
    ants = ants % 3;
  }
  if (ants >= 1) {
    answer += ants;
  }
  return answer;
}

/*
[풀이 일자] : 2024.03.27
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 
[문제 풀이] : 
[배운 점] : 그리디와 유사한 단순 조건 문제.

*/
