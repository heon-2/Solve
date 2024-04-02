function solution(my_string) {
  var numbers = my_string.split("").filter((i) => !isNaN(i));
  numbers = numbers.map((i) => parseInt(i));
  var answer = numbers.reduce((acc, cur) => acc + cur);
  return answer;
}

/*
[풀이 일자] : 2024.04.02
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 
[문제 풀이] : 
[배운 점] : [...my_string]으로 스프레드 연산을 하면 되는데 왜 자꾸 split으로 분리하는지!!!!
*/
function solution(my_string) {
  return my_string
    .split("")
    .filter((v) => !isNaN(v))
    .reduce((a, b) => parseInt(a) + parseInt(b));
}

// parseInt로 reduce 쓰는 방법도 있음. 맵함수 돌리지 않고.
