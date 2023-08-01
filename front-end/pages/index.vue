<script setup lang="ts">
import { z } from 'zod'
import { useYTDLStore } from '~/stores/myStore'
const store = useYTDLStore()

const colorMode = useColorMode()
const darkMode = ref('lofi')

const inputError = ref(false)

watch(darkMode, (mode) => {
    colorMode.preference = mode
})


const urlInput = ref({
    url: ''
})
// This will check if the input field is empty. If it is then it will remove the error box
watch(urlInput.value, (newInput, oldInput) => {
    if (newInput.url.length === 0) {
        inputError.value = false
    }
})
const urlSchema = z.object({
    url: z.string().url()
})


const onSubmit = async (e: Event) => {
    validateUrl()
    try {
        const res = await fetch('http://127.0.0.1:3001/api/video', {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ 'link': urlInput.value.url })
        })
        urlInput.value.url = ''
        const result = await res.json()
        store.addVideoToList(result)
        // ytdlStore.addVideoToList(result)
        // console.log(result.requested_formats[0].url)
        const url = new URL(result.requested_formats[0].url)
        const params = new URLSearchParams(url.search)
        const expire = params.get('expire')
        console.log(expire)
        // console.log(`valid: ${valid.url}`)
    } catch (error) {
        inputError.value = true
        // console.log(error)
    }


}

const validateUrl = () => {
    try {
        const valid = urlSchema.parse(urlInput.value)
        if (valid) inputError.value = false
    } catch (error) {
        inputError.value = true
    }
}

const remove = (id: string) => {
    store.removeFromList(id)
}

</script>

<template>
    <div class="grid grid-cols-1  h-screen">
        <header class="bg-accent flex justify-center items-center col-span-1 max-h-24">
            <form class="flex justify-center  items-center py-3 gap-2 flex-grow" @submit.prevent="onSubmit">
                <input class="input input-bordered  max-w-sm flex-grow" type="text" placeholder="Enter video URL"
                    v-model="urlInput.url" :class="{ 'input-error border-2': inputError }" />
                <button class="btn btn-primary" type="submit">Submit</button>
            </form>
            <div class="px-4"><input type="checkbox" class="toggle toggle-primary" true-value="black" false-value="lofi"
                    v-model="darkMode" /></div>
        </header>
        <main class="mx-auto w-full px-52 col-span-1 overflow-y-scroll">
            <div>
                <ul class="flex flex-col gap-3 ">
                    <li v-for="video in  store.videoList " :key="video.id">
                        <Card :title="video.title" :thumbnail-url="video.thumbnail" :remove="() => remove(video.id)" />
                    </li>
                </ul>
                <!-- <Card title="Hello" />
                <Card />
                <Card />
                <Card /> -->
            </div>
        </main>
    </div>
</template>