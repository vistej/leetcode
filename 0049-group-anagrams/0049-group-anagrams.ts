function groupAnagrams(strs: string[]): string[][] {
    const map = new Map();

    for (const str of strs) {
        const sortedStr = str.split('').sort().join('');
        const res = map.get(sortedStr) || [];
        res.push(str);
        map.set(sortedStr, res);

    }

    return Array.from(map.values());
};