<script lang="ts">
	import '../app.css';
	import { resolve } from '$app/paths';

	let { children } = $props();
</script>

<div class="flex min-h-screen flex-col bg-gray-50 font-sans">
	<header
		class="sticky top-0 z-10 flex w-full justify-center border-b border-gray-200 bg-white/50 p-4 backdrop-blur-sm"
	>
		<nav class="flex flex-wrap items-center justify-center gap-4">
			<a href={resolve('/')} class="px-4 py-2 transition-colors hover:text-primary">Home</a>
			<a href={resolve('/skills')} class="px-4 py-2 transition-colors hover:text-primary">スキル</a>
			<a href={resolve('/career')} class="px-4 py-2 transition-colors hover:text-primary">経歴</a>
			<a href={resolve('/products')} class="px-4 py-2 transition-colors hover:text-primary"
				>開発実績</a
			>

			<a
				href={resolve('/login')}
				class="hover:bg-opacity-90 rounded bg-primary px-4 py-2 text-white transition-opacity"
			>
				ログイン
			</a>
		</nav>
	</header>

	<main class="mx-auto flex w-full max-w-4xl flex-1 flex-col items-center justify-center p-4">
		{@render children()}
	</main>

	<footer class="p-4 text-center text-sm text-gray-400">&copy; 2026 marumo333 Portfolio</footer>
</div>
