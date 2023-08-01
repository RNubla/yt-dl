import { defineStore } from "pinia";

export const useYTDLStore = defineStore('youtubeDL', {
    state: () => ({ videoList: [] }),
    actions: {
        addVideoToList(payload: any) {
            this.videoList.push(payload)
        },
        removeFromList(id: string) {
            const objWithIdIndex = this.videoList.findIndex((obj) => obj.id === id)
            if (objWithIdIndex > -1) {
                this.videoList.splice(objWithIdIndex, 1)
            }
        }
    }
    // const videoList = ref([])

    // function addVideoToList(payload: any) {
    //     videoList.value.push(payload)
    // }
})