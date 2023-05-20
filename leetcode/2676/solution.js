/**
 * https://leetcode.com/problems/throttle/description/?gio_link_id=bR7jOnr9
 * 2676. Throttle
 * Given a function fn and a time in milliseconds t, return a throttled version of that function.
 * A throttled function is first called without delay and then, for a time interval of t milliseconds, can't be executed but should store the latest function arguments provided to call fn with them after the end of the delay.
 * For instance, t = 50ms, and the function was called at 30ms, 40ms, and 60ms. The first function call would block calling functions for the following t milliseconds. The second function call would save arguments, and the third call arguments should overwrite currently stored arguments from the second call because the second and third calls are called before 80ms. Once the delay has passed, the throttled function should be called with the latest arguments provided during the delay period, and it should also create another delay period of 80ms + t.
 */

/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var throttle = function (fn, t) {
  let buf = null;
  let blocking = false;

  let startThrottle = () => {
    blocking = true;
    setTimeout(() => {
      blocking = false;
      // If we have args in the buffer, invoke callback
      // and start throttling again
      if (buf) {
        fn(...buf);
        buf = null;
        startThrottle();
      }
    }, t);
  };

  return function (...args) {
    if (blocking) {
      // we have a pending callback -> Update buf
      buf = args;
    } else {
      // No pending callback
      // -> invoke function immediately and start throttling
      fn(...args);
      startThrottle();
    }
  };
};

/**
 * const throttled = throttle(console.log, 100);
 * throttled("log"); // logged immediately.
 * throttled("log"); // logged at t=100ms.
 */
