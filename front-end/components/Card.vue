<script lang="ts" setup>
import { RequestedFormat } from '~/server/models/youtube.schema';

// defineProps(['title', 'thumbnailUrl', 'downloadLinks', 'videoURL', 'remove', 'downloadLinks'])
const props = defineProps<{
    title: string,
    thumbnailUrl: string,
    audioUrl?: string,
    videoUrl?: string,
    downloadLinks: RequestedFormat[]
}>()

console.log('downloadLinks: ', props.downloadLinks)
const audioLink = props.downloadLinks.find((field) => field.video_ext === "none")
const videoLink = props.downloadLinks.find((field) => field.video_ext === "webm")

console.log('audioLink', audioLink)

const download = async (url: string) => {
    try {
        console.log('url', url)
        const response = await fetch(url, {
            method: 'GET',
            mode: 'no-cors',
            headers: {
                'Content-Type': 'audio/webm'
            }
        })

        console.log('response', response)

        if (response.status === 200) {
            console.log('response', response)
        }
    } catch (error) {

    }
}

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
                <button class="btn btn-primary hover:bg-info " @click="download(audioLink!.url)">Audio</button>
                <button class="btn btn-secondary hover:bg-info " @click="download(videoLink!.url)">Video</button>
            </div>
        </div>
    </div>
</template>