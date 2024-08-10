import { Entity, PrimaryKey, Property } from '@mikro-orm/core';
import { v4 } from 'uuid';

@Entity({ abstract: true })
export abstract class BaseModel {
    @PrimaryKey()
    id!: number;

    @Property({ type: 'date', onCreate: () => new Date() })
    createdAt = new Date();

    @Property({ type: 'date', onUpdate: () => new Date() })
    updatedAt = new Date();
}