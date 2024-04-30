function solution(my_string) {
  let answer = my_string.split("").filter((i) => !isNaN(i));
  answer.sort();
  answer = answer.map((i) => parseInt(i));
  return answer;
}

/*
[풀이 일자] : 2024.04.02
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 
[문제 풀이] :
1. 문자열을 split으로 배열로 바꾼 후,
2. filter로 숫자만 걸러내고,
3. sort로 정렬하고
4. map으로 다시 숫자로 바꾸어 리턴한다.
[배운 점] : isNaN(인자) 는 인자값이 NaN이면 true 반환. 주로 숫자인지 아닌지 확인할때.

v = v*1 하면 자바스크립트에서 문자가 숫자로 바뀌기도 함. 
*/
