/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    const map = new Map()

    for (const n of nums) {
        const val = (map.get(n) || 0) + 1
        map.set(n, val)
    }

    const res = []

    const vals = Array.from(map.entries());
    vals.sort((a, b) => b[1] - a[1]);
    let i = 0;
    while (i < k) {
        res.push(vals[i][0])
        i++;
    }
    return res
};