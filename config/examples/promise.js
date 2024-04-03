const isPrime = num => {
  for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++) {
    if(num % i === 0) return false;
  }
  return num > 1;
};
console.log(isPrime(13)); // Output: true


