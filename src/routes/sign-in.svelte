<script>
	import SignInForm from '$lib/components/SignInForm.svelte';
	import { goto } from '$app/navigation';
	import { session } from '$app/stores';

	let error;
	let result = null;
	async function handleSubmit({ detail:{username, password } }) {
		
		const response = await fetch(`http://localhost:8000/sign-in?username=${username}&password=${password}`, {
			method: 'POST',
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({"username": username, "password": password }),
		});
		const body = await response.json();
		//result = JSON.stringify(body)



		if (response.ok) {
			result = "why"
			// session from getSession hook will otherwise not be set before navigation
			// that would trigger redirect from /protected back to /sign-in
			$session = body;
			await goto('/protected');
		result = $session
		}
		error = body.message;
	}
</script>

<pre>
{result}
</pre>

<h1 class="text-2xl font-semibold text-center">Sign In</h1>
{#if error}
	<p class="mt-3 text-red-500 text-center font-semibold">{error}</p>
{/if}
<SignInForm class="max-w-xl mx-auto mt-8" on:submit={handleSubmit} />
