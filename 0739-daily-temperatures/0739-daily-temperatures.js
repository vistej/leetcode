/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function(temperatures) {
    const len = temperatures.length;
    const stack = []
    const res = Array(len).fill(0);
    let i = len - 1;
    while (i >= 0) {
        let cm = stack.length - 1;

        while (stack.length && temperatures[i] >= temperatures[stack[cm]]){
            cm--;
            stack.pop()
        }
        res[i] = !stack.length ? 0 : stack[cm] - i;
        stack.push(i)
        i--;
    }

    return res;
};