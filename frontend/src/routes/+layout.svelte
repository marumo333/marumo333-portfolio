<script lang="ts">
    import '../app.css';

    let { children } = $props();
</script>

<div class="min-h-screen bg-gray-50 flex flex-col font-sans">
    
    <header class="w-full p-4 flex justify-center border-b border-gray-200 bg-white/50 backdrop-blur-sm sticky top-0 z-10">
        <nav class="flex flex-wrap gap-4 items-center justify-center">
            <a href="/skills" class="px-4 py-2 hover:text-primary transition-colors">スキル</a>
            <a href="/career" class="px-4 py-2 hover:text-primary transition-colors">経歴</a>
            <a href="/products" class="px-4 py-2 hover:text-primary transition-colors">開発実績</a>
            
            <a href="/login" class="px-4 py-2 bg-primary text-white rounded hover:bg-opacity-90 transition-opacity">
                ログイン
            </a>
        </nav>
    </header>

    <main class="flex-1 flex flex-col justify-center items-center p-4 w-full max-w-4xl mx-auto">
        {@render children()}
    </main>

    <footer class="p-4 text-center text-gray-400 text-sm">
        &copy; 2026 marumo333 Portfolio
    </footer>

</div>
