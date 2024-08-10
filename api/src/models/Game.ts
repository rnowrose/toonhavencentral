import { Entity, Property } from '@mikro-orm/core';
import { BaseModel } from './BaseModel';

@Entity({tableName: 'game', schema: 'games'})
export class Game extends BaseModel {
    @Property()
    name: string;

    @Property()
    slug: string;
  
    @Property()
    url: string;

    @Property({ type: 'text' })
    summary: string;
    
    @Property({ type: 'text' })
    storyline: string;

    @Property
    

    
}