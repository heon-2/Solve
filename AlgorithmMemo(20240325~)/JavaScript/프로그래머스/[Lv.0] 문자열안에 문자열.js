function solution(str1, str2) {
  let answer;
  answer = str1.includes(str2) ? 1 : 2;
  return answer;
}

/*
[풀이 일자] : 2024.03.29
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 
[문제 풀이] : 
[배운 점] : 문자열이 들어있는지 아닌지를 확인하기 위해서는 .includes() 메소드를 사용하면 된다.
*/
