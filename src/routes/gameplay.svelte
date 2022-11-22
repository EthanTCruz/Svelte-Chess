<script context="module">
import { session } from '$app/stores';


	export async function load({ session }) {
		if (!session?.username) {
			return {
				status: 302,
				redirect: '/sign-in',
			};
		}
		return {
			props: {
				user_id: session.user_id,
				user: session.username,
				game_id: session.game_id,
				pieces_and_positions: session.pieces_and_positions,
				player_color: session.player_color,

			},
		};
	}

	import { io } from 'socket.io-client'

const socket = io()

socket.on('eventFromServer', (message) => {
  console.log(message)
})
	
</script>
<script>

	export let user;
	export let user_id;
	export let game_id;
	export let pieces_and_positions;
	export let player_color





	//"rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"


	let board = [
{row: 1, positions: ['RW','NW','BW','QW','KW','BW','NW','RW']},
{row: 2, positions: ['PB','  ','PW','  ','  ','PW','  ','PW']},
{row: 3, positions: ['  ','  ','  ','  ','  ','  ','  ','  ']},
{row: 4, positions: ['  ','  ','  ','  ','  ','  ','  ','  ']},
{row: 5, positions: ['  ','  ','  ','  ','  ','  ','  ','  ']},
{row: 6, positions: ['  ','  ','  ','  ','  ','  ','  ','  ']},
{row: 7, positions: ['PB','  ','PB','  ','  ','PB','  ','PB']},
{row: 8, positions: ['RB','NB','BB','QB','KB','BB','NB','RB']},
];

 function adjustBoard(){

	let fen_components = pieces_and_positions.split(" ")

	let fen_board = fen_components[0].split("/")

	for (let i = 0; i < 8; i++){
		let board_column = 0
		for (let j = 0; j < fen_board[i].length; j++){
			
			let team = ''
			let piece = fen_board[i].charAt(j)
			const blacks = ['q','k','b','n','r','p']
			const whites = ['Q','K','B','N','R','P']
			if (whites.includes(piece)){
				team = 'W'
				board[7-i].positions[board_column] = `${piece}${team}`
				board_column++
			} else if(blacks.includes(piece)){
				team = 'B'
				board[7-i].positions[board_column] = `${piece.toUpperCase()}${team}`
			board_column++
			} else {
				let value = Number(fen_board[i].charAt(j))
					for( let m = Number(board_column);m<Number(board_column+value);m++){
						board[7-i].positions[m] = "  "
					}
					board_column += value
			}


		
	}

	}

	let fen_en_passant = fen_components[3]
	if (fen_en_passant == '-'){
		en_passant = [0,0]
	} else {
		let column = fen_en_passant.charAt(0)
		let row = Number(fen_en_passant.charAt(1)) - 1

		column = columns.indexOf(column) - 1
		en_passant = [row,column]
	}


	let fen_castle = fen_components[2].split("")
	if (!(fen_castle.includes('k'))){
		w_rook_has_moved[1] = true
	}
	if (!(fen_castle.includes('q'))){
		w_rook_has_moved[0] = true
	}
	if (!(fen_castle.includes('K'))){
		b_rook_has_moved[1] = true
	}
	if (!(fen_castle.includes('Q'))){
		b_rook_has_moved[0] = true
	}
	turn = fen_components[1].toUpperCase()
	return 1
}

