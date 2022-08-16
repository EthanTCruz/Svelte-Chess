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
	export let game_status = "None";
	function handleClick() {
		alert('no more alerts')
	}
	// import { session } from '$app/stores';
	// $session.user;
</script>
<a href="/gameplay">Click here to start a game</a>

<h1 class="text-2xl font-semibold text-center">Hi! You are registered with usernam {user}.</h1>

<a href="/past-games">Click here for past games</a>


<p>{game_status}</p>
<button on:click|once={handleClick}>
	Click me
</button>
