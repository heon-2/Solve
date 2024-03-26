function solution(numbers) {
  let answer;
  let summ = 0;
  for (i = 0; i < numbers.length; i++) {
    summ += numbers[i];
  }
  answer = summ / numbers.length;
  return answer;
}

/*
[풀이 일자] : 2024.03.26
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 수학
[문제 풀이] : 반복문을 돌려 summ을 구한 후, numbers의 길이로 나눠줌.
[배운 점] : 평균을 구할 때, reduce를 사용하면 더 간단하게 구할 수 있다. 
아래 코드 참조.
*/

function solution(numbers) {
  summ = numbers.reduce((acc, cur) => acc + cur);
  return summ / numbers.length;
}
