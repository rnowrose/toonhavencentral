import Fastify from 'fastify';
import config from './config/mikro-orm.config';
import { MikroORM } from '@mikro-orm/postgresql'; // or any other SQL driver package

//import userRoutes from './routes/userRoutes';
//import productRoutes from './routes/productRoutes';

const fastify = Fastify({ logger: true });


// Initialize MikroORM
const orm = await MikroORM.init(config);
fastify.decorate('orm', orm);

// Register routes
//fastify.register(userRoutes, { prefix: '/users' });
//fastify.register(productRoutes, { prefix: '/products' });

// Define a basic route
fastify.get('/', async (request, reply) => {
    return { message: 'Welcome to Fastify with MikroORM!' };
});

// Define port and host
const PORT = 3000;
const HOST = '0.0.0.0';

// Use server.listen() instead of app.listen()
fastify.listen({ port: PORT, host: HOST }, (err, address) => {
    if (err) {
        fastify.log.error(err);
        process.exit(1);
    }
    fastify.log.info(`Server listening at ${address}`);

    return fastify;
});
