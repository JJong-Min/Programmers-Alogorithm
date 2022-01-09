function solution(clothes) {
    let answer = 1;
    let clothes_cnt = {};
    for (let cloth of clothes) {
        clothes_cnt[cloth[1]] = (clothes_cnt[cloth[1]] || 0) + 1;
    }

    for (let key in clothes_cnt) {
        answer *= (clothes_cnt[key] + 1);
    }
    
    return answer - 1;
}