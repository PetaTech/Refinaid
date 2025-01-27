from pydantic import BaseModel


def get_model_fields_with_aliases(model: BaseModel):
    return [
        field.alias if field.alias else name
        for name, field in model.model_fields.items()
    ]
