function solution(age) {
    let alpha = 'abcdefghij';
    let answer = '';
    age = age.toString();
    for (let i = 0; i < age.length; i++) {
        answer += alpha[age[i]];
    }
    return answer;
}
