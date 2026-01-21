import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
import tailwindcss from '@tailwindcss/vite'; // ← これが必要です！

export default defineConfig({
	plugins: [
		sveltekit(),
		tailwindcss() // ← これがないとTailwindが動きません
	],
	server: {
		proxy: {
			'/api': {
				target: 'http://backend:8000',
				changeOrigin: true,
				rewrite: (path) => path.replace(/^\/api/, '')
			}
		}
	}
});
