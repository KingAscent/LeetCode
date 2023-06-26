class Calculator {
  constructor(value) {
      this.result = value;
  }

  add(value){
      return this.result += value;
  }

  subtract(value){
      return this.result -= value;
  }

  multiply(value) {
      return this.result *= value;
  }

  divide(value) {
      if(value == 0)
        throw Error("Division by zero is not allowed");
      return this.result /= value;
  }

  power(value) {
      return this.result = Math.pow(this.result, value);
  }

  getResult() {
      return this.result;
  }
}
