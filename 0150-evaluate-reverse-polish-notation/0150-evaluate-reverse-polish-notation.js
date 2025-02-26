/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function(tokens) {
    const stack = [];
    const set = new Set('+-*/');
    for (const ch of tokens) {
        if (!set.has(ch)) {
            stack.push(Number(ch));
        } else {
            const y = stack.pop();
            const x = stack.pop();
            if (ch === '+') stack.push(x + y);
            if (ch === '-') stack.push(x - y);
            if (ch === '/') {
                const val = x / y;
                if (val < 0) stack.push(Math.ceil(val));
                else stack.push(Math.floor(val));
            }
            if (ch === '*') stack.push(x * y);
        }
    }
    return stack.pop();
};