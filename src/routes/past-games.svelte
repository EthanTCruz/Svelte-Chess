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

				user_id: session.user_id
			},
		};
	}


</script>

<script>
export let user_id
import { onMount } from 'svelte';

let pgns = [];

onMount(async () => {
	const res = await fetch(`http://localhost:8000/past_games/${user_id}?skip=0&limit=100`);
	pgns = await res.json();
	let real_pgn = []

	let move_string = "1. "
	let id = -1
	let row = -1
	for(let m = 0; m<pgns.length;m++){
		if (id != pgns[m].game_id){
			row++
			console.log("ntghd")
			console.log(id)
			id =  pgns[m].game_id
			real_pgn.push({"game_id": id,"moves":move_string})
			console.log(real_pgn)
		
		}
		
	
		//move_string += pgns[m].move
		console.log(real_pgn[row])
		real_pgn[row].moves = " "+real_pgn[row].moves +" "+  pgns[m].move+ " "
		if (m % 2 == 1){
			real_pgn[row].moves += ` ${Number((m+3)/2)}. `
		}

		console.log(real_pgn)
	}
	pgns = real_pgn
	console.log(pgns)

});
</script>

<p>past game png's will appear here if you have any</p>


<h1>Pgn</h1>

<div>
	{#each pgns as pgn}
		<p>{pgn.moves}</p>
	{:else}
		<p>No games Played</p>
	{/each}
</div>