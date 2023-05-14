let player1 = prompt("Player One: Enter your name. You will play with Blue Chips!");
let player1Color = 'rgb(86, 151, 255)';

let player2 = prompt("Player Two: Enter your name. You will play with Red Chips!");
let player2Color = 'rgb(237, 45, 73)';

let gameOn = true;
let table = $('table tr');

const changeColor = (row, col, colorCode) => {
	return table.eq(row).find('td').eq(col).find('button').css('background-color', colorCode);
};

const getColor = (row, col) => {
	return table.eq(row).find('td').eq(col).find('button').css('background-color');
};

const reportWin = (row, col) => {
	let playerColor = getColor(row, col);
	let victor = '';
	if (player1Color === playerColor) victor = player1;
	else if (player2Color === playerColor) victor = player2;
	console.log(victor + " won starting at this row, col: {" + row + ", " + col + "}");
};

const checkBottom = (col) => {
	for (let r = 5; r >= 0; r--) {
		let slotColor = getColor(r, col);
		if (slotColor === 'rgb(128, 128, 128)') {
			return r;
		}
	}
	return -1;
};

const colorMatchCheck = (one, two, three, four) => {
	return (one !== undefined && one !== 'rgb(128, 128, 128)' && one === two && one === three && one === four);
};

const horizontalWinCheck = () => {
	console.log('starting horizontal win check....');
	for (let r = 0; r < 6; r++) {
		console.log('row ' + r);
		for (let c = 0; c < 4; c++) {
			console.log('col ' + c);
			let one = getColor(r, c);
			let two = getColor(r, c+1);
			let three = getColor(r, c+2);
			let four = getColor(r, c+3);
			if (colorMatchCheck(one, two, three, four)) {
				console.log('Horizontal Win');
				reportWin(r, c);
				return true;
			}
		}
	}
	console.log('completed horizontal win check....');
	return false;
};

const verticalWinCheck = () => {
	console.log('starting vertical win check....');
	for (let c = 0; c < 7; c++) {
		console.log('col ' + c);
		for (let r = 0; r < 3; r++) {
			console.log('row ' + r);
			let one = getColor(r, c);
			let two = getColor(r+1, c);
			let three = getColor(r+2, c);
			let four = getColor(r+3, c);
			if (colorMatchCheck(one, two, three, four)) {
				console.log('Vertical Win');
				reportWin(r, c);
				return true;
			}
		}
	}
	console.log('completed vertical win check....');
	return false;
};

const diagonalWinCheck = () => {
	console.log('starting diagonal win check....');
	for (let r = 0; r < 3; r++) {
		console.log('row ' + r);
		// negative slope
		for (let c = 0; c < 4; c++) {
			console.log('col ' + c);
			let one = getColor(r, c);
			let two = getColor(r+1, c+1);
			let three = getColor(r+2, c+2);
			let four = getColor(r+3, c+3);
			if (colorMatchCheck(one, two, three, four)) {
				console.log('Diagonal Win');
				reportWin(r, c);
				return true;
			}
		}

		// positive slope
		for (let c = 3; c < 7; c++) {
			console.log('col ' + c);
			let one = getColor(r, c);
			let two = getColor(r-1, c-1);
			let three = getColor(r-2, c-2);
			let four = getColor(r-3, c-3);
			if (colorMatchCheck(one, two, three, four)) {
				console.log('Diagonal Win');
				reportWin(r, c);
				return true;
			}
		}
	}
	console.log('completed diagonal win check....');
	return false;
};

const winCheck = () => {
	if (verticalWinCheck() || horizontalWinCheck() || diagonalWinCheck()) {
		$('h1').text("Congratulations " + turn.name + "! You won the game!");
		$('.game-text').fadeOut("fast");
		return true;
	}
	return false;
};

// turn object
let turn = {
	player: 1,
	name: player1,
	color: player1Color
};

const toggleTurn = () => {
	console.log('Toggling player details....');
	if (turn.player === 1) {
		turn.player = 2; turn.name = player2; turn.color = player2Color;
	} else if (turn.player === 2) {
		turn.player = 1; turn.name = player1; turn.color = player1Color;
	}
	//changing prompt
	$('#game-prompt').text(turn.name + " it is your turn, pick a column to drop your chip in!");
};

//changing prompt
$('#game-prompt').text(turn.name + " it is your turn, pick a column to drop your chip in!");

$('.board button').click(function() {
	console.log('button clicked!');
	let col = $(this).closest('td').index();
	let bottomRow = checkBottom(col);
	console.log(bottomRow + ", " + col);
	changeColor(bottomRow, col, turn.color);

	if (!winCheck()) {
		toggleTurn();
	}
});