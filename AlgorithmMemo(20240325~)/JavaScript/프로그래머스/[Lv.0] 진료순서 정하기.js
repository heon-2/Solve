function solution(emergency) {
  var answer = [];
  let not_sorted_emergency = JSON.parse(JSON.stringify(emergency));
  let sorted_emergency = emergency.sort((a, b) => b - a);
  for (i = 0; i < rank.length; i++) {
    let priority = sorted_emergency.indexOf(not_sorted_emergency[i]);
    answer.push(priority + 1);
  }
  return answer;
}

/*
[풀이 일자] : 2024.04.29
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 
[문제 풀이] : 
[배운 점] : 자바스크립트에서 깊은 복사를 하는 방법
1. JSON.stringify(object)를 통해 객체를 JSON 문자열로 변환한 다음. JSON.parse를 통해 객체로 파싱하는 것.
2. lodash 라이브러리의 _.cloneDeep() 같은 함수를 사용하여 깊은 복사 가능.
import _ from 'lodash';
const deepCopy = _.cloneDeep(object);

sort()를 사용하면 원본 배열도 바뀜.
*/

function solution(emergency) {
  var answer = [];
  const rank = [...emergency]; // 구조분해할당으로 emergency의 얕은 복사복인 rank를 만들어서 rank를 정렬함. (얕은복사)
  // 얕은 복사는 객체의 첫 번째 레벨의 프로퍼티만 새 객체로 복사. -> 중첩된 구조가 있으면 깊은 복사가 필요.
  let sorted_emergency = rank.sort((a, b) => b - a);
  for (i = 0; i < rank.length; i++) {
    let priority = sorted_emergency.indexOf(emergency[i]);
    answer.push(priority + 1);
  }
  return answer;
}
