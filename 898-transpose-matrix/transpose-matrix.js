var transpose = function(matrix) {
    const row = matrix.length;
    const col = matrix[0].length;
    const trans = Array.from({ length: col }, () => Array(row));

    for (let i = 0; i < col; i++) {
        for (let j = 0; j < row; j++) {
            trans[i][j] = matrix[j][i];
        }
    }
    return trans;
};