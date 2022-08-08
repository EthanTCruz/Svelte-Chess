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

<p>past game png's will appear here if you have any</p>