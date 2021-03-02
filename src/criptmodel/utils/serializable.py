import abc


class Serializable(abc.ABC):
    """Base abstract class for a serializable object."""

    def as_dict(self):
        return {k: self.__getattribute__(k) for k in vars(self)}
