/**
 * @param {string} colors
 * @return {boolean}
 */
var winnerOfGame = function (colors) {
  let alice = 0;
  for (let i = 0; i < colors.length - 2; i++) {
    if (colors[i] == colors[i + 1] && colors[i] == colors[i + 2]) {
      alice += colors[i] == "A" ? 1 : -1;
    }
  }

  return alice > 0;
};
