import path from 'path';
const config = {
    entities: [path.join(__dirname, '../entities')], // Point to the directory containing your TypeScript entities // Add your entities here
    dbName: 'your-database-name',
    user: 'your-username',
    password: 'your-password',
    host: 'localhost',
    port: 5432,
    debug: true,
};
export default config;
