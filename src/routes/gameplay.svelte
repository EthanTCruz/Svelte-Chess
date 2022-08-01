<script context="module">
	export async function load({ session }) {
		if (!session?.username) {
			return {
				status: 302,
				redirect: '/sign-in',
			};
		}
		return {
			props: {
				user: session.username,
			},
		};
	}
</script>
<script>
	export let user;

	
	import { board } from './store.js'	

	let turn = 'W';
	let move_no;
	let positions_selected = 0;
	let move_from;
	let move_to;

	function checkMove(){
		let piece = board[move_from[1]].positions[move_from[0]]
		
		let team = piece.charAt(piece.length - 1);
		if (team != turn){
			return false
		}
		piece = piece.charAt(0);
		console.log(team)
		console.log(piece)
		if (piece == 'P'){
			//add check en passant
			return checkPawn(piece,team)
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
		console.log(`x: ${x}`)
		console.log(`y: ${y}`)
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
		console.log(team,direction,location)
		if (team == 'W') {
			opponent = 'B'
		} else {
			opponent = 'W'
		}


		console.log(`locations: ${location}`)
		console.log(`direction: ${direction}`)

		let next = [0,0]
		next[0] = location[0]
		next[1] = location[1]
		next[0] = next[0] + direction[0]
		next[1] = next[1] + direction[1]
		if (next[0] == 8 || next[0] == -1 || next[1] == 8 || next[1] == -1)
		return false
		console.log(`next: ${next}`)
		
		
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
		console.log(`x: ${x}`)
		console.log(`y: ${y}`)
		if (x == 0){
		if (y < 0){
			direction = 1
		} else if (y > 0){
			direction = -1
		} else {
			return false
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

	function in_check(team){
		let from_holder = [0,0]
		let to_holder = [0,0]
		from_holder[0] = move_from[0]
		from_holder[1] = move_from[1]
		to_holder[0] = move_to[0]
		to_holder[1] = move_to[1]
		let found_king=false
		
		for(let i = 0;!found_king;i++){
			for (let j = 1; j <8; j++){
				let king = board[j].positions[i]
				if (king.charAt(0) == 'K'&&king.charAt(1)==team){
					found_king = true
					move_from[0] = i
					move_from[1] = j
				}
			}
		}
		let opponent
		if (team == 'W') {
			opponent = 'B'
		} else {
			opponent = 'W'
		}

		let checks = checkKnight('N',opponent) || checkLaterally(opponent)||checkDiagonally(opponent) || checkDiagonally(opponent) || checkLaterally(opponent) 
		
		return !(checks)
		//add check en passant
		
		
		//return all check functions here

	}

	function checkDirection(team,direction,axis,location){
		let opponent
		console.log(team,direction,axis,location)
		if (team == 'W') {
			opponent = 'B'
		} else {
			opponent = 'W'
		}
		console.log(`locations: ${location}`)
		console.log(`direction: ${direction}`)
		console.log(`axis: ${axis}`)
		let next = [0,0]
		next[0] = location[0]
		next[1] = location[1]
		next[axis] = next[axis] + direction
		if (next[axis] == -1 || next[axis] == 8)
		return false
		console.log(`next: ${next}`)
		
		
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
			return checkDirection(team=team,direction=direction,axis=axis,next=next)
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

	function checkPawn(piece,team){
		let direction;
		let opponent;
		let row_check = move_from[1] >= 1 && move_from[1] <= 6
		let cond1
		let cond2
		let cond3
		let cond4
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

		return (cond1 || cond2 || cond3 || cond4)


	
	}

	function movePiece(row,column){

		if (positions_selected == 1){
			positions_selected = 0;
			move_to = [row-1,column-1];
			if (move_from[0] == move_to[0] && move_from[1] == move_to[1]){
				positions_selected = 1
				return false
			}
			if (checkMove()){
			//console.log(`piece: ${board[move_to[1]].positions[move_to[1]]}, row: ${move_to[1]}, column: ${move_to[0]}`)
			//console.log(`piece: ${board[move_from[1]].positions[move_from[1]]}, row: ${move_from[1]}, column: ${move_from[0]}`)
			board[move_to[1]].positions[move_to[0]] = board[move_from[1]].positions[move_from[0]];
			board = board
			board[move_from[1]].positions[move_from[0]] = "  ";
			board = board
			if (turn == 'W'){
				turn = 'B'
			} else {
				turn = 'W'
			}
			
			if (turn == false){
				move_no++
			}
			return true
		} else{
			console.log("invalid move")
			return false
		}
		} else{
		
			positions_selected++;
			move_from = [row-1,column-1];

			return false
		}
	}

	//$: console.log(board)

	function selectCell(row,column){

console.log(row)
console.log(column)

	}
$: console.log(`move_from: ${move_from}`)
$: console.log(`move_to: ${move_to}`)
</script>


{#each board as row}
<div class="row">
	{#each row.positions as position, i}
	<div class = "cell" on:click="{() => movePiece(i+1,row.row)}">
	{position}

</div>
	{/each}
	</div>
{/each}

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
<h1>gameplay {user}</h1>