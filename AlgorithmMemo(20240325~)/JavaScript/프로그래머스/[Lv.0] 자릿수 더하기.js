function solution(n) {
  let answer = 0;
  n = n.toString().split("");
  answer = n.reduce((acc, cur) => acc + parseInt(cur), 0);
  return answer;
}

/*
[풀이 일자] : 2024.03.26
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 수학
[문제 풀이] : 
[배운 점] : .toString()을 통해 문자열로 바꾼 후, split('')을 통해 배열로 만들어주고,
reduce를 통해 각 자리수를 더해준다.
acc에 0을 넣어주는 이유는, reduce의 두번째 인자로 초기값을 넣어주기 위함.

*/

// 참고할 코드
function solution(n) {
  return n
    .toString()
    .split("")
    .reduce((acc, cur) => acc + Number(cur), 0);
}

// parseInt(string, radix)는 문자열을 파싱하여 특정 진수(radix)의 정수로 변환합니다. radix는 옵션이며, 2에서 36 사이의 값을 가질 수 있습니다.
// parseInt는 문자열의 시작 부분에 있는 숫자를 읽고, 숫자가 아닌 문자를 만나면 그 지점에서 파싱을 멈춥니다. 즉, "123abc"를 parseInt로 변환하면 123을 얻습니다.
// 숫자로 변환할 수 없는 문자열은 NaN을 반환합니다.
// parseInt는 문자열에서 숫자만 추출할 때 사용하는 것.
