const MyPromise = require("./mypromise");
// const MyPromise = Promise;

const DEFAULT_VALUE = " default";
const URL = "https://swapi.dev/api/films/1/";

describe("then", () => {
  it("should update value asynchronously", (done) => {
    expect.assertions(1);
    new MyPromise((resolve, reject) => {
      resolve(1);
    }).then((v) => {
      expect(v).toBe(1);
      done();
    });
  });

  it("should be capable of method chaining", (done) => {
    expect.assertions(1);
    new MyPromise((resolve, reject) => {
      resolve(1);
    })
      .then((result) => result * 20)
      .then((a) => a + 15)
      .then((v) => {
        expect(v).toBe(35);
        done();
      });
  });
});

describe("catch", () => {
  it("should catch error", (done) => {
    expect.assertions(1);
    new MyPromise((resolve, reject) => {
      reject(new Error("error!"));
    }).catch((reason) => {
      expect(reason.message).toEqual("error!");
      done();
    });
  });
});
