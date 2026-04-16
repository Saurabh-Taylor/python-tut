function caesar(text, shift) {
    let alphabets = "abcdefghijklmnopqrstuvwxyz!@#$"
    for (let i = 0; i < text.length; i++) {
        console.log(alphabets[(alphabets.indexOf(text[i]) + shift)])
    }
}

caesar("saurabh", 5)