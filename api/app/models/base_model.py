from tortoise.models import Model
from tortoise import fields
from tortoise.exceptions import DoesNotExist
from api.app.core.exceptions import UnsupportedType


class AbstractModel(Model):
    '''
    Had to split this one out and name it as such because BaseModel was already made and used by many models.
    But we want other models to not have create/modify_date, but still able to use find()
    '''
    class Meta:
        abstract = True

    @classmethod
    def find(cls, ref, default=None, ignore_refs=['', None]):
        if ref in ignore_refs:
            return default

        if isinstance(ref, cls):
            return ref
        elif isinstance(ref, int) or isinstance(ref, str):
            try:
                return cls.get(pk=ref)
            except cls.DoesNotExist:
                pass
        else:
            raise UnsupportedType("{} {}".format(ref.__class__, ref))

        return default


class BaseModel(AbstractModel):
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    checksum = fields.UUIDField()

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.pk)