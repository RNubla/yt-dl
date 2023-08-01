import { defineStore } from "pinia";
import { VideoInfo } from "server/models/youtube.schema";

export const useYTDLStore = defineStore('youtubeDL', {
    state: () => {
        const videoList: VideoInfo[] = []

        return {
            videoList
        }
    },
    actions: {
        addVideoToList(payload: VideoInfo) {
            this.videoList.push(payload)
        },
        removeFromList(id: string) {
            const objWithIdIndex = this.videoList.findIndex((obj) => obj.id === id)
            if (objWithIdIndex > -1) {
                this.videoList.splice(objWithIdIndex, 1)
            }
        }
    }
})