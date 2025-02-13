/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length !== t.length) return false;
    const obj = {};

    for (const c of s) obj[c] = (obj[c] || 0) + 1;

    for (const c of t) {
        if (!obj[c]) return false;
        obj[c]--;
    }

    return true
};