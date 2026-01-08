
import { Hono } from 'hono';
import { streamText } from 'hono/streaming'


let videos = [
  {
    id: Math.random().toString(36).substring(2, 9),
    title: "Video 1",
    description: "This is video 1",
    duration: 120,
  },
  {
    id: Math.random().toString(36).substring(2, 9),
    title: "Video 2",
    description: "This is video 2",
    duration: 180,
  },
  {
    id: Math.random().toString(36).substring(2, 9),
    title: "Video 3",
    description: "This is video 3",
    duration: 240,
  },
];

const app = new Hono();

app.get('/', (c) => {
    return c.json({ message: videos });
})

app.post('/videos', async (c) => {
    const { title, description, duration } = await c.req.json();
    const newVideo = {
        id : Math.random().toString(36).substring(2, 9),
        title,
        description,
        duration,
    };
    videos.push(newVideo);
    return c.json({ message: 'Video added successfully', video: newVideo });
});


app.delete('/videos/:id', (c) => {
    const videoId = c.req.param('id');
    videos = videos.filter(video => video.id !== videoId);
    return c.json({ message: 'Video deleted successfully' });
})

app.post('/vidoe/id', async (c) => {
    const { id } = await c.req.json();
    const video = videos.find(video => video.id === id);
    // update the conten tof the Video
    if (video) {
        const { title, description, duration } = await c.req.json();
        video.title = title || video.title;
        video.description = description || video.description;
        video.duration = duration || video.duration;
        return c.json({ message: 'Video updated successfully', video });
    } else {
        return c.json({ message: 'Video not found' }, 404);
    }
})

app.get('/video', async c => {
    return streamText(c, async (stream) => {
      for (const video of videos){
        await stream.writeln(JSON.stringify(video))
        await stream.sleep(2000);
      }
    })
})

export default app;
