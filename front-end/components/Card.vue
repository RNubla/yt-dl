<script lang="ts" setup>
defineProps(['title', 'thumbnailUrl', 'audioUrl', 'videoURL', 'remove'])
</script>

<template>
    <div class="card w-[35rem] sm:card-side bg-base-100 shadow-md p-2 relative">
        <div class="absolute right-0 top-0">
            <button class="btn btn-secondary hover:btn-error" @click="remove">X</button>
        </div>
        <figure><img class="object-fill w-[15rem]" :src="thumbnailUrl" alt="Album" />
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