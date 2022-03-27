from VictoryApp import models
import datetime
x = datetime.datetime.now()


def entity(context):
    y = x.year
    entity = models.Entity.objects.first()
    return {'entity': entity,
            'x': y,
            }

