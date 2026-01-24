<script lang="ts">
	type Props = {
		text: string;
		duration?: number; // アニメーション時間（秒）
		class?: string;
	};

	let { text, duration = 2.5, class: className = '' }: Props = $props();
</script>

<span
	class="typewriter {className}"
	style="
		--char-count: {text.length};
		--duration: {duration}s;
		--steps: {text.length};
	"
>
	{text}
</span>

<style>
	.typewriter {
		display: inline-block;
		overflow: hidden;
		white-space: nowrap;
		border-right: 4px solid var(--color-primary, #f15922);
		width: 0;
		animation:
			typing var(--duration) steps(var(--steps)) forwards,
			blinks 0.75s step-end infinite;
	}

	@keyframes typing {
		from {
			width: 0;
		}
		to {
			width: calc(var(--char-count) * 1ch);
		}
	}

	@keyframes blinks {
		from,
		to {
			border-color: transparent;
		}
		50% {
			border-color: var(--color-primary, #f15922);
		}
	}
</style>
