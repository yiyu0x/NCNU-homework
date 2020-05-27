const deepCopy = (arr) => JSON.parse(JSON.stringify(arr))
const printBoard = (board, row, col) => {
    const size = board.length
    for (let y = 0; y < size; y++) {
        console.log(board[y], row[y])
    }
    console.log('  ' + col.join(', '))
    console.log()
}

const getRowSum = (board, y) => {
    let row_sum = 0
    for (let x_index = 0; x_index < board.length; x_index++)
        if (board[y][x_index])
            row_sum += x_index + 1
    return row_sum
}

const getColSum = (board, x) => {
    let col_sum = 0
    for (let y_index = 0; y_index < board.length; y_index++)
        if (board[y_index][x])
            col_sum += y_index + 1
    return col_sum
}

const isAns = (board, row, col, x, y) => {
    const size = board.length
    const rowSum = 0
    const colSum = 0
    for (let i = 0; i < size; i++) {
        if (getRowSum(board, i) !== row[i]) return false
        if (getColSum(board, i) !== col[i]) return false
    }
    return true
}
const dfs = (board, row, col, x, y) => {
    //終止條件
    if (x === board.length && y === board.length - 1) {
        if (isAns(board, row, col, x, y)) {
            printBoard(board, row, col)
            return
        }
        return
    }
    //update x and y
    if (x === board.length) {
        y = y + 1
        x = 0
    }
    dfs(deepCopy(board), row, col, x + 1, y)
    //如果有一些條件不符合，則不用選該點，直接略過（剪枝）
    if (row[y] !== 0 && col[x] !== 0) {
        if (getRowSum(board, y) + (x + 1) <= row[y] && getColSum(board, x) + (y + 1) <= col[x]) {
            board[y][x] = 1
            dfs(board, row, col, x + 1, y)
        }
    }
}

const main = (size, row, col) => {
    const board = [...Array(size)].map(x => Array(size).fill(0))
    dfs(board, row, col, 0, 0)
}

const size = 4
const row = [3, 4, 6, 7]
const col = [1, 4, 4, 9]

// const size = 6
// const row = [14, 6, 5, 11, 8, 6]
// const col = [13, 6, 12, 5, 10, 5]
main(size, row, col)