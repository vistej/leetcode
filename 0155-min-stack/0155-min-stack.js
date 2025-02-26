
var MinStack = function() {
    this.list = [];
    this.minList = [];
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    const l = this.list.length;
    const minVal = l ? Math.min(this.minList[l - 1], val): val;
    this.list.push(val);
    this.minList.push(minVal);
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    this.list.pop();
    this.minList.pop();
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    const l = this.list.length;
    return l ? this.list[l - 1] : null;
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    const l = this.list.length;
    return l ? this.minList[l - 1] : null;
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */