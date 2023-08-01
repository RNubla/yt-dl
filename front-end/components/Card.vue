<script lang="ts" setup>
defineProps(['title', 'thumbnailUrl', 'audioUrl', 'videoURL'])
</script>

<template>
    <div class="card w-[35rem] sm:card-side bg-base-100 shadow-md p-2">
        <figure><img src="https://daisyui.com/images/stock/photo-1494232410401-ad00d5433cfa.jpg" alt="Album" />
        </figure>
        <div class="card-body">
            <h2 class="card-title">{{ title }}</h2>
            <p>Click the button to listen on Spotiwhy app.</p>
            <div class="card-actions justify-end">
                <button class="btn btn-primary hover:bg-info ">Audio</button>
                <button class="btn btn-secondary hover:bg-info ">Video</button>
            </div>
        </div>
    </div>
</template>