async function adjustBoardWithFEN(FEN){

let fen_components = FEN.split(" ")

let fen_board = fen_components[0].split("/")

for (let i = 0; i < 8; i++){
	let board_column = 0
	for (let j = 0; j < fen_board[i].length; j++){
		
		let team = ''
		let piece = fen_board[i].charAt(j)
		const blacks = ['q','k','b','n','r','p']
		const whites = ['Q','K','B','N','R','P']
		if (whites.includes(piece)){
			team = 'W'
			board[7-i].positions[board_column] = `${piece}${team}`
			board_column++
		} else if(blacks.includes(piece)){
			team = 'B'
			board[7-i].positions[board_column] = `${piece.toUpperCase()}${team}`
		board_column++
		} else {
			let value = Number(fen_board[i].charAt(j))
				for( let m = Number(board_column);m<Number(board_column+value);m++){
					board[7-i].positions[m] = "  "
				}
				board_column += value
		}


	
}

}

let fen_en_passant = fen_components[3]
if (fen_en_passant == '-'){
	en_passant = [0,0]
} else {
	let column = fen_en_passant.charAt(0)
	let row = Number(fen_en_passant.charAt(1)) - 1

	column = columns.indexOf(column) - 1
	en_passant = [row,column]
}


let fen_castle = fen_components[2].split("")
if (!(fen_castle.includes('k'))){
	w_rook_has_moved[1] = true
}
if (!(fen_castle.includes('q'))){
	w_rook_has_moved[0] = true
}
if (!(fen_castle.includes('K'))){
	b_rook_has_moved[1] = true
}
if (!(fen_castle.includes('Q'))){
	b_rook_has_moved[0] = true
}
turn = fen_components[1].toUpperCase()
return 1
}





	

	let turn = 'W';
	let move_no = 0;
	let positions_selected = 0;
	let move_from;
	let move_to;
	let last_move = [0,0];
	//let columns = ['h','g','f','e','d','c','b','a']
	let columns = ['a','b','c','d','e','f','g','h']
	let en_passant = [0,0];
	


	let b_castle = true
	let w_castle = true
	let w_king_has_moved = false
	let b_king_has_moved = false
	let w_rook_has_moved = [false,false]
	let b_rook_has_moved = [false,false]

	let fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
	import { afterUpdate, beforeUpdate,onMount } from 'svelte';



	onMount(async () => {
		setBoard()
	});

	async function setBoard(){
		const fetchPromise = fetch(`http://localhost:8000/current_games/board/${user_id}/${game_id}`);
		fetchPromise.then(response => {
		const body = response.json();
		console.log(`api move ${body.pieces_and_positions}`)
		fen = body.pieces_and_positions
		adjustBoard()
		board=board
		return body
});	
	}



	 function moveRequest(move) {
		let fetchPromise = fetch(`http://localhost:8000/current_games/board/${user_id}/${game_id}/${move}`).then(response => {
		
		const body = response.json();
		console.log(`api move ${body.pieces_and_positions}`)
		fen = body.pieces_and_positions
		return body
});	
console.log(fetchPromise)
fen = fetchPromise.then(response => {
	console.log(`response: ${response}`)
	let result = response
	return result
})
console.log(`FEN: ${fen}`)
console.log(2)
adjustBoardWithFEN(FEN=fen)
console.log(3)
	}
	


	function sendMove(){
		let from = `${columns[move_from[0]]}${Math.abs(move_from[1]+1)}`
		let to = `${columns[move_to[0]]}${Math.abs(move_to[1]+1)}`
		let move = `${from}${to}`
		console.log(`move is : ${move}`)
		moveRequest(move=move)
	}


	function checkMove(){
		let piece = board[move_from[1]].positions[move_from[0]]
		
		let team = piece.charAt(piece.length - 1);
		if (team != turn){
			return false
		}
		piece = piece.charAt(0);

		if (piece == 'P'){
			//add check en passant
			let pawnCheck = checkPawn(piece,team)
			if (pawnCheck){
				if (turn == 'W'){
					if (move_to[1] == 7){
						let pieceChoice = prompt("Please enter Q, N or R")
						while (!(pieceChoice == 'Q'||pieceChoice=='N'||pieceChoice=='R')){
						 pieceChoice = prompt("Please enter Q, N or R")
						}
						board[move_from[1]].positions[move_from[0]] = `${pieceChoice}W`;

					}
				} else {
					if (move_to[1] == 0){
						let pieceChoice = prompt("Please enter Q, N or R")
						while (!(pieceChoice == 'Q'||pieceChoice=='N'||pieceChoice=='R')){
						 pieceChoice = prompt("Please enter Q, N or R")
						}
						board[move_from[1]].positions[move_from[0]] = `${pieceChoice}B`;

					}
				}
			}

			return pawnCheck
		} else if (piece == 'N'){
			return checkKnight(piece,team)
		} else if (piece == 'R') {
			return checkLaterally(team)
		} else if (piece == 'B'){
			return checkDiagonally(team)
		} else if (piece == 'Q'){
			return checkDiagonally(team) || checkLaterally(team)
		} else if (piece == 'K'){
			//add check castle
			
			return checkKing(team)
		}


		return true || in_check(team)
	}

	function checkPawn(piece,team){
		let direction;
		let opponent;
		let row_check = move_from[1] >= 1 && move_from[1] <= 6
		let cond1
		let cond2
		let cond3
		let cond4
		let cond5 = false
		let right_check
		let left_check 
		if (team == 'W'){
			direction = 1
			opponent = 'B'
			cond1 = move_from[1]+2*direction == move_to[1] && move_from[1] == 1
		} else {
			direction = -1
			opponent = 'W'
			cond1 = move_from[1]+2*direction == move_to[1] && move_from[1] == 6

		}
		if (cond1){
			en_passant[0] = move_to[0]
			en_passant[1] = move_to[1]-1*direction

		}

			if (en_passant[0] == move_to[0] && en_passant[1] == move_to[1]){
				cond5 = true
			}

		
		right_check = 1 <= move_from[0]+1 && move_from[0]+1 <= 7
		right_check = right_check && board[move_to[1]].positions[move_to[0]].charAt(1) == opponent
		left_check = 2 <= move_from[0]+1 && move_from[0]+1 <= 8
		left_check = left_check && board[move_to[1]].positions[move_to[0]].charAt(1) == opponent
		
		cond2 = move_from[1]+1*direction == move_to[1] && move_from[0] == move_to[0] 
		if (right_check){
			cond3 = move_from[1]+1*direction == move_to[1] && move_from[0]+1 == move_to[0]

		} else {
			cond3 = false
		}
		if (left_check){
			cond4 = move_from[1]+1*direction == move_to[1] && move_from[0]-1 == move_to[0]

		} else {
			cond4 = false
		}


		return (cond1 || cond2 || cond3 || cond4 || cond5)


	
	}

	function checkKing(team){
		let x = move_from[0] - move_to[0]
		let y = move_from[1] - move_to[1]
		x = x*x
		y=y*y
		let opponent

		if ((x == 0 || x == 1)&&(y == 0||y == 1)&&(board[move_to[1]].positions[move_to[0]].charAt(1) != team)){
			return true
		}
		return false
	}

	function checkDiagonally(team){
		let x = move_from[0] - move_to[0]
		let y = move_from[1] - move_to[1]
		let direction = [1,1]

		if (x > 0){
			direction[0] = -1
		}
		if (y > 0){
			direction[1] = -1
		} 
		return checkDiagonal(team,direction,move_from)	
	}

	function checkDiagonal(team,direction,location){
		let opponent

		if (team == 'W') {
			opponent = 'B'
		} else {
			opponent = 'W'
		}




		let next = [0,0]
		next[0] = location[0]
		next[1] = location[1]
		next[0] = next[0] + direction[0]
		next[1] = next[1] + direction[1]
		if (next[0] == 8 || next[0] == -1 || next[1] == 8 || next[1] == -1)
		return false

		
		
		let next_space_team = board[next[1]].positions[next[0]].charAt(1)
		if (next_space_team == opponent){
			if (next[0] == move_to[0] && next[1] == move_to[1]){
				return true
			}
			return false
		} else if (next_space_team == ' '){
			if (next[0] == move_to[0] && next[1] == move_to[1]){
				return true
			}
			return checkDiagonal(team=team,direction=direction,next=next)
		} else { 
			return false
		}


	}

	function checkLaterally(team){
		let x = move_from[0] - move_to[0]
		let y = move_from[1] - move_to[1]
		let direction

		if (x == 0){
		if (y < 0){
			direction = 1
		} else if (y > 0){
			direction = -1
		} else {
			return false
		}
		let check = checkDirection(team,direction,1,move_from)
		if (getPiece(move_from[0],move_from[1]).charAt(0) == 'R' && check){
			if (team == 'W'){
				if (move_from[0] == 0 && move_from[1]==0){
						w_rook_has_moved[0] = true
				} else if (move_from[0] == 0 && move_from[1] == 7){
						w_rook_has_moved[1] = true
				}

			} else 	if (team == 'B'){
				if (move_from[0] == 7 && move_from[1]==0){
						b_rook_has_moved[0] = true
				} else if (move_from[0] == 7 && move_from[1] == 7){
						b_rook_has_moved[1] = true
				}

			}
		}

		return checkDirection(team,direction,1,move_from)	
		} else 	if (y == 0){		
		if (x < 0){
			direction = 1
		} else if (x > 0){
			direction = -1
		} else {
			return false
		}

			return checkDirection(team,direction,0,move_from)	
		} else {
			return false
		}
			
	}
