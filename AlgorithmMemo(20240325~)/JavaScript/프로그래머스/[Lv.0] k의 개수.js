function solution(i, j, k) {
    var answer = 0;
    for (let a=i; a <=j; a++) {
        let num = [...a.toString()]
        for (let b=0; b<=num.length; b++) {
            if (num[b] == k) {
                answer += 1
            }
        }
    }
    return answer;
}

// 참고할 코드

function solution(i, j, k) {
    let a ='';
    for(i;i<=j;i++){
        a += i;
    }
    return a.split(k).length-1;
}

