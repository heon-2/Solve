function solution(s1, s2) {
  var answer = 0;
  for (i = 0; i < s1.length; i++) {
    for (j = 0; j < s2.length; j++) {
      if (s1[i] == s2[j]) {
        answer += 1;
      }
    }
  }
  return answer;
}

/*
[풀이 일자] : 2024.03.26
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 수학
[문제 풀이] : 단순 구현.
[배운 점] : filter를 사용하면 더 간단하게 구현 가능. + includes가 있는 것을 배움.


*/
// 참고할 코드.
function solution(s1, s2) {
  const intersection = s1.filter((x) => s2.includes(x));
  return intersection.length;
}