function in_check_location(team,location){
	let checks = InCheckByDiagonally(team,location)
		checks = checks || InCheckByLaterally(team,location)
		checks = checks || InCheckByKing(team,location)
		checks = checks || InCheckByKnight(team,location)




		return !(checks)
}
	function in_check(team){

		let found_king=false
		let king_location = [0,0]
		
		for(let i = 0;!found_king;i++){
			for (let j = 1; j <8; j++){
				let king = board[i].positions[j]

				if (king.charAt(0) == 'K'&&king.charAt(1)==team){
					found_king = true
					king_location[0] = i
					king_location[1] = j

				}
			}
		}
		console.log(`king location: ${king_location}, ${getPiece(king_location[0],king_location[1])}`)
		let opponent
		if (team == 'W') {
			opponent = 'B'
		} else {
			opponent = 'W'
		}

		let checks = InCheckByDiagonally(team,king_location)
		checks = checks || InCheckByLaterally(team,king_location)
		checks = checks || InCheckByKing(team,king_location)
		checks = checks || InCheckByKnight(team,king_location)




		return !(checks)
		//add check en passant
		
		
		//return all check functions here

	}

	function getPiece(x,y){
		return board[x].positions[y]
	}
	function getPieceCorrect(x,y){
		return board[y].positions[x]
	}

	function InCheckByKing(team,king_location){
		let x = king_location[0]
		let y = king_location[1]
		//add pawn check in here
		let opponent

		if (team == 'W') {
			opponent = 'B'
		} else {
			opponent = 'W'
		}

		if (x < 7){
			if (getPiece(x+1,y).charAt(0) == 'K')
			return true
			if (y<7){
				if (getPiece(x+1,y+1).charAt(0) == 'K')
			return true
			if (getPiece(x+1,y+1).charAt(0) == 'PW' && team == 'B')
			return true
			} else if (y>0){
				if (getPiece(x+1,y-1).charAt(0) == 'PW' && team == 'B')
			return true
			if (getPiece(x+1,y-1).charAt(0) == 'K')
			return true
			}
		}
		if (x > 0){
			if (getPiece(x-1,y).charAt(0) == 'K')
			return true
			if (y<7){
				if (getPiece(x-1,y+1).charAt(0) == 'K')
			return true
			if (getPiece(x-1,y+1).charAt(0) == 'PB' && team == 'W')
			return true
			} else if (y>1){
				if (getPiece(x-1,y-1).charAt(0) == 'K')
			return true
			if (getPiece(x-1,y-1).charAt(0) == 'PB' && team == 'W')
			return true
			}
		}
		if (y<7){
			if (getPiece(x,y+1).charAt(0) == 'K')
			return true
		}
		if (y>1){
			if (getPiece(x,y-1).charAt(0) == 'K')
			return true
		}

		return false
	}

	function InCheckByKnight(team,king_location){
		let opponent;
		if (team == 'W'){
			opponent = 'B'
		} else {
			opponent = 'W'
		}
		let r2_check = king_location[0] >= 0 && king_location[0] <= 5;
		let l2_check = king_location[0] >= 2 && king_location[0] <= 7;
		let d2_check = king_location[1] >= 2 && king_location[1] <= 7;
		let u2_check = king_location[1] >= 0 && king_location[1] <= 5;
		let r1_check = king_location[0] >= 0 && king_location[0] <= 6;
		let l1_check = king_location[0] >= 1 && king_location[0] <= 7;
		let d1_check = king_location[1] >= 1 && king_location[1] <= 7;
		let u1_check = king_location[1] >= 0 && king_location[1] <= 6;

		
		let condition;

		if (r2_check) {

			if (d1_check){

				let piece = getPiece(king_location[0]+2,king_location[1]-1)
				condition = piece.charAt(1) == opponent && piece.charAt(0) == 'N'

				if(condition){
					return true
				} 
			} 
			if (u1_check) {
			
				let piece = getPiece(king_location[0]+2,king_location[1]+1)
				condition = piece.charAt(1) == opponent && piece.charAt(0) == 'N'
				if(condition){
					return true
				}
			}
		} 

		if (l2_check) {

			if (d1_check){
				let piece = getPiece(king_location[0]-2,king_location[1]-1)
				condition = piece.charAt(1) == opponent && piece.charAt(0) == 'N'
				if(condition){
					return true
				}
			} 
			if (u1_check) {

				let piece = getPiece(king_location[0]-2,king_location[1]+1)
				condition = piece.charAt(1) == opponent && piece.charAt(0) == 'N'
				if(condition){
					return true
				}
			}
		
		} 

		 if (u2_check) {
			

			if (l1_check){
				

				let piece = getPiece(king_location[0]-1,king_location[1]+2)
				condition = piece.charAt(1) == opponent && piece.charAt(0) == 'N'
				if(condition){
					return true
				}
			} 
			if (r1_check) {

				let piece = getPiece(king_location[0]+1,king_location[1]+2)
				condition = piece.charAt(1) == opponent && piece.charAt(0) == 'N'
				if(condition){
					return true
				}
			}
		
		}  
		 if (d2_check) {
			

			if (l1_check){

				let piece = getPiece(king_location[0]-1,king_location[1]-2)
				condition = piece.charAt(1) == opponent && piece.charAt(0) == 'N'
				if(condition){
					return true
				}
			} 
			 if (r1_check) {
			
				let piece = getPiece(king_location[0]+1,king_location[1]-2)
				condition = piece.charAt(1) == opponent && piece.charAt(0) == 'N'
				if(condition){
					return true
				}
			}
		
		}


		return false


	}

	function InCheckByDiagonally(team,king_location){

		let checks =  InCheckByDiagonal(team,[1,1],king_location)	
		checks = checks || InCheckByDiagonal(team,[1,-1],king_location)	
		checks = checks || InCheckByDiagonal(team,[-1,1],king_location)	
		checks = checks || InCheckByDiagonal(team,[-1,-1],king_location)	

		return checks
	}

	function InCheckByDiagonal(team,direction,king_location){
		let opponent

		if (team == 'W') {
			opponent = 'B'
		} else {
			opponent = 'W'
		}




		let next = [0,0]
		next[0] = king_location[0]
		next[1] = king_location[1]
		next[0] = next[0] + direction[0]
		next[1] = next[1] + direction[1]
		if (next[0] == 8 || next[0] == -1 || next[1] == 8 || next[1] == -1)
		return false

		
		
		let next_space = getPiece(next[0],next[1])
		let next_space_team = next_space.charAt(1)
		let next_space_piece = next_space.charAt(0)
		if (next_space_team == opponent){
			if (next_space_piece == 'Q' || next_space_piece == 'B'){
				return true
			}
			return false
		} else if (next_space_team == ' '){
			return InCheckByDiagonal(team,direction,next)
		} else { 
			return false
		}


	}

	function InCheckByLaterally(team,king_location){
		
		console.log(`check from ${king_location}, ${getPiece(king_location[1],king_location[1])}`)

		let checks = InCheckByDirection(team,1,1,king_location)

		checks = checks || InCheckByDirection(team,-1,1,king_location)

		checks = checks || InCheckByDirection(team,-1,0,king_location)

		checks = checks || InCheckByDirection(team,1,0,king_location)





		return checks
			
	}

	function InCheckByDirection(team,direction,axis,king_location){
		let opponent

		if (team == 'W') {
			opponent = 'B'
		} else {
			opponent = 'W'
		}

		let next = [0,0]
		next[0] = king_location[0]
		next[1] = king_location[1]
		next[axis] = next[axis] + direction
		if (next[axis] == -1 || next[axis] == 8)
		return false
		
		
		let next_space = getPieceCorrect(next[0],next[1])
		let next_space_team = next_space.charAt(1)
		let next_space_piece = next_space.charAt(0)
		if (next_space_team == team) {
			return false
		}else if (next_space_team == opponent){
			if (next_space_piece == 'Q' || next_space_piece == 'R'){
				console.log(`check from ${next}, ${next_space_piece}${next_space_team}`)
				return true
			}
			return false
		} else if (next_space_team == ' '){
			return InCheckByDirection(team,direction,axis,next)
		} else { 
			return false
		}

	}

	function checkDirection(team,direction,axis,location){
		let opponent

		if (team == 'W') {
			opponent = 'B'
		} else {
			opponent = 'W'
		}

		let next = [0,0]
		next[0] = location[0]
		next[1] = location[1]
		next[axis] = next[axis] + direction
		if (next[axis] == -1 || next[axis] == 8)
		return false

		
		
		let next_space_team = board[next[1]].positions[next[0]].charAt(1)
		if (next_space_team == opponent){
			if (next[0] == move_to[0] && next[1] == move_to[1]){
				return true
			}
			return false
		} else if (next_space_team == ' '){
			if (next[0] == move_to[0] && next[1] == move_to[1]){
				return true
			}
			return checkDirection(team,direction,axis,next)
		} else { 
			return false
		}

	}


	function checkKnight(piece,team){
		let opponent;
		if (team == 'W'){
			opponent = 'B'
		} else {
			opponent = 'W'
		}
		let r2_check = move_from[0] >= 0 && move_from[0] <= 5;
		let l2_check = move_from[0] >= 2 && move_from[0] <= 7;
		let d2_check = move_from[1] >= 2 && move_from[1] <= 7;
		let u2_check = move_from[1] >= 0 && move_from[1] <= 5;
		let r1_check = move_from[0] >= 0 && move_from[0] <= 6;
		let l1_check = move_from[0] >= 1 && move_from[0] <= 7;
		let d1_check = move_from[1] >= 1 && move_from[1] <= 7;
		let u1_check = move_from[1] >= 0 && move_from[1] <= 6;

		
		let condition;

		if (r2_check) {
			let r_condition = move_from[0] + 2 == move_to[0] 
			if (d1_check){
				condition =  r_condition && move_from[0] + 2 == move_to[0]
				
				condition =  r_condition && move_from[1] - 1  == move_to[1]
				
				condition = condition && board[move_to[1]].positions[move_to[0]].charAt(1) != team
				
				if(condition){
					return true
				} 
			} 
			if (u1_check) {
				condition =  r_condition && move_from[0] + 2 == move_to[0]
				condition =  r_condition && move_from[1] + 1  == move_to[1]
				condition = condition && board[move_to[1]].positions[move_to[0]].charAt(1) != team
				if(condition){
					return true
				}
			}
		} 

		if (l2_check) {
			let l_condition = move_from[0] - 2 == move_to[0] 
			if (d1_check){
				condition =  l_condition && move_from[0] - 2 == move_to[0]
				condition =  l_condition && move_from[1] - 1  == move_to[1]
				condition = condition && board[move_to[1]].positions[move_to[0]].charAt(1) != team
				if(condition){
					return true
				}
			} 
			if (u1_check) {
				condition =  l_condition && move_from[0] + 2 == move_to[0]
				condition =  l_condition && move_from[1] + 1  == move_to[1]
				condition = condition && board[move_to[1]].positions[move_to[0]].charAt(1) != team
				if(condition){
					return true
				}
			}
		
		} 

		 if (u2_check) {
			
			let u_condition = move_from[1] + 2 == move_to[1] 
			if (l1_check){
				
				condition =  u_condition && move_from[1] + 2 == move_to[1]
				
				condition =  u_condition && move_from[0] - 1  == move_to[0]
				
				condition = condition && board[move_to[1]].positions[move_to[0]].charAt(1) != team
				
				if(condition){
					return true
				}
			} 
			if (r1_check) {
				condition =  u_condition && move_from[1] + 2 == move_to[1]

				condition =  u_condition && move_from[0] + 1  == move_to[0]

				condition = condition && board[move_to[1]].positions[move_to[0]].charAt(1) != team
				if(condition){
					return true
				}
			}
		
		}  
		 if (d2_check) {
			
			let d_condition = move_from[1] - 2 == move_to[1] 
			if (l1_check){
				condition =  d_condition && move_from[1] - 2 == move_to[1]
				condition =  d_condition && move_from[0] - 1  == move_to[0]
				condition = condition && board[move_to[1]].positions[move_to[0]].charAt(1) != team
				if(condition){
					return true
				}
			} 
			 if (r1_check) {
				condition =  d_condition && move_from[1] - 2 == move_to[1]
				condition =  d_condition && move_from[0] + 1  == move_to[0]
				condition = condition && board[move_to[1]].positions[move_to[0]].charAt(1) != team
				if(condition){
					return true
				}
			}
		
		}


		return false


	}



