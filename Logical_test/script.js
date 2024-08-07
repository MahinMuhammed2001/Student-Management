function GPattern(rows, cols) {
    for (let row = 0; row < rows; row++) {
        let line = '';
        for (let col = 0; col < cols; col++) {
            if (col === 0 || (row === 0 && col < 4) || (row === 6 && col < 4) || (row === 3 && col >= 3) || 
                (col === 4 && row !== 0 && row !== 6 && row >= 3)) {
                line += '*';
            } else {
                line += ' ';

            }

        }

        
        console.log(line);
    }
}

GPattern(7, 6);
