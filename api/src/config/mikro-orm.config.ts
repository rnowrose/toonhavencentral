import { Options } from '@mikro-orm/core';
import path from 'path';


const config: Options = {
  entities: [path.join(__dirname, '../entities')], // Point to the directory containing your TypeScript entities // Add your entities here
  dbName: 'games',
  user: 'rownokn',
  password: 'rownokn',
  host: 'localhost',
  port: 5434,
  debug: true,
};

export default config;