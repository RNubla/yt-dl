import { number, string, z } from "zod";


export const requestedFormatSchema = z.object({
    filesize: number(),
    format_id: string(),
    format_note: string(),
    fps: number().optional().nullable(),
    url: string(),
    ext: string(),
    resolution: string(),
    video_ext: string(),
    audio_ext: string(),
})

export const videoInfoSchema = z.object({
    id: string(),
    title: string(),
    thumbnail: string(),
    description: string(),
    channel_id: string(),
    channel_url: string(),
    channel: string(),
    format: string(),
    requested_formats: z.array(requestedFormatSchema)
})

export type RequestedFormat = z.TypeOf<typeof requestedFormatSchema>
export type VideoInfo = z.TypeOf<typeof videoInfoSchema>