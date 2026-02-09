<script lang="ts">
	import PageWithOpening from '$lib/components/ui/PageWithOpening.svelte';
	import type { PageData } from './$types';

	let { data }: { data: PageData } = $props();
</script>

<PageWithOpening title="marumo333's Portfolio" duration={2.5}>
	<div
		class="flex flex-col items-center text-base leading-relaxed text-gray-700 md:text-lg lg:text-xl"
	>
		{#if data.profile}
			{#if data.profile.avatarUrl}
				<img
					src={data.profile.avatarUrl}
					alt="marumo333 avatar"
					class="mb-4 h-24 w-24 rounded-full border-4 border-white object-cover shadow-lg"
				/>
			{/if}

			<p>{data.profile.bio}</p>
		{:else}
			<p>
				marumo333のスキル・経歴・開発実績が参照できるportfolioのwebアプリ<br />
				(プロフィールの読み込みに失敗しました)
			</p>
		{/if}

		<p class="mt-4 text-sm text-gray-400">
			RAGを用いたportfolio記載の内容に限定したchatが可能(ログインのみ)
		</p>
	</div>
</PageWithOpening>
