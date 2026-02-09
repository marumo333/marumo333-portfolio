<script lang="ts">
	type Skill = {
		name: string;
		category: string;
		level: number;
		yearsOfExperience: number;
		description?: string | null;
		iconUrl?: string | null;
	};

	type Props = {
		skill: Skill;
		index: number;
	};

	let { skill, index }: Props = $props();

	const getLevelLabel = (level: number) => {
		if (level === 5) return 'Expert';
		if (level >= 4) return 'Advanced';
		if (level >= 3) return 'Intermediate';
		return 'Beginner';
	};
</script>

<div
	class="skill-card flex flex-col gap-3 rounded-xl border border-gray-200 bg-white p-5 shadow-sm transition-shadow hover:shadow-md"
	style="animation-delay: {index * 100}ms"
>
	<div class="flex items-center gap-3">
		{#if skill.iconUrl}
			<img src={skill.iconUrl} alt={skill.name} class="h-10 w-10 object-contain" />
		{:else}
			<div
				class="flex h-10 w-10 items-center justify-center rounded-full bg-gray-100 font-bold text-gray-500"
			>
				{skill.name.slice(0, 1)}
			</div>
		{/if}

		<div>
			<h3 class="text-lg font-bold text-gray-900">{skill.name}</h3>
			<span
				class="inline-block rounded bg-blue-100 px-2 py-0.5 text-xs font-medium text-blue-800"
			>
				{skill.category}
			</span>
		</div>
	</div>

	<div class="mt-2 space-y-2 text-sm text-gray-600">
		<div class="flex justify-between">
			<span>Experience:</span>
			<span class="font-medium">{skill.yearsOfExperience} years</span>
		</div>

		<div class="flex flex-col gap-1">
			<div class="flex justify-between text-xs">
				<span>Level</span>
				<span>{getLevelLabel(skill.level)} ({skill.level}/5)</span>
			</div>
			<div class="h-2 w-full overflow-hidden rounded-full bg-gray-100">
				<div
					class="h-full bg-blue-500 transition-all duration-1000"
					style="width: {(skill.level / 5) * 100}%"
				></div>
			</div>
		</div>
	</div>

	{#if skill.description}
		<p class="mt-2 line-clamp-2 text-xs text-gray-500">
			{skill.description}
		</p>
	{/if}
</div>

<style>
	@keyframes slideDown {
		from {
			opacity: 0;
			transform: translateY(-50px);
		}
		to {
			opacity: 1;
			transform: translateY(0);
		}
	}

	.skill-card {
		opacity: 0;
		animation: slideDown 0.5s ease-out forwards;
	}
</style>
