from datetime import datetime
from models import storage
import uuid


class BaseModel:

    """BaseModel class defined here"""
    global for_mat
    for_mat = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """created the instantiation stage"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key_num, value_val in kwargs.items():
                if key_num != "__class__":
                    if key_num in ["created_at", "updated_at"]:
                        value_val = datetime.strptime(value_val, for_mat)
                    setattr(self, key_num, value_val)

    def __str__(self):
        """String instantiation of the BaseModel"""
        cl_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cl_name, self.id, self.__dict__)

    def save(self):
        """Updating time and date at the point of saving"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Redefining dictionary"""
        my_dict = self.__dict__.copy()
        my_dict.update({
            "__class__": self.__class__.__name__,
            "created_at": str(self.created_at.isoformat()),
            "updated_at": str(self.updated_at.isoformat())
            })
        return my_dict