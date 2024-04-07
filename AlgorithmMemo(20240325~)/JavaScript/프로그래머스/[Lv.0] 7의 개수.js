function solution(array) {
    var answer = 0;
    let arr = array.join('').match(/7/g);
    
    return arr === null ? 0:arr.length;
}

