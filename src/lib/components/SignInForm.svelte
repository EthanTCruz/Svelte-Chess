<script>
	import Input from '$lib/components/Input.svelte';
	import Button from '$lib/components/Button.svelte';

	import { createEventDispatcher } from 'svelte';

	let username = '';
	let password = '';

	const dispatch = createEventDispatcher();

	function submit() {
		dispatch('submit', {
			username,
			password,
		});
	}
</script>

<form on:submit|preventDefault={submit} class="space-y-5 {$$props.class}">
	<Input label="Username" id="username" name="username" type="text" bind:value={username} required />
	<Input label="Password" id="password" name="password" type="password" bind:value={password} required />
	<Button type="submit">Sign In</Button>
</form>
