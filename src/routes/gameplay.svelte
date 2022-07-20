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
</script>

<h1>gameplay {user}</h1>