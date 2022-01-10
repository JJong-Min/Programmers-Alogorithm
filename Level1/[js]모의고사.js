function solution(answers) {
    let answer = [];
    let firstPersonAnswers = [1, 2, 3, 4, 5];
    let secondPersonAnswers = [2, 1, 2, 3, 2, 4, 2, 5];
    let thirdPersonAnswers = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    let firstPersonCorrect = 0;
    let secondPersonCorrect = 0;
    let thirdPersonCorrect = 0;
    
    answers.forEach(function(element, index) {
        // 첫 번째 사람 정답 판단
        if (element === firstPersonAnswers[index % 5]) {
            firstPersonCorrect += 1;
        }
        if (element === secondPersonAnswers[index % 8]) {
            secondPersonCorrect += 1;
        }
        if (element === thirdPersonAnswers[index % 10]) {
            thirdPersonCorrect += 1;
        }
    })
    
    let maxCorrect = Math.max(firstPersonCorrect, secondPersonCorrect, thirdPersonCorrect);
    
    if (maxCorrect === firstPersonCorrect) {
        answer.push(1);
    }
    if (maxCorrect === secondPersonCorrect) {
        answer.push(2);
    }
    if (maxCorrect === thirdPersonCorrect) {
        answer.push(3);
    }
    
    return answer;
}