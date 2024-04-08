function findFactor(num) {
  let factors = 0;
  for (let i = 1; i <= num; i++) {
    if (num % i === 0) {
      factors += 1;
    }
    if (factors >= 3) {
      break;
    }
  }
  return factors >= 3 ? 1 : 0;
}
function solution(n) {
  var answer = 0;
  for (let i = 1; i <= n; i++) {
    answer += findFactor(i);
  }
  return answer;
}

/*
[풀이 일자] : 2024.04.08
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 수학
[문제 풀이] : -
[배운 점] : 각기 다른 함수에서 반복문을 돌릴 때, i가 겹치면 전역변수로 선언되어 두 함수 간에 충돌이 발생함. (아래코드 참고)
따라서 앞으로 for문 돌릴 때, let을 붙여주는 습관을 들여야 할듯. let을 사용하면 i를 지역변수로 선언 가능.
*/

function findFactor(num) {
  let factors = 0;
  for (i = 1; i <= num; i++) {
    if (num % i === 0) {
      factors += 1;
    }
    if (factors >= 3) {
      break;
    }
  }
  return factors >= 3 ? 1 : 0;
}
function solution(n) {
  var answer = 0;
  for (i = 1; i <= n; i++) {
    answer += findFactor(i);
  }
  return answer;
}
