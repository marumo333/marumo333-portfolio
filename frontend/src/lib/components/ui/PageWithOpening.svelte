<script lang="ts">
	import { fade } from 'svelte/transition';
	import TypewriterText from './TypewriterText.svelte';

	type Props = {
		title: string;
		duration?: number; // タイピングアニメーション時間
		children?: import('svelte').Snippet; // ページコンテンツ
	};

	let { title, duration = 1, children }: Props = $props();

	// オープニング表示状態
	let showOpening = $state(true);

	// アニメーション時間 + 余白でオープニング終了
	$effect(() => {
		const timer = setTimeout(
			() => {
				showOpening = false;
			},
			duration * 1000 + 500
		);

		return () => clearTimeout(timer);
	});
</script>

{#if showOpening}
	<div
		class="fixed inset-0 z-50 flex items-center justify-center bg-white"
		out:fade={{ duration: 500 }}
	>
		<h1 class="text-3xl font-bold text-primary md:text-5xl">
			<TypewriterText text={title} {duration} />
		</h1>
	</div>
{:else}
	<div in:fade={{ duration: 800, delay: 200 }}>
		<section class="max-w-2xl text-center">
			<h1 class="mb-4 text-4xl font-bold text-primary md:text-4xl lg:text-5xl">
				{title}
			</h1>
			{#if children}
				{@render children()}
			{:else}
				<p class="text-base leading-relaxed text-gray-700 md:text-lg lg:text-xl">準備中</p>
			{/if}
		</section>
	</div>
{/if}
