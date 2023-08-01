<script setup lang="ts">
const colorMode = useColorMode()

const darkMode = ref('lofi')

watch(darkMode, (mode) => {
    // console.log(`mode: ${mode}`)
    colorMode.preference = mode
})

const onSubmit = () => {
    alert(
        'onSubmit'
    )
}

</script>

<template>
    <div class="grid grid-cols-1  h-screen">
        <header class="bg-accent flex justify-center items-center col-span-1 ">
            <form class="flex justify-center  items-center py-3 gap-2 flex-grow" @submit.prevent="onSubmit">
                <input class="input input-bordered  max-w-sm flex-grow" type="text" placeholder="Enter video URL" />
                <button class="btn btn-primary" type="submit">Submit</button>
            </form>
            <div class="px-4"><input type="checkbox" class="toggle toggle-primary" true-value="black" false-value="lofi"
                    v-model="darkMode" /></div>
        </header>
        <main class="mx-auto w-full px-52 col-span-1 overflow-y-scroll">
            <div class="flex flex-col gap-3 ">
                <Card title="Hello" />
                <Card />
                <Card />
                <Card />
            </div>
        </main>
    </div>
</template>