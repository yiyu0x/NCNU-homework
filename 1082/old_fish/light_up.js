let res = 0
const print = (board) => {
    board.forEach((row) => console.log(row))
    console.log()
}

const deepCopy = (arr) => JSON.parse(JSON.stringify(arr))

const toggle = (board, x, y) => {
    const len = board.length
    board[x][y] ^= 1
    if (check_safe(len, x + 1, y))
        board[x + 1][y] ^= 1
    if (check_safe(len, x - 1, y))
        board[x - 1][y] ^= 1
    if (check_safe(len, x, y + 1))
        board[x][y + 1] ^= 1
    if (check_safe(len, x, y - 1))
        board[x][y - 1] ^= 1
}

const check_safe = (n, x, y) => {
    if (x === n || y === n || x === -1 || y === -1) return false
    else return true
}

const backtrack = (board, x) => {
    if (x !== 0) return !board[x - 1].every((elem) => elem === 1)
    return false
}

const dfs = (board, x, y, path) => {
    const len = board.length
    if (y === len && backtrack(board, x)) return

    x = y === len ? x + 1 : x
    y = y === len ? 0 : y

    if (x >= len - 2 && check_ans(board, len)) {
        res += 1
        // console.log('->', path)
        return
    }
    if (x === len) return
    dfs(deepCopy(board), x, y + 1, [...path])
    toggle(board, x, y)
    path.push([x, y])
    dfs(board, x, y + 1, path)

}

const check_ans = (board, n) => {
    return board.every(row => row.every(elem => elem === 1) === true)
}

const main = (n) => {
    let board = Array.from(Array(n), () => new Array(n).fill(0))
    dfs(board, 0, 0, [])
    console.log(`n: ${n}, res: ${res}`)
}

main(4)