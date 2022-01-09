function solution(progresses, speeds) {
    let answer = [];
    let stack = [];
    let cnt = 0;
    for (let i in progresses) {
        let work_day = Math.ceil((100 - progresses[i]) / speeds[i]);
        if (stack.length === 0) {
            stack.push(work_day);
            cnt += 1;
        } else {
            if (stack[stack.length - 1] >= work_day) {
                cnt += 1;
            } else {
                stack.pop();
                answer.push(cnt);
                stack.push(work_day);
                cnt = 1;
            }
        }
    }
    answer.push(cnt);
    return answer;
}