function solution(cipher, code) {
  var answer = "";
  for (i = 0; i < cipher.length; i++) {
    if ((i + 1) % code === 0) {
      answer += cipher[i];
    }
  }
  return answer;
}

/*
[풀이 일자] : 2024.03.27
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : -
[문제 풀이] : 문자열도 += 가 사용이 가능함.
[배운 점] : -
*/
