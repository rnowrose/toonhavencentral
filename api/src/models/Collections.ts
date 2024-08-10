import { Cascade, Collection, Entity, OneToMany, Property } from '@mikro-orm/core';
import { BaseModel } from './BaseModel';
import { Game } from './Game';

@Entity({tableName: 'collection', schema: 'games'})
export class Collections extends BaseModel {
    @Property()
    name: string;

    @Property()
    slug: string;
  
    @Property()
    url: string;

    @Property({ type: 'text' })
    summary: string;
    
    @OneToMany(() => Game, (game: Game) => game, { cascade: [Cascade.ALL] })
    game = new Collection<Game>(this)
    

    
}