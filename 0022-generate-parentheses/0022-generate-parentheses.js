/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    const res = [];

    const loop = (x, y, cs) => {
        if (!x && !y) {
            res.push(cs);
            return;
        }
        if (x) loop(x - 1, y, cs + '(')
        if (y && y > x) loop(x, y - 1, cs + ')');
    }

    loop(n, n, '');
    return res;
};