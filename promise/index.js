class MyClass {
  constructor(value) {
    this.value = value;
  }

  get() {
    console.log(this.value);
  }
  set(newValue) {
    this.value = newValue;
  }
}

const a = new MyClass(1);
console.log(a.get());
