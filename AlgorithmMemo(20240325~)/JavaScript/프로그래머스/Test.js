// console.log(isNaN("text")); // true, "text"는 숫자로 변환될 수 없으므로
// console.log(Number.isNaN("text")); // false, "text"는 숫자 타입이 아니므로

// console.log(isNaN(NaN)); // true, NaN은 숫자가 아니므로
// console.log(Number.isNaN(NaN)); // true, NaN은 숫자 타입이고 값도 NaN이므로

// const array1 = ["a", "b", "c"];
// const array2 = ["d", "e", "f"];
// const answer = array1.concat(array2);
// console.log(answer);

// const array1 = ["a", "b", "c", "d", "e"];
// console.log(array1.copyWithin(0, 3, 4)); // [ 'd', 'b', 'c', 'd', 'e' ]

// const isBelowThreshold = (cur) => cur < 40;
// const array1 = [1, 30, 39, 29, 10, 13];
// console.log(array1.every(isBelowThreshold)); // true

// const array = [1, 2, 3, 4];
// console.log(array.fill(0, 0, 2)); // [ 0, 0, 3, 4 ]

// const words = ["a", "ab", "abc", "abcd", "abcde", "abcdef"];
// const result = words.filter((word) => word.length > 2);
// console.log(result); // [ 'abc', 'abcd', 'abcde', 'abcdef' ]

// const array = [1, 2, 3, 4, 5];
// const found = array.find((element) => element > 3);
// console.log(found); // 4

// const array = ["a", "b", "c"];
// const iterator = array.keys();
// for (const key of iterator) {
//   console.log(key);
// Expected output: 0
// Expected output: 1
// Expected output: 2
// }

const alphabet = ["a", "b", "c"];
const count = alphabet.push("e");
console.log(count);
