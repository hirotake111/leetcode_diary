class MyPromise {
  constructor(callback) {
    try {
      callback(this.#onResolve, this.#onReject);
    } catch (e) {
      this.error = e;
    }
  }

  then = (cb) => {
    this.value = cb(this.value);
    return this;
  };

  catch = (cb) => {
    cb(this.error);
  };

  #onResolve = (value) => {
    this.value = value;
  };

  #onReject = (error) => {
    this.error = error;
  };
}

module.exports = MyPromise;

const cb = () => {};
const p = new MyPromise(cb);
