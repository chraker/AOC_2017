from solutions import *


class AbstractSolution(ABC):

    @abstractmethod
    def run(self) -> int:
        pass

    @abstractmethod
    def run_input(self, custom_input: any) -> int:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass

