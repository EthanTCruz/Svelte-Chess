<script context="module">
import { session } from "$app/stores";


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
				username: session.username,
				game_id: -1,
				pieces_and_positions: "wait",
				player_color: " ",
			},
		};
	}
	
	let game_status = 'None';


</script>

<script>
	import { goto } from '$app/navigation';
	export let username
	export let user_id

	export let game_status = "None";






	let result
	async function joinGame() {
		console.log(session.user_id)
		const response = await fetch('http://localhost:8000/join/current_games/', {
			method: 'POST',
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({"user_id": user_id,"username": username}),
		});
		const body = await response.json();
		$session.game_id = body.game_id
		$session.pieces_and_positions = body.pieces_and_positions
		$session.player_color = body.player_color
		await goto('/gameplay');
		//result = JSON.stringify(body)
		if (response.ok) {
			result = "why"
			// session from getSession hook will otherwise not be set before navigation
			// that would trigger redirect from /protected back to /sign-in
		}
		game_status = body.game_id;

	}


	// import { session } from '$app/stores';
	// $session.user;
</script>


<a href="/past-games">Click here for past games</a>



<p> </p>
<button on:click|once={joinGame} href="/gameplay">
join game
</button>
