function solution(num, total) {
  let num_list = [];
  for (let i = -1000; i <= total + 1000; i++) {
    num_list.push(i);
  }
  for (let j = 0; j <= total + 1000; j++) {
    let section = num_list.slice(j, j + num);
    if (section.reduce((acc, cur) => acc + cur, 0) === total) {
      return section;
    }
  }
}

/*
[풀이 일자] : 2024.04.18
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 
[문제 풀이] : 추후 채울 예정 + 밑의 코드 이해하기.
[배운 점] : 

*/
function solution(num, total) {
  var min = Math.ceil(total / num - Math.floor(num / 2));
  var max = Math.floor(total / num + Math.floor(num / 2));

  return new Array(max - min + 1).fill(0).map((el, i) => {
    return i + min;
  });
}
