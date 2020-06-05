const print = (graph, counter) => {
	graph.forEach(row => {
		console.log(row.join(' '))
	})
	console.log('--------------', 'result:', counter)
}

const isPeopleSurround = (graph, y, x) => {
	//左
	if (x - 1 >= 0 && graph[y][x - 1] === 'O') return true
	//右
	if (x + 1 < graph[y].length && graph[y][x + 1] === 'O') return true
	//上
	if (y - 1 >= 0 && graph[y - 1][x] === 'O') return true
	//下
	if (y + 1 < graph.length && graph[y + 1][x] === 'O') return true
	//左上
	if (y - 1 >= 0 && x - 1 >= 0 && graph[y - 1][x - 1] === 'O') return true
	//右上
	if (y - 1 >= 0 && x + 1 < graph[y].length && graph[y - 1][x + 1] === 'O') return true
	//左下
	if (y + 1 < graph.length && x - 1 >= 0 && graph[y + 1][x - 1] === 'O') return true
	//右下
	if (y + 1 < graph.length && x + 1 < graph[y].length && graph[y + 1][x + 1] === 'O') return true
	//左左
	if (x - 2 >= 0 && graph[y][x - 2] === 'O') return true
	//右右
	if (x + 2 < graph[y].length && graph[y][x + 2] === 'O') return true
	//上上
	if (y - 2 >= 0 && graph[y - 2][x] === 'O') return true
	//下下
	if (y + 2 < graph.length && graph[y + 2][x] === 'O') return true
	return false
}

const dfs = (graph, rows, y, x, counter=0) => {
	//update info
	//console.log(x,y, rows[y])
	if (x === rows[y]) {
		y += 1
		x = 0
		//end game
		if (y === graph.length) {
			if (counter > max) {
				max = counter
				print(graph, counter)
			}
			return
		}
	}

	if (isPeopleSurround(graph, y, x))
		dfs(graph,      rows, y, x + 1, counter)
	else {
		//pick
		graph[y][x] = 'O'
		dfs([...graph],      rows, y, x + 1, counter + 1)
		//not pick
		graph[y][x] = 'X'
		dfs([...graph], rows, y, x + 1, counter)
	}
}

let max = 0
const main = () => {
	const rowAmount = 5
	const rows = [7, 7, 7, 7, 7]
	const maxRow = Math.max(...rows)
	const graph = [...Array(rowAmount)].map(() => Array(maxRow).fill())

	for (let i = 0; i < rowAmount; i++) {
		let counter = 0
		while (counter < rows[i])
			graph[i][counter++] = 'X'

	}
	dfs(graph, rows, 0, 0)
	console.log('final result:', max)
}

main()
