function solution(number) {
    let answer = 0;
    let res = 0;
    for (let i=0; i<number.length; i++) {
        answer += Number(number[i]);
    }
    res = answer % 9;
    return res;
}