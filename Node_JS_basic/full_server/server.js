import express from 'express';
import routes from './routes/index.js';

const app = express();

app.use('/', routes);

const PORT = 1245;

if (process.env.NODE_ENV !== 'test') {
  app.listen(PORT, () => {
    // eslint-disable-next-line no-console
    console.log(`Server is listening on port ${PORT}`);
  });
}

export default app;
