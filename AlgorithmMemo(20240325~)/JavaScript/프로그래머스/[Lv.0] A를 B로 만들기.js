function solution(before, after) {
  return JSON.stringify([...before].sort()) ===
    JSON.stringify([...after].sort())
    ? 1
    : 0;
}

/*
[풀이 일자] : 2024.04.03
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : -
[문제 풀이] : 구조 분해하여 정렬한 뒤, 같은지 다른지를 비교함.
[배운 점] : 자바스크립트에서 배열간의 동등 비교를 하려면 JSON.stringify를 사용해야 한다.
왜냐면 자바스크립트에서 배열 === == 비교는 배열 구성을 비교하는 것이 아닌, 배열 메모리의 주소값을 비교하기 때문. (reference type 이기 때문)
JSON.stringify() 메소드로 배열을 직렬화(문자열) 하여 문자열 비교
출처: https://inpa.tistory.com/entry/JS-🚀-자바스크립트-배열-구성-비교하기 [Inpa Dev 👨‍💻:티스토리]

*/
