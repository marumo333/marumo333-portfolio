<script lang="ts">
	import { onMount } from 'svelte';
	import PageWithOpening from '$lib/components/ui/PageWithOpening.svelte';
	import SkillCard from '$lib/components/ui/SkillCard.svelte';
	import type { PageData } from './$types';

	let { data }: { data: PageData } = $props();

	let showSkills = $state(false);

	// PageWithOpeningのオープニング完了後にスキルカードを表示
	// duration(1s) + 余白(500ms) + fade(200ms遅延 + 800ms) + バッファ(200ms) = 2700ms
	onMount(() => {
		setTimeout(() => {
			showSkills = true;
		}, 2700);
	});
</script>

<PageWithOpening title="Skills">
	<div class="grid grid-cols-1 gap-6 p-6 md:grid-cols-2 lg:grid-cols-3">
		{#if showSkills}
			{#each data.skills as skill, i}
				<SkillCard {skill} index={i} />
			{/each}
		{/if}
	</div>
</PageWithOpening>
