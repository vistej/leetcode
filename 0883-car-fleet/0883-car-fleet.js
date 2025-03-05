/**
 * @param {number} target
 * @param {number[]} position
 * @param {number[]} speed
 * @return {number}
 */
var carFleet = function(target, position, speed) {
    
    const cars = position.map((p, i) => [p, (target - p) / speed[i]]).sort((a, b) => b[0] - a[0]);

    let res = 0;
    let prevTime = 0;

    for (const [pos, time] of cars) {
        if (time > prevTime) {
            res++;
            prevTime = time;
        }
    }

    return res;
};