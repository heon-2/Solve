function solution(strlist) {
  var answer = [];
  for (i = 0; i < strlist.length; i++) {
    answer.push(strlist[i].length);
  }
  return answer;
}

/*
[풀이 일자] : 2024.03.26
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 수학
[문제 풀이] : 반복문을 돌려 각 요소의 길이를 length로 측정하고, push를 통해 배열에 집어넣음.
[배운 점] : 파이썬의 append가 자바스크립트의 push라는 것을 한 번 더 이해했고,
추가로 이렇게 반복문을 돌릴게 아니라 map함수를 쓰면 더 깔끔하다는 것을 이해함.
*/

function solution(strlist) {
  return strlist.map((el) => el.length);
}

// map 함수를 사용하면 새로운 배열을 반환한다.
