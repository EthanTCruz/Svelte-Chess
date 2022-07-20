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

	// import { session } from '$app/stores';
	// $session.user;
</script>
<a href="/gameplay">Home</a>
<h1 class="text-2xl font-semibold text-center">Hi! You are registered with usernam {user}.</h1>