function turnComplete(){

			if (turn == 'W'){
				turn = 'B'
			} else {
				turn = 'W'
			}
			last_move[0] = move_to[0]
			last_move[1] = move_to[1]
			
			
			if (turn == 'B'){
				move_no++
			}
			sendMove()
board=board
}

	function movePiece(row,column){

		if (positions_selected == 1){
			positions_selected = 0;
			move_to = [row-1,column-1];
			if (move_from[0] == move_to[0] && move_from[1] == move_to[1]){
				positions_selected = 1
				return false
			}

			let piece = getPiece(move_from[0],move_from[1])
			let castle_checks
			if (turn == 'W'){
				castle_checks = !w_king_has_moved
				
				if (castle_checks){
					castle_checks = move_to[1] == 0 && (move_to[0]==2 || move_to[0]==6)

					
				}
			} else{
				castle_checks = !b_king_has_moved
				
				if (castle_checks){
					castle_checks = move_to[1] == 7 && (move_to[0]==2 || move_to[0]==6)

					
				}
			}
			if (checkMove()){
			let temp = board[move_to[1]].positions[move_to[0]]
	
			if (move_to[0] == en_passant[0] && move_to[1] == en_passant[1]){

				let direction
				if (turn == 'W'){
			direction = 1
			} else if (m){

			}
		else {
			direction = -1
		}
			let temp = board[move_to[1]].positions[move_to[0]]
			board[move_to[1]].positions[move_to[0]] = board[move_from[1]].positions[move_from[0]];
			
			board[move_from[1]].positions[move_from[0]] = "  ";

			board[move_to[1]-direction].positions[move_to[0]] = "  ";
			} else{

			let temp = board[move_to[1]].positions[move_to[0]]
			board[move_to[1]].positions[move_to[0]] = board[move_from[1]].positions[move_from[0]];
			board[move_from[1]].positions[move_from[0]] = "  ";
			
		}


			if (!(in_check(turn))){

				board[move_from[1]].positions[move_from[0]] = board[move_to[1]].positions[move_to[0]]
				board[move_to[1]].positions[move_to[0]] = temp

				console.log("king is in check")
				return false

			}
			turnComplete()

			return true
		} else if(castle_checks){

			if (move_to[0] == 2){

				let empty_check

				empty_check = getPiece(move_from[1],move_from[0]-1) == '  '
				empty_check = empty_check && getPiece(move_from[1],move_from[0]-2) == '  '
				empty_check = empty_check && getPiece(move_from[1],move_from[0]-3) == '  '
				
				if (empty_check){
				let check_spaces
				check_spaces = in_check_location(turn, [move_from[0]-1,move_from[1]])
				check_spaces = check_spaces && in_check_location(turn, [move_from[0]-2,move_from[1]])
				check_spaces = check_spaces && in_check_location(turn, [move_from[0]-3,move_from[1]])
				if (check_spaces){
			let temp = board[move_from[1]].positions[move_from[0]]
			board[move_from[1]].positions[move_from[0]-2] = `K${turn}`
			board[move_from[1]].positions[move_from[0]-1] = `R${turn}`;
			board[move_from[1]].positions[0] = "  ";
			board[move_from[1]].positions[move_from[0]] = "  ";
			turnComplete()
			//need rook has moved check
			}	
			
			} else {
					console.log("spaces not empty")
				}
			} else if (move_to[0] == 6){
				let empty_check

	empty_check = getPiece(move_from[1],move_from[0]+1) == '  '
	empty_check = empty_check && getPiece(move_from[1],move_from[0]+2) == '  '


if (empty_check){
let check_spaces
check_spaces = in_check_location(turn, [move_from[0]+1,move_from[1]])
check_spaces = check_spaces && in_check_location(turn, [move_from[0]+2,move_from[1]])
if (check_spaces){
let temp = board[move_from[1]].positions[move_from[0]]
board[move_from[1]].positions[move_from[0]+2] = `K${turn}`
board[move_from[1]].positions[move_from[0]+1] = `R${turn}`;
board[move_from[1]].positions[7] = "  ";
board[move_from[1]].positions[move_from[0]] = "  ";
turnComplete()
//need rook has moved check
}	

} else {
	console.log("spaces not empty")
}
			}


		}
		else{
			console.log("invalid move")
			return false
		}
		} else{
		
			positions_selected++;
			move_from = [row-1,column-1];

			return false
		}
	}







</script>

{#key board}
{#each board as row}
<div class="row">
	{#each row.positions as position, i}
	<!-- svelte-ignore a11y-click-events-have-key-events -->
	<div class = "cell" on:click="{() => movePiece(i+1,row.row)}">
	{position}

</div>
	{/each}
	</div>
{/each}
{/key}

<style>
	.row {
		display: flex;
		margin: 4px 0;
	}
	.cell {
		width: 5px;
		height: 5px;
		flex-shrink: 0;
		text-align: center;
		padding: 30px;
		border: 3px solid black;
	}	

</style>
<h2>turn {turn}</h2>
<h1>gameplay{pieces_and_positions} color: {player_color}</h1>
<h1> user: {user}</h1>
