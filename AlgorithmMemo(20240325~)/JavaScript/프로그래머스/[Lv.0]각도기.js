function solution(angle) {
  let answer;
  if (0 < angle && angle < 90) {
    answer = 1;
  } else if (angle === 90) {
    answer = 2;
  } else if (90 < angle && angle < 180) {
    answer = 3;
  } else if (angle === 180) {
    answer = 4;
  }
  return answer;
}
/*
[풀이 일자] : 2024.03.25
[문제 출처] : 프로그래머스
[난이도] : Level 0
[문제 유형] : 단순 조건문
[문제 풀이] : -
[배운 점] : - 
```
function solution(angle) {
    let answer;
    if (0 < angle <90) {
        answer = 1
    }
    else if (angle===90) {
        answer = 2
    }
    else if (90 < angle < 180) {
        answer = 3
    }
    else if (angle === 180) {
        answer = 4
    }
    
    return answer;
}
```

처음에 짰던 코드는 이렇게 생겼다.
당연히 파이썬처럼 풀면 될 줄 알았는데, 이렇게 쓰니깐 어떤 값을 넣어도 1이 리턴된다.

이유를 찾아보니 자바스크립트에서 0 < angle < 90 이 부분을 판별하는 게 다르더라.
자바스크립트에서 표현식은 왼쪽부터 순차적으로 평가되기 때문에 0 < angle 이 평가되어 true 혹은 false가 반환된다.
근데 자바스크립트에서 true나 false는 1 또는 0이기 때문에 그 다음 1 < 90 혹은 0 < 90 이런 식으로 평가되어 참이든 거짓이든 항상 그 다음 평가에서 true가 반환되게 된다.
따라서 0 < angle < 90 이런 식으로 쓰면 안되고, 0 < angle && angle < 90 이런 식으로 써야 한다.

리액트로 코딩할 때, 이런 부분을 고려해본 적이 없어서 상당히 당황스럽지만 언능 익혀야겠다.

참고로 

function solution(angle) {
    return angle < 90 ? 1 : angle == 90 ? 2 : angle < 180 ? 3 : 4;
}

이런식으로 삼항 연산자를 사용해 간결하게 표현이 가능하다.

*/
