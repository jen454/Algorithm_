function solution(phone) {
    return "*".repeat(phone.length-4) + phone.slice(-4);
}