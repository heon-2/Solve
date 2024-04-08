console.log(isNaN("text")); // true, "text"는 숫자로 변환될 수 없으므로
console.log(Number.isNaN("text")); // false, "text"는 숫자 타입이 아니므로

console.log(isNaN(NaN)); // true, NaN은 숫자가 아니므로
console.log(Number.isNaN(NaN)); // true, NaN은 숫자 타입이고 값도 NaN이므로
