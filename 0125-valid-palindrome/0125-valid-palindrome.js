/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    const regex = /[^a-zA-Z0-9]/g;
    const ns = s.toLowerCase().replace(regex, '');
    return ns === ns.split('').reverse().join('');
};