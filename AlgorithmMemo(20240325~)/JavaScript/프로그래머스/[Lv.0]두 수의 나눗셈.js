function solution(num1, num2) {
  var answer = parseInt((num1 / num2) * 1000);
  return answer;
}
/*
[풀이 일자] : 2024.03.25
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 수학
[문제 풀이] : -
[배운 점] : Math.trunc() 함수를 이용해 소수점 이하를 버릴 수 있다.
Math.floor() 는 24.2인경우 24가 되지만, -24.2인 경우 -25가 되기 때문에, 음수인 경우를 생각하면 Math.trunc()를 사용하는 것이 좋은 듯 하다.

*/
