from enum import Enum


class FilterType(Enum):
    """FilterType
    Clase enum para los tipos de filtros
    """
    AND = 1
    OR = 2
    DATE = 3


def make_filters(type: FilterType, filters: dict, **kwargs) -> dict:
    """make_filters
    Genera un diccionario con los filtros para la consulta de documentos
    en mongodb.
    :param type: Tipo de filtro que se va a generar
    :param filters: Diccionario con los filtros mandados desde el cliente.
    :param kwargs: Argumentos clave/valor en el cual se mandan algunos
        nombres de campos dentro de la coleccion.
    :return: Diccionario con el filtro para mongodb
    """
    if type == FilterType.AND:
        return {"$and": [{key, value} for key, value in filters.items()]}
    elif type == FilterType.OR:
        return {"$or": [{key, value} for key, value in filters.items()]}
    elif type == FilterType.DATE and "date_field" in kwargs:
        return {kwargs["date_field"]: {{"$gte": filters["from_date"]},
                                       {"$lte": filters["to_date"]}}}
    else:
        raise Exception("El tipo de filtro no es un tipo valido.")


def validate_params(params: dict) -> bool:
    """validate_params
    valida el contenido de los parametros enviados por el cliente
    :param params: diccionario con los parametros a validar
    :return: boolean. True si los parametros enviados cumplen con
        el esquema de los parametros. False si no lo cumplen.
    """
    if "type" in params and "filters" in params:
        if params["type"] in ["and", "or", "date"]:
            return True
    return False
