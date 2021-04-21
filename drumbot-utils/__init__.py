from bson import ObjectId


class Model(dict):
    """
    Esta clase define a los modelos de mongodb. Contiene metodos de
    consulta e interaccion con la base de datos de mongo.
    """
    __getattr__ = dict.get
    __delattr__ = dict.__delattr__
    __setattr__ = dict.__setattr__

    def save(self):
        """
        Guarda el modelo en la base de datos
        """
        if not self._id:
            self.collection.insert_one(self)
        else:
            self.collection.replace_one({"_id": ObjectId(self._id)})

    def reload(self):
        """
        Actualiza el modelo con los datos de la base de datos.
        """
        if self._id:
            self.update(self.collection.find_one({"_id": ObjectId(self._id)}))

    def remove(self):
        """
        Elimina los datos del modelo de la base de datos.
        """
        if self._id:
            self.collection.delete_one({"_id": ObjectId(self._id)})
            self.clear()

    def find(self, filters: dict):
        """
        busca los datos de un modelo en la base de datos.
        :param filters: diccionario con los filtros para buscar
        """
        if dict is not None:
            self.update(self.collection.find_one(filters))

    @classmethod
    def find_all(cls, filters: dict) -> list:
        """
        Encuentra todos los documentos en la base de datos que
        coincidan con los filtros que se envian en los parametros.
        :param filters: diccionario con los filtros para buscar.
        :return: lista con todos los documentos encontrados.
        """
        return [document for document in cls.collection.find(filters)]

    @classmethod
    def save_all(cls, documents: list):
        """
        Guarda en la base de datos la lista de documentos que se
        envia en los parametros.
        :param documents: lista de documentos que se van a guardar
        """
        cls.collection.insert_many(documents)