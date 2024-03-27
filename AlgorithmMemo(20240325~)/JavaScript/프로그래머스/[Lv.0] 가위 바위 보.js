function solution(rsp) {
  var answer = "";
  for (i = 0; i < rsp.length; i++) {
    if (rsp[i] === "2") {
      answer += "0";
    } else if (rsp[i] === "0") {
      answer += "5";
    } else if (rsp[i] === "5") {
      answer += "2";
    }
  }
  return answer;
}

/*
[풀이 일자] : 2024.03.27
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 수학
[문제 풀이] : 단순 조건문
[배운 점] : - 
*/
