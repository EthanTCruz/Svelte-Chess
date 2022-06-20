<script>
	import { session } from '$app/stores';
	import { goto } from '$app/navigation';

	const navigation = [
		{
			href: '/',
			name: 'Home',
		},
		{
			href: '/protected',
			name: `${$session.user ? '🔓' : '🔒'} Protected`,
		},
	];

	async function handleSignOut() {
		await fetch('/api/sign-out');
		$session = {};
		await goto('/sign-in');
	}
</script>

<header class="bg-indigo-600">
	<nav class="container mx-auto">
		<div class="w-full py-4 flex items-center justify-between">
			<div class="ml-10 space-x-4">
				{#if $session.user}
					<button
						on:click={handleSignOut}
						class="inline-block bg-indigo-500 py-2 px-4 border border-transparent rounded-md text-base font-medium text-white hover:bg-opacity-75"
					>
						Sign out
					</button>
				{:else}
					<a
						href="/sign-in"
						class="inline-block bg-indigo-500 py-2 px-4 border border-transparent rounded-md text-base font-medium text-white hover:bg-opacity-75"
					>
						Sign in
					</a>

				{/if}
			</div>
		</div>
	</nav>
</header>